"""
=============================================================================
MODEL: Linear Regression — Setup Complet, Gata de Rulat
=============================================================================
Lab: 5 | Dataset: Car Price Prediction
Algoritm: Regresie Liniară (sklearn) cu cross-validare

RULARE: python model_linear_regression.py
pip install numpy scikit-learn matplotlib
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
import os

# --- Încărcare / generare date ---
def load_data():
    if os.path.exists('data/training_data.npy'):
        X = np.load('data/training_data.npy')
        y = np.load('data/prices.npy')
        print(f"Date încărcate: {X.shape}")
    else:
        print("[INFO] Generez date Car Price sintetice.")
        np.random.seed(42)
        n = 1000
        X = np.column_stack([
            np.random.randint(2000, 2022, n).astype(float),
            np.random.uniform(0, 300000, n),
            np.random.uniform(10, 30, n),
            np.random.choice([1000,1500,2000,2500], n).astype(float),
            np.random.uniform(60, 300, n),
            np.random.choice([5, 7], n).astype(float),
            np.random.randint(1, 5, n).astype(float),
            *[np.random.randint(0, 2, n).astype(float) for _ in range(7)]
        ])
        y = (2000*(X[:,0]-2000) - 0.05*X[:,1] + 500*X[:,2]
             + 100*X[:,4] - 100000*X[:,6]
             + np.random.normal(0, 50000, n))
        y = np.maximum(y, 100000)
    X, y = shuffle(X, y, random_state=0)
    return X, y

X, y = load_data()
print(f"Shape X: {X.shape}, Shape y: {y.shape}")

# ===================== HYPERPARAMETRI (SCHIMBĂ AICI) ========================
N_SPLITS = 3    # numărul de fold-uri pentru cross-validare: {3, 5, 10}
# Linear Regression nu are alpha — nu există regularizare
# ============================================================================

FEATURE_NAMES = [
    'an_fabricatie', 'km', 'mileage', 'motor', 'putere', 'nr_locuri',
    'nr_proprietari', 'combustibil_1', 'combustibil_2', 'combustibil_3',
    'combustibil_4', 'combustibil_5', 'transmisie_manual', 'transmisie_auto'
][:X.shape[1]]

# --- Normalizare (funcție) ---
def normalize(train, test=None):
    mean = np.mean(train, axis=0)
    std  = np.std(train, axis=0)
    std  = np.where(std == 0, 1, std)
    train_n = (train - mean) / std
    test_n  = (test - mean) / std if test is not None else None
    return train_n, test_n, mean, std

# --- Cross-validare manuală (cu normalizare corectă în fiecare fold) ---
kf = KFold(n_splits=N_SPLITS, shuffle=True, random_state=42)
mse_scores, mae_scores, r2_scores = [], [], []

for fold, (tr_idx, val_idx) in enumerate(kf.split(X)):
    X_tr, X_val = X[tr_idx], X[val_idx]
    y_tr, y_val = y[tr_idx], y[val_idx]

    X_tr_n, X_val_n, _, _ = normalize(X_tr, X_val)

    model = LinearRegression()
    model.fit(X_tr_n, y_tr)
    y_pred = model.predict(X_val_n)

    mse_scores.append(mean_squared_error(y_val, y_pred))
    mae_scores.append(mean_absolute_error(y_val, y_pred))
    r2_scores.append(r2_score(y_val, y_pred))

print(f"\nCross-validare {N_SPLITS} fold-uri — Linear Regression:")
print(f"  MSE  medie: {np.mean(mse_scores):.2f} ± {np.std(mse_scores):.2f}")
print(f"  MAE  medie: {np.mean(mae_scores):.2f} ± {np.std(mae_scores):.2f}")
print(f"  RMSE medie: {np.sqrt(np.mean(mse_scores)):.2f}")
print(f"  R²   medie: {np.mean(r2_scores):.4f}")

# --- Antrenare pe tot setul + analiză coeficienți ---
X_norm, _, mean_X, std_X = normalize(X)
model_full = LinearRegression()
model_full.fit(X_norm, y)

print(f"\nBias (intercept): {model_full.intercept_:.2f}")
print(f"\nCoeficienți sortați după importanță:")
coef_abs = np.abs(model_full.coef_)
sorted_i = np.argsort(coef_abs)[::-1]
for i, idx in enumerate(sorted_i):
    name = FEATURE_NAMES[idx] if idx < len(FEATURE_NAMES) else f'feat_{idx}'
    print(f"  {i+1}. {name}: {model_full.coef_[idx]:.4f}")

# --- Vizualizare ---
y_pred_all = model_full.predict(X_norm)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Predicție vs Real
axes[0].scatter(y, y_pred_all, alpha=0.3, s=5)
axes[0].plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
axes[0].set_xlabel('Preț real'); axes[0].set_ylabel('Preț prezis')
axes[0].set_title('Linear Regression: Predicție vs Real')

# Coeficienți
axes[1].bar(range(len(model_full.coef_)), model_full.coef_)
axes[1].set_xlabel('Index atribut'); axes[1].set_ylabel('Coeficient')
axes[1].set_title('Coeficienți Linear Regression')

# Reziduuri
residuals = y - y_pred_all
axes[2].hist(residuals, bins=30)
axes[2].set_xlabel('Reziduu'); axes[2].set_ylabel('Frecvență')
axes[2].set_title('Distribuție reziduuri')

plt.tight_layout(); plt.show()

# --- Predicție pe un exemplu nou ---
print("\n--- Predicție exemplu nou ---")
example = X[0].copy()
example_norm = (example - mean_X) / std_X
pred_price = model_full.predict(example_norm.reshape(1, -1))[0]
print(f"Preț prezis: {pred_price:.2f} (real: {y[0]:.2f})")

print("\nModel Linear Regression completat!")
