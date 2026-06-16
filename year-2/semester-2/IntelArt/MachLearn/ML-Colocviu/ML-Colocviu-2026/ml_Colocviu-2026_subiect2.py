import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class Reader:
    def __init__(self, examples_path, label_path=None):
        self.examples_path=examples_path
        self.label_path=label_path
        self.readfile()

        #incarcam coord
        if self.label_path is not None:
            self.labels=np.load(label_path)
        else:
            self.labels=None

    def readfile(self):
        file=open(self.examples_path, "r")
        lines = file.readlines()
        self.documents = []

        for line in lines:
            idk=line.strip()
            self.documents.append(idk)




def gasesteLimite(coordonate):
    latitudini=coordonate[:,0]
    lognitudini=coordonate[:,1]

    min_lat=np.min(latitudini)
    max_lat=np.max(latitudini)

    min_long=np.min(lognitudini)
    max_long=np.max(lognitudini)

    #impartim coord in 5
    lim_latitudini=np.linspace(min_lat, max_lat,5)
    lim_longitudine=np.linspace(min_long,max_long,5)

    return lim_latitudini, lim_longitudine





def atribuieDocumentePeReguini(documente, coordonate, limite_latitudine, limite_longitudine):
    #avem 16 regiuni in total
    subregiuni={i:[] for i in range(16)}

    for doc, coord in zip(documente, coordonate):
        lat,long=coord[0],coord[1]

        #cautam unde pica
        index_lat=np.digitize(lat, limite_latitudine)-1 #digitize returneaza idici incepand de la 1
        index_long=np.digitize(long,limite_longitudine)-1

        #sa nu dea out of bounds
        if index_lat>=4:
            index_lat=3
        if index_long>=4:
            index_long=3

        #calculam id regiune
        id_reg=index_lat*4+index_long
        subregiuni[id_reg].append(doc)

    return subregiuni

def creeazaSuperDoc(subregiuni):

    super_documente=[]
    for i in range(16):
        #unim intr-un string
        super_doc=" ".join(subregiuni[i])
        super_documente.append(super_doc)


    return super_documente

def extrageVocabular(super_documente):
    #aplica td idf pe super documente si pastram 500
    vectorizer=TfidfVectorizer()

    matrice_scor=vectorizer.fit_transform(super_documente).toarray()
    cuv_feature=np.array(vectorizer.get_feature_names_out())

    #pastram doar cuvinte unice
    vocabular_general=set()

    for i in range(matrice_scor.shape[0]):
        scoruri=matrice_scor[i]

        #gasim indicii cuvintlrot cu cel mai mare scor
        if len(scoruri)>500:
            indici=np.argsort(scoruri)[-500:]#laum cele mai mari 500
        else:
            #daca nu sunt destule le luam pe toate
            indici=np.argsort(scoruri)

        cuvinte_top500=cuv_feature[indici]

        for cuvant in cuvinte_top500:
            vocabular_general.add(cuvant)
    return vocabular_general


def ex2(documente, coordonate):

    #
    limite_lat, limite_long=gasesteLimite(coordonate)

    subregiuni=atribuieDocumentePeReguini(documente,coordonate, limite_lat, limite_long)

    super_doc=creeazaSuperDoc(subregiuni)

    vocabular=extrageVocabular(super_doc)

    return vocabular



train_reader = Reader("train_samples.txt", "train_coordinates.npy")
test_reader = Reader("test_samples.txt")

vocabular=ex2(train_reader.documents,train_reader.labels)
print(vocabular)








