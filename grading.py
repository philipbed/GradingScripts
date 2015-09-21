from zip_download import Driver
import unzip

def main():

    d = Driver()
    go_to = 'https://mycourses.rit.edu'
    d.open(go_to)
    #d.login()
    d.navigate_to_lab()
    d.select_all()
    d.change_windows()
    d.download_all()

    unzip.unzip()

main()