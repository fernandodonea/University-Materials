"""
=============================================================================
MODEL: K-Nearest Neighbors — Setup Complet, Gata de Rulat
=============================================================================
Lab: 3 | Dataset: MNIST subset
Algoritm: KNN din scratch + sklearn KNeighborsClassifier

RULARE: python model_knn.py
pip install numpy matplotlib scikit-learn
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import os

# ===================== HYPERPARAMETRI (SCHIMBĂ AICI) ========================
K      = 3          # numărul de vecini: {1, 3, 5, 7, 9}
METRIC = 'l2'       # distanța: 'l1' sau 'l2'
# ============================================================================

# --- Încărcare date ---
def load_data():
    if os.path.exists('train_images.txt'):
        return (np.loadtxt('train_images.txt'),
                np.loadtxt('train_labels.txt').astype(int),
                np.loadtxt('test_images.txt'),
                np.loadtxt('test_labels.txt').astype(int))
    print("[INFO] Fișiere lipsă — generez MNIST sintetic.")
    np.random.seed(42)
    n_classes = 10
    tr_img, tr_lbl, te_img, te_lbl = [], [], [], []
    for c in range(n_classes):
        for _ in range(100):
            img = np.random.randint(0, 50, 784)
            img[c*78:(c+1)*78] = np.random.randint(150, 255, 78)
            tr_img.append(img); tr_lbl.append(c)
        for _ in range(50):
            img = np.random.randint(0, 50, 784)
            img[c*78:(c+1)*78] = np.random.randint(150, 255, 78)
            te_img.append(img); te_lbl.append(c)
    return (np.array(tr_img), np.array(tr_lbl),
            np.array(te_img), np.array(te_lbl))

train_images, train_labels, test_images, test_labels = load_data()
print(f"Train: {train_images.shape}, Test: {test_images.shape}")

# --- Model KNN din scratch ---
class KnnClassifier:
    def __init__(self, train_images, train_labels):
        self.train_images = train_images
        self.train_labels = train_labels

    def classify_image(self, test_image, num_neighbors=3, metric='l2'):
        if metric == 'l2':
            diff = self.train_images - test_image
            distances = np.sqrt(np.sum(diff ** 2, axis=1))
        elif metric == 'l1':
            diff = self.train_images - test_image
            distances = np.sum(np.abs(diff), axis=1)
        else:
            raise ValueError(f"Metric '{metric}' necunoscut. Folosiți 'l1' sau 'l2'.")

        sorted_indices  = np.argsort(distances)
        k_nearest_idx   = sorted_indices[:num_neighbors]
        k_labels        = self.train_labels[k_nearest_idx]
        votes           = np.bincount(k_labels, minlength=len(np.unique(self.train_labels)))
        return np.argmax(votes)

    def classify_batch(self, test_imgs, num_neighbors=3, metric='l2'):
        results = []
        for i, img in enumerate(test_imgs):
            results.append(self.classify_image(img, num_neighbors, metric))
            if (i + 1) % 50 == 0:
                print(f"  [{i+1}/{len(test_imgs)}]")
        return np.array(results)

# Reducem setul de test pentru viteză (mărește pentru rezultate exacte)
DEMO = 100  # SCHIMBABIL: 500 pentru test complet
te_sub  = test_images[:DEMO]
lbl_sub = test_labels[:DEMO]

knn = KnnClassifier(train_images, train_labels)

print(f"\nClasificare KNN (K={K}, metric={METRIC}) pe {DEMO} exemple...")
y_pred = knn.classify_batch(te_sub, num_neighbors=K, metric=METRIC)
accuracy = np.mean(y_pred == lbl_sub)
print(f"Acuratețe: {accuracy:.4f}")

# Salvare predicții
np.savetxt(f'predictii_{K}nn_{METRIC}_mnist.txt', y_pred, fmt='%d')
print(f"Predicții salvate în predictii_{K}nn_{METRIC}_mnist.txt")

# Comparare K
print("\n--- Comparare K și distanță ---")
k_values = [1, 3, 5, 7, 9]
acc_l2, acc_l1 = [], []
for k in k_values:
    a2, _ = knn.classify_batch(te_sub, k, 'l2'), None
    a2 = np.mean(knn.classify_batch(te_sub, k, 'l2') == lbl_sub)
    a1 = np.mean(knn.classify_batch(te_sub, k, 'l1') == lbl_sub)
    acc_l2.append(a2)
    acc_l1.append(a1)
    print(f"  K={k}: L2={a2:.4f}, L1={a1:.4f}")

np.savetxt('acuratete_l2.txt', np.column_stack([k_values, acc_l2]))

plt.figure(figsize=(8, 5))
plt.plot(k_values, acc_l2, 'b-o', label='L2 (Euclidean)')
plt.plot(k_values, acc_l1, 'r-s', label='L1 (Manhattan)')
plt.xlabel('K'); plt.ylabel('Acuratețe')
plt.title('KNN MNIST — L1 vs L2')
plt.legend(); plt.grid(True); plt.xticks(k_values)
plt.tight_layout(); plt.show()

# Sklearn KNN (mult mai rapid)
print("\n--- Sklearn KNeighborsClassifier ---")
sk_metric = 'euclidean' if METRIC == 'l2' else 'manhattan'
knn_sk = KNeighborsClassifier(
    n_neighbors=K,
    metric=sk_metric,
    algorithm='auto',
    weights='uniform'  # SCHIMBABIL: 'distance' ponderează vecinii după distanță
)
knn_sk.fit(train_images, train_labels)
acc_sk = knn_sk.score(te_sub, lbl_sub)
print(f"Sklearn KNN K={K} {METRIC}: {acc_sk:.4f}")

print("\nModel KNN completat!")
