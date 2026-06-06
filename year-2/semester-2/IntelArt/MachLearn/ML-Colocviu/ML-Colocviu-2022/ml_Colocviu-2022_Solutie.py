
import numpy as np

# ex 1
def similaritetStringKernel(s, t, p):
    ngrama_s=set([s[i:i + p] for i in range(0, len(s) - p)])
    ngrama_t=set([t[i:i+p] for i in range(0, len(t) - p)])

    return  len(set(ngrama_s.intersection(ngrama_t)))

print(similaritetStringKernel("ananas copt","“banana verde",p=4))

# ex 2
test_data=np.load("data/test_data.npy")
train_data=np.load("data/train_data.npy")
train_label=np.load("data/train_labels.npy")

def classify(test):
    #calculam distantele imaginii test

    diferente=np.zeros(len(train_data))
    for i in range(len(train_data)):
        diferente[i]=similaritetStringKernel(train_data[i],test,p=8)

    #pastram cei mai apropiati k vecini
    labels=[]
    indici=np.argsort(diferente)[::-1]
    k=5
    for i in range(0,k):
        labels.append(train_label[indici[i]])

    givenLabel=max(labels)
    return givenLabel

# f=open("solutie.txt","w")
# for test in test_data:
#     label=classify(test)
#     f.write(str(label)+"\n")
# f.close()



# ex 3
def matriceKernel(x,z,p=4):
    K=np.zeros((len(x),len(z)))
    for i in range(len(x)):
        for j in range(len(z)):
            K[i][j]=similaritetStringKernel(x[i],z[j],p)
    return K

# print(matriceKernel(train_data,train_data))
# print(matriceKernel(train_data,test_data))







