"""
=============================================================================
MODEL: MLPClassifier (Sklearn) — Setup Complet, Gata de Rulat
=============================================================================
Lab: 6 | Dataset: MNIST (sklearn digits 8x8 sau MNIST 28x28)
Algoritm: MLPClassifier cu configurații multiple, normalizare

RULARE: python model_mlp_sklearn.py
pip install numpy scikit-learn matplotlib
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

# ===================== HYPERPARAMETRI (SCHIMBĂ AICI) ========================
HIDDEN_LAYERS   = (100,)        # arhitectura: (10,), (100,), (100,50), (512,512)
ACTIVATION      = 'relu'        # 'relu', 'tanh', 'logistic', 'identity'
SOLVER          = 'sgd'         # 'sgd', 'adam', 'lbfgs'
LEARNING_RATE   = 1e-2          # rata de învățare
MAX_ITER        = 200           # epoci maxime
ALPHA_REG       = 0.0001        # regularizare L2
BATCH_SIZE      = 'auto'        # 'auto' = min(200, n_samples) sau int
MOMENTUM        = 0.9           # momentul pentru SGD
EARLY_STOPPING  = False         # oprire dacă val_loss nu se îmbunătățește
RANDOM_SEED     = 42
# ============================================================================

# --- Încărcare date ---
def load_mnist():
    """
    Încearcă să încarce datele MNIST din fișierele laboratorului.
    Fallback: sklearn digits (8x8, mai rapid).
    """
    if os.path.exists('train_images.txt'):
        print("Încărcând MNIST din fișiere...")
        X_tr = np.loadtxt('train_images.txt')
        y_tr = np.loadtxt('train_labels.txt').astype(int)
        X_te = np.loadtxt('test_images.txt')
        y_te = np.loadtxt('test_labels.txt').astype(int)
        return X_tr, y_tr, X_te, y_te, '28x28'
    else:
        print("[INFO] Folosesc sklearn digits (8x8, 1797 exemple).")
        from sklearn.datasets import load_digits
        digits = load_digits()
        X, y   = digits.data, digits.target
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=RANDOM_SEED)
        return X_tr, y_tr, X_te, y_te, '8x8'

X_train, y_train, X_test, y_test, img_size = load_mnist()
print(f"Train: {X_train.shape}, Test: {X_test.shape}, Imagini: {img_size}")

# --- Normalizare (OBLIGATORIU pentru MLP) ---
# Fără normalizare, antrenarea e instabilă și lentă
scaler  = StandardScaler()
X_tr_n  = scaler.fit_transform(X_train)
X_te_n  = scaler.transform(X_test)

# --- Model principal ---
print(f"\nAntrenare MLP: hidden={HIDDEN_LAYERS}, act={ACTIVATION}, lr={LEARNING_RATE}")
model = MLPClassifier(
    hidden_layer_sizes  = HIDDEN_LAYERS,
    activation          = ACTIVATION,
    solver              = SOLVER,
    alpha               = ALPHA_REG,
    batch_size          = BATCH_SIZE,
    learning_rate       = 'constant',  # SCHIMBABIL: 'invscaling', 'adaptive'
    learning_rate_init  = LEARNING_RATE,
    max_iter            = MAX_ITER,
    shuffle             = True,
    random_state        = RANDOM_SEED,
    tol                 = 1e-4,
    n_iter_no_change    = 10,
    momentum            = MOMENTUM,
    early_stopping      = EARLY_STOPPING,
    validation_fraction = 0.1 if EARLY_STOPPING else 0.1,
    verbose             = False
)
model.fit(X_tr_n, y_train)

# Evaluare
y_pred = model.predict(X_te_n)
acc    = accuracy_score(y_test, y_pred)
print(f"\nAcuratețe: {acc:.4f}")
print(f"Epoci antrenate: {model.n_iter_}")
print(classification_report(y_test, y_pred, zero_division=0))

# Curba de pierdere
plt.figure(figsize=(8, 4))
plt.plot(model.loss_curve_)
plt.title(f'Pierdere antrenare — hidden={HIDDEN_LAYERS}, act={ACTIVATION}')
plt.xlabel('Iterație'); plt.ylabel('Loss'); plt.grid(True)
plt.tight_layout(); plt.show()

# --- Comparare configurații (ca în exercițiile laboratorului) ---
print("\n" + "=" * 60)
print("COMPARARE CONFIGURAȚII (Lab 6, Exercițiu 1)")
print("=" * 60)

configs = [
    # (hidden_layer_sizes, activation, learning_rate, label)
    ((1,),       'tanh',  1e-2, 'a) 1 neuron, tanh, lr=1e-2'),
    ((10,),      'tanh',  1e-2, 'b) 10 neuroni, tanh, lr=1e-2'),
    ((10,),      'tanh',  1e-5, 'c) 10 neuroni, tanh, lr=1e-5'),
    ((10,),      'tanh',  10,   'd) 10 neuroni, tanh, lr=10'),
    ((10, 10),   'tanh',  1e-2, 'e) 10x10, tanh, lr=1e-2'),
    ((10, 10),   'relu',  1e-2, 'f) 10x10, relu, lr=1e-2'),
    ((100, 100), 'relu',  1e-2, 'g) 100x100, relu, lr=1e-2'),
    ((100, 100), 'relu',  1e-2, 'h) 100x100, relu, lr=1e-2, mom=0.9'),
]

results = []
for hidden, act, lr, label in configs:
    use_momentum = 0.9 if 'mom=0.9' in label else 0.0
    m = MLPClassifier(
        hidden_layer_sizes=hidden, activation=act,
        solver='sgd', learning_rate_init=lr,
        max_iter=100, random_state=RANDOM_SEED,
        momentum=use_momentum
    )
    m.fit(X_tr_n, y_train)
    acc = m.score(X_te_n, y_test)
    results.append((label, acc))
    print(f"  {label}: {acc:.4f}")

# Plot comparare
labels_plot, accs_plot = zip(*results)
plt.figure(figsize=(12, 5))
bars = plt.bar(range(len(accs_plot)), accs_plot, color='steelblue')
plt.xticks(range(len(labels_plot)), [l[:25] for l in labels_plot], rotation=45, ha='right')
plt.ylabel('Acuratețe')
plt.title('Comparare configurații MLP')
plt.ylim(0, 1.1)
for bar, acc in zip(bars, accs_plot):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
             f'{acc:.3f}', ha='center', va='bottom', fontsize=8)
plt.tight_layout(); plt.show()

# --- Learning rate adaptiv vs constant ---
print("\n--- Comparare learning_rate ---")
for lr_policy in ['constant', 'invscaling', 'adaptive']:
    m = MLPClassifier(
        hidden_layer_sizes=(100,), activation='relu', solver='sgd',
        learning_rate=lr_policy, learning_rate_init=1e-2,
        max_iter=100, random_state=RANDOM_SEED
    )
    m.fit(X_tr_n, y_train)
    acc = m.score(X_te_n, y_test)
    print(f"  learning_rate={lr_policy}: {acc:.4f} (epoci={m.n_iter_})")

# --- Early stopping ---
print("\n--- Early stopping ---")
m_es = MLPClassifier(
    hidden_layer_sizes=(100,), activation='relu', solver='sgd',
    learning_rate_init=1e-2, max_iter=500,
    early_stopping=True, n_iter_no_change=10,
    validation_fraction=0.1, random_state=RANDOM_SEED
)
m_es.fit(X_tr_n, y_train)
print(f"  Epoci până la oprire: {m_es.n_iter_} (din 500)")
print(f"  Acuratețe: {m_es.score(X_te_n, y_test):.4f}")

# --- Exemple misclasificate ---
misclass_idx = np.where(y_pred != y_test)[0]
print(f"\nExemple misclasificate: {len(misclass_idx)}")

if len(misclass_idx) > 0:
    n_side = int(np.sqrt(X_test.shape[1]))  # 8 pentru 8x8, 28 pentru 28x28
    fig, axes = plt.subplots(2, 5, figsize=(12, 5))
    for i, ax in enumerate(axes.flat):
        if i < min(10, len(misclass_idx)):
            idx = misclass_idx[i]
            ax.imshow(X_test[idx].reshape(n_side, n_side), cmap='gray')
            ax.set_title(f"R:{y_test[idx]} P:{y_pred[idx]}", fontsize=9)
        ax.axis('off')
    plt.suptitle("Exemple misclasificate — MLP")
    plt.tight_layout(); plt.show()

print("\nModel MLPClassifier sklearn completat!")
