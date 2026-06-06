"""
=============================================================================
MODEL: Support Vector Machine (SVM) — Setup Complet, Gata de Rulat
=============================================================================
Lab: 4 | Dataset: SMS Spam Classification
Algoritm: SVM cu kernel Linear și RBF, Bag-of-Words, normalizare L2

RULARE: python model_svm.py
pip install numpy scikit-learn
=============================================================================
"""

import numpy as np
from sklearn import svm, preprocessing
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# ===================== HYPERPARAMETRI (SCHIMBĂ AICI) ========================
C_VALUE = 1.0       # penalitate eroare: {0.01, 0.1, 1, 10, 100}
KERNEL  = 'linear'  # kernel: 'linear' | 'rbf'
GAMMA   = 'scale'   # coef. RBF: 'scale' | 'auto' | float (doar pentru RBF)
NORM    = 'l2'      # normalizare: 'l1' | 'l2' | 'standard' | None
# ============================================================================

# --- Încărcare date SMS Spam ---
import os

def load_sms_spam_data():
    """
    Dacă ai datele din laborator, structura e:
    Fișier CSV/TSV cu coloane: label (spam/ham), message
    Înlocuiește codul de mai jos cu citirea din fișierele reale.
    """
    if os.path.exists('data_spam.txt'):
        # Înlocuiește cu citirea fișierului tău
        # Exemplu format: "spam\tURGENT! Win a prize..."
        # train_msgs, train_labels, test_msgs, test_labels = parse_file(...)
        pass

    print("[INFO] Generez date SMS demo.")
    spam_words = ['FREE', 'CALL', 'WIN', 'PRIZE', 'URGENT', 'GUARANTEED',
                  'mobile', 'txt', 'STOP', 'claim', 'Cash', 'award', 'TEXT',
                  'WINNER', 'service', 'number', 'Send', 'reply', 'contact']
    ham_words  = ['hello', 'hi', 'hey', 'how', 'are', 'you', 'friend',
                  'going', 'today', 'ok', 'great', 'see', 'tomorrow', 'home',
                  'good', 'morning', 'night', 'thanks', 'please', 'coming']
    np.random.seed(42)

    def gen_msgs(spam_n, ham_n):
        msgs, labels = [], []
        for _ in range(spam_n):
            msg = list(np.random.choice(spam_words, np.random.randint(3,8)))
            msg += list(np.random.choice(ham_words, np.random.randint(0,3)))
            msgs.append(msg); labels.append(1)
        for _ in range(ham_n):
            msg = list(np.random.choice(ham_words, np.random.randint(3,10)))
            msgs.append(msg); labels.append(0)
        return msgs, np.array(labels)

    tr_msgs, tr_lbl = gen_msgs(800,  4800)   # 6:1 raport ham:spam
    te_msgs, te_lbl = gen_msgs(100,  600)
    return tr_msgs, tr_lbl, te_msgs, te_lbl

train_msgs, train_labels, test_msgs, test_labels = load_sms_spam_data()
print(f"Train: {len(train_msgs)} mesaje | Test: {len(test_msgs)} mesaje")
print(f"Train spam: {train_labels.sum()}, ham: {(train_labels==0).sum()}")

# --- Bag of Words ---
class BagOfWords:
    def __init__(self):
        self.vocabulary = {}
        self.vocabulary_list = []

    def build_vocabulary(self, data):
        self.vocabulary = {}
        self.vocabulary_list = []
        idx = 0
        for msg in data:
            for word in msg:
                if word not in self.vocabulary:
                    self.vocabulary[word] = idx
                    self.vocabulary_list.append(word)
                    idx += 1
        print(f"Dimensiune vocabular: {len(self.vocabulary)}")

    def get_features(self, data):
        features = np.zeros((len(data), len(self.vocabulary)), dtype=np.float64)
        for i, msg in enumerate(data):
            for word in msg:
                if word in self.vocabulary:
                    features[i, self.vocabulary[word]] += 1
        return features

bow = BagOfWords()
bow.build_vocabulary(train_msgs)
X_train_raw = bow.get_features(train_msgs)
X_test_raw  = bow.get_features(test_msgs)

# --- Normalizare ---
def normalize_data(train_data, test_data, norm_type='l2'):
    if norm_type is None:
        return train_data, test_data
    elif norm_type == 'standard':
        scaler = preprocessing.StandardScaler()
        return scaler.fit_transform(train_data), scaler.transform(test_data)
    elif norm_type in ('l1', 'l2'):
        norm   = preprocessing.Normalizer(norm=norm_type)
        return norm.transform(train_data), norm.transform(test_data)
    raise ValueError(f"norm_type necunoscut: {norm_type}")

X_train, X_test = normalize_data(X_train_raw, X_test_raw, NORM)

# --- Model SVM ---
model = svm.SVC(
    C=C_VALUE,
    kernel=KERNEL,
    gamma=GAMMA if KERNEL == 'rbf' else 'scale',
    random_state=42
)

# Antrenare
print(f"\nAntrenare SVM (kernel={KERNEL}, C={C_VALUE})...")
model.fit(X_train, train_labels)

# Predicție și evaluare
y_pred = model.predict(X_test)
acc    = accuracy_score(test_labels, y_pred)
f1     = f1_score(test_labels, y_pred, average='binary', pos_label=1, zero_division=0)
print(f"\nAcuratețe: {acc:.4f}")
print(f"F1-Score:  {f1:.4f}")
print(classification_report(test_labels, y_pred,
                             target_names=['ham', 'spam'], zero_division=0))

# Analiza cuvintelor (NUMAI pentru kernel='linear')
if KERNEL == 'linear' and hasattr(model, 'coef_'):
    coefs    = model.coef_[0]
    vocab    = np.array(bow.vocabulary_list)
    sorted_i = np.argsort(coefs)
    print(f"\nTop 10 cuvinte cu ponderi negative (spam):")
    print(f"  {vocab[sorted_i[:10]]}")
    print(f"Top 10 cuvinte cu ponderi pozitive (ham):")
    print(f"  {vocab[sorted_i[-10:][::-1]]}")

# Comparare C
print("\n--- Comparare C (kernel=linear) ---")
for C in [0.01, 0.1, 1, 10, 100]:
    m = svm.SVC(C=C, kernel='linear', random_state=42)
    m.fit(X_train, train_labels)
    a = m.score(X_test, test_labels)
    f = f1_score(test_labels, m.predict(X_test), pos_label=1, zero_division=0)
    print(f"  C={C:6}: acc={a:.4f}, f1={f:.4f}")

# Comparare kernel
print("\n--- Comparare kernel ---")
for ker, g in [('linear', 'scale'), ('rbf', 'scale'), ('rbf', 0.1)]:
    m = svm.SVC(C=1.0, kernel=ker, gamma=g, random_state=42)
    m.fit(X_train, train_labels)
    a = m.score(X_test, test_labels)
    print(f"  kernel={ker}, gamma={g}: acc={a:.4f}")

print("\nModel SVM completat!")
