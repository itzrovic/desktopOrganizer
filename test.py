import os
from pathlib import Path


desktopPath = Path.home() / 'Desktop'
deskOrg = desktopPath / 'Desktop Organizer'
print(deskOrg)
print(os.listdir(desktopPath))
