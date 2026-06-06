import csv
import numpy as np
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import CategoricalNB, GaussianNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from tqdm import tqdm

class Reader:

    def __init__(self, examples_path, mapping_path, labels_path=None):
        self.examples_path = examples_path
        self.read_file()
        dict_character_number = {}
        with open(mapping_path) as f: 
            reader_obj = csv.reader(f)  
            for row in reader_obj:
                dict_character_number[row[0]] = int(row[1])
        self.dict_character_number = dict_character_number    
        self.apply_mapping()
        if labels_path is not None:
            self.labels = np.load(labels_path)

    def read_file(self):
        file = open(self.examples_path, 'r')
        lines = file.readlines()
        self.documents = []
        self.word_lists = []
        for line in lines:
            self.documents.append(line[:-1])
            list = line[:-1].split(" ")
            self.word_lists.append(list)

    def apply_mapping(self):
        data = []
        for doc in self.documents:
            list_curr_doc = []
            for ch in doc:
                if ch in self.dict_character_number:
                    list_curr_doc.append(self.dict_character_number[ch])
                else:
                    list_curr_doc.append(0)
            data.append(np.array(list_curr_doc))
        self.data=data

train_reader = Reader("./data_set/train_sentences.txt", "./data_set/mapping.txt", "./data_set/train_labels.npy")
test_reader = Reader("./data_set/test_sentences.txt", "./data_set/mapping.txt", "./data_set/test_labels.npy")
words_reader = Reader("./data_set/words.txt", "./data_set/mapping.txt", None)

####### Ex1 ###########
bow = CountVectorizer(analyzer='char')
train_matrix = bow.fit_transform(train_reader.documents).toarray().squeeze()
test_matrix = bow.transform(test_reader.documents).toarray().squeeze()
print("Ex1:")
nb = MultinomialNB()
nb.fit(train_matrix, train_reader.labels)
preds = nb.predict(test_matrix)
print(f"Accuracy: {np.mean(preds==test_reader.labels)}")

# ######### Ex2 ##########
def convolve(sample, kernels):
    b, kernel_length, = kernels.shape
    initial_length, = sample.shape
    # print(kernel.shape, sample.shape)
    output_length = initial_length - kernel_length + 1
    if output_length <0:
        return np.zeros((b, 1))
    output = np.zeros((b, output_length))
    for i in range(0, output_length):
        output[:, i] = np.sum(sample[None, i:i+kernel_length]*kernels, axis=1)/(np.linalg.norm(sample[i:i+kernel_length])*np.linalg.norm(kernels, axis=1))
    return output
    
def apply_convolution(data, filters, threshold):
    new_data = []
    for example in tqdm(data):
        convolution_output = convolve(example, np.array(filters))
        new_data.append(np.sum(convolution_output>threshold, axis=1))
    return np.array(new_data)


# word_max_length = np.max([len(filter) for filter in words_reader.data])
# new_filters = []
# for filter in words_reader.data:
#     new_filters.append(np.pad(filter, (0, word_max_length-len(filter))))
train_data = apply_convolution(train_reader.data, words_reader.data, threshold=0.9)
test_data = apply_convolution(test_reader.data, words_reader.data, threshold=0.9)

#### Ex3 ####
print("Ex3:")
predictions = []
for i in range(4):
  new_train_labels = ((train_reader.labels == i) * 2) - 1
  krr = KernelRidge(kernel="linear",alpha=100)
  krr.fit(train_data, new_train_labels)
  predictions.append(krr.predict(test_data))

predictions = np.array(predictions)
predictions = np.argmax(predictions, axis=0)
print(f"Accuracy KRR:{(predictions==test_reader.labels).mean()}")

#### Ex4 ####
print("Ex4:")

def hellinger_kernel(features1, features2):
    features1 = np.sqrt(features1)
    features2 = np.sqrt(features2)
    matrix = np.matmul(features1, features2.T)
    return matrix
train_matrix = hellinger_kernel(train_data, train_data)
test_matrix = hellinger_kernel(test_data, train_data)
model = SVC(kernel='precomputed', C=10 )
model.fit(train_matrix, train_reader.labels)
preds = model.predict(test_matrix)
print(f"Accuracy: {np.mean(preds==test_reader.labels)}")



