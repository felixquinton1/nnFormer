import os
import json
import shutil
input_db = "/home/felix/Bureau/DATASET/nnFormer_raw/nnFormer_raw_data/Task01_ACDC/"
output_db = "/home/felix/Bureau/db_nnformer_acdc/"
path_json = "../dataset_json/ACDC_dataset.json"

f = open(path_json)
dic = json.load(f)


for i in dic['training']:
    im = i['image'][11:-7]
    shutil.copyfile(os.path.join(input_db, im[:10],im + ".nii.gz"), os.path.join(output_db, "imagesTs", im + ".nii.gz"))
    # shutil.copyfile(os.path.join(input_db, im[:10],im + ".nii.gz"), os.path.join(output_db, "imagesTr", im + ".nii.gz"))
    # shutil.copyfile(os.path.join(input_db, im[:10],im + ".nii.gz"), os.path.join(output_db, "labelsTr", im + "_gt.nii.gz"))
