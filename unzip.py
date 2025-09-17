import zipfile
import os

zip_path = r"C:\Users\wahbi\PycharmProjects\FALL 25\Project 1\stylegan2-ada\mydataset.zip"          # path to your zip
extract_path = "stylegan2-ada/datasets/volcano"  # folder where images will go

os.makedirs(extract_path, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Unzipped successfully!")
