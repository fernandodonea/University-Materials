"""
=============================================================================
LABORATOR 4 - Bag-of-Words, Normalizare, SVM
=============================================================================
Materie: Inteligență Artificială - Machine Learning
Acoperire: Bag-of-Words pentru text, StandardScaler, normalizare L1/L2,
           SVM cu kernel linear și RBF, clasificare SMS Spam

RULARE: python lab4_bow_normalizare_svm.py
Dependențe: pip install numpy scikit-learn
Date: arhiva cu SMS Spam (train_spam.txt, test_spam.txt etc.)
      sau fallback automat cu dataset sklearn
=============================================================================
"""

import numpy as np
from sklearn import preprocessing, svm
from sklearn.metrics import accuracy_score, f1_score
import os

# =============================================================================
# 1. TEORIA
# =============================================================================
"""
BAG OF WORDS (BoW):
    - Reprezintă un document text ca vector de frecvențe de cuvinte
    - Pasul 1: Construiești vocabularul (dicționar cuvânt → index unic) din TRAIN
    - Pasul 2: Fiecare document devine vector de dimensiune |vocabular|,
               unde features[word_idx] = nr aparitii cuvant cu id word_idx
    - Pierde informația de ordine a cuvintelor, dar simplu și eficient

NORMALIZARE:
    Standardizare (z-score):
        x_scaled = (x - mean(x)) / std(x)
        → fiecare atribut are medie 0 și deviație standard 1
        → sensibil la outlieri

    L1:
        x_scaled = x / ||x||_1, unde ||x||_1 = sum |x_i|
        → fiecare exemplu devine vector cu suma absolută = 1
        → robust la outlieri mari

    L2:
        x_scaled = x / ||x||_2, unde ||x||_2 = sqrt(sum x_i^2)
        → fiecare exemplu devine vector unitar (normă = 1)
        → cel mai folosit cu SVM

SVM (Support Vector Machine):
    - Clasificator liniar care maximizează MARGINEA dintre clase
    - Hyperplan optim: w·x + b = 0
    - Soft margin cu parametrul C:
        C mare: margine mică, puțin tolerant la erori → risc overfitting
        C mic:  margine mare, tolerant la erori → risc underfitting

    Kernels:
        Linear: K(u,v) = u^T · v (date liniar separabile)
        RBF:    K(u,v) = exp(-gamma * ||u-v||^2) (date neliniar separabile)

        gamma (pentru RBF):
            Mare: decizie locală, frontieră complexă → overfitting
            Mic:  decizie globală, frontieră lină → underfitting

    Multi-class: sklearn folosește One-vs-One (nr_clase*(nr_clase-1)/2 clasificatori)
"""

# =============================================================================
# 2. NORMALIZAREA DATELOR
# =============================================================================

print("=" * 60)
print("2. NORMALIZARE DATE")
print("=" * 60)

# DEMO cu date simple
x_train = np.array([[1., -1.,  2.],
                     [2.,  0.,  0.],
                     [0.,  1., -1.]])
x_test  = np.array([[-1., 1., 0.]])

# --- 2.1 Standardizare (StandardScaler) ---
print("\n--- 2.1 Standardizare ---")
scaler = preprocessing.StandardScaler()
scaler.fit(x_train)  # calculează medie și std DOAR pe train

print(f"Medie:    {scaler.mean_}")
print(f"Std:      {scaler.scale_}")

scaled_x_train = scaler.transform(x_train)  # aplică pe train
scaled_x_test  = scaler.transform(x_test)   # ACELAȘI scaler pe test!
print(f"Train standardizat:\n{scaled_x_train}")
print(f"Test standardizat:\n{scaled_x_test}")

# --- 2.2 Normalizare L1 ---
print("\n--- 2.2 Normalizare L1 ---")
l1_normalizer = preprocessing.Normalizer(norm='l1')
l1_normalized = l1_normalizer.fit_transform(x_train)
print(f"L1 normalized:\n{l1_normalized}")
print(f"Suma abs. primei linii: {np.abs(l1_normalized[0]).sum():.2f}")  # = 1.0

# --- 2.3 Normalizare L2 ---
print("\n--- 2.3 Normalizare L2 ---")
l2_normalizer = preprocessing.Normalizer(norm='l2')
l2_normalized = l2_normalizer.fit_transform(x_train)
print(f"L2 normalized:\n{l2_normalized}")
print(f"Norma L2 primei linii: {np.sqrt((l2_normalized[0]**2).sum()):.2f}")  # = 1.0

# --- FUNCȚIE GENERICĂ DE NORMALIZARE (din exerciții) ---
def normalize_data(train_data, test_data, norm_type=None):
    """
    Normalizează datele de antrenare și testare.

    Parametri:
        train_data : np.array — date antrenare
        test_data  : np.array — date testare
        norm_type  : None | 'standard' | 'l1' | 'l2'

    Returnează:
        (train_normalized, test_normalized)

    IMPORTANT: Statisticile se calculează DOAR pe train, aplicate pe ambele!
    (prevenire data leakage)
    """
    if norm_type is None:
        return train_data, test_data

    elif norm_type == 'standard':
        scaler = preprocessing.StandardScaler()
        scaler.fit(train_data)
        return scaler.transform(train_data), scaler.transform(test_data)

    elif norm_type in ('l1', 'l2'):
        normalizer = preprocessing.Normalizer(norm=norm_type)
        # Normalizer normalizează per-exemplu, nu per-feature
        # Deci nu e nevoie să fie "fit" pe train separat
        return normalizer.transform(train_data), normalizer.transform(test_data)

    else:
        raise ValueError(f"norm_type necunoscut: {norm_type}")


# =============================================================================
# 3. BAG OF WORDS
# =============================================================================

print("\n" + "=" * 60)
print("3. BAG OF WORDS")
print("=" * 60)

class BagOfWords:
    """
    Implementare Bag-of-Words din scratch.

    Utilizare:
        bow = BagOfWords()
        bow.build_vocabulary(train_messages)   # construiește vocabularul din TRAIN
        features = bow.get_features(messages)   # obține reprezentarea BoW
    """

    def __init__(self):
        self.vocabulary = {}      # {cuvant: id} — dicționar cuvânt → index
        self.vocabulary_list = [] # lista cuvintelor în ordinea adăugării

    def build_vocabulary(self, data):
        """
        Construiește vocabularul din datele de antrenare.

        data : list de list de str — [[cuvant1, cuvant2, ...], [cuvant1, ...], ...]
        """
        self.vocabulary = {}
        self.vocabulary_list = []
        idx = 0
        for message in data:
            for word in message:
                if word not in self.vocabulary:
                    self.vocabulary[word] = idx
                    self.vocabulary_list.append(word)
                    idx += 1
        print(f"Dimensiune vocabular: {len(self.vocabulary)}")

    def get_features(self, data):
        """
        Obține reprezentarea BoW pentru o listă de mesaje.

        data : list de list de str — mesajele de procesat

        Returnează:
            np.array shape (len(data), len(vocabulary)) cu frecvențele cuvintelor
        """
        n_samples = len(data)
        vocab_size = len(self.vocabulary)
        features   = np.zeros((n_samples, vocab_size), dtype=np.int32)

        for i, message in enumerate(data):
            for word in message:
                if word in self.vocabulary:
                    word_idx = self.vocabulary[word]
                    features[i, word_idx] += 1
                # Cuvintele din vocabular sunt ignorate (OOV - out of vocabulary)

        return features


# DEMO cu mesaje simple
train_messages = [
    ['hello', 'world', 'free', 'prize'],
    ['hello', 'friend', 'how', 'are', 'you'],
    ['FREE', 'CALL', 'NOW', 'WIN', 'prize'],
    ['hey', 'are', 'you', 'coming', 'today'],
]
test_messages = [
    ['hello', 'FREE', 'unknown_word'],
    ['you', 'are', 'friend'],
]
labels_demo = np.array([1, 0, 1, 0])  # 1 = spam, 0 = ham

bow = BagOfWords()
bow.build_vocabulary(train_messages)
train_features = bow.get_features(train_messages)
test_features  = bow.get_features(test_messages)

print(f"\nTrain features shape: {train_features.shape}")
print(f"Primele 2 linii:\n{train_features[:2]}")

# Normalizare L2 pe features BoW (recomandat cu SVM)
train_norm, test_norm = normalize_data(
    train_features.astype(float),
    test_features.astype(float),
    norm_type='l2'
)

# =============================================================================
# 4. SVM — SKLEARN
# =============================================================================

print("\n" + "=" * 60)
print("4. SVM — SKLEARN")
print("=" * 60)

"""
SVM cu sklearn.svm.SVC

Parametri importanți:
    C     : penalitate eroare (default=1.0)
    kernel: 'linear' | 'rbf' | 'poly' | 'sigmoid'
    gamma : coef. kernel RBF ('scale' | 'auto' | float)

Metode:
    svm_model.fit(X_train, y_train)
    svm_model.predict(X_test)
    svm_model.score(X_test, y_test)
    svm_model.coef_  # ponderile (doar pentru kernel='linear')
                     # shape: (n_classes, n_features) sau (1, n_features) pentru 2 clase
"""

# --- 4.1 Încărcare date SMS Spam ---
def load_sms_data():
    """
    Încearcă să încarce datele SMS Spam din laborator.
    Fallback: generează date sintetice demonstrative.
    """
    # Structura datelor din laborator:
    # Fiecare linie: "spam/ham cuvant1 cuvant2 ..."
    # Sau separate în train/test cu labels separat

    # Generăm date sintetice pentru demonstrație
    print("Generând date SMS demo (înlocuiește cu datele reale din arhivă)")

    spam_words = ['FREE', 'CALL', 'WIN', 'PRIZE', 'URGENT', 'GUARANTEED',
                  'mobile', 'txt', 'STOP', 'claim', 'Cash', 'award']
    ham_words  = ['hello', 'hi', 'hey', 'how', 'are', 'you', 'friend',
                  'going', 'today', 'ok', 'great', 'see', 'tomorrow']

    np.random.seed(42)
    train_msgs, train_y = [], []
    for _ in range(200):  # 200 spam
        msg = list(np.random.choice(spam_words, size=np.random.randint(3, 8)))
        msg += list(np.random.choice(ham_words, size=np.random.randint(0, 3)))
        train_msgs.append(msg)
        train_y.append(1)
    for _ in range(1200):  # 1200 ham (raport 6:1)
        msg = list(np.random.choice(ham_words, size=np.random.randint(3, 10)))
        train_msgs.append(msg)
        train_y.append(0)

    test_msgs, test_y = [], []
    for _ in range(100):
        msg = list(np.random.choice(spam_words, size=np.random.randint(3, 8)))
        test_msgs.append(msg)
        test_y.append(1)
    for _ in range(600):
        msg = list(np.random.choice(ham_words, size=np.random.randint(3, 10)))
        test_msgs.append(msg)
        test_y.append(0)

    return train_msgs, np.array(train_y), test_msgs, np.array(test_y)

train_msgs, train_labels_sms, test_msgs, test_labels_sms = load_sms_data()

# BoW + normalizare
bow_sms = BagOfWords()
bow_sms.build_vocabulary(train_msgs)
train_f = bow_sms.get_features(train_msgs).astype(float)
test_f  = bow_sms.get_features(test_msgs).astype(float)
train_norm_sms, test_norm_sms = normalize_data(train_f, test_f, norm_type='l2')

# --- 4.2 SVM Linear ---
print("\n--- SVM cu kernel Linear ---")
svm_linear = svm.SVC(
    C=1.0,          # SCHIMBABIL: testează {0.1, 1, 10, 100}
    kernel='linear',
    random_state=42
)
svm_linear.fit(train_norm_sms, train_labels_sms)
y_pred_linear = svm_linear.predict(test_norm_sms)

acc_linear = accuracy_score(test_labels_sms, y_pred_linear)
f1_linear  = f1_score(test_labels_sms, y_pred_linear, average='binary',
                       pos_label=1, zero_division=0)
print(f"Acuratețe: {acc_linear:.4f}")
print(f"F1-Score:  {f1_linear:.4f}")

# Cuvintele cu cele mai mari/mici ponderi (kernel linear)
if hasattr(svm_linear, 'coef_'):
    coefs = svm_linear.coef_[0]
    sorted_idx  = np.argsort(coefs)
    vocab_arr   = np.array(bow_sms.vocabulary_list)
    print(f"\nTop 10 cuvinte SPAM (ponderi mari pozitiv nu înseamnă neapărat spam):")
    print(f"  cele mai negative (spam): {vocab_arr[sorted_idx[:10]]}")
    print(f"  cele mai pozitive (ham):  {vocab_arr[sorted_idx[-10:]]}")

# --- 4.3 SVM RBF ---
print("\n--- SVM cu kernel RBF ---")
svm_rbf = svm.SVC(
    C=1.0,          # SCHIMBABIL
    kernel='rbf',
    gamma='scale',  # SCHIMBABIL: 'scale', 'auto', sau float
    random_state=42
)
svm_rbf.fit(train_norm_sms, train_labels_sms)
y_pred_rbf = svm_rbf.predict(test_norm_sms)
acc_rbf = accuracy_score(test_labels_sms, y_pred_rbf)
f1_rbf  = f1_score(test_labels_sms, y_pred_rbf, average='binary',
                    pos_label=1, zero_division=0)
print(f"Acuratețe: {acc_rbf:.4f}")
print(f"F1-Score:  {f1_rbf:.4f}")

# --- 4.4 Comparare C (hiperparametru) ---
print("\n--- Comparare parametru C ---")
for C_val in [0.1, 1, 10, 100]:
    model = svm.SVC(C=C_val, kernel='linear', random_state=42)
    model.fit(train_norm_sms, train_labels_sms)
    acc = model.score(test_norm_sms, test_labels_sms)
    print(f"  C={C_val:5}: Acuratețe={acc:.4f}")

# =============================================================================
# 5. F1-SCORE — EXPLICAȚIE
# =============================================================================
"""
F1-Score este important când clasele sunt dezechilibrate (de ex. 6:1 ham:spam).

Precision = TP / (TP + FP)  — din mesajele prezise spam, câte chiar sunt spam
Recall    = TP / (TP + FN)  — din mesajele spam reale, câte am detectat
F1        = 2 * (Precision * Recall) / (Precision + Recall)

average='binary':  calculat pentru clasa pozitivă (spam=1)
average='macro':   media aritmetică pentru toate clasele (fiecare cu aceeași pondere)
average='weighted': media ponderată cu suportul fiecărei clase

from sklearn.metrics import classification_report
print(classification_report(test_labels_sms, y_pred_linear))
"""

from sklearn.metrics import classification_report
print("\n--- Report complet (SVM linear) ---")
print(classification_report(test_labels_sms, y_pred_linear,
                             target_names=['ham', 'spam'], zero_division=0))

# =============================================================================
# 6. SKLEARN CountVectorizer — ALTERNATIVĂ LA BOW DIN SCRATCH
# =============================================================================

print("\n" + "=" * 60)
print("6. SKLEARN CountVectorizer (echivalent BoW)")
print("=" * 60)

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# CountVectorizer face exact ce face BagOfWords de mai sus, dar mai eficient
train_texts = [' '.join(msg) for msg in train_msgs]  # lista de stringuri
test_texts  = [' '.join(msg) for msg in test_msgs]

vectorizer = CountVectorizer()
X_train_cv = vectorizer.fit_transform(train_texts)  # returnează matrice sparsă
X_test_cv  = vectorizer.transform(test_texts)

# Normalizare L2 pe matrice sparsă
from sklearn.preprocessing import normalize
X_train_cv_norm = normalize(X_train_cv, norm='l2')
X_test_cv_norm  = normalize(X_test_cv, norm='l2')

svm_cv = svm.SVC(C=1.0, kernel='linear', random_state=42)
svm_cv.fit(X_train_cv_norm, train_labels_sms)
acc_cv = svm_cv.score(X_test_cv_norm, test_labels_sms)
print(f"Acuratețe cu CountVectorizer: {acc_cv:.4f}")

# TF-IDF — mai bun decât BoW simplu: ponderează cuvintele rare mai mult
vectorizer_tfidf = TfidfVectorizer()
X_train_tfidf = vectorizer_tfidf.fit_transform(train_texts)
X_test_tfidf  = vectorizer_tfidf.transform(test_texts)
svm_tfidf = svm.SVC(C=1.0, kernel='linear', random_state=42)
svm_tfidf.fit(X_train_tfidf, train_labels_sms)
acc_tfidf = svm_tfidf.score(X_test_tfidf, test_labels_sms)
print(f"Acuratețe cu TF-IDF: {acc_tfidf:.4f}")

# =============================================================================
# NOTE: CE POATE FI MODIFICAT
# =============================================================================
"""
VARIANTE ȘI IMPACTE:

1. Parametrul C (SVM):
   - C mare (100, 1000): mai mulți vectori suport, frontieră complexă → overfitting
   - C mic (0.01, 0.1): mai puțini vectori suport, frontieră simplă → underfitting
   - Optim: căutat cu GridSearchCV sau cross-validation

2. Kernel:
   - 'linear': rapid, interpretabil (coef_ disponibil), bun pentru text BoW
   - 'rbf': mai puternic pentru date neliniar separabile, dar mai lent
   - Modificare cod: doar schimbi kernel='rbf' și adaugi gamma
   - Cu RBF, coef_ NU mai e disponibil (model non-liniar)

3. Normalizare:
   - None: funcționează rău dacă atributele au scări diferite
   - 'l2': recomandat pentru SVM (face vectorii unitari)
   - 'standard': recomandat când atributele au distribuții diferite
   - Impactul: cu SVM, normalizarea L2 a feature-urilor BoW e esențială

4. BoW vs TF-IDF:
   - BoW: frecvențe brute — cuvintele comune (ex: "the") au ponderi mari
   - TF-IDF: cuvintele rare și informative primesc ponderi mai mari
   - TF-IDF performează de obicei mai bine pentru clasificare text

5. One-vs-One vs One-vs-All:
   - sklearn SVC folosește OVO (One-vs-One) implicit
   - sklearn LinearSVC folosește OVA (One-vs-All) — mai rapid pentru multe clase
   - from sklearn.svm import LinearSVC  # mai rapid pentru n_classes >> 2

6. Preprocesare text (neacoperită în laborator dar importantă):
   - Lowercase, eliminare punctuație, stopwords, stemming
   - Îmbunătățește calitatea vocabularului și acuratețea
"""

print("\nLaborator 4 completat!")
