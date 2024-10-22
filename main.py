import shutil
from fileTypes import *
from varNames import *

def createDO():
    Path(deskOrg).mkdir(parents=True, exist_ok=True)
    Path(orgVid).mkdir(parents=True, exist_ok=True)
    Path(orgImg).mkdir(parents=True, exist_ok=True)
    Path(orgDir).mkdir(parents=True, exist_ok=True)
    Path(orgFile).mkdir(parents=True, exist_ok=True)

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_file(file):
    return os.path.splitext(file)[1] in file

def sortData():
    for file in deskAll:
        filePath = desktopPath / file

        if filePath.name == 'Desktop Organizer':
            print(f"skip: {file}")
            continue

        if filePath.suffix in skip:
            # print(f"skip: {file}")
            continue

        target_folder = None
        if filePath.is_dir():
            target_folder = orgDir
        elif is_audio(file):
            target_folder = orgAud
        elif is_video(file):
            target_folder = orgVid
        elif is_image(file):
            target_folder = orgImg
        elif is_file(file):
            target_folder = orgFile

        # Wenn die Datei ein unterstützter Typ ist
        if target_folder:
            # Überprüfen, ob eine Datei mit demselben Namen bereits existiert
            target_path = target_folder / file
            if not target_path.exists():
                shutil.move(filePath, target_folder)
            else:
                print(f"file already exists -> skip: {file}")
        else:
            print(f"unknown filetyp -> skip: {file}")

def main():
    createDO()
    print('DO created')
    sortData()
    print('data sorted')



if __name__ == '__main__':
    main()
    