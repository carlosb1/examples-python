import os
from ebooklib import epub

def read_epub_metadata(file_path):
    try:
        book = epub.read_epub(file_path)
        title = book.get_metadata('DC', 'title')
        author = book.get_metadata('DC', 'creator')
        language = book.get_metadata('DC', 'language')
        return {
            "file": os.path.basename(file_path),
            "title": title[0][0] if title else "Unknown",
            "author": author[0][0] if author else "Unknown",
            "language": language[0][0] if language else "Unknown"
        }
    except Exception as e:
        return {
            "file": os.path.basename(file_path),
            "error": str(e)
        }

def read_folder_metadata(folder_path):
    metadata_list = []
    for file in os.listdir(folder_path):
        if file.lower().endswith(".epub"):
            full_path = os.path.join(folder_path, file)
            metadata = read_epub_metadata(full_path)
            metadata_list.append(metadata)
    return metadata_list


import os
import re
from ebooklib import epub

def sanitize_filename(name):
    # Remove characters that are invalid in file names
    return re.sub(r'[\\/*?:"<>|]', '', name)

def read_epub_metadata(file_path):
    try:
        book = epub.read_epub(file_path)
        title = book.get_metadata('DC', 'title')
        author = book.get_metadata('DC', 'creator')
        title_str = title[0][0].strip() if title else None
        author_str = author[0][0].strip() if author else None
        return title_str, author_str
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")
        return None, None

def rename_epub_files(folder_path):
    for file in os.listdir(folder_path):
        if file.lower().endswith(".epub"):
            full_path = os.path.join(folder_path, file)
            title, author = read_epub_metadata(full_path)
            if title and author:
                new_filename = f"{sanitize_filename(author)} - {sanitize_filename(title)}.epub"
                new_full_path = os.path.join(folder_path, new_filename)

                # Avoid overwriting existing files
                if not os.path.exists(new_full_path):
                    os.rename(full_path, new_full_path)
                    print(f"Renamed: {file} -> {new_filename}")
                else:
                    print(f"Skipped (already exists): {new_filename}")
            else:
                print(f"Skipped (missing metadata): {file}")

# Example usage
folder = "/home/carlosb/Desktop/518000"
rename_epub_files(folder)

# Example usage:
#metadata = read_folder_metadata(folder)

#for book in metadata:
#    print(book)
