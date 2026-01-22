import os
import shutil

# Define the directory to clean
target_dir = r"C:\Users\PC\Downloads"

# the file categories
extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Programs": [".exe", ".msi"],
    "Compressed":[".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".cpp", ".java", ".html", ".css", ".js"],
    "Music": [".mp3", ".m4a"]
}

print(f"Cleaning {target_dir}...")

# loops
for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)

    # Is this a file?
    if os.path.isfile(file_path):
        
        # extract extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # check which category the file belongs to
        found = False
        for folder_name, ext_list in extensions.items():
            if ext in ext_list:
                # states where it should go
                folder_path = os.path.join(target_dir, folder_name)

                # CREATE folder if it doesn't exist
                os.makedirs(folder_path, exist_ok=True) # if folder exist

                # move the file
                new_file_path = os.path.join(folder_path, filename)
                shutil.move(file_path, new_file_path)
                
                print(f"Moved: {filename} -> {folder_name}")
                found = True
                break # once category found, it breaks

        if not found and ext: # 'and ext' ensures we don't move files with no extension
            other_folder = os.path.join(target_dir, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} -> Others")

print("Cleanup Complete!")