

# Laborator  MACHINE LEARNING


#### STRUCTURA FIȘIERELOR:

FIȘIERE LABORATOR (teorie + exerciții complete):
- [lab1_numpy_matplotlib.py](ML-Laborator-1/lab1_numpy_matplotlib.py)     → NumPy, Matplotlib, operații pe imagini
- [lab2_naive_bayes.py](ML-Laborator-2/lab2_naive_bayes.py)            → Naive Bayes, MNIST, discretizare, confuzie
- [lab3_knn.py](ML-Laborator-3/lab3_knn.py)                  → KNN din scratch, L1/L2, comparare K
- [lab4_bow_normalizare_svm.py](ML-Laborator-4/lab4_bow_normalizare_svm.py)    → Bag-of-Words, StandardScaler, L1/L2, SVM
- [lab5_regresie.py](ML-Laborator-5/lab5_regresie.py)              → Linear/Ridge/Lasso, cross-validare, Car Price
- [lab6_perceptron_retele.py](ML-Laborator-6/lab6_perceptron_retele.py)      → Widrow-Hoff, Rețea XOR, MLP sklearn + PyTorch

FIȘIERE MODEL (fiecare model separat, gata de rulat):
- [model_naive_bayes.py](ML-Modele/model_naive_bayes.py)[model_naive_bayes.py]()          → Lab 2 — MultinomialNB sklearn
- [model_knn.py](ML-Modele/model_knn.py)                   → Lab 3 — KnnClassifier din scratch
- [model_svm.py](ML-Modele/model_svm.py)                   → Lab 4 — SVM linear + RBF
- [model_linear_regression.py](ML-Modele/model_linear_regression.py)     → Lab 5 — LinearRegression
- [model_ridge_regression.py](ML-Modele/model_ridge_regression.py)      → Lab 5 — Ridge (L2)
- [model_lasso_regression.py](ML-Modele/model_lasso_regression.py)      → Lab 5 — Lasso (L1)
- [model_perceptron_widrow_hoff.py](ML-Modele/model_perceptron_widrow_hoff.py) → Lab 6 — Perceptron + Rețea numpy
- [model_mlp_sklearn.py](ML-Modele/model_mlp_sklearn.py)           → Lab 6 — MLPClassifier sklearn
- [model_mlp_pytorch.py](ML-Modele/model_mlp_pytorch.py)           → Lab 6 — MLP PyTorch complet


### PAȘII SKLEARN (identici pentru ORICE model):

```python
from sklearn.XXX import YYY            # 1. Import
model = YYY(param1=val1, ...)          # 2. Definire
model.fit(X_train, y_train)            # 3. Antrenare
y_pred = model.predict(X_test)         # 4. Predicție
acc = model.score(X_test, y_test)      # 5. Evaluare
```


### MODELE SKLEARN — CHEATSHEET


##### NAIVE BAYES (Lab 2)
```
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB(alpha=1.0)
```
DATE: discretizate (np.digitize cu bins), valori întregi ≥ 0

##### KNN (Lab 3)
```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
```
metric: 'euclidean'=L2, 'manhattan'=L1

##### SVM (Lab 4)
```python
from sklearn.svm import SVC
model = SVC(C=1.0, kernel='linear')       # linear
model = SVC(C=1.0, kernel='rbf', gamma='scale')  # RBF
# coef_ disponibil NUMAI pentru kernel='linear'
```

##### LINEAR REGRESSION (Lab 5)
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
```

##### RIDGE (Lab 5)
```python
from sklearn.linear_model import Ridge
model = Ridge(alpha=10)  # alpha ∈ {1, 10, 100, 1000}
```

##### LASSO (Lab 5)
```python
from sklearn.linear_model import Lasso
model = Lasso(alpha=10, max_iter=10000)  # creste max_iter dacă apare warning
```

##### MLP SKLEARN (Lab 6)
```
from sklearn.neural_network import MLPClassifier
model = MLPClassifier(
    hidden_layer_sizes=(100,),  # sau (100, 50) pentru 2 straturi
    activation='relu',          # sau 'tanh'
    solver='sgd',
    learning_rate_init=1e-2,
    max_iter=200
)
```

### METRICE EVALUARE

```python
from sklearn.metrics import (
    accuracy_score,            # (y_true, y_pred)
    mean_squared_error,        # (y_true, y_pred)
    mean_absolute_error,       # (y_true, y_pred)
    f1_score,                  # (y_true, y_pred, average='binary')
    classification_report,     # (y_true, y_pred)
    r2_score,                  # (y_true, y_pred)
)
import numpy as np
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
```


### NORMALIZARE — REGULĂ DE AUR


#### ÎNTOTDEAUNA: fit pe TRAIN, transform pe TRAIN și TEST separat!
```python
from sklearn.preprocessing import StandardScaler, Normalizer

scaler = StandardScaler()
X_train_n = scaler.fit_transform(X_train)   # fit + transform pe train
X_test_n  = scaler.transform(X_test)        # DOAR transform pe test (nu fit!)
```

#### L1/L2 normalizare per exemplu (pentru SVM + BoW):
```python
from sklearn.preprocessing import Normalizer
norm = Normalizer(norm='l2')
X_n = norm.transform(X)  # nu necesită fit (normalizare per exemplu)
```


#### CROSS-VALIDARE

```python
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline

# Manual (corect pentru normalizare în fiecare fold):
kf = KFold(n_splits=3, shuffle=True, random_state=42)
for train_idx, val_idx in kf.split(X):
    X_tr, X_val = X[train_idx], X[val_idx]
    # ... normalizare + antrenare + evaluare

# Cu Pipeline (recomandat):
pipe = Pipeline([('scaler', StandardScaler()), ('model', Ridge(alpha=10))])
scores = cross_val_score(pipe, X, y, cv=3, scoring='neg_mean_squared_error')
mse_mean = -scores.mean()
```


### PYTORCH — STRUCTURA MINIMĂ
```python
import torch, torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Normalize, Compose

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 10)
    def forward(self, x):
        x = self.flatten(x)
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model     = MLP().to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=1e-2)
loss_fn   = nn.CrossEntropyLoss()
```
```
# TRAIN LOOP:
model.train()
for X_batch, y_batch in train_loader:
    pred = model(X_batch)
    loss = loss_fn(pred, y_batch)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```
```
# EVAL LOOP:
model.eval()
with torch.no_grad():
    for X_batch, y_batch in test_loader:
        pred = model(X_batch)
        correct += (pred.argmax(1) == y_batch).sum().item()
```

### DISCRETIZARE (Naive Bayes)
```python
import numpy as np
bins = np.linspace(0, 255, num_bins)     # num_bins intervale
X_discretized = np.digitize(X, bins)     # indici de la 1
```


### BAG OF WORDS — SKLEARN (echivalent cu implementarea din scratch)
```python
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
X_train_bow = vect.fit_transform(train_texts)  # matrice sparsă
X_test_bow  = vect.transform(test_texts)       # NU fit! Doar transform
```


### HIPERPARAMETRI — IMPACT RAPID

##### Naive Bayes:
- num_bins ↑ → mai discriminativ, potențial overfitting
- alpha ↑    → mai mult smoothing, mai robust la date puține

##### KNN:
- K=1  → overfitting | K mare → underfitting
- L2 > L1 de obicei pe imagini

##### SVM:
- C ↑  → margine mică, sensibil la training → overfitting
- C ↓  → margine mare, tolerant → underfitting
- gamma ↑ (RBF) → frontieră locală complexă → overfitting

##### Ridge:
- alpha ↑ → ponderi mai mici → model mai simplu

##### Lasso:
- alpha ↑ → mai multe ponderi zero → mai sparse

##### MLP:
- lr prea mare → oscilații | lr prea mic → convergență lentă
- Neuroni ↑   → mai multă capacitate, posibil overfitting
- relu > tanh în general pentru rețele adânci



