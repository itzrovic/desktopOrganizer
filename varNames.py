import os
from pathlib import Path

desktopPath = Path.home() / 'Desktop'
deskOrg = desktopPath / 'Desktop Organizer'
deskAll = os.listdir(desktopPath)
orgVid = deskOrg / 'videos'
orgImg = deskOrg / 'images'
orgDir = deskOrg / 'folders'
orgFile = deskOrg / 'files'
orgAud = deskOrg / 'audios'

print(deskOrg)
print(deskAll)
print(orgVid)
print(orgImg)
print(orgDir)
print(orgFile)
print(orgAud)
