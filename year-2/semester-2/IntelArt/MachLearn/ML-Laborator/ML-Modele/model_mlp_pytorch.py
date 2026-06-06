"""
=============================================================================
MODEL: MLP PyTorch — Setup Complet, Gata de Rulat
=============================================================================
Lab: 6 | Dataset: MNIST (28x28)
Algoritm: Multilayer Perceptron cu PyTorch, SGD/Adam, CrossEntropyLoss

RULARE: python model_mlp_pytorch.py
pip install torch torchvision numpy matplotlib
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# ===================== HYPERPARAMETRI (SCHIMBĂ AICI) ========================
HIDDEN_SIZE    = 512     # neuroni per strat ascuns: {64, 128, 256, 512}
NUM_LAYERS     = 2       # număr straturi ascunse: {1, 2, 3}
ACTIVATION     = 'relu'  # 'relu' sau 'tanh'
LEARNING_RATE  = 1e-2    # rata de învățare: {1e-4, 1e-3, 1e-2}
OPTIMIZER_TYPE = 'sgd'   # 'sgd' sau 'adam'
MOMENTUM       = 0.0     # momentum SGD: {0.0, 0.9}
BATCH_SIZE     = 64      # mărimea batch: {32, 64, 128}
NUM_EPOCHS     = 5       # numărul de epoci: {5, 10, 20}
# ============================================================================

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    from torch.utils.data import DataLoader
    from torchvision import datasets
    from torchvision.transforms import Compose, ToTensor, Normalize
except ImportError:
    print("PyTorch nu este instalat!")
    print("Instalează cu: pip install torch torchvision")
    exit(1)

print(f"PyTorch {torch.__version__}")
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device: {device}")

# --- Dataset MNIST ---
# Normalizare cu media și std-ul MNIST
# mean=0.1307, std=0.3081 sunt valorile standard pentru MNIST
transform = Compose([
    ToTensor(),
    Normalize(mean=(0.1307,), std=(0.3081,))  # SCHIMBABIL: dacă nu normalizezi,
    # antrenarea e mai lentă și mai instabilă
])

train_data = datasets.MNIST(root="data", train=True,  download=True, transform=transform)
test_data  = datasets.MNIST(root="data", train=False, download=True, transform=transform)

train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
test_loader  = DataLoader(test_data,  batch_size=BATCH_SIZE, shuffle=False)

print(f"Train: {len(train_data)} exemple, Test: {len(test_data)} exemple")
print(f"Nr. batch-uri train: {len(train_loader)}")

# --- Definire model ---
class MLP(nn.Module):
    """
    Multilayer Perceptron flexibil pentru MNIST.

    Input: 28x28 = 784 pixeli → Flatten
    Straturi ascunse: NUM_LAYERS × Linear → Activare
    Output: Linear(hidden, 10) → 10 clase

    nn.Module este clasa de bază pentru orice model PyTorch.
    TREBUIE să implementezi __init__ și forward.
    """
    def __init__(self, hidden_size=512, num_layers=2, activation='relu'):
        super().__init__()
        self.flatten = nn.Flatten()  # transformă (batch, 1, 28, 28) → (batch, 784)

        # Construim straturile dinamic
        layers = []
        in_size = 28 * 28
        for i in range(num_layers):
            layers.append(nn.Linear(in_size, hidden_size))
            # Linear: y = x·W^T + b (W are shape (out_features, in_features))

            if activation == 'relu':
                layers.append(nn.ReLU())
            elif activation == 'tanh':
                layers.append(nn.Tanh())
            elif activation == 'sigmoid':
                layers.append(nn.Sigmoid())
            in_size = hidden_size

        # Stratul de output: fără activare (CrossEntropyLoss include softmax intern)
        layers.append(nn.Linear(in_size, 10))

        self.network = nn.Sequential(*layers)

    def forward(self, x):
        """
        Pasul forward: procesează datele de intrare.
        Apelat automat la model(x).
        """
        x = self.flatten(x)    # (batch, 1, 28, 28) → (batch, 784)
        return self.network(x)  # (batch, 784) → (batch, 10)


model = MLP(hidden_size=HIDDEN_SIZE, num_layers=NUM_LAYERS, activation=ACTIVATION)
model = model.to(device)

# Afișare arhitectură
print(f"\nArhitectură model:")
print(model)
total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"Parametri totali: {total_params:,}")

# --- Optimizer ---
if OPTIMIZER_TYPE == 'sgd':
    optimizer = torch.optim.SGD(
        model.parameters(),
        lr=LEARNING_RATE,
        momentum=MOMENTUM      # SCHIMBABIL: 0.9 ajută mult la convergență
    )
elif OPTIMIZER_TYPE == 'adam':
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=LEARNING_RATE,
        betas=(0.9, 0.999),    # SCHIMBABIL: parametri Adam (de obicei nu se schimbă)
        eps=1e-8
    )

# --- Funcție de pierdere ---
loss_fn = nn.CrossEntropyLoss()
# CrossEntropyLoss = LogSoftmax + NLLLoss
# Alternativă: nn.NLLLoss() cu F.log_softmax(pred, dim=1) în forward

# --- Funcții de antrenare și evaluare ---
def train_one_epoch(model, loader, optimizer, loss_fn, device, epoch):
    model.train()  # activează Dropout, BatchNorm etc. (dacă există)
    total_loss = 0.0
    for batch_idx, (X_batch, y_batch) in enumerate(loader):
        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)

        # Forward
        pred = model(X_batch)                     # (batch, 10) — logits
        loss = loss_fn(pred, y_batch)             # scalar

        # Backward
        optimizer.zero_grad()   # IMPORTANT: șterge gradienții din pasul anterior!
        loss.backward()         # calculează gradienții
        optimizer.step()        # actualizează ponderile: W -= lr * grad_W

        total_loss += loss.item()
        if batch_idx % 200 == 0:
            print(f"  Batch {batch_idx:4d}/{len(loader)}, loss: {loss.item():.4f}")

    return total_loss / len(loader)


def evaluate(model, loader, loss_fn, device):
    model.eval()  # dezactivează Dropout, BatchNorm în mod evaluare
    correct    = 0
    total_loss = 0.0

    with torch.no_grad():  # nu calculăm gradienți la evaluare (economie memorie/timp)
        for X_batch, y_batch in loader:
            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)

            pred        = model(X_batch)
            total_loss += loss_fn(pred, y_batch).item()

            # pred.argmax(1) = clasa cu scorul maxim
            correct    += (pred.argmax(1) == y_batch).type(torch.float).sum().item()

    accuracy = correct / len(loader.dataset)
    avg_loss = total_loss / len(loader)
    return accuracy, avg_loss


# --- Loop de antrenare ---
print(f"\n{'='*60}")
print(f"ANTRENARE: {OPTIMIZER_TYPE.upper()}, lr={LEARNING_RATE}, momentum={MOMENTUM}")
print(f"Arhitectură: {NUM_LAYERS}×{HIDDEN_SIZE} {ACTIVATION.upper()}, batch={BATCH_SIZE}")
print('='*60)

train_losses, test_accs = [], []
best_acc = 0.0

for epoch in range(NUM_EPOCHS):
    print(f"\n=== Epocă {epoch+1}/{NUM_EPOCHS} ===")
    tr_loss = train_one_epoch(model, train_loader, optimizer, loss_fn, device, epoch)
    te_acc, te_loss = evaluate(model, test_loader, loss_fn, device)

    train_losses.append(tr_loss)
    test_accs.append(te_acc)

    if te_acc > best_acc:
        best_acc = te_acc
        torch.save(model.state_dict(), 'best_mlp_mnist.pth')

    print(f"  Train Loss: {tr_loss:.4f} | Test Loss: {te_loss:.4f} | Test Acc: {te_acc:.4f}")

print(f"\nCea mai bună acuratețe: {best_acc:.4f}")

# --- Vizualizare ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(range(1, NUM_EPOCHS+1), train_losses, 'b-o')
ax1.set_xlabel('Epocă'); ax1.set_ylabel('Train Loss')
ax1.set_title('Pierdere antrenare'); ax1.grid(True)

ax2.plot(range(1, NUM_EPOCHS+1), [a*100 for a in test_accs], 'g-o')
ax2.set_xlabel('Epocă'); ax2.set_ylabel('Test Accuracy (%)')
ax2.set_title('Acuratețe test'); ax2.grid(True)

plt.suptitle(f'MLP MNIST — {OPTIMIZER_TYPE.upper()}, lr={LEARNING_RATE}, {NUM_LAYERS}×{HIDDEN_SIZE}')
plt.tight_layout(); plt.show()

# --- Predicție pe exemple individuale ---
print("\n--- Predicție exemple ---")
model.eval()
test_examples = next(iter(test_loader))
X_ex, y_ex = test_examples[0][:10].to(device), test_examples[1][:10]
with torch.no_grad():
    preds = model(X_ex).argmax(1).cpu().numpy()

fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    img = X_ex[i].cpu().squeeze().numpy()
    ax.imshow(img, cmap='gray')
    color = 'green' if preds[i] == y_ex[i].item() else 'red'
    ax.set_title(f"R:{y_ex[i].item()} P:{preds[i]}", color=color, fontsize=9)
    ax.axis('off')
plt.suptitle("Predicții (verde=corect, roșu=greșit)")
plt.tight_layout(); plt.show()

# --- Custom Dataset (structura din laborator) ---
print("\n--- Structura Custom Dataset ---")
print("""
# Dacă ai datele tale (nu din torchvision), folosești structura:

import os
import pandas as pd
from torch.utils.data import Dataset
from torchvision.io import read_image

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels      = pd.read_csv(annotations_file)
        self.img_dir         = img_dir
        self.transform       = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image    = read_image(img_path)
        label    = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label

# Utilizare:
# dataset = CustomImageDataset('labels.csv', 'images/', transform=ToTensor())
# loader  = DataLoader(dataset, batch_size=32, shuffle=True)
""")

print("\nModel MLP PyTorch completat!")
