"""
=============================================================================
LABORATOR 1 - Introducere în NumPy și Matplotlib
=============================================================================
Materie: Inteligență Artificială - Machine Learning
Acoperire completă: vectori, indexare, operații matematice, broadcasting, plotare

RULARE: python lab1_numpy_matplotlib.py
Dependențe: pip install numpy matplotlib scikit-image
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. CREAREA ARRAY-URILOR NUMPY
# =============================================================================

print("=" * 60)
print("1. CREAREA ARRAY-URILOR")
print("=" * 60)

# Din liste Python
a = np.array([1, 2, 3])
print(f"Vector 1D: {a}")                      # [1 2 3]
print(f"Tip obiect: {type(a)}")               # numpy.ndarray
print(f"Tip date: {a.dtype}")                 # int64
print(f"Shape: {a.shape}")                    # (3,)
print(f"Primul element: {a[0]}")              # 1

b = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nMatrice 2D shape: {b.shape}")       # (2, 3)
print(f"Element [0][2]: {b[0, 2]}")           # 3

# Funcții de creare
print("\n--- Funcții de creare ---")
zero_array     = np.zeros((3, 2))             # matrice de zerouri
ones_array     = np.ones((2, 2))              # matrice de unuri
constant_array = np.full((2, 2), 8)           # matrice constantă
identity       = np.eye(3)                    # matrice identitate 3x3
random_uniform = np.random.random((2, 3))     # uniform [0, 1)
random_normal  = np.random.normal(0, 0.1, (3, 6))  # Gaussian, medie=0, std=0.1
first_5        = np.arange(5)                 # [0 1 2 3 4]
linspace_arr   = np.linspace(0, 255, 5)       # 5 valori uniform între 0 și 255

print(f"zeros(3,2):\n{zero_array}")
print(f"ones(2,2):\n{ones_array}")
print(f"full(2,2,8):\n{constant_array}")
print(f"eye(3):\n{identity}")
print(f"arange(5): {first_5}")
print(f"linspace(0,255,5): {linspace_arr}")

# =============================================================================
# 2. INDEXARE ȘI SLICING
# =============================================================================

print("\n" + "=" * 60)
print("2. INDEXARE ȘI SLICING")
print("=" * 60)

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Slicing de bază: arr[linii, coloane]
print(f"Toate liniile, coloanele 0-2:\n{arr[:, 0:3]}")
print(f"Linia 2:\n{arr[2, :]}")
print(f"Ultimele 2 linii, ultimele 2 col:\n{arr[1:, 2:]}")

# IMPORTANT: slicing creează o referință, nu o copie!
slice_ref  = arr[:, 0:3]   # referință — modificările afectează originalul
slice_copy = np.copy(arr[:, 0:3])  # copie independentă

# Indexare cu vector de întregi
print(f"\nElementele [0,1] și [0,3]: {arr[[0, 0], [1, 3]]}")  # [2, 4]

# Indexare booleană — extrem de utilă în ML pentru filtrare
bool_mask = arr > 10
print(f"\nElementele > 10: {arr[bool_mask]}")   # [11, 12]
print(f"Direct: {arr[arr > 5]}")               # toate > 5

# Reshape — modifică forma fără a copia datele
reshaped = np.reshape(arr, (2, 6))
print(f"\nReshape (2,6):\n{reshaped}")

# ravel — aplatizare la 1D
flat = np.ravel(arr)
print(f"Ravel: {flat}")

# =============================================================================
# 3. FUNCȚII MATEMATICE
# =============================================================================

print("\n" + "=" * 60)
print("3. FUNCȚII MATEMATICE")
print("=" * 60)

x = np.array([[1., 2.], [3., 4.]])
y = np.array([[5., 6.], [7., 8.]])

print(f"x + y:\n{x + y}")               # suma element cu element
print(f"x - y:\n{x - y}")               # diferență
print(f"x * y:\n{x * y}")               # produs element cu element (NU înmulțire matrici!)
print(f"x / y:\n{x / y}")               # împărțire element cu element
print(f"sqrt(x):\n{np.sqrt(x)}")        # radical
print(f"x^3: {np.power(np.arange(5), 3)}")  # putere: [0, 1, 8, 27, 64]

# Produs scalar / înmulțire matrici
v = np.array([9, 10])
w = np.array([11, 12])
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"\nProdus scalar v·w: {v.dot(w)}")            # 219
print(f"Matrice x vector: {np.matmul(A, v)}")        # [29, 67]
print(f"Matrice x matrice:\n{np.matmul(A, B)}")      # [[19,22],[43,50]]
print(f"Transpusa:\n{A.T}")
print(f"Inversa:\n{np.linalg.inv(A.astype(float))}")

# Operații pe axe — esențiale pentru calculul mediei, normalizării etc.
z = np.array([[1, 2], [3, 4], [5, 6]])  # shape (3, 2)
print(f"\nSum total: {np.sum(z)}")
print(f"Sum pe coloane (axis=0): {np.sum(z, axis=0)}")   # suma fiecărei coloane
print(f"Sum pe linii (axis=1): {np.sum(z, axis=1)}")     # suma fiecărei linii
print(f"Mean pe coloane: {np.mean(z, axis=0)}")
print(f"Std pe coloane: {np.std(z, axis=0)}")
print(f"Argmax pe linii: {np.argmax(z, axis=1)}")        # indexul max pe fiecare linie

# Funcții utile pentru ML
print(f"\nMin: {np.min(z)}, Max: {np.max(z)}")
print(f"Argsort: {np.argsort(np.array([3,1,2]))}")      # [1 2 0] — indecși sortați
print(f"Bincount: {np.bincount(np.array([0,1,1,3,2,1,7]))}")  # nr aparitii fiecărei valori
print(f"Where (elem>3): {np.where(z > 3)}")

# =============================================================================
# 4. BROADCASTING
# =============================================================================

print("\n" + "=" * 60)
print("4. BROADCASTING")
print("=" * 60)

# Broadcasting permite operații între array-uri de forme diferite
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # (4, 3)
v = np.array([1, 0, 1])  # (3,) — se adaugă automat la fiecare linie
print(f"m + v:\n{m + v}")

# Normalizare tip z-score cu broadcasting (utilizată frecvent în ML):
mean = m.mean(axis=0)    # medie pe coloane, shape (3,)
std  = m.std(axis=0)     # std pe coloane, shape (3,)
normalized = (m - mean) / (std + 1e-8)  # 1e-8 previne împărțirea la 0
print(f"\nNormalizat z-score:\n{normalized.round(3)}")

# Reguli broadcasting:
# 1. Dacă array-urile nu au același nr de dim, cel mai mic e extins cu 1 la stânga
# 2. Array-urile sunt compatibile pe o dim dacă au aceeași lungime SAU unul are lungimea 1
# 3. Broadcasting se aplică dacă sunt compatibile pe TOATE dimensiunile
# ex: (4,3) cu (3,) => (4,3) cu (1,3) => OK

# =============================================================================
# 5. FUNCȚII NUMPY ESENȚIALE PENTRU LABORATOR
# =============================================================================

print("\n" + "=" * 60)
print("5. FUNCȚII UTILE PENTRU LABORATOARE")
print("=" * 60)

# np.digitize — discretizare valori continue în intervale (folosit în Lab 2 - Naive Bayes)
values = np.array([10, 50, 128, 200, 255])
bins   = np.linspace(0, 255, 5)   # [0, 63.75, 127.5, 191.25, 255]
print(f"Bins: {bins}")
discrete = np.digitize(values, bins)
print(f"Digitize {values} -> {discrete}")  # indicii intervalelor

# np.loadtxt — încărcare date din fișier text (Lab 2, 3)
# train_images = np.loadtxt('train_images.txt')
# train_labels = np.loadtxt('train_labels.txt', dtype='int')

# np.load / np.save — format binar .npy (Lab 1, 5)
temp_data = np.array([1, 2, 3, 4])
np.save('/tmp/temp_data.npy', temp_data)
loaded   = np.load('/tmp/temp_data.npy')
print(f"\nSalvat și încărcat .npy: {loaded}")

# np.savetxt — salvare în text (Lab 3)
np.savetxt('/tmp/predictions.txt', np.array([0, 1, 2, 1, 0]))

# shuffle cu sklearn.utils.shuffle (Lab 5)
from sklearn.utils import shuffle
data   = np.array([[1, 2], [3, 4], [5, 6]])
labels = np.array([0, 1, 2])
data_s, labels_s = shuffle(data, labels, random_state=42)
print(f"Shuffled data:\n{data_s}")

# =============================================================================
# 6. MATPLOTLIB — PLOTARE
# =============================================================================

print("\n" + "=" * 60)
print("6. MATPLOTLIB")
print("=" * 60)

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot simplu
fig1, ax1 = plt.subplots()
ax1.plot(x, y_sin, label='Sine')
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_title('Sinus')
ax1.legend()

# Plot puncte (fără interpolație)
fig2, ax2 = plt.subplots()
ax2.plot(x[::5], y_sin[::5], 'o')   # 'o' = puncte, 'r+' = cruciulițe roșii
ax2.set_title('Puncte')

# Subploturi
fig3, (ax3a, ax3b) = plt.subplots(2, 1, figsize=(8, 6))
ax3a.plot(x, y_sin)
ax3a.set_title('Sine')
ax3b.plot(x, y_cos)
ax3b.set_title('Cosine')
plt.tight_layout()

# Vizualizare imagine MNIST-like (28x28)
fig4, ax4 = plt.subplots()
fake_image = np.random.randint(0, 255, (28, 28))
ax4.imshow(fake_image.astype(np.uint8), cmap='gray')
ax4.set_title('Imagine 28x28 (demo)')

plt.show()
print("Graficele au fost afișate.")

# =============================================================================
# 7. EXERCIȚIUL 1 DIN LABORATOR — Car Images
# =============================================================================

print("\n" + "=" * 60)
print("7. DEMO EXERCIȚIU LAB 1 — Operații pe imagini")
print("=" * 60)

# Creăm imagini sintetice ca demonstrație (în laborator se citesc din fisiere)
np.random.seed(42)
images = np.random.randint(0, 255, (9, 400, 600), dtype=np.uint8)
# În laborator: images[i] = np.load(f'images/car_{i}.npy') pentru i în 0..8

# a. Array de imagini — shape (9, 400, 600)
print(f"Shape images: {images.shape}")

# b. Suma totală a tuturor pixelilor
total_sum = np.sum(images)
print(f"Suma totală pixeli: {total_sum}")

# c. Suma pixelilor pentru fiecare imagine
per_image_sum = np.sum(images, axis=(1, 2))  # suma pe axele 1 și 2 (H și W)
print(f"Suma per imagine: {per_image_sum}")

# d. Imaginea cu suma maximă
max_idx = np.argmax(per_image_sum)
print(f"Imaginea cu suma maximă: index {max_idx}")

# e. Imaginea medie
mean_image = np.mean(images, axis=0)  # media pe prima axă (nr imagini)
print(f"Imaginea medie — shape: {mean_image.shape}, dtype: {mean_image.dtype}")
# io.imshow(mean_image.astype(np.uint8))  # descomenteaza dacă ai scikit-image

# f. Deviația standard
std_val = np.std(images)
print(f"Deviație standard totală: {std_val:.2f}")

# g. Normalizare z-score pe imagini
mean_img = np.mean(images, axis=0)
std_img  = np.std(images, axis=0)
normalized_images = (images - mean_img) / (std_img + 1e-8)
print(f"Normalizat — min: {normalized_images.min():.2f}, max: {normalized_images.max():.2f}")

# h. Decupare (crop): linii 200-300, coloane 280-400
cropped = images[:, 200:300, 280:400]
print(f"Cropped shape: {cropped.shape}")  # (9, 100, 120)

# =============================================================================
# NOTE: CE POATE FI MODIFICAT
# =============================================================================
"""
VARIANTE ȘI IMPACTE:

1. dtype la np.array:
   - np.array([1.0, 2.0]) → dtype float64 (mai lent, mai precis)
   - np.array([1, 2], dtype=np.int32) → ocupă mai puțină memorie
   - Impactul în ML: operațiile de gradient necesită float32/float64

2. axis la np.sum/mean/std:
   - axis=None → scalar (toate elementele)
   - axis=0 → reduce prima dimensiune (media pe coloane pentru matrice)
   - axis=1 → reduce a doua dimensiune (media pe linii)
   - axis=(1,2) → reduce dimensiunile 1 și 2 simultan (suma unui batch de imagini)

3. np.random.seed(42):
   - Fixează sămânța pentru reproducibilitate
   - Fără seed, rezultatele sunt diferite la fiecare rulare

4. Broadcasting vs for-loop:
   - (m - mean) / std este de ~100x mai rapid decât un for-loop în Python
   - Întotdeauna preferat în ML pentru performanță

5. np.copy vs slice:
   - Slicingul CREEAZĂ O REFERINȚĂ, modificările afectează originalul
   - np.copy() este necesar când vrei o copie independentă
"""

print("\nLaborator 1 completat cu succes!")
