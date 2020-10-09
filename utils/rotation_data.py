
import nibabel
import numpy as np
import os
from array2gif import write_gif
def save_to_nii(im, filename, outdir="", mode="image", system="nibabel"):
    """
    Save numpy array to nii.gz format to submit
    im: 3d numpy array ex: [155, 240, 240]
    """
    if system == "sitk":
        if mode == 'label':
            img = sitk.GetImageFromArray(im.astype(np.uint8))
        else:
            img = sitk.GetImageFromArray(im.astype(np.float32))
        if not os.path.exists("./{}".format(outdir)):
            os.mkdir("./{}".format(outdir))
        sitk.WriteImage(img, "./{}/{}.nii.gz".format(outdir, filename))
    elif system == "nibabel":
        # img = np.rot90(im, k=2, axes= (1,2))
        # img = np.moveaxis(im, 0, -1)
        # img = np.moveaxis(img, 0, 1)
        img = im
        OUTPUT_AFFINE = np.array(
                [[0, 0, 1, 0],
                [0, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 1]])
        if mode == 'label':
            img = nibabel.Nifti1Image(img.astype(np.uint8), OUTPUT_AFFINE)
        else:
            img = nibabel.Nifti1Image(img.astype(np.float32), OUTPUT_AFFINE)
        if not os.path.exists("./{}".format(outdir)):
            os.mkdir("./{}".format(outdir))
        nibabel.save(img, filename)
    else:
        img = np.rot90(im, k=2, axes= (1,2))
        OUTPUT_AFFINE = np.array(
                [[0, 0, 1, 0],
                [0, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 1]])
        if mode == 'label':
            img = nibabel.Nifti1Image(img.astype(np.uint8), OUTPUT_AFFINE)
        else:
            img = nibabel.Nifti1Image(img.astype(np.float32), OUTPUT_AFFINE)
        if not os.path.exists("./{}".format(outdir)):
            os.mkdir("./{}".format(outdir))
        nibabel.save(img, "./{}/{}.nii.gz".format(outdir, filename))

def convert_to_truth_axis(filename,output):
    """
    load nifty image into numpy array, and transpose it based on the [z,y,x] axis order
    The output array shape is like [Depth, Height, Width]
    inputs:
        filename: the input file name, should be *.nii or *.nii.gz
        with_header: return affine and hearder infomation
    outputs:
        data: a numpy data array
    """
    img = nibabel.load(filename)
    data = img.get_data()

    # data = np.transpose(data, [2,1,0])
    
    print("filename ",filename)
    print("data 0 ",data.shape)
    
    data = np.moveaxis(data, 0, -1)
    print("data ",data.shape)
    # exit()
    # data = np.transpose(data, [2,1,0]) #(155, 240, 240)
    
    # # convert to origin shape
    # print("data 1 ",data.shape)
    # data = np.transpose(data, (1, 0, 2))

    print("before save ",data.shape)
    path_save = os.path.join(output,filename.split("/")[-1])
    save_to_nii(data,path_save)
    
    
    print("shape after save : ",nibabel.load(path_save).get_data().shape)
    print("ID ",path_save)

# path_truth = "/vinai/vuonghn/Research/BraTS/BraTS_data/MICCAI_BraTS2020_TrainingData/training/HGG/BraTS20_Training_115/BraTS20_Training_115_flair.nii.gz"
# path_wrong = "/vinai/vuonghn/Research/BraTS/BraTS_data/MICCAI_BraTS2020_TrainingData/training/HGG/BraTS20_Training_357/BraTS20_Training_357_flair.nii.gz"
# convert_to_truth_axis(path_truth,output)

path_bug = "/vinai/vuonghn/Research/BraTS/BraTS_data/fixbug_rotation/BraTS20_Training_357_bug"
output = "/vinai/vuonghn/Research/BraTS/BraTS_data/fixbug_rotation/BraTS20_Training_357"


mod = os.listdir(path_bug)
for m in mod:
    path_image = os.path.join(path_bug,m)
    convert_to_truth_axis(path_image,output)
