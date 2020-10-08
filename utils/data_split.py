import os
from sklearn.model_selection import train_test_split
import pickle

def save_plk(obj, path_pkl):
    with open(path_pkl, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_plk(path_pkl):
    with open(path_pkl,'rb') as f:
        return pickle.load(f)
def save_list_to_txt(values,path_txt):
    with open(path_txt, 'w') as output:
        for row in values:
            output.write(str(row) + '\n')


path_BraTS20_train ='/vinai/vuonghn/Research/BraTS/BraTS_data/MICCAI_BraTS2020_TrainingData/training/HGG/'
list_ID = os.listdir(path_BraTS20_train)
train_size = 0.8
test_size = 0.2
random_state = 182
train_IDs, val_IDs = train_test_split(list_ID,train_size=train_size,test_size=test_size, random_state=random_state) 


save_load_pkl = False
if save_load_pkl: 

    data = {"train_IDs": train_IDs, "val_IDs":val_IDs,"train_size":train_size,"test_size":test_size,"random_state":random_state}
    load_data = load_plk("./data_splited/data_82_182.pkl")
    save_plk(data,"./data_splited/data_82_182.pkl")
    print("load_data ", len(load_data["train_IDs"]))
save_load_txt = True
if save_load_txt:
    save_list_to_txt(train_IDs,"./data_splited/train_IDs_fold1_82_182.txt")
    save_list_to_txt(val_IDs,"./data_splited/val_IDs_fold1_82_182.txt")

