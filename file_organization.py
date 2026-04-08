import os
import shutil


def organize_folder(folder_path):
    file_types = {
        "Images": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".svg",
            ".webp",
            ".tiff",
            ".raw",
            ".ai",
            ".eps",
        ],
        "Documents": [
            ".pdf",
            ".docx",
            ".pptx",
            ".txt",
            ".xlsx",
            ".odt",
            ".rtf",
            ".xls",
            ".ppt",
            ".doc",
            ".md",
        ],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".webm"],
        "Audio": [
            ".mp3",
            ".wav",
            ".flac",
            ".aac",
            ".ogg",
            ".m4a",
            ".oga",
            ".wma",
            ".aiff",
            ".aif",
        ],
        "Archives": [
            ".zip",
            ".rar",
            ".7z",
            ".tar",
            ".cab",
            ".iso",
            ".gz",
            ".gzip",
            ".zst",
            ".zstd",
            ".bz2",
            ".xz",
        ],
        "Scripts": [".py", ".js", ".bat", ".cmd", ".vbs", ".rb", ".ps1", ".sh"],
        "Config": [
            ".ini",
            ".cfg",
            ".conf",
            ".xml",
            ".json",
            ".yaml",
            ".toml",
            ".properties",
        ],
        "Applications": [".exe", ".app", ".msi", ".scr"],
    }

    print(f"Organizing files in: {folder_path}\n")

    files_moved = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            moves = False

            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved: {filename} to {folder}/")
                    files_moved += 1
                    moved = True
                    break

            if not moved:
                print(f"Skipped {filename} because of 'Unknown type'")

    print(f"Done! Total files moved: {files_moved}")


organize_folder("your file path here")
