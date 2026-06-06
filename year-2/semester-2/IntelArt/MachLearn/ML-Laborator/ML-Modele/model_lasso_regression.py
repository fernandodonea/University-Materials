"""
=============================================================================
MODEL: Lasso Regression (L1) — Setup Complet, Gata de Rulat
=============================================================================
Lab: 5 | Dataset: Car Price Prediction
Algoritm: Lasso (regularizare L1) — creează soluție sparsă (selecție atribute)

RULARE: python model_lasso_regression.py
pip install numpy scikit-learn matplotlib
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso, LassoCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import KFold
from sklearn.utils import shuffle
import os

# ===================== HYPERPARAMETRI (SCHIMBĂ AICI) ========================
ALPHA    = 10       # regularizare L1: {1, 10, 100, 1000}
N_SPLITS = 3        # fold-uri cross-validare
MAX_ITER = 10000    # iterații maxime Lasso (crești dacă apare ConvergenceWarning)
# ============================================================================

# --- Încărcare date ---
def load_data():
    if os.path.exists('data/training_data.npy'):
        X = np.load('data/training_data.npy')
        y = np.load('data/prices.npy')
    else:
        print("[INFO] Generez date sintetice.")
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
    return shuffle(X, y, random_state=0)

X, y = load_data()

FEATURE_NAMES = [
    'an_fabricatie', 'km', 'mileage', 'motor', 'putere', 'nr_locuri',
    'nr_proprietari', 'combustibil_1', 'combustibil_2', 'combustibil_3',
    'combustibil_4', 'combustibil_5', 'transmisie_manual', 'transmisie_auto'
][:X.shape[1]]

# --- Normalizare ---
def normalize(train, test=None):
    mean = np.mean(train, axis=0)
    std  = np.std(train, axis=0)
    std  = np.where(std == 0, 1, std)
    return ((train-mean)/std, (test-mean)/std if test is not None else None, mean, std)

# --- Cross-validare pentru diferite alpha ---
print("=" * 60)
print("COMPARARE ALPHA — Lasso Regression (L1)")
print("=" * 60)
print("Lasso creează soluție SPARSĂ — unele coeficienți devin exact 0!")

kf = KFold(n_splits=N_SPLITS, shuffle=True, random_state=42)
alpha_grid = [1, 10, 100, 1000]
results = {}

for alpha in alpha_grid:
    mse_scores = []
    n_nonzero_coef = []

    for tr_idx, val_idx in kf.split(X):
        X_tr, X_val = X[tr_idx], X[val_idx]
        y_tr, y_val = y[tr_idx], y[val_idx]
        X_tr_n, X_val_n, _, _ = normalize(X_tr, X_val)

        model = Lasso(alpha=alpha, max_iter=MAX_ITER)
        model.fit(X_tr_n, y_tr)
        y_pred = model.predict(X_val_n)
        mse_scores.append(mean_squared_error(y_val, y_pred))
        n_nonzero_coef.append(np.sum(model.coef_ != 0))

    mean_mse = np.mean(mse_scores)
    avg_nz   = int(np.mean(n_nonzero_coef))
    results[alpha] = mean_mse
    marker = " ← ALES" if alpha == ALPHA else ""
    print(f"  alpha={alpha:5}: MSE={mean_mse:.2f}, coef nenule≈{avg_nz}/{X.shape[1]}{marker}")

best_alpha = min(results, key=results.get)
print(f"\nAlpha optim (cel mai mic MSE): {best_alpha}")

# --- Antrenare cu alpha ales pe tot setul ---
print(f"\nAntrenare Lasso (alpha={ALPHA}) pe tot setul...")
X_norm, _, mean_X, std_X = normalize(X)
model_full = Lasso(alpha=ALPHA, max_iter=MAX_ITER)
model_full.fit(X_norm, y)

y_pred_all = model_full.predict(X_norm)
mse_train  = mean_squared_error(y, y_pred_all)
mae_train  = mean_absolute_error(y, y_pred_all)
r2_train   = r2_score(y, y_pred_all)
print(f"MSE antrenare:  {mse_train:.2f}")
print(f"MAE antrenare:  {mae_train:.2f}")
print(f"R² antrenare:   {r2_train:.4f}")

print(f"\nBias (intercept): {model_full.intercept_:.2f}")

# Analiza sparsității
nonzero_idx  = np.where(model_full.coef_ != 0)[0]
zero_idx     = np.where(model_full.coef_ == 0)[0]
print(f"\nCoeficienți NENULI ({len(nonzero_idx)}/{X.shape[1]}):")
for idx in nonzero_idx:
    name = FEATURE_NAMES[idx] if idx < len(FEATURE_NAMES) else f'feat_{idx}'
    print(f"  {name}: {model_full.coef_[idx]:.4f}")

print(f"\nCoeficienți ZERO ({len(zero_idx)}/{X.shape[1]}) — atribute eliminate:")
for idx in zero_idx:
    name = FEATURE_NAMES[idx] if idx < len(FEATURE_NAMES) else f'feat_{idx}'
    print(f"  {name}")

# --- Comparare Linear vs Ridge vs Lasso ---
from sklearn.linear_model import LinearRegression, Ridge
print("\n--- Comparare modele de regresie ---")
models = [
    ('LinearRegression', LinearRegression()),
    (f'Ridge(alpha={ALPHA})', Ridge(alpha=ALPHA)),
    (f'Lasso(alpha={ALPHA})', Lasso(alpha=ALPHA, max_iter=MAX_ITER)),
]

for name, m in models:
    mse_cv = []
    for tr_idx, val_idx in kf.split(X):
        X_tr, X_val = X[tr_idx], X[val_idx]
        y_tr, y_val = y[tr_idx], y[val_idx]
        X_tr_n, X_val_n, _, _ = normalize(X_tr, X_val)
        m.fit(X_tr_n, y_tr)
        mse_cv.append(mean_squared_error(y_val, m.predict(X_val_n)))
    print(f"  {name:30s}: MSE={np.mean(mse_cv):.2f}, RMSE={np.sqrt(np.mean(mse_cv)):.2f}")

# --- Vizualizare ---
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Predicție vs Real
axes[0].scatter(y, y_pred_all, alpha=0.3, s=5, color='purple')
axes[0].plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
axes[0].set_xlabel('Preț real'); axes[0].set_ylabel('Preț prezis')
axes[0].set_title(f'Lasso (alpha={ALPHA})')

# Coeficienți — vizualizare sparsitate
colors = ['green' if c != 0 else 'gray' for c in model_full.coef_]
axes[1].bar(range(len(model_full.coef_)), model_full.coef_, color=colors)
axes[1].set_xlabel('Index atribut'); axes[1].set_ylabel('Coeficient')
axes[1].set_title(f'Coeficienți Lasso — verde=activ, gri=eliminat')

# MSE vs alpha
alphas_plot = list(results.keys())
mse_plot    = [results[a] for a in alphas_plot]
axes[2].plot(alphas_plot, mse_plot, 'purple', marker='o')
axes[2].axvline(ALPHA, color='r', linestyle='--', label=f'alpha={ALPHA}')
axes[2].set_xscale('log')
axes[2].set_xlabel('alpha (log)'); axes[2].set_ylabel('MSE')
axes[2].set_title('MSE vs alpha (Lasso)')
axes[2].legend()

plt.tight_layout(); plt.show()

print("\nModel Lasso Regression completat!")
