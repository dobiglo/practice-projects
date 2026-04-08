import os
import shutil


def organize_folder(folder_path):
    file_types = {
        "images": [
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
        "documents": [
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
        "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".webm"],
        "audio": [
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
        "archives": [
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
        "scripts": [".py", ".js", ".bat", ".cmd", ".vbs", ".rb", ".ps1", ".sh"],
        "config": [
            ".ini",
            ".cfg",
            ".conf",
            ".xml",
            ".json",
            ".yaml",
            ".toml",
            ".properties",
        ],
        "applications": [".exe", ".app", ".msi", ".scr"],
    }

    print(f"Organizing files in: {folder_path}\n")

    files_moved = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not os.path.isfile(file_path):
            continue

        _, ext = os.path.splitext(filename)
        folder = _find_folder_for_extension(file_types, ext)
        if not folder:
            print(f"Skipped {filename} because of unknown extension")
            continue

        folder_name = folder.capitalize()
        target_folder = os.path.join(folder_path, folder_name)
        os.makedirs(target_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"Moved: {filename} to {folder_name}")
        files_moved += 1

    print(f"Done! Total files moved: {files_moved}")


def _find_folder_for_extension(file_types, ext):
    folder = None

    for dir, extensions in file_types.items():
        if not ext.lower() in extensions:
            continue
        folder = dir
        break

    return folder


organize_folder("your file path here")
