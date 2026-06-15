# synent-task-4---File-orangizer---Madhav-
# File Organizer (Python)

## Project Overview

The File Organizer is a Python-based automation tool that helps keep directories clean and organized. It automatically sorts files into categorized folders such as **Images**, **Docs**, and **Videos** based on their file extensions. The program uses Python's `os` and `shutil` modules to create folders and move files.

## Features

* Automatically organizes files by type
* Creates folders automatically if they do not exist
* Sorts files into:

  * Images
  * Documents
  * Videos
* Supports multiple file extensions
* Easy-to-use command-line interface
* Helps maintain a clean directory structure

## Requirements

* Python 3.x

## Modules Used

### `os`

Used for:

* Accessing files and directories
* Creating folders
* Checking file paths

### `shutil`

Used for:

* Moving files between folders

## Supported File Types

| Category | Extensions                           |
| -------- | ------------------------------------ |
| Images   | .jpg, .jpeg, .png, .gif, .bmp        |
| Docs     | .pdf, .doc, .docx, .txt, .ppt, .pptx |
| Videos   | .mp4, .avi, .mkv, .mov               |

## How to Run

1. Save the program as `file_organizer.py`
2. Open a terminal or command prompt.
3. Navigate to the folder containing the file.
4. Run the program:

```bash
python file_organizer.py
```

5. Enter the directory path you want to organize.

## Example

### Before Organization

```text
MyFolder/
│
├── photo.jpg
├── report.pdf
├── movie.mp4
├── notes.txt
├── image.png
```

### After Organization

```text
MyFolder/
│
├── Images/
│   ├── photo.jpg
│   └── image.png
│
├── Docs/
│   ├── report.pdf
│   └── notes.txt
│
├── Videos/
│   └── movie.mp4
```

## Sample Output

```text
Enter folder path: C:\Users\Madhav\Downloads

Moved: photo.jpg -> Images
Moved: report.pdf -> Docs
Moved: movie.mp4 -> Videos
Moved: notes.txt -> Docs

File organization completed!
```

## Program Logic

1. Accept a folder path from the user.
2. Create category folders if they do not already exist.
3. Scan all files in the selected directory.
4. Identify file types using their extensions.
5. Move files into their corresponding folders.
6. Display the status of each moved file.
7. Show a completion message.

## Project Structure

```text
FileOrganizer/
│
├── file_organizer.py
└── README.md
```

## Future Enhancements

* Add support for Audio files
* Add support for ZIP and RAR archives
* Organize files into subfolders by date
* Provide a graphical user interface (GUI)
* Generate organization reports
* Allow custom folder categories

## Benefits

* Saves time by automating file management
* Keeps folders neat and organized
* Reduces manual sorting effort
* Improves productivity

## Author

**Madhav**
Python Automation Project – File Organizer 🚀
