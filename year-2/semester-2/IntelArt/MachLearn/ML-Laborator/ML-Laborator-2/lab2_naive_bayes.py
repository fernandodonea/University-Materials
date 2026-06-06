"""
=============================================================================
LABORATOR 2 - Naive Bayes pe MNIST
=============================================================================
Materie: Inteligență Artificială - Machine Learning
Acoperire: Regula Bayes, Naive Bayes din scratch, MultinomialNB sklearn,
           discretizare valori continue, matrice de confuzie

RULARE: python lab2_naive_bayes.py
Dependențe: pip install numpy matplotlib scikit-learn
Date: descarcă arhiva de pe site-ul cursului (train_images.txt, test_images.txt,
      train_labels.txt, test_labels.txt)
      SAU rulează cu MNIST din sklearn ca fallback (generat automat mai jos)
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import os

# =============================================================================
# 1. TEORIA — REGULA LUI BAYES ȘI NAIVE BAYES
# =============================================================================
"""
REGULA BAYES:
    P(c|X) = P(X|c) * P(c) / P(X)

    Deoarece P(X) este constant pentru toți c, maximizăm:
    argmax_c P(c|X) = argmax_c P(X|c) * P(c)

NAIVE BAYES (presupune independența atributelor):
    P(c|X) = P(c) * prod_{i=1}^{n} P(x_i|c)

    Aplicând log (pentru stabilitate numerică):
    log P(c|X) ≈ log P(c) + sum_{i=1}^{n} log P(x_i|c)

PENTRU MNIST (28x28 = 784 pixeli, clasificare cifre 0-9):
    - Fiecare pixel este un atribut
    - Presupunem că pixelii sunt independenți
    - Valorile continue (0-255) trebuie discretizate înainte

FORMULELE:
    P(c) = nr_exemple_clasa_c / nr_total_exemple
    P(x_i | c) = nr_exemple_din_clasa_c_cu_pixelul_i_egal_x / nr_exemple_clasa_c
"""

# =============================================================================
# 2. ÎNCĂRCARE DATE
# =============================================================================

def load_mnist_data():
    """
    Încearcă să încarce datele din fișierele laboratorului.
    Dacă nu există, folosește sklearn MNIST ca fallback.
    """
    if os.path.exists('train_images.txt'):
        print("Încărcând datele din fișierele laboratorului...")
        train_images = np.loadtxt('train_images.txt')
        train_labels = np.loadtxt('train_labels.txt').astype(int)
        test_images  = np.loadtxt('test_images.txt')
        test_labels  = np.loadtxt('test_labels.txt').astype(int)
    else:
        print("Fișierele laboratorului nu au fost găsite.")
        print("Folosind sklearn MNIST (70k imagini, poate fi mai lent)...")
        from sklearn.datasets import fetch_openml
        mnist = fetch_openml('mnist_784', version=1, as_frame=False)
        X = mnist.data.astype(np.float64)
        y = mnist.target.astype(int)
        # Subsamplingăm la 1000 train, 500 test (ca în laborator)
        train_images = X[:1000]
        train_labels = y[:1000]
        test_images  = X[1000:1500]
        test_labels  = y[1000:1500]

    print(f"Train: {train_images.shape}, Test: {test_images.shape}")
    print(f"Label range: {train_labels.min()} - {train_labels.max()}")
    return train_images, train_labels, test_images, test_labels

train_images, train_labels, test_images, test_labels = load_mnist_data()

# =============================================================================
# 3. VIZUALIZARE IMAGINE
# =============================================================================

def show_image(image_vector, label=None, title=None):
    """Afișează un vector 784 ca imagine 28x28."""
    image_2d = np.reshape(image_vector, (28, 28))
    plt.imshow(image_2d.astype(np.uint8), cmap='gray')
    t = title if title else f"Label: {label}"
    plt.title(t)
    plt.axis('off')
    plt.show()

# Afișăm prima imagine
show_image(train_images[0], train_labels[0])

# =============================================================================
# 4. DISCRETIZARE VALORI CONTINUE (bins)
# =============================================================================

def values_to_bins(X, bins):
    """
    Discretizează matricea X folosind intervalele 'bins'.

    Parametri:
        X    : np.array shape (n_samples, n_features) — valori continue [0, 255]
        bins : array cu capetele intervalelor (din np.linspace)

    Returnează:
        np.array shape (n_samples, n_features) — indici interval (de la 1)

    ATENȚIE: np.digitize returnează indici de la 1 (nu 0)!
    """
    return np.digitize(X, bins)

# num_bins determină granularitatea discretizării
# Valori mici → mai puțini parametri, mai puțin precise
# Valori mari → mai mulți parametri, risc de suprainvățare
NUM_BINS = 5  # SCHIMBABIL: testează {3, 5, 7, 9, 11}

bins = np.linspace(start=0, stop=255, num=NUM_BINS)
print(f"\nBins ({NUM_BINS} intervale): {bins}")

train_discretized = values_to_bins(train_images, bins)
test_discretized  = values_to_bins(test_images, bins)

print(f"Valori originale [0]: min={train_images[0].min()}, max={train_images[0].max()}")
print(f"Valori discrete [0]: min={train_discretized[0].min()}, max={train_discretized[0].max()}")

# =============================================================================
# 5. NAIVE BAYES DIN SCRATCH
# =============================================================================

class NaiveBayesClassifier:
    """
    Implementare Naive Bayes Multinomial din scratch.

    Parametri constructor:
        num_bins : int — numărul de intervale pentru discretizare

    Metode:
        fit(X, y)     — antrenare
        predict(X)    — prezicere
        score(X, y)   — acuratețe
    """

    def __init__(self, num_bins=5):
        self.num_bins = num_bins
        self.class_priors = None        # log P(c)
        self.feature_probs = None       # log P(x_i | c)
        self.classes = None
        self.num_classes = None
        self.num_features = None

    def fit(self, X, y):
        """
        Antrenare: calculează prior-urile claselor și probabilitățile condiționate.

        X : shape (n_samples, n_features) — date discretizate
        y : shape (n_samples,) — etichete
        """
        self.classes     = np.unique(y)
        self.num_classes  = len(self.classes)
        self.num_features = X.shape[1]
        n_samples         = X.shape[0]

        # P(c) = nr_exemple_clasa_c / nr_total
        self.class_priors = np.zeros(self.num_classes)

        # P(x_i = val | c) pentru fiecare clasă, fiecare feature, fiecare valoare posibilă
        # shape: (num_classes, num_features, num_bins+1)
        self.feature_probs = np.zeros((self.num_classes, self.num_features, self.num_bins + 2))

        for idx, c in enumerate(self.classes):
            X_c = X[y == c]
            self.class_priors[idx] = X_c.shape[0] / n_samples

            for feature in range(self.num_features):
                counts = np.bincount(X_c[:, feature].astype(int),
                                     minlength=self.num_bins + 2)
                # Laplace smoothing: adăugăm 1 la fiecare numărătoare
                # Previne log(0) când o valoare nu apare în antrenare
                counts = counts + 1
                self.feature_probs[idx, feature] = counts / counts.sum()

        # Lucrăm în spațiul log pentru stabilitate numerică
        self.log_class_priors = np.log(self.class_priors)
        self.log_feature_probs = np.log(self.feature_probs)

    def predict(self, X):
        """
        Predicție: returnează clasa cu probabilitatea log maximă.

        X : shape (n_samples, n_features)
        """
        predictions = []

        for sample in X:
            # log P(c|X) ≈ log P(c) + sum_i log P(x_i | c)
            log_posteriors = self.log_class_priors.copy()

            for feature, value in enumerate(sample.astype(int)):
                val = min(value, self.num_bins + 1)
                log_posteriors += self.log_feature_probs[:, feature, val]

            predictions.append(self.classes[np.argmax(log_posteriors)])

        return np.array(predictions)

    def score(self, X, y):
        return np.mean(self.predict(X) == y)


# Antrenare și evaluare
nb_scratch = NaiveBayesClassifier(num_bins=NUM_BINS)
nb_scratch.fit(train_discretized, train_labels)
acc_scratch = nb_scratch.score(test_discretized, test_labels)
print(f"\n[Scratch] Acuratețe Naive Bayes (bins={NUM_BINS}): {acc_scratch:.4f}")

# =============================================================================
# 6. MULTINOMIAL NAIVE BAYES — SKLEARN
# =============================================================================

print("\n" + "=" * 60)
print("6. SKLEARN MultinomialNB")
print("=" * 60)

"""
MultinomialNB din sklearn:
    - Parametru principal: alpha (Laplace/Lidstone smoothing, default=1.0)
    - alpha > 0 previne probabilitățile zero
    - alpha mic → mai puțin smoothing → mai sensibil la date
    - alpha mare → mai mult smoothing → mai robust la date rare
"""

# Pași standard sklearn:
# 1. import
# 2. definire model
naive_bayes_model = MultinomialNB(alpha=1.0)   # SCHIMBABIL: alpha ∈ {0.1, 0.5, 1.0, 2.0}

# 3. antrenare
naive_bayes_model.fit(train_discretized, train_labels)

# 4. predicție
y_pred = naive_bayes_model.predict(test_discretized)

# 5. evaluare
acc_sklearn = naive_bayes_model.score(test_discretized, test_labels)
print(f"Acuratețe MultinomialNB sklearn: {acc_sklearn:.4f}")

# Testare pentru diferite valori de num_bins
print("\n--- Acuratețe pentru diferite num_bins ---")
for nb in [3, 5, 7, 9, 11]:
    bins_i = np.linspace(0, 255, nb)
    train_d = values_to_bins(train_images, bins_i)
    test_d  = values_to_bins(test_images, bins_i)
    model   = MultinomialNB(alpha=1.0)
    model.fit(train_d, train_labels)
    acc = model.score(test_d, test_labels)
    print(f"  num_bins={nb:2d}: {acc:.4f}")

# =============================================================================
# 7. MATRICEA DE CONFUZIE
# =============================================================================

def confusion_matrix_custom(y_true, y_pred):
    """
    Calculează matricea de confuzie.
    C[i, j] = numărul de exemple din clasa i clasificate ca clasa j.

    y_true, y_pred: array de etichete (valori în {0..num_classes-1})
    """
    classes   = np.unique(np.concatenate([y_true, y_pred]))
    n_classes = len(classes)
    cm        = np.zeros((n_classes, n_classes), dtype=int)

    for i, true_c in enumerate(classes):
        for j, pred_c in enumerate(classes):
            cm[i, j] = np.sum((y_true == true_c) & (y_pred == pred_c))

    return cm

cm = confusion_matrix_custom(test_labels, y_pred)
print(f"\nMATRICEA DE CONFUZIE (shape {cm.shape}):")
print(cm)

# Vizualizare grafică a matricei de confuzie
fig, ax = plt.subplots(figsize=(8, 7))
im = ax.imshow(cm, cmap='Blues')
plt.colorbar(im)
ax.set_xlabel('Clasa prezisă')
ax.set_ylabel('Clasa reală')
ax.set_title('Matricea de confuzie — Naive Bayes MNIST')
ax.set_xticks(np.arange(cm.shape[0]))
ax.set_yticks(np.arange(cm.shape[0]))
plt.tight_layout()
plt.show()

# =============================================================================
# 8. EXEMPLE MISCLASIFICATE
# =============================================================================

misclassified_idx = np.where(y_pred != test_labels)[0]
print(f"\nNr. exemple misclasificate: {len(misclassified_idx)}")

fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    if i < len(misclassified_idx):
        idx = misclassified_idx[i]
        img = test_images[idx].reshape(28, 28)
        ax.imshow(img.astype(np.uint8), cmap='gray')
        ax.set_title(f"Real:{test_labels[idx]} Pred:{y_pred[idx]}", fontsize=8)
        ax.axis('off')
plt.suptitle('Exemple misclasificate')
plt.tight_layout()
plt.show()

# =============================================================================
# 9. EXERCIȚIUL 1 DIN LABORATOR — Calcul manual Bayes
# =============================================================================

print("\n" + "=" * 60)
print("9. EXERCIȚIU 1 — Calcul manual (înălțimi Fată/Băiat)")
print("=" * 60)

"""
Date antrenare: [(160,F),(165,F),(155,F),(172,F),(175,B),(180,B),(177,B),(190,B)]
Intervale (4): 150-160, 161-170, 171-180, 181-190
Exemplu nou: 178 cm → interval 171-180 (indice 3)
"""

# Înălțimi și etichete
heights = np.array([160, 165, 155, 172, 175, 180, 177, 190])
labels  = np.array(['F', 'F', 'F', 'F', 'B', 'B', 'B', 'B'])

bins_h = np.array([150, 160, 170, 180, 190])
disc_h = np.digitize(heights, bins_h)

new_person = 178
new_disc   = np.digitize(np.array([new_person]), bins_h)[0]
print(f"Interval 178cm: {new_disc}")  # 3 (intervalul 171-180)

# P(F) și P(B)
pF = np.sum(labels == 'F') / len(labels)  # 0.5
pB = np.sum(labels == 'B') / len(labels)  # 0.5

# P(interval_3 | F) și P(interval_3 | B)
fete     = disc_h[labels == 'F']
baieti   = disc_h[labels == 'B']
p_int_F  = np.sum(fete == new_disc) / len(fete)
p_int_B  = np.sum(baieti == new_disc) / len(baieti)

print(f"P(F) = {pF}, P(B) = {pB}")
print(f"P(interval_3 | F) = {p_int_F}")
print(f"P(interval_3 | B) = {p_int_B}")
print(f"P(F|178) ∝ {pF * p_int_F}")
print(f"P(B|178) ∝ {pB * p_int_B}")
print(f"Predicție: {'Fată' if pF*p_int_F > pB*p_int_B else 'Băiat'}")

# =============================================================================
# NOTE: CE POATE FI MODIFICAT
# =============================================================================
"""
VARIANTE ȘI IMPACTE:

1. num_bins (numărul de intervale):
   - Mic (3-5): mai puțin discriminativ, dar robust la date puține
   - Mare (9-11): mai discriminativ, dar poate overfita
   - Optim pentru MNIST: ~5-7 pe subsetul de 1000 exemple

2. alpha (Laplace smoothing în MultinomialNB):
   - alpha=0: fără smoothing → P=0 pentru valori nevăzute → probleme cu log(0)
   - alpha=1 (default): smoothing Laplace standard
   - alpha>1: mai mult smoothing → model mai "blând"
   - Impactul: afectează clasificarea pe clase rare sau atribute rar văzute

3. Presupunerea de independență:
   - Naive Bayes presupune că pixelii sunt independenți (presupunere FALSE!)
   - În realitate, pixelii vecini sunt corelați
   - Cu toate acestea, NB funcționează surprinzător de bine în practică

4. Alternativă: GaussianNB din sklearn:
   - Folosit când atributele sunt continue (nu necesită discretizare)
   - from sklearn.naive_bayes import GaussianNB
   - model = GaussianNB()
   - Modelează P(x_i | c) cu o distribuție Gaussiană
"""

print("\nLaborator 2 completat!")
