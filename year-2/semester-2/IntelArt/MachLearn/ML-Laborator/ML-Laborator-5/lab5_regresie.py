"""
=============================================================================
LABORATOR 5 - Regresia Liniară, Ridge, Lasso
=============================================================================
Materie: Inteligență Artificială - Machine Learning
Acoperire: Regresie liniară, Ridge (L2), Lasso (L1), cross-validare,
           MSE, MAE, normalizare pentru regresie, Car Price Prediction

RULARE: python lab5_regresie.py
Dependențe: pip install numpy scikit-learn
Date: training_data.npy, prices.npy (sau fallback cu date sintetice)
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import cross_val_score, KFold
from sklearn.utils import shuffle
import os

# =============================================================================
# 1. TEORIA
# =============================================================================
"""
REGRESIE LINIARĂ:
    y_hat = w1*x1 + w2*x2 + ... + wn*xn + b = X·W + b

    Funcție cost: MSE
    MSE(y, y_hat) = (1/n) * sum (y_hat_i - y_i)^2

    Soluție analitică (Normal Equation):
    W = (X^T X)^{-1} X^T y

    Sau numeric: minimizare MSE prin gradient descent.

REGRESIE RIDGE (L2 regularizare):
    cost_Ridge(y, y_hat) = MSE + alpha * ||W||^2_2
    = MSE + alpha * sum w_i^2

    - Penalizează ponderile mari → ponderile sunt mici dar NENULE
    - alpha=0 → Ridge = Linear Regression
    - alpha mare → ponderile tind spre 0 (model simplu)
    - Bun când: toate atributele contribuie puțin (nu vrei să elimini niciunul)

REGRESIE LASSO (L1 regularizare):
    cost_Lasso(y, y_hat) = MSE + alpha * ||W||_1
    = MSE + alpha * sum |w_i|

    - Penalizează norma L1 a ponderilor → unele ponderi devin exact 0
    - Creează reprezentare SPARSĂ (selecție automată de atribute)
    - Bun când: crezi că puține atribute sunt relevante

COMPARARE:
    Linear: nici o penalizare, overfitting pe date puține/zgomotoase
    Ridge:  toate ponderile reduse proporțional, bun pentru colinearitate
    Lasso:  selecție automată atribute, sparse solution

METRICE:
    MSE  = (1/n) * sum (y_hat - y)^2  (penalizează erori mari)
    MAE  = (1/n) * sum |y_hat - y|    (robust la outlieri)
    RMSE = sqrt(MSE)                   (în aceleași unități cu y)
    R²   = 1 - MSS_residual/MSS_total  (1=perfect, 0=nu mai bun decât media)

CROSS-VALIDATION (validare încrucișată):
    - Împarte datele în K fold-uri
    - Antrenează pe K-1 fold-uri, validează pe 1
    - Repetă pentru fiecare fold, returnează K scoruri
    - Media scorurilor = estimare mai robustă a performanței
    - Folosit când nu ai set de testare separat
"""

# =============================================================================
# 2. ÎNCĂRCARE DATE
# =============================================================================

def load_car_price_data():
    """
    Încearcă să încarce datele Car Price Prediction.

    Structura datelor procesate (14 atribute):
    1: an fabricație
    2: km
    3: mileage
    4: motor
    5: putere
    6: nr locuri
    7: nr proprietari (1-4)
    8-12: tip combustibil (one-hot 5 valori)
    13-14: tip transmisie (one-hot: Manual/Automatic)
    """
    if os.path.exists('data/training_data.npy'):
        print("Încărcând datele Car Price Prediction...")
        training_data = np.load('data/training_data.npy')
        prices        = np.load('data/prices.npy')
    else:
        print("Datele nu au fost găsite. Generând date sintetice demo...")
        np.random.seed(42)
        n = 4879
        # Simulăm cele 14 atribute
        year         = np.random.randint(2000, 2022, n).astype(float)
        km           = np.random.uniform(0, 300000, n)
        mileage      = np.random.uniform(10, 30, n)
        engine       = np.random.choice([1000, 1200, 1500, 1800, 2000, 2500], n).astype(float)
        power        = np.random.uniform(60, 300, n)
        seats        = np.random.choice([5, 7, 8], n).astype(float)
        owners       = np.random.randint(1, 5, n).astype(float)
        fuel_onehot  = np.eye(5)[np.random.randint(0, 5, n)]
        trans_onehot = np.eye(2)[np.random.randint(0, 2, n)]

        training_data = np.column_stack([
            year, km, mileage, engine, power, seats, owners,
            fuel_onehot, trans_onehot
        ])
        # Prețul simulat ca funcție liniară + zgomot
        prices = (
            2000 * (year - 2000) -
            0.05 * km +
            500 * mileage +
            0.01 * engine +
            100 * power +
            50 * seats -
            100000 * owners +
            np.random.normal(0, 50000, n)
        )
        prices = np.maximum(prices, 100000)  # prețuri pozitive

    print(f"Date: {training_data.shape}, Prețuri: {prices.shape}")
    print(f"Primele 4 exemple:\n{training_data[:4]}")
    print(f"Primele 4 prețuri: {prices[:4]}")
    return training_data, prices

training_data, prices = load_car_price_data()

# Amestecăm datele
training_data, prices = shuffle(training_data, prices, random_state=0)

# =============================================================================
# 3. NORMALIZARE
# =============================================================================

def normalize_train_test(train_data, test_data=None):
    """
    Normalizează datele folosind standardizare z-score.

    IMPORTANT: Statisticile se calculează NUMAI pe train_data!
    Dacă aplici pe date noi (test), folosești aceeași medie și std din train.

    Parametri:
        train_data : np.array — date antrenare
        test_data  : np.array | None — date testare (opțional)

    Returnează:
        train_norm : date antrenare normalizate
        test_norm  : date testare normalizate (sau None)
        mean, std  : statisticile din train (pt a putea denormaliza sau reaplica)
    """
    mean = np.mean(train_data, axis=0)    # medie pe fiecare coloană (atribut)
    std  = np.std(train_data, axis=0)
    std  = np.where(std == 0, 1, std)     # evita împărțirea la 0

    train_norm = (train_data - mean) / std
    test_norm  = (test_data - mean) / std if test_data is not None else None

    return train_norm, test_norm, mean, std

# Pentru cross-validare, vom normaliza în interiorul foldurilor
# (corect metodologic — nu "cunoaștem" statisticile test-ului înainte)

# =============================================================================
# 4. CROSS-VALIDARE CU 3 FOLD-URI
# =============================================================================

print("\n" + "=" * 60)
print("4. CROSS-VALIDARE 3 FOLD-URI")
print("=" * 60)

kf = KFold(n_splits=3, shuffle=True, random_state=42)

def cross_validate_model(model, X, y, n_splits=3):
    """
    Cross-validare manuală cu normalizare internă foldului.

    Returnează MSE și MAE medii pe fold-urile de validare.
    """
    kf_cv = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    mse_scores = []
    mae_scores = []

    for train_idx, val_idx in kf_cv.split(X):
        X_train_fold, X_val_fold = X[train_idx], X[val_idx]
        y_train_fold, y_val_fold = y[train_idx], y[val_idx]

        # Normalizare INTERNĂ foldului (fără data leakage)
        X_train_norm, X_val_norm, _, _ = normalize_train_test(X_train_fold, X_val_fold)

        # Antrenare și evaluare
        model.fit(X_train_norm, y_train_fold)
        y_pred = model.predict(X_val_norm)

        mse_scores.append(mean_squared_error(y_val_fold, y_pred))
        mae_scores.append(mean_absolute_error(y_val_fold, y_pred))

    return np.mean(mse_scores), np.mean(mae_scores)

# --- Regresie Liniară ---
print("\n--- Regresie Liniară ---")
lin_reg = LinearRegression()
mse_lin, mae_lin = cross_validate_model(lin_reg, training_data, prices, n_splits=3)
print(f"MSE medie: {mse_lin:.2f}")
print(f"MAE medie: {mae_lin:.2f}")
print(f"RMSE medie: {np.sqrt(mse_lin):.2f}")

# --- Regresie Ridge ---
print("\n--- Regresie Ridge ---")
for alpha in [1, 10, 100, 1000]:
    ridge = Ridge(alpha=alpha)
    mse_r, mae_r = cross_validate_model(ridge, training_data, prices, n_splits=3)
    print(f"  alpha={alpha:5}: MSE={mse_r:.2f}, MAE={mae_r:.2f}")

# --- Regresie Lasso ---
print("\n--- Regresie Lasso ---")
for alpha in [1, 10, 100, 1000]:
    lasso = Lasso(alpha=alpha, max_iter=10000)
    mse_l, mae_l = cross_validate_model(lasso, training_data, prices, n_splits=3)
    print(f"  alpha={alpha:5}: MSE={mse_l:.2f}, MAE={mae_l:.2f}")

# =============================================================================
# 5. ANTRENARE PE DATE COMPLETE + ANALIZA COEFICIENȚILOR
# =============================================================================

print("\n" + "=" * 60)
print("5. ANTRENARE PE DATE COMPLETE (EXERCIȚIU 4)")
print("=" * 60)

# Cel mai bun alpha din exercitiul 3 (înlocuiește cu valoarea optimă găsită)
BEST_ALPHA = 10   # SCHIMBABIL: pune alpha-ul cu cel mai bun MSE din ex. 3

# Normalizare
X_norm, _, mean_data, std_data = normalize_train_test(training_data)

# Antrenare Ridge pe tot training set-ul
best_ridge = Ridge(alpha=BEST_ALPHA)
best_ridge.fit(X_norm, prices)

print(f"Bias (intercept): {best_ridge.intercept_:.2f}")
print(f"Coeficienți: {best_ridge.coef_}")

# Analiza atributelor
feature_names = [
    'an_fabricatie', 'km', 'mileage', 'motor', 'putere', 'nr_locuri',
    'nr_proprietari', 'combustibil_1', 'combustibil_2', 'combustibil_3',
    'combustibil_4', 'combustibil_5', 'transmisie_manual', 'transmisie_auto'
]

coef_abs = np.abs(best_ridge.coef_)
sorted_idx = np.argsort(coef_abs)[::-1]  # sortat descrescător

print(f"\nAtributele sortate după importanță (|coeficient|):")
for i, idx in enumerate(sorted_idx):
    name = feature_names[idx] if idx < len(feature_names) else f'feature_{idx}'
    print(f"  {i+1}. {name}: coef={best_ridge.coef_[idx]:.4f}")

print(f"\nCel mai semnificativ atribut:    {feature_names[sorted_idx[0]]}")
print(f"Al doilea semnificativ:          {feature_names[sorted_idx[1]]}")
print(f"Cel mai puțin semnificativ:      {feature_names[sorted_idx[-1]]}")

# =============================================================================
# 6. VIZUALIZARE
# =============================================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Predicție vs Valori reale
y_pred_all = best_ridge.predict(X_norm)
axes[0].scatter(prices, y_pred_all, alpha=0.3, s=5)
axes[0].plot([prices.min(), prices.max()], [prices.min(), prices.max()], 'r--')
axes[0].set_xlabel('Preț real')
axes[0].set_ylabel('Preț prezis')
axes[0].set_title('Ridge Regression: Predicție vs Real')

# Coeficienți
axes[1].bar(range(len(best_ridge.coef_)), best_ridge.coef_)
axes[1].set_xlabel('Index atribut')
axes[1].set_ylabel('Coeficient')
axes[1].set_title(f'Coeficienți Ridge (alpha={BEST_ALPHA})')
axes[1].set_xticks(range(len(best_ridge.coef_)))

plt.tight_layout()
plt.show()

# =============================================================================
# 7. COMPARARE SKLEARN — CU CV DIRECT
# =============================================================================

print("\n" + "=" * 60)
print("7. CROSS-VALIDARE SKLEARN (metodă rapidă)")
print("=" * 60)

"""
Alternativă rapidă: sklearn.model_selection.cross_val_score
ATENȚIE: nu face normalizare internă foldului!
Folosiți Pipeline pentru normalizare + model corect.
"""
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Pipeline: normalizare + Ridge (corect din punct de vedere al data leakage)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('ridge',  Ridge(alpha=BEST_ALPHA))
])

# neg_mean_squared_error: sklearn întoarce negative MSE (mai mare = mai bun)
cv_scores = cross_val_score(pipeline, training_data, prices,
                             cv=3, scoring='neg_mean_squared_error')
mse_cv = -cv_scores.mean()
print(f"Pipeline Ridge (alpha={BEST_ALPHA}): MSE={mse_cv:.2f}, RMSE={np.sqrt(mse_cv):.2f}")

# =============================================================================
# NOTE: CE POATE FI MODIFICAT
# =============================================================================
"""
VARIANTE ȘI IMPACTE:

1. alpha (Ridge / Lasso):
   - alpha=0 → echivalent cu Linear Regression
   - Crești alpha → ponderile scad → model mai simplu → mai puțin overfitting
   - Prea mare → underfitting (model prea simplu)
   - Optim: căutat cu cross-validare pe {1, 10, 100, 1000}
   - Cod: nimic altceva nu se schimbă, doar Ridge(alpha=X) sau Lasso(alpha=X)

2. Linear vs Ridge vs Lasso:
   - Linear: nu are alpha; coeficienții pot deveni mari dacă atributele sunt corelate
   - Ridge: ponderile mici dar nenule; bun pentru colinearitate (ex: one-hot features)
   - Lasso: unele ponderi exact 0; face selecție automată de atribute
   - Codul: schimbi doar clasa modelului; .fit() și .predict() identice

3. Metrica de evaluare:
   - MSE: penalizează erori mari (din cauza ridicării la pătrat)
   - MAE: mai robustă la outlieri (nu ridică la pătrat)
   - RMSE: în aceleași unități cu y (mai ușor de interpretat)
   - R²: scor relativ (1=perfect, 0=nu e mai bun decât media)
   - Adăugare cod: from sklearn.metrics import r2_score
     r2 = r2_score(y_true, y_pred)

4. n_splits în KFold:
   - 3: rapid, estimare mai variabilă
   - 5 sau 10: standard, estimare mai stabilă dar mai lent
   - Leave-One-Out: maxim de fold-uri (n_splits=n), extrem de lent

5. Normalizare (StandardScaler):
   - Esențial pentru Ridge și Lasso! Fără normalizare, alpha afectează inegal atributele
   - Cu normalizare: atributele cu scări diferite (km: 0-300000, seats: 5-8) devin comparabile
   - Fără normalizare: coeficienții nu pot fi comparați direct pentru importanță atribute

6. max_iter pentru Lasso:
   - Default=1000, poate să nu conveargă pe date mari
   - Mărește la max_iter=10000 sau mai mult dacă primești ConvergenceWarning
"""

print("\nLaborator 5 completat!")
