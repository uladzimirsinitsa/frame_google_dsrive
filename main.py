
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from dotenv import load_dotenv

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
load_dotenv()


def upload_file(dir_path='data'):
    try:
        drive = GoogleDrive(gauth)

        for file_name in os.listdir(dir_path):
            file = drive.CreateFile({'title': f'{file_name}'})
            file.SetContentFile(os.path.join(dir_path, file_name))
            file.Upload()
        return f'File: {file_name}was uploaded.'
    except:
        return 'Check trouble.'


def main():

    upload_file()

if __name__=='__main__':
    main()