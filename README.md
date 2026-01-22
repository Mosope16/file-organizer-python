# Python File Organizer
A simple, automated tool to clean up messy directories by sorting files into categories based on their extensions.

## How it Works
The script scans a target directory and move files into the following categories:
* **Images:** .jpg, .png, .svg, etc.
* **Documents:** .pdf, .docx, .txt, etc.
* **Code:** .py, .cpp, .js, etc.
* **Programs:**  .exe, .msi, etc.
* **Compressed** .zip, .7z, .rar, etc.

## Setup
1. Clone this repo.
2. Open 'file_organizer.py'.
3. Change the 'target_dir' variable to any path you would like to clean up.
4. Run the script: 'python file_organizer.py'.

## Future Improvements
* Add  a GUI for folder selection
* Allow custom extension mapping via a config file.