"""
=============================================================================
MODEL: Ridge Regression (L2) — Setup Complet, Gata de Rulat
=============================================================================
Lab: 5 | Dataset: Car Price Prediction
Algoritm: Ridge (regularizare L2) cu cross-validare și alegere alpha

RULARE: python model_ridge_regression.py
pip install numpy scikit-learn matplotlib
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import KFold
from sklearn.utils import shuffle
import os

# ===================== HYPERPARAMETRI (SCHIMBĂ AICI) ========================
ALPHA    = 10       # regularizare L2: {1, 10, 100, 1000}
N_SPLITS = 3        # fold-uri cross-validare
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
print("COMPARARE ALPHA — Ridge Regression")
print("=" * 60)

kf = KFold(n_splits=N_SPLITS, shuffle=True, random_state=42)
alpha_grid = [1, 10, 100, 1000]
results    = {}

for alpha in alpha_grid:
    mse_scores = []
    for tr_idx, val_idx in kf.split(X):
        X_tr, X_val = X[tr_idx], X[val_idx]
        y_tr, y_val = y[tr_idx], y[val_idx]
        X_tr_n, X_val_n, _, _ = normalize(X_tr, X_val)

        model = Ridge(alpha=alpha)
        model.fit(X_tr_n, y_tr)
        y_pred = model.predict(X_val_n)
        mse_scores.append(mean_squared_error(y_val, y_pred))

    mean_mse = np.mean(mse_scores)
    results[alpha] = mean_mse
    marker = " ← ALES" if alpha == ALPHA else ""
    print(f"  alpha={alpha:5}: MSE={mean_mse:.2f}, RMSE={np.sqrt(mean_mse):.2f}{marker}")

best_alpha = min(results, key=results.get)
print(f"\nAlpha optim (cel mai mic MSE): {best_alpha}")

# --- Antrenare cu alpha ales pe tot setul ---
print(f"\nAntrenare Ridge (alpha={ALPHA}) pe tot setul de antrenare...")
X_norm, _, mean_X, std_X = normalize(X)
model_full = Ridge(alpha=ALPHA)
model_full.fit(X_norm, y)

# Evaluare pe date de antrenare (pentru analiza coeficienților)
y_pred_all = model_full.predict(X_norm)
mse_train  = mean_squared_error(y, y_pred_all)
mae_train  = mean_absolute_error(y, y_pred_all)
r2_train   = r2_score(y, y_pred_all)
print(f"MSE antrenare:  {mse_train:.2f}")
print(f"MAE antrenare:  {mae_train:.2f}")
print(f"RMSE antrenare: {np.sqrt(mse_train):.2f}")
print(f"R² antrenare:   {r2_train:.4f}")

print(f"\nBias (intercept): {model_full.intercept_:.2f}")

# Analiza coeficienților
coef_abs = np.abs(model_full.coef_)
sorted_i = np.argsort(coef_abs)[::-1]
print("\nAtribute sortate după importanță:")
for i, idx in enumerate(sorted_i):
    name = FEATURE_NAMES[idx] if idx < len(FEATURE_NAMES) else f'feat_{idx}'
    print(f"  {i+1:2d}. {name:20s}: coef={model_full.coef_[idx]:.4f}, |coef|={coef_abs[idx]:.4f}")

# --- RidgeCV — selectare automată alpha cu CV intern ---
print("\n--- RidgeCV (selectare automată alpha) ---")
ridge_cv = RidgeCV(alphas=[1, 10, 100, 1000], cv=N_SPLITS, scoring='neg_mean_squared_error')
ridge_cv.fit(X_norm, y)
print(f"Alpha selectat de RidgeCV: {ridge_cv.alpha_}")
print(f"Scor R²: {ridge_cv.score(X_norm, y):.4f}")

# --- Comparare Linear vs Ridge ---
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_norm, y)
mse_lr = mean_squared_error(y, lr.predict(X_norm))

print(f"\nComparare pe train (informativ — nu validare reală):")
print(f"  LinearRegression MSE: {mse_lr:.2f}")
print(f"  Ridge(alpha={ALPHA}) MSE: {mse_train:.2f}")
print(f"  Ridge reduce dimensiunea coef: {np.max(np.abs(lr.coef_)):.2f} → {np.max(np.abs(model_full.coef_)):.2f}")

# --- Vizualizare ---
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Predicție vs Real
axes[0].scatter(y, y_pred_all, alpha=0.3, s=5)
axes[0].plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
axes[0].set_xlabel('Preț real'); axes[0].set_ylabel('Preț prezis')
axes[0].set_title(f'Ridge (alpha={ALPHA}): Pred vs Real')

# Coeficienți
axes[1].bar(range(len(model_full.coef_)), model_full.coef_)
axes[1].set_xlabel('Index atribut'); axes[1].set_ylabel('Coeficient')
axes[1].set_title(f'Coeficienți Ridge (alpha={ALPHA})')

# MSE vs alpha
alphas_plot = list(results.keys())
mse_plot    = [results[a] for a in alphas_plot]
axes[2].plot(alphas_plot, mse_plot, 'b-o')
axes[2].axvline(ALPHA, color='r', linestyle='--', label=f'alpha={ALPHA}')
axes[2].set_xscale('log')
axes[2].set_xlabel('alpha (log scale)'); axes[2].set_ylabel('MSE')
axes[2].set_title('MSE vs alpha')
axes[2].legend()

plt.tight_layout(); plt.show()

print("\nModel Ridge Regression completat!")
