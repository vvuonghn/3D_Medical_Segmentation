import os
from sklearn.model_selection import train_test_split
import pickle

def save_plk(obj, path_pkl):
    with open(path_pkl, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_plk(path_pkl):
    with open(path_pkl,'rb') as f:
        return pickle.load(f)


path_BraTS20_train ='/vinai/vuonghn/Research/BraTS/BraTS_data/MICCAI_BraTS2020_TrainingData/training/HGG/'
list_ID = os.listdir(path_BraTS20_train)
train_size = 0.8
test_size = 0.2
random_state = 182
train_IDs, val_IDs = train_test_split(list_ID,train_size=train_size,test_size=test_size, random_state=random_state)
data = {"train_IDs": train_IDs, "val_IDs":val_IDs,"train_size":train_size,"test_size":test_size,"random_state":random_state}

load_data = load_plk("./data_splited/data_82_182.pkl")


# save_plk(data,"./data_splited/data_82_182.pkl")
# print("load_data ", len(load_data["train_IDs"]))

# print(len(train_IDs))
# print(len(val_IDs))
# print("data_82_182 ",data)