EXTENSION_MAP = { #mapping each file type to a category
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".mp4": "Videos",
    ".mov": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",

    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
}

def get_category(extension): #function that takes file extension as input and returns the category
    return EXTENSION_MAP.get(extension, "Others") #returns the category of the file based on the extension. If the extension is not found in the EXTENSION_MAP  --> returns "Others" as the default category.