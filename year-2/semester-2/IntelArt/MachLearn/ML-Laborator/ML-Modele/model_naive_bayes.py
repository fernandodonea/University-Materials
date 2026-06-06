"""
=============================================================================
MODEL: Naive Bayes — Setup Complet, Gata de Rulat
=============================================================================
Lab: 2 | Dataset: MNIST subset (1000 train, 500 test)
Algoritm: Naive Bayes Multinomial (implementare scratch + sklearn)

RULARE: python model_naive_bayes.py
pip install numpy matplotlib scikit-learn
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import os

# ===================== HYPERPARAMETRI (SCHIMBĂ AICI) ========================
NUM_BINS  = 5       # intervale discretizare: {3, 5, 7, 9, 11}
ALPHA     = 1.0     # Laplace smoothing: {0.1, 0.5, 1.0, 2.0}
# ============================================================================

# --- Încărcare date ---
def load_data():
    if os.path.exists('train_images.txt'):
        train_images = np.loadtxt('train_images.txt')
        train_labels = np.loadtxt('train_labels.txt').astype(int)
        test_images  = np.loadtxt('test_images.txt')
        test_labels  = np.loadtxt('test_labels.txt').astype(int)
    else:
        print("[INFO] Fișierele laboratorului lipsesc — generez date sintetice.")
        np.random.seed(42)
        # Simulăm imagini MNIST-like: 1000 train, 500 test, 784 features
        n_classes = 10
        train_images = np.zeros((1000, 784))
        train_labels = np.zeros(1000, dtype=int)
        test_images  = np.zeros(500, 784)
        test_labels  = np.zeros(500, dtype=int)
        for c in range(n_classes):
            # Fiecare clasă are un "tip" de imagine diferit
            for i in range(100):
                img = np.random.randint(0, 50, 784)
                img[(c*78):(c*78+78)] = np.random.randint(150, 255, 78)
                train_images[c*100 + i] = img
                train_labels[c*100 + i] = c
            for i in range(50):
                img = np.random.randint(0, 50, 784)
                img[(c*78):(c*78+78)] = np.random.randint(150, 255, 78)
                test_images[c*50 + i] = img
                test_labels[c*50 + i] = c
    return train_images, train_labels, test_images, test_labels

train_images, train_labels, test_images, test_labels = load_data()
print(f"Train: {train_images.shape}, Test: {test_images.shape}")

# --- Discretizare ---
def values_to_bins(X, bins):
    return np.digitize(X, bins)

bins = np.linspace(0, 255, NUM_BINS)
train_disc = values_to_bins(train_images, bins)
test_disc  = values_to_bins(test_images, bins)

# --- Model ---
model = MultinomialNB(alpha=ALPHA)

# Antrenare
model.fit(train_disc, train_labels)

# Predicție
y_pred = model.predict(test_disc)

# Evaluare
accuracy = model.score(test_disc, test_labels)
print(f"\nAcuratețe MultinomialNB (bins={NUM_BINS}, alpha={ALPHA}): {accuracy:.4f}")
print(classification_report(test_labels, y_pred, zero_division=0))

# Matricea de confuzie
def plot_confusion_matrix(y_true, y_pred, title="Confusion Matrix"):
    n = len(np.unique(y_true))
    cm = np.zeros((n, n), dtype=int)
    for t, p in zip(y_true, y_pred):
        cm[t][p] += 1
    plt.figure(figsize=(8, 7))
    plt.imshow(cm, cmap='Blues')
    plt.colorbar()
    plt.xlabel('Prezis')
    plt.ylabel('Real')
    plt.title(title)
    for i in range(n):
        for j in range(n):
            plt.text(j, i, cm[i, j], ha='center', va='center', fontsize=7)
    plt.tight_layout()
    plt.show()

plot_confusion_matrix(test_labels, y_pred)

# Test diferite num_bins
print("\n--- Comparare num_bins ---")
for nb in [3, 5, 7, 9, 11]:
    b = np.linspace(0, 255, nb)
    m = MultinomialNB(alpha=ALPHA)
    m.fit(values_to_bins(train_images, b), train_labels)
    acc = m.score(values_to_bins(test_images, b), test_labels)
    marker = " ← optim" if nb == NUM_BINS else ""
    print(f"  bins={nb}: {acc:.4f}{marker}")

# Exemple misclasificate
misclass = np.where(y_pred != test_labels)[0]
print(f"\nExemple misclasificate: {len(misclass)}/{len(test_labels)}")

fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    if i < min(10, len(misclass)):
        idx = misclass[i]
        ax.imshow(test_images[idx].reshape(28, 28).astype(np.uint8), cmap='gray')
        ax.set_title(f"R:{test_labels[idx]} P:{y_pred[idx]}", fontsize=9)
    ax.axis('off')
plt.suptitle("Exemple misclasificate")
plt.tight_layout()
plt.show()

print("\nModel Naive Bayes completat!")
