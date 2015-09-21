"""

"""
from zipfile import ZipFile
import os
import os.path

def unzip(path):
    zip_path = path + '.zip'
    with ZipFile(zip_path) as zfile:
        zfile.extractall(path)
        zfile.close()
    return zip_path

def deleteZip(path):
    os.remove(path)

def main():

    path = 'C:\Python34\Lab'
    path += input("what is the lab number?")
    delete_path = unzip(path)
    #unzip(path)
    deleteZip(delete_path)

main()
