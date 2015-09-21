from GradingUtils.zip_download import Driver
from GradingUtils.unzip import *

def main():

    d = Driver()
    go_to = 'https://mycourses.rit.edu'
    d.open(go_to)
    d.navigate_to_lab()
    d.select_all()
    d.change_windows()
    d.download_all()

    path = 'C:\Python34\Lab'
    path += input("what is the lab number?")
    delete_path = unzip(path)
    #unzip(path)
    deleteZip(delete_path)

main()