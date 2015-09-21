"""
This file will extract all of the contents of the recently downloaded zip file
then remove the zip folder from the directory
"""
from zipfile import ZipFile
import os
import os.path

def unzip(path):
    """
    Opens the zip file then extracts all of its contents into a
    new folder then closes the file. Returns the path to the
    zip file.

    path - path of the folder to extract the contents to.
    """
    zip_path = path + '.zip'
    with ZipFile(zip_path) as zfile:
        zfile.extractall(path)
        zfile.close()
    return zip_path

def deleteZip(path):
    """
    Deletes the specified zip file.

    path- path of the zip file to delete
    """
    os.remove(path)

if __name__ == '__main__':

    path = 'C:\Python34\Lab'
    path += input("what is the lab number?")
    delete_path = unzip(path)
    #unzip(path)
    deleteZip(delete_path)

