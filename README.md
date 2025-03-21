# Automatic-Link-Generator
This python program automatically generates shareable links from your google drive.  

Overview  
This Python script retrieves all files from a specified Google Drive folder and generates direct shareable links for each file. The links are then stored in a text file for easy access.  

Features  
- Authenticates Google Drive access using OAuth 2.0  
- Fetches all files from a specified folder  
- Generates direct download links for each file  
- Saves the links to a text file  

Requirements  
Before running the script, install the required dependencies:  

```sh
pip install pydrive
pip install qrcode[pil]
```  

Setup & Usage  

1. Enable Google Drive API  
- Go to the [Google Cloud Console](https://console.cloud.google.com/)  
- Create a new project and enable the **Google Drive API**  
- Generate OAuth 2.0 credentials (Client ID and Secret)  
- Download the `client_secrets.json` file  

2. Clone the Repository  
```sh
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```

3. Update the Script  
- Replace `###` in the script with the correct paths:  
  - **OAuth client file path** (`path_to_client_secret.json`)  
  - **Folder ID** from Google Drive  
  - **Path to save the links** (`path_to_save_links.txt`)  

4. Run the Script  
```sh
python drive_link_generator.py
```

Notes  
- Ensure that Google Drive API is enabled and configured correctly.  
- The script will open a web browser for authentication during the first run.  
- Modify the script to match your folder ID and file paths.  
- The generated links can be used for direct downloads or embedding.  

License  
This project is open-source and available under the [MIT License](LICENSE).  
