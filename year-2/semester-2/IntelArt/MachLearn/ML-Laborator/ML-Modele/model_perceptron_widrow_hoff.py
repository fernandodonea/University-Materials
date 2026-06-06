"""
=============================================================================
MODEL: Perceptron Widrow-Hoff + Rețea Feedforward (Numpy) — Setup Complet
=============================================================================
Lab: 6 | Dataset: XOR, date liniar separabile
Algoritm: Widrow-Hoff (LMS), gradient descent, backpropagation manual

RULARE: python model_perceptron_widrow_hoff.py
pip install numpy matplotlib
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# ===================== HYPERPARAMETRI (SCHIMBĂ AICI) ========================
# Perceptron Widrow-Hoff
LR_WIDROW      = 0.1    # rata de învățare: {0.01, 0.1, 0.5}
EPOCHS_WIDROW  = 70     # epoci: {50, 70, 100, 200}

# Rețea feedforward
LR_NN          = 0.5    # rata de învățare rețea: {0.1, 0.5, 1.0}
EPOCHS_NN      = 200    # epoci rețea: {70, 200, 500}
NUM_HIDDEN     = 5      # neuroni strat ascuns: {2, 5, 10, 20}
MIU            = 0      # media init ponderi: 0
SIGMA          = 1      # std init ponderi: {0.1, 0.5, 1}
RANDOM_SEED    = 42
# ============================================================================

# =============================================================================
# FUNCȚII DE ACTIVARE
# =============================================================================

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def tanh_d(x):
    """Derivata funcției tanh."""
    return 1 - np.tanh(x) ** 2

# =============================================================================
# 1. PERCEPTRON WIDROW-HOFF
# =============================================================================

print("=" * 60)
print("1. PERCEPTRON WIDROW-HOFF")
print("=" * 60)

class PerceptronWidrowHoff:
    """
    Perceptron cu algoritmul Widrow-Hoff (gradient descent stochastic).
    Funcție de activare la predicție: sign() → returnează -1 sau +1
    Funcție de activare la antrenare: identitatea (f(x)=x)

    Regula de actualizare:
        W ← W - lr * (y_hat - y) * x
        b ← b - lr * (y_hat - y)
    """
    def __init__(self, learning_rate=0.1, epochs=70, random_state=42):
        self.lr     = learning_rate
        self.epochs = epochs
        self.rs     = random_state
        self.W      = None
        self.b      = None
        self.loss_history = []
        self.acc_history  = []

    def fit(self, X, y, verbose=True):
        np.random.seed(self.rs)
        n_samples, n_features = X.shape
        self.W = np.zeros(n_features)
        self.b = 0.0

        for epoch in range(self.epochs):
            idx = np.random.permutation(n_samples)
            X_s, y_s = X[idx], y[idx]
            epoch_loss = 0.0

            for t in range(n_samples):
                x_t    = X_s[t]
                y_t    = y_s[t]
                y_hat  = x_t.dot(self.W) + self.b     # identitate ca activare
                error  = y_hat - y_t
                epoch_loss += error ** 2 / 2

                # Update (gradient descent stochastic)
                self.W -= self.lr * error * x_t
                self.b -= self.lr * error

            acc = self.score(X, y)
            self.loss_history.append(epoch_loss / n_samples)
            self.acc_history.append(acc)

            if verbose and (epoch % 10 == 0 or epoch == self.epochs - 1):
                print(f"  Epocă {epoch:3d}: loss={epoch_loss/n_samples:.4f}, acc={acc:.4f}")

    def predict(self, X):
        return np.sign(X.dot(self.W) + self.b)

    def score(self, X, y):
        return np.mean(self.predict(X) == y)


# Date liniar separabile (Exercițiu 2)
X_lin = np.array([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
y_lin = np.array([-1., 1., 1., 1.])

print("Date: X_lin, y_lin")
print("Așteptat: acuratețe 1.0 (liniar separabil)")

pw = PerceptronWidrowHoff(learning_rate=LR_WIDROW, epochs=EPOCHS_WIDROW, random_state=RANDOM_SEED)
pw.fit(X_lin, y_lin, verbose=True)
print(f"\nAcuratețe finală: {pw.score(X_lin, y_lin):.4f}")
print(f"Ponderi W: {pw.W}")
print(f"Bias b: {pw.b:.4f}")

# Vizualizare dreapta de decizie
def plot_boundary(X, y, W, b, title):
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.set_ylim(-0.5, 1.5); ax.set_xlim(-0.5, 1.5)
    ax.plot(X[y==-1, 0], X[y==-1, 1], 'b+', ms=15, label='Clasa -1')
    ax.plot(X[y== 1, 0], X[y== 1, 1], 'r+', ms=15, label='Clasa +1')
    # Dreapta: x0*W[0] + x1*W[1] + b = 0 → x1 = (-x0*W[0] - b) / W[1]
    xx = np.array([-0.5, 1.5])
    yy = (-xx * W[0] - b) / (W[1] + 1e-10)
    ax.plot(xx, yy, 'k-', label='Dreapta decizie')
    ax.legend(); ax.set_title(title); ax.grid(True)
    plt.tight_layout(); plt.show()

plot_boundary(X_lin, y_lin, pw.W, pw.b, "Widrow-Hoff — Liniar Separabil")

# Date XOR (Exercițiu 3 — nu e liniar separabil!)
X_xor = np.array([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
y_xor = np.array([-1., 1., 1., -1.])

pw_xor = PerceptronWidrowHoff(learning_rate=LR_WIDROW, epochs=EPOCHS_WIDROW, random_state=RANDOM_SEED)
pw_xor.fit(X_xor, y_xor, verbose=False)
print(f"\nXOR — Acuratețe perceptron: {pw_xor.score(X_xor, y_xor):.4f}")
print("(< 1.0 așteptat — XOR nu e liniar separabil cu un singur perceptron)")
plot_boundary(X_xor, y_xor, pw_xor.W, pw_xor.b, "Widrow-Hoff — XOR (imposibil liniar)")

# =============================================================================
# 2. REȚEA FEEDFORWARD (2 straturi) — REZOLVĂ XOR
# =============================================================================

print("\n" + "=" * 60)
print("2. REȚEA FEEDFORWARD — XOR")
print("=" * 60)

"""
Arhitectură:
    Input (2) → [W1, b1] → tanh → Hidden (num_hidden) → [W2, b2] → sigmoid → Output (1)

Funcție pierdere: Binary Cross-Entropy (logistic loss)
    loss = -y*log(y_hat) - (1-y)*log(1-y_hat)

Predicție:
    y_hat = sigmoid(tanh(X·W1 + b1)·W2 + b2)
"""

class FeedForwardXOR:
    """
    Rețea feedforward cu un strat ascuns pentru clasificare binară.
    Antrenată cu backpropagation și gradient descent.
    """
    def __init__(self, num_hidden=5, lr=0.5, epochs=200,
                 miu=0, sigma=1, random_state=42):
        self.num_hidden = num_hidden
        self.lr         = lr
        self.epochs     = epochs
        self.miu        = miu
        self.sigma      = sigma
        self.rs         = random_state
        self._init_weights()

    def _init_weights(self):
        np.random.seed(self.rs)
        self.W1 = np.random.normal(self.miu, self.sigma, (2, self.num_hidden))
        self.b1 = np.zeros(self.num_hidden)
        self.W2 = np.random.normal(self.miu, self.sigma, (self.num_hidden, 1))
        self.b2 = np.zeros(1)

    def forward(self, X):
        self.z1 = X.dot(self.W1) + self.b1        # (n, num_hidden)
        self.a1 = np.tanh(self.z1)                 # (n, num_hidden)
        self.z2 = self.a1.dot(self.W2) + self.b2  # (n, 1)
        self.a2 = sigmoid(self.z2)                 # (n, 1)
        return self.a2

    def backward(self, X, y):
        n      = X.shape[0]
        y_col  = y.reshape(-1, 1)

        # Strat output
        dz2 = self.a2 - y_col                     # (n, 1)
        dW2 = self.a1.T.dot(dz2) / n              # (num_hidden, 1)
        db2 = np.sum(dz2, axis=0) / n             # (1,)

        # Strat hidden
        da1 = dz2.dot(self.W2.T)                  # (n, num_hidden)
        dz1 = da1 * tanh_d(self.z1)               # (n, num_hidden)
        dW1 = X.T.dot(dz1) / n                    # (2, num_hidden)
        db1 = np.sum(dz1, axis=0) / n             # (num_hidden,)

        return dW1, db1, dW2, db2

    def fit(self, X, y, verbose=True):
        loss_h, acc_h = [], []
        for ep in range(self.epochs):
            # Shuffle
            idx   = np.random.permutation(len(X))
            X_s, y_s = X[idx], y[idx]

            # Forward
            a2   = self.forward(X_s)

            # Loss (logistic)
            eps  = 1e-8
            y_c  = y_s.reshape(-1, 1)
            loss = (-y_c*np.log(a2+eps) - (1-y_c)*np.log(1-a2+eps)).mean()
            acc  = np.mean(np.round(a2).flatten() == y_s)
            loss_h.append(loss); acc_h.append(acc)

            # Backward + update
            dW1, db1, dW2, db2 = self.backward(X_s, y_s)
            self.W1 -= self.lr * dW1
            self.b1 -= self.lr * db1
            self.W2 -= self.lr * dW2
            self.b2 -= self.lr * db2

            if verbose and (ep % 20 == 0 or ep == self.epochs - 1):
                print(f"  Epocă {ep:3d}: loss={loss:.4f}, acc={acc:.4f}")

        return loss_h, acc_h

    def predict(self, X):
        return np.round(self.forward(X)).flatten().astype(int)

    def score(self, X, y):
        return np.mean(self.predict(X) == y)


# Date XOR cu etichete 0/1 (pentru sigmoid)
X_xor_01 = np.array([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
y_xor_01  = np.array([0., 1., 1., 0.])

print(f"Antrenare rețea XOR: {NUM_HIDDEN} neuroni ascunși, lr={LR_NN}, epoci={EPOCHS_NN}")
nn = FeedForwardXOR(num_hidden=NUM_HIDDEN, lr=LR_NN, epochs=EPOCHS_NN,
                    miu=MIU, sigma=SIGMA, random_state=RANDOM_SEED)
loss_h, acc_h = nn.fit(X_xor_01, y_xor_01, verbose=True)

print(f"\nAcuratețe finală XOR: {nn.score(X_xor_01, y_xor_01):.4f}")
print(f"Predicții: {nn.predict(X_xor_01)}")
print(f"Etichete:  {y_xor_01.astype(int)}")

# Vizualizare antrenare
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(loss_h); ax1.set_title('Pierdere per epocă'); ax1.set_xlabel('Epocă'); ax1.grid(True)
ax2.plot(acc_h, 'g'); ax2.set_title('Acuratețe per epocă'); ax2.set_xlabel('Epocă')
ax2.set_ylim(0, 1.1); ax2.grid(True)
plt.tight_layout(); plt.show()

# Vizualizare funcție de decizie (spațiu 2D)
def plot_decision_2d(nn, X_data, y_data, title):
    np.random.seed(0)
    xx = np.random.uniform(-0.5, 1.5, 10000)
    yy = np.random.uniform(-0.5, 1.5, 10000)
    grid = np.column_stack([xx, yy])
    preds = nn.predict(grid)

    plt.figure(figsize=(6, 5))
    plt.plot(grid[preds==0, 0], grid[preds==0, 1], 'b.', alpha=0.1, ms=2)
    plt.plot(grid[preds==1, 0], grid[preds==1, 1], 'r.', alpha=0.1, ms=2)
    plt.plot(X_data[y_data==0, 0], X_data[y_data==0, 1], 'bs', ms=12)
    plt.plot(X_data[y_data==1, 0], X_data[y_data==1, 1], 'rs', ms=12)
    plt.title(title); plt.xlim(-0.5, 1.5); plt.ylim(-0.5, 1.5)
    plt.grid(True); plt.tight_layout(); plt.show()

plot_decision_2d(nn, X_xor_01, y_xor_01, f"Funcție de decizie XOR (hidden={NUM_HIDDEN})")

print("\nModel Perceptron + Rețea Feedforward completat!")
