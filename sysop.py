import os
import subprocess

def volume_up():
    os.system("nircmd.exe changesysvolume 5000")

def volume_down():
    os.system("nircmd.exe changesysvolume -5000")

def mute_volume():
    os.system("nircmd.exe mutesysvolume 1")

def unmute_volume():
    os.system("nircmd.exe mutesysvolume 2")

def shutdown():
    os.system("shutdown /s /t 5")



folder_shortcuts = {
    "downloads": os.path.expanduser("~\\Downloads"),
    "documents": os.path.expanduser("~\\Documents"),
    "pictures": os.path.expanduser("~\\Pictures"),
    "music": os.path.expanduser("~\\Music"),
    "desktop": os.path.expanduser("~\\Desktop")
}

def open_folder_by_name(name):
    path = folder_shortcuts.get(name.lower())
    if path and os.path.exists(path):
        os.startfile(path)
        return f"Opening
