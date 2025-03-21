from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import qrcode

# Authenticate Google Drive
gauth = GoogleAuth()
gauth.LoadClientConfigFile(r"###") # path_to_client_secret.js 
gauth.LocalWebserverAuth()  # Follow the login steps
drive = GoogleDrive(gauth)

# Google Drive Folder ID where your photos/videos are stored
FOLDER_ID = "###" #your_folder_ID

# List all files in the folder
file_list = drive.ListFile({'q': f"'{FOLDER_ID}' in parents and trashed=false"}).GetList()

# Store file links
links = []

for file in file_list:
    file_link = f"https://drive.google.com/uc?id={file['id']}"  # Direct file link
    links.append(file_link)

# Save links to a text file
with open(r"###", "w") as f: #path_to_save_links.txt
    for link in links:
        f.write(link + "\n")

print("✅ Shareable links generated!")
