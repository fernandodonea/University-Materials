"""
=============================================================================
LABORATOR 3 - K-Nearest Neighbors (KNN) pe MNIST
=============================================================================
Materie: Inteligență Artificială - Machine Learning
Acoperire: KNN din scratch, distanțele L1 și L2, alegerea K,
           comparare performanță, funcții numpy esențiale

RULARE: python lab3_knn.py
Dependențe: pip install numpy matplotlib scikit-learn
Date: train_images.txt, test_images.txt, train_labels.txt, test_labels.txt
      (sau fallback automat sklearn MNIST)
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# =============================================================================
# 1. TEORIA — K-NEAREST NEIGHBORS
# =============================================================================
"""
KNN — Metoda celor mai apropiați K vecini:

CLASIFICARE:
  - Stochează TOATE datele de antrenare (model "lazy" — nu există antrenare propriu-zisă)
  - Pentru un exemplu nou X_test:
    1. Calculează distanța de la X_test la fiecare exemplu din antrenare
    2. Selectează cei mai apropiați K vecini
    3. Atribuie eticheta cu cele mai multe voturi dintre vecini

DISTANȚE:
  L1 (Manhattan): d(X,Y) = sum |X_i - Y_i|
  L2 (Euclidean): d(X,Y) = sqrt(sum (X_i - Y_i)^2)

  L1 vs L2:
  - L1 e mai robustă la outlieri (nu ridică la pătrat diferențele mari)
  - L2 e mai sensibilă la outlieri dar mai utilizată în practică
  - Pe imagini, L2 tinde să performeze mai bine

HIPERPARAMETRI:
  - K (num_neighbors):
    K=1 → overfitting (sensibil la zgomot)
    K mare → underfitting (supra-netezire a frontierei de decizie)
    Optim: K ∈ {3, 5, 7, 9} (valori impare pentru a evita egalitățile)

  - Distanța: L1 sau L2

COMPLEXITATE:
  - Predicție O(n*d) per exemplu, unde n=nr antrenare, d=nr features
  - Scump computațional pentru seturi mari
"""

# =============================================================================
# 2. ÎNCĂRCARE DATE
# =============================================================================

def load_data():
    if os.path.exists('train_images.txt'):
        print("Încărcând datele laboratorului...")
        train_images = np.loadtxt('train_images.txt')
        train_labels = np.loadtxt('train_labels.txt').astype(int)
        test_images  = np.loadtxt('test_images.txt')
        test_labels  = np.loadtxt('test_labels.txt').astype(int)
    else:
        print("Fișierele lipsesc. Folosesc sklearn MNIST (1000 train, 500 test)...")
        from sklearn.datasets import fetch_openml
        mnist = fetch_openml('mnist_784', version=1, as_frame=False)
        X, y = mnist.data.astype(np.float64), mnist.target.astype(int)
        train_images, train_labels = X[:1000], y[:1000]
        test_images,  test_labels  = X[1000:1500], y[1000:1500]

    print(f"Train: {train_images.shape}, Test: {test_images.shape}")
    return train_images, train_labels, test_images, test_labels

train_images, train_labels, test_images, test_labels = load_data()

# =============================================================================
# 3. CLASA KNN DIN SCRATCH (exact ca în laborator)
# =============================================================================

class KnnClassifier:
    """
    KNN Classifier implementat din scratch.

    Constructor primește datele de antrenare și le stochează.
    Nu există pas de "antrenare" propriu-zisă — KNN e un learner "lazy".
    """

    def __init__(self, train_images, train_labels):
        self.train_images = train_images    # shape: (n_train, n_features)
        self.train_labels = train_labels    # shape: (n_train,)

    def classify_image(self, test_image, num_neighbors=3, metric='l2'):
        """
        Clasifică un singur exemplu folosind KNN.

        Parametri:
            test_image    : np.array shape (1, n_features) sau (n_features,)
            num_neighbors : int — K, numărul de vecini luați în considerare
            metric        : str — 'l1' sau 'l2'

        Returnează:
            int — eticheta prezisă

        NOTE:
        - train_images.shape = (n_train, n_features) — exemple pe linii
        - test_image.shape = (1, n_features) sau (n_features,)
        """
        # Calculul distanțelor vectorizat (fără for-loop!)
        if metric == 'l2':
            # d(X, Y) = sqrt(sum (X_i - Y_i)^2)
            diff = self.train_images - test_image  # broadcasting: (n_train, features) - (features,)
            distances = np.sqrt(np.sum(diff ** 2, axis=1))
        elif metric == 'l1':
            # d(X, Y) = sum |X_i - Y_i|
            diff = self.train_images - test_image
            distances = np.sum(np.abs(diff), axis=1)
        else:
            raise ValueError(f"Metric necunoscut: {metric}. Folosiți 'l1' sau 'l2'.")

        # Indecșii celor mai apropiați K vecini
        # argsort returnează indecșii care ar sorta array-ul (crescător)
        sorted_indices = np.argsort(distances)         # sortat crescător după distanță
        k_nearest_idx  = sorted_indices[:num_neighbors] # primii K

        # Etichetele vecinilor
        k_labels = self.train_labels[k_nearest_idx]

        # Votul majoritar: bincount numără aparițiile fiecărei etichete
        # Dacă etichetele sunt 0-9, bincount returnează vectorul de frecvențe
        votes     = np.bincount(k_labels, minlength=10)  # vector de 10 elemente
        predicted = np.argmax(votes)                       # eticheta cu cele mai multe voturi

        return predicted

    def classify_all(self, test_images, num_neighbors=3, metric='l2'):
        """
        Clasifică toate imaginile de test.
        ATENȚIE: poate fi lent pentru seturi mari!
        """
        predictions = []
        n = test_images.shape[0]
        for i in range(n):
            pred = self.classify_image(test_images[i], num_neighbors, metric)
            predictions.append(pred)
            if (i + 1) % 50 == 0:
                print(f"  Procesate {i+1}/{n} exemple...")
        return np.array(predictions)

    def score(self, test_images, test_labels, num_neighbors=3, metric='l2'):
        """Calculează acuratețea pe mulțimea de test."""
        preds = self.classify_all(test_images, num_neighbors, metric)
        return np.mean(preds == test_labels), preds


# =============================================================================
# 4. EXERCIȚIUL 3 — Acuratețe K=3, L2
# =============================================================================

knn = KnnClassifier(train_images, train_labels)

print("\n--- Exercițiu 3: K=3, L2 ---")
print("Clasificând... (poate dura 1-2 min pe 500 exemple)")
accuracy_3nn_l2, predictions_3nn_l2 = knn.score(test_images, test_labels,
                                                   num_neighbors=3, metric='l2')
print(f"Acuratețe 3-NN L2: {accuracy_3nn_l2:.4f}")  # Așteptat: ~0.898

# Salvare predicții
np.savetxt('predictii_3nn_l2_mnist.txt', predictions_3nn_l2, fmt='%d')
print("Predicții salvate în predictii_3nn_l2_mnist.txt")

# =============================================================================
# 5. EXERCIȚIUL 4 — Comparare K ∈ {1,3,5,7,9}, L1 vs L2
# =============================================================================

k_values = [1, 3, 5, 7, 9]

print("\n--- Exercițiu 4: Comparare K și distanță ---")
print("NOTĂ: Rularea completă poate dura ~10 min. Reduceți test_images dacă e prea lent.")

# Opțional: reducere set de test pentru demo rapid
DEMO_SIZE = 100  # SCHIMBABIL: crești la 500 pentru rezultate exacte
test_sub  = test_images[:DEMO_SIZE]
labels_sub = test_labels[:DEMO_SIZE]

accuracies_l2 = []
accuracies_l1 = []

for k in k_values:
    acc_l2, _ = knn.score(test_sub, labels_sub, num_neighbors=k, metric='l2')
    acc_l1, _ = knn.score(test_sub, labels_sub, num_neighbors=k, metric='l1')
    accuracies_l2.append(acc_l2)
    accuracies_l1.append(acc_l1)
    print(f"  K={k}: L2={acc_l2:.4f}, L1={acc_l1:.4f}")

# Salvare și plotare
np.savetxt('acuratete_l2.txt', np.column_stack([k_values, accuracies_l2]))

plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracies_l2, 'b-o', label='L2 (Euclidean)')
plt.plot(k_values, accuracies_l1, 'r-s', label='L1 (Manhattan)')
plt.xlabel('K (număr vecini)')
plt.ylabel('Acuratețe')
plt.title(f'KNN pe MNIST — Comparare K și distanță (subset {DEMO_SIZE} exemple)')
plt.legend()
plt.grid(True)
plt.xticks(k_values)
plt.tight_layout()
plt.show()

# =============================================================================
# 6. FUNCȚII NUMPY ESENȚIALE (din laborator)
# =============================================================================

print("\n" + "=" * 60)
print("6. FUNCȚII NUMPY ESENȚIALE PENTRU KNN")
print("=" * 60)

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Array: {arr}")
print(f"np.sort:    {np.sort(arr)}")          # sortat
print(f"np.argsort: {np.argsort(arr)}")       # indecși care sortează
print(f"np.bincount:{np.bincount(np.array([0,1,1,3,2,1,7]))}")  # frecvențe
print(f"np.where(arr>4): {np.where(arr > 4)}")  # indecși unde condiția e True

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 4, 5, 6, 7])
print(f"np.intersect1d: {np.intersect1d(x, y)}")  # intersecția a 2 array-uri

# =============================================================================
# 7. KNN SKLEARN — COMPARARE
# =============================================================================

from sklearn.neighbors import KNeighborsClassifier

print("\n" + "=" * 60)
print("7. KNN SKLEARN (pentru comparare)")
print("=" * 60)

# sklearn KNN — mult mai rapid datorită optimizărilor interne (KD-Tree, Ball-Tree)
knn_sklearn = KNeighborsClassifier(
    n_neighbors=3,      # SCHIMBABIL: K
    metric='euclidean', # SCHIMBABIL: 'euclidean' (L2) sau 'manhattan' (L1)
    algorithm='auto',   # 'auto', 'ball_tree', 'kd_tree', 'brute'
    weights='uniform',  # SCHIMBABIL: 'uniform' (vot egal) sau 'distance' (ponderat după distanță)
)
knn_sklearn.fit(train_images, train_labels)
acc_sk = knn_sklearn.score(test_sub, labels_sub)
print(f"KNN sklearn K=3 L2: {acc_sk:.4f}")

# =============================================================================
# NOTE: CE POATE FI MODIFICAT
# =============================================================================
"""
VARIANTE ȘI IMPACTE:

1. num_neighbors (K):
   - K=1: acuratețe maximă pe antrenare (100%), dar overfitting
   - K impar: evită egalitățile la vot
   - K mare: frontieră de decizie mai lină, dar pierde detalii
   - Optim tipic: K ∈ {3, 5, 7} pentru MNIST

2. metric ('l1' vs 'l2'):
   - L2 performează mai bine pe imagini (mai sensibil la diferențe mari = fundal alb)
   - L1 mai robust la outlieri pixeli
   - Ambele funcționează bine pe MNIST

3. weights='distance' în sklearn:
   - Vot ponderat: vecinii mai apropiați au influență mai mare
   - Poate îmbunătăți puțin acuratețea față de 'uniform'

4. Normalizare date:
   - KNN e sensibil la scara atributelor
   - Pe imagini 0-255 normalizarea la [0,1] sau z-score poate ajuta
   - train_images_norm = train_images / 255.0

5. Reducere dimensionalitate (PCA):
   - KNN pe 784 features e lent; PCA la ~50-100 componente menține acuratețea
   - from sklearn.decomposition import PCA
   - pca = PCA(n_components=50)
   - train_reduced = pca.fit_transform(train_images)
   - Viteză: de ~5-10x mai rapid după PCA

6. algorithm în sklearn:
   - 'brute': caută exhaustiv (bun pentru date mici)
   - 'kd_tree': rapid pentru spații cu puțini vectori
   - 'ball_tree': robust pentru spații cu mulți vectori
   - 'auto': alege automat cel mai bun
"""

print("\nLaborator 3 completat!")
