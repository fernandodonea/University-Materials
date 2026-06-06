"""
=============================================================================
LABORATOR 6 - Perceptronul și Rețele de Perceptroni
=============================================================================
Materie: Inteligență Artificială - Machine Learning
Acoperire: Perceptron cu Widrow-Hoff, rețea feedforward numpy (XOR),
           MLPClassifier sklearn, PyTorch MLP, backpropagation

RULARE: python lab6_perceptron_retele.py
Dependențe: pip install numpy matplotlib scikit-learn
            pip install torch torchvision  (pentru secțiunea PyTorch)
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. TEORIA
# =============================================================================
"""
PERCEPTRONUL:
    y_hat = f(x · W + b)
    W = {w1, ..., wn} — ponderi
    b = w0            — bias
    f                 — funcție de activare

ALGORITMUL WIDROW-HOFF (Least Mean Squares):
    - Funcție activare: identitatea (f(x) = x)
    - Funcție pierdere: loss = (y_hat - y)^2 / 2
    - Regula de actualizare (gradient descent per exemplu):
        W ← W - η * (y_hat - y) * x
        b ← b - η * (y_hat - y)
    - η (eta) = rata de învățare (learning rate)

REȚEA FEEDFORWARD (2 straturi):
    Strat 1 (ascuns): z1 = X·W1 + b1,  a1 = tanh(z1)
    Strat 2 (ieșire): z2 = a1·W2 + b2, a2 = sigmoid(z2)
    Predicție: y_hat = sigmoid(tanh(X·W1+b1)·W2+b2)

FUNCȚII DE ACTIVARE:
    sigmoid(x) = 1 / (1 + exp(-x))  → output ∈ (0,1), derivata = s*(1-s)
    tanh(x)    = (e^2x - 1)/(e^2x + 1) → output ∈ (-1,1), derivata = 1 - tanh(x)^2
    ReLU(x)    = max(0, x)              → derivata = 1 dacă x>0, 0 altfel

FUNCȚIE DE PIERDERE:
    Logistic (Binary Cross-Entropy):
    loss = -y*log(y_hat) - (1-y)*log(1-y_hat)

BACKPROPAGATION (pentru rețeaua 2 straturi):
    dz2 = a2 - y
    dW2 = a1.T · dz2 / n
    db2 = sum(dz2) / n
    da1 = dz2 · W2.T
    dz1 = da1 * tanh_derivative(z1)
    dW1 = X.T · dz1 / n
    db1 = sum(dz1) / n

UPDATE PONDERI:
    W1 -= lr * dW1,  b1 -= lr * db1
    W2 -= lr * dW2,  b2 -= lr * db2
"""

# =============================================================================
# 2. FUNCȚII DE ACTIVARE ȘI DERIVATELE LOR
# =============================================================================

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

def tanh_activation(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x) ** 2

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

# =============================================================================
# 3. PERCEPTRON CU ALGORITMUL WIDROW-HOFF
# =============================================================================

class PerceptronWidrowHoff:
    """
    Perceptron simplu antrenat cu algoritmul Widrow-Hoff.
    Funcție de activare: identitatea (regresie liniară cu SGD).
    """

    def __init__(self, learning_rate=0.1, epochs=70):
        self.lr = learning_rate
        self.epochs = epochs
        self.W = None
        self.b = None

    def fit(self, X, y):
        """
        Antrenare cu Widrow-Hoff (gradient descent stochastic).
        X : shape (n_samples, n_features)
        y : shape (n_samples,)
        """
        n_samples, n_features = X.shape
        self.W = np.zeros(n_features)   # inițializare cu 0
        self.b = 0.0

        for epoch in range(self.epochs):
            # Amestecă datele la fiecare epocă
            indices = np.random.permutation(n_samples)
            X_shuffled = X[indices]
            y_shuffled = y[indices]

            for t in range(n_samples):
                x_t = X_shuffled[t]
                y_t = y_shuffled[t]

                # Forward: predicție (activare identitate)
                y_hat = x_t.dot(self.W) + self.b

                # Loss: (y_hat - y)^2 / 2

                # Backward: update ponderi
                error  = y_hat - y_t
                self.W -= self.lr * error * x_t
                self.b -= self.lr * error

    def predict(self, X):
        """Predicție: returnează 1 sau -1 (sau valoarea continuă)."""
        linear_output = X.dot(self.W) + self.b
        return np.sign(linear_output)   # -1 sau +1

    def predict_continuous(self, X):
        return X.dot(self.W) + self.b

    def score(self, X, y):
        return np.mean(self.predict(X) == y)


# --- Exercițiu 1: Date liniar separabile ---
print("=" * 60)
print("EXERCIȚIU 1 — Clasificare liniară")
print("=" * 60)

X_lin = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_lin = np.array([-1, 1, 1, 1])  # -1 pentru [0,0], +1 pentru rest

print("Date antrenare:")
for i in range(len(X_lin)):
    print(f"  X={X_lin[i]}, y={y_lin[i]}")

# Perceptronul poate separa aceste date (nu e XOR)
perceptron_lin = PerceptronWidrowHoff(learning_rate=0.1, epochs=70)
perceptron_lin.fit(X_lin, y_lin)
acc_lin = perceptron_lin.score(X_lin, y_lin)
print(f"\nAcuratețe pe antrenare: {acc_lin:.4f}")
print(f"Ponderi W: {perceptron_lin.W}")
print(f"Bias b: {perceptron_lin.b:.4f}")

# --- Exercițiu 3: XOR (nu e liniar separabil!) ---
print("\n" + "=" * 60)
print("EXERCIȚIU 3 — XOR (nu liniar separabil)")
print("=" * 60)

X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([-1, 1, 1, -1])  # XOR

perceptron_xor = PerceptronWidrowHoff(learning_rate=0.1, epochs=70)
perceptron_xor.fit(X_xor, y_xor)
acc_xor = perceptron_xor.score(X_xor, y_xor)
print(f"Acuratețe perceptron pe XOR: {acc_xor:.4f}")
print("(Se așteaptă acuratețe < 1.0 — XOR nu e liniar separabil!)")

# Funcție de afișare dreapta de decizie
def compute_y_boundary(x, W, b):
    """Calculează coordonata y a dreptei de decizie pentru un x dat."""
    return (-x * W[0] - b) / (W[1] + 1e-10)

def plot_decision_boundary(X, y, W, b, title="Dreapta de decizie"):
    x1, x2 = -0.5, 1.5
    y1 = compute_y_boundary(x1, W, b)
    y2 = compute_y_boundary(x2, W, b)

    plt.figure(figsize=(6, 5))
    plt.ylim(-0.5, 1.5)
    plt.xlim(-0.5, 1.5)
    plt.plot(X[y == -1, 0], X[y == -1, 1], 'b+', markersize=15, label='Clasa -1')
    plt.plot(X[y ==  1, 0], X[y ==  1, 1], 'r+', markersize=15, label='Clasa +1')
    plt.plot([x1, x2], [y1, y2], 'k-', label='Dreapta decizie')
    plt.legend()
    plt.title(title)
    plt.grid(True)
    plt.show()

plot_decision_boundary(X_lin, y_lin, perceptron_lin.W, perceptron_lin.b,
                        "Widrow-Hoff — Date liniar separabile")

# =============================================================================
# 4. REȚEA FEEDFORWARD NUMPY (din scratch) — Rezolvare XOR
# =============================================================================

print("\n" + "=" * 60)
print("4. REȚEA FEEDFORWARD — XOR")
print("=" * 60)

class FeedForwardNetwork:
    """
    Rețea neuronală feedforward cu un strat ascuns.
    Arhitectură: Input → [tanh] → Hidden → [sigmoid] → Output

    Parametri:
        input_dim       : dimensiunea datelor de intrare
        num_hidden      : numărul de neuroni pe stratul ascuns
        learning_rate   : rata de învățare
        epochs          : numărul de epoci
        miu, sigma      : media și deviația pentru inițializare ponderi
    """

    def __init__(self, input_dim=2, num_hidden=5, learning_rate=0.5,
                 epochs=70, miu=0, sigma=1, random_state=42):
        self.input_dim = input_dim
        self.num_hidden = num_hidden
        self.lr = learning_rate
        self.epochs = epochs
        self.miu = miu
        self.sigma = sigma
        self.random_state = random_state

        self._init_weights()

    def _init_weights(self):
        np.random.seed(self.random_state)
        # W1: shape (input_dim, num_hidden)
        self.W1 = np.random.normal(self.miu, self.sigma, (self.input_dim, self.num_hidden))
        self.b1 = np.zeros(self.num_hidden)
        # W2: shape (num_hidden, 1)
        self.W2 = np.random.normal(self.miu, self.sigma, (self.num_hidden, 1))
        self.b2 = np.zeros(1)

    def forward(self, X):
        """
        Pasul forward: calculează predicțiile rețelei.

        Returnează z1, a1, z2, a2 (necesare pentru backpropagation).
        """
        z1 = X.dot(self.W1) + self.b1      # (n, num_hidden)
        a1 = tanh_activation(z1)            # (n, num_hidden)
        z2 = a1.dot(self.W2) + self.b2      # (n, 1)
        a2 = sigmoid(z2)                    # (n, 1)
        return z1, a1, z2, a2

    def _compute_loss(self, a2, y):
        """Logistic loss (Binary Cross-Entropy)."""
        eps = 1e-8
        y_col = y.reshape(-1, 1)
        return (-y_col * np.log(a2 + eps) - (1 - y_col) * np.log(1 - a2 + eps)).mean()

    def backward(self, X, y, a1, a2, z1):
        """
        Pasul backward: calculează gradienții prin backpropagation.
        """
        n = X.shape[0]
        y_col = y.reshape(-1, 1)

        # Stratul 2 (output)
        dz2 = a2 - y_col                          # (n, 1) — derivata logistic_loss față de z2
        dW2 = a1.T.dot(dz2) / n                   # (num_hidden, 1)
        db2 = np.sum(dz2, axis=0) / n             # (1,)

        # Stratul 1 (hidden)
        da1 = dz2.dot(self.W2.T)                  # (n, num_hidden)
        dz1 = da1 * tanh_derivative(z1)            # (n, num_hidden)
        dW1 = X.T.dot(dz1) / n                    # (input_dim, num_hidden)
        db1 = np.sum(dz1, axis=0) / n             # (num_hidden,)

        return dW1, db1, dW2, db2

    def fit(self, X, y, verbose=True):
        """
        Antrenare completă cu gradient descent.
        """
        loss_history = []
        acc_history  = []

        for epoch in range(self.epochs):
            # Amestecă datele
            idx = np.random.permutation(X.shape[0])
            X_s, y_s = X[idx], y[idx]

            # Forward
            z1, a1, z2, a2 = self.forward(X_s)

            # Loss și acuratețe
            loss = self._compute_loss(a2, y_s)
            acc  = np.mean(np.round(a2).flatten() == y_s)
            loss_history.append(loss)
            acc_history.append(acc)

            if verbose and (epoch % 10 == 0 or epoch == self.epochs - 1):
                print(f"  Epocă {epoch:3d}: loss={loss:.4f}, acc={acc:.4f}")

            # Backward
            dW1, db1, dW2, db2 = self.backward(X_s, y_s, a1, a2, z1)

            # Update ponderi
            self.W1 -= self.lr * dW1
            self.b1 -= self.lr * db1
            self.W2 -= self.lr * dW2
            self.b2 -= self.lr * db2

        return loss_history, acc_history

    def predict(self, X):
        _, _, _, a2 = self.forward(X)
        return np.round(a2).flatten().astype(int)

    def score(self, X, y):
        return np.mean(self.predict(X) == y)


# Antrenare rețea pentru XOR
print("Antrenare rețea pentru XOR...")
X_xor_bin = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor_bin = np.array([0, 1, 1, 0])  # 0/1 pentru sigmoid (nu -1/1)

nn_xor = FeedForwardNetwork(
    input_dim=2,
    num_hidden=5,        # SCHIMBABIL: mai mulți neuroni → mai puternic dar mai lent
    learning_rate=0.5,   # SCHIMBABIL: prea mare → oscilații, prea mic → convergență lentă
    epochs=70,
    miu=0,               # SCHIMBABIL: media pentru inițializare
    sigma=1,             # SCHIMBABIL: std pentru inițializare
    random_state=42
)
loss_h, acc_h = nn_xor.fit(X_xor_bin, y_xor_bin, verbose=True)

print(f"\nAcuratețe finală XOR: {nn_xor.score(X_xor_bin, y_xor_bin):.4f}")

# Plot pierdere și acuratețe
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(loss_h)
ax1.set_title('Pierdere per epocă')
ax1.set_xlabel('Epocă')
ax1.set_ylabel('Logistic Loss')
ax1.grid(True)

ax2.plot(acc_h, color='green')
ax2.set_title('Acuratețe per epocă')
ax2.set_xlabel('Epocă')
ax2.set_ylabel('Acuratețe')
ax2.set_ylim(0, 1.1)
ax2.grid(True)
plt.tight_layout()
plt.show()

# =============================================================================
# 5. SKLEARN — MLPClassifier
# =============================================================================

print("\n" + "=" * 60)
print("5. SKLEARN MLPClassifier")
print("=" * 60)

from sklearn.neural_network import MLPClassifier

"""
MLPClassifier parametri:
    hidden_layer_sizes : tuple — ex: (100,) = 1 strat ascuns cu 100 neuroni
                                     (100, 50) = 2 straturi ascunse
    activation         : 'relu' (default), 'tanh', 'logistic', 'identity'
    solver             : 'adam' (default), 'sgd', 'lbfgs'
    learning_rate_init : float (default=0.001) — rata de învățare inițială
    max_iter           : int (default=200) — numărul maxim de epoci
    alpha              : float (default=0.0001) — regularizare L2
    batch_size         : int sau 'auto' — min(200, n_samples) dacă 'auto'
    momentum           : float (default=0.9) — pentru SGD cu momentum
    early_stopping     : bool — oprire dacă nu se îmbunătățește pe validare
"""

# XOR cu MLPClassifier
mlp_xor = MLPClassifier(
    hidden_layer_sizes=(5,),          # SCHIMBABIL: (10,), (10, 5), etc.
    activation='tanh',                # SCHIMBABIL: 'relu', 'logistic'
    solver='sgd',                     # lab folosește SGD
    learning_rate_init=0.5,           # SCHIMBABIL
    max_iter=70,                      # SCHIMBABIL
    random_state=42
)
mlp_xor.fit(X_xor_bin, y_xor_bin)
print(f"MLPClassifier XOR acuratețe: {mlp_xor.score(X_xor_bin, y_xor_bin):.4f}")

# MNIST cu MLPClassifier
print("\n--- MLPClassifier pe MNIST ---")
from sklearn.datasets import load_digits  # 8x8 digits, mai rapid decât MNIST complet
digits = load_digits()
X_d, y_d = digits.data, digits.target

from sklearn.model_selection import train_test_split
X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(
    X_d, y_d, test_size=0.2, random_state=42
)

# Normalizare
from sklearn.preprocessing import StandardScaler
scaler_d = StandardScaler()
X_train_d = scaler_d.fit_transform(X_train_d)
X_test_d  = scaler_d.transform(X_test_d)

for config in [
    {'hidden_layer_sizes': (10,),   'activation': 'tanh',  'learning_rate_init': 1e-2},
    {'hidden_layer_sizes': (100,),  'activation': 'tanh',  'learning_rate_init': 1e-2},
    {'hidden_layer_sizes': (100,),  'activation': 'relu',  'learning_rate_init': 1e-2},
    {'hidden_layer_sizes': (100, 100), 'activation': 'relu', 'learning_rate_init': 1e-2},
]:
    mlp = MLPClassifier(solver='sgd', max_iter=100, random_state=42, **config)
    mlp.fit(X_train_d, y_train_d)
    acc = mlp.score(X_test_d, y_test_d)
    layers = config['hidden_layer_sizes']
    act    = config['activation']
    lr     = config['learning_rate_init']
    print(f"  Straturi={layers}, act={act}, lr={lr}: {acc:.4f}")

# =============================================================================
# 6. PYTORCH MLP
# =============================================================================

print("\n" + "=" * 60)
print("6. PYTORCH MLP")
print("=" * 60)

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    from torch.utils.data import DataLoader
    from torchvision import datasets
    from torchvision.transforms import ToTensor

    print(f"PyTorch disponibil: {torch.__version__}")

    # Verificare GPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    # Definire rețea
    class NeuralNetworkMNIST(nn.Module):
        """
        MLP simplu pentru MNIST.
        Input: 28x28 = 784 → Flatten → Linear(784, 512) → ReLU →
               Linear(512, 512) → ReLU → Linear(512, 10)
        """
        def __init__(self, hidden_size=512, num_hidden_layers=2, activation='relu'):
            super().__init__()
            self.flatten = nn.Flatten()

            # Construim straturi dinamic
            layers = []
            in_size = 28 * 28
            for _ in range(num_hidden_layers):
                layers.append(nn.Linear(in_size, hidden_size))
                if activation == 'relu':
                    layers.append(nn.ReLU())
                elif activation == 'tanh':
                    layers.append(nn.Tanh())
                in_size = hidden_size
            layers.append(nn.Linear(in_size, 10))  # 10 clase cifre

            self.network = nn.Sequential(*layers)

        def forward(self, x):
            x = self.flatten(x)
            return self.network(x)

    # Descărcare MNIST și creare DataLoaders
    train_data = datasets.MNIST(root="data", train=True, download=True, transform=ToTensor())
    test_data  = datasets.MNIST(root="data", train=False, download=True, transform=ToTensor())

    train_dataloader = DataLoader(train_data, batch_size=64, shuffle=True)
    test_dataloader  = DataLoader(test_data,  batch_size=64, shuffle=False)

    # Creare model și optimizer
    model     = NeuralNetworkMNIST(hidden_size=512, num_hidden_layers=2, activation='relu')
    model     = model.to(device)
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.0)
    # SCHIMBABIL: lr, momentum, sau
    # optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)  — converge mai rapid

    loss_fn = nn.CrossEntropyLoss()  # SCHIMBABIL: nn.NLLLoss() cu LogSoftmax, etc.

    NUM_EPOCHS = 5  # SCHIMBABIL

    def train_epoch(model, dataloader, optimizer, loss_fn, device):
        model.train()
        total_loss = 0
        for batch, (X_batch, y_batch) in enumerate(dataloader):
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)

            pred = model(X_batch)            # forward
            loss = loss_fn(pred, y_batch)    # calcul loss

            optimizer.zero_grad()            # reset gradienți
            loss.backward()                  # backpropagation
            optimizer.step()                 # actualizare ponderi

            total_loss += loss.item()
            if batch % 200 == 0:
                print(f"    Batch {batch}/{len(dataloader)}, loss: {loss.item():.4f}")

        return total_loss / len(dataloader)

    def evaluate(model, dataloader, loss_fn, device):
        model.eval()
        correct = 0
        total_loss = 0
        size = len(dataloader.dataset)

        with torch.no_grad():
            for X_batch, y_batch in dataloader:
                X_batch, y_batch = X_batch.to(device), y_batch.to(device)
                pred       = model(X_batch)
                total_loss += loss_fn(pred, y_batch).item()
                correct    += (pred.argmax(1) == y_batch).type(torch.float).sum().item()

        accuracy = correct / size
        avg_loss = total_loss / len(dataloader)
        return accuracy, avg_loss

    print("\nAntrenare PyTorch MLP pe MNIST...")
    for epoch in range(NUM_EPOCHS):
        print(f"\n=== Epocă {epoch+1}/{NUM_EPOCHS} ===")
        train_loss = train_epoch(model, train_dataloader, optimizer, loss_fn, device)
        acc, test_loss = evaluate(model, test_dataloader, loss_fn, device)
        print(f"Epocă {epoch+1}: train_loss={train_loss:.4f}, test_acc={acc:.4f}")

    print(f"\nAcuratețe finală pe test: {acc:.4f}")

except ImportError:
    print("PyTorch nu este instalat. Rulează: pip install torch torchvision")
    print("Secțiunea PyTorch a fost sărită.")

# =============================================================================
# NOTE: CE POATE FI MODIFICAT
# =============================================================================
"""
VARIANTE ȘI IMPACTE:

1. learning_rate (η):
   - Prea mare (0.5+ pentru rețele adânci): oscilații, pierdere crește
   - Prea mic (1e-5): convergență lentă, poate rămâne blocat
   - Optim: 1e-2 pentru SGD pe MNIST; 1e-3 pentru Adam
   - Impact cod: nimic altceva nu se schimbă

2. num_hidden_neurons (MLPClassifier / NeuralNetworkMNIST):
   - Mai mulți neuroni → mai multă capacitate → posibil overfitting dacă date puține
   - Mai puțini neuroni → model mai simplu → posibil underfitting
   - Regula practică: 2x features pentru strat simplu

3. Funcție activare:
   - 'tanh': output ∈ (-1,1), centrat în origine, bun pentru rețele mici
   - 'relu': nu saturează pentru x>0, standard în deep learning
   - 'logistic'/'sigmoid': output ∈ (0,1), se saturează la extreme (dispariția gradientului)
   - Schimbare cod: MLPClassifier(activation='relu'); PyTorch: nn.ReLU() / nn.Tanh()

4. Optimizer (PyTorch):
   - SGD: simplu, stabil, necesită tuning manual al lr
   - SGD+momentum: converge mai rapid, acumulează direcție de coborâre
     optimizer = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)
   - Adam: adaptiv, nu necesită tuning extins, standard în practică
     optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

5. batch_size (PyTorch DataLoader):
   - batch_size=1: SGD pur — zgomot mare, convergență lentă
   - batch_size=32/64: mini-batch — echilibru bun
   - batch_size=toată mulțimea: gradient descent complet — lent per epocă
   - Impactul: batch mai mare → gradient mai stabil dar mai puțin generalizare

6. Inițializarea ponderilor:
   - zeros: problematic (toți neuronii evoluează identic = breaking symmetry)
   - random small: standard pentru Widrow-Hoff din laborator
   - Xavier/Glorot: recomandat pentru tanh (PyTorch default)
   - He/Kaiming: recomandat pentru ReLU (PyTorch default pentru nn.Linear cu ReLU)

7. Minima locale în XOR:
   - Rețeaua poate converge la minime locale diferite în funcție de inițializare
   - Solut: mai mulți neuroni, learning rate diferit, mai multe epoci
   - random_state diferit → rezultate diferite
"""

print("\nLaborator 6 completat!")
