import numpy as np
import matplotlib.pyplot as plt

def thue_morse_sequence(n):
    seq=[0]
    while len(seq)<n:
        seq += [1-b for b in seq]
    return seq[:n]

def generate_step_data(n):
    base=np.ones(n)
    
    A_ab=np.cumsum([(base[i] if i%2==0 else 0) for i in range(n)])
    B_ab=np.cumsum([(base[i] if i%2==1 else 0) for i in range(n)])

    A_ab=np.insert(A_ab, 0, 0)
    B_ab=np.insert(B_ab, 0, 0)

    tm=thue_morse_sequence(n)
    A_tm=np.cumsum([(base[i] if tm[i]==0 else 0) for i in range(n)])
    B_tm=np.cumsum([(base[i] if tm[i]==1 else 0) for i in range(n)])
    
    A_tm=np.insert(A_tm, 0, 0)
    B_tm=np.insert(B_tm, 0, 0)

    return A_ab, B_ab, A_tm, B_tm

n=22
A_ab, B_ab, A_tm, B_tm = generate_step_data(n)

x=np.arange(n + 1)

fig, axs = plt.subplots(2, 2, figsize=(8, 6))
plt.subplots_adjust(wspace=0.4, hspace=0.4)

for ax in axs.flat:
    ax.set_xticks([])
    ax.set_yticks([])

axs[0, 0].plot(x, A_ab, color="blue")
axs[0, 0].plot(x, B_ab, color="orange")
axs[0, 0].text(2.5, -3.0, r"(a) ABABABABAB...", fontsize=12, color="blue")

axs[0, 1].plot(x, np.cumsum(A_ab) / (x+1), color="blue")
axs[0, 1].plot(x, np.cumsum(B_ab) / (x+1), color="orange")
axs[0, 1].text(3.0, -1.5, r"(b) Running average", fontsize=12, color="blue")

axs[1, 0].plot(x, A_tm, color="blue")
axs[1, 0].plot(x, B_tm, color="orange")
axs[1, 0].text(4.0, -2.9, r"(c) Thue-Morse", fontsize=12, color="blue")

axs[1, 1].plot(x, np.cumsum(A_tm) / (x+1), color="blue")
axs[1, 1].plot(x, np.cumsum(B_tm) / (x+1), color="orange")
axs[1, 1].text(2, -1.5, r"(d) Thue-Morse average", fontsize=12, color="blue")

plt.show()
