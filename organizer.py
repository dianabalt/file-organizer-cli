import shutil
from pathlib import Path #imports Path from pathlib module
from utils import get_category #imports get_category function from utils.py file

category_folders = {
    "Images", "Documents", "Audio", "Videos", "Archives","Code", "Others"
}

def organize_files(folder_path, dry_run = True, recursive = False): #takes 3 parameters, folder_path (folder we want to organize), dry_run with default value of True, and recursive with default value of False
    folder = Path(folder_path) #converts the string folder_path into a Path object

    processed_count = 0 #counter to keep track of # of files processed
    moved_count = 0 #counter to keep track of # of files moved
    skipped_count = 0 #counter to keep track of # of files skipped

    if recursive:
        items = folder.rglob("*") #recursively gets all items in the folder and its subfolders 
    else:
        items = folder.iterdir() #gets all items in current folder only

    for item in items:
        if any(part in category_folders for part in item.parts):
            continue
        
        if item.is_file(): #pathlib method that checks if its a file. True --> its a file | False --> its a folder
            processed_count += 1 #increments processed count by 1 for each file found in the folder
            extension =item.suffix.lower() #changes file extension to lowercase
            category = get_category(extension) #calls get_category  to determine the category of the file 

            destination_folder = folder / category #creates a new path for destination folder, combining the original folder path with the category name
            destination_file = destination_folder / item.name #creates a new path for the destination file, combining the destination folder path + original file name

            if dry_run:
                if destination_file.exists(): #checks if file with same name exists in destination folder
                    print(f"[DRY RUN] Would skip {item.name} (already exists in {destination_folder})") #indicates file would be skipped due to name conflict
                    skipped_count += 1 #increments skipped count by 1 if file is not being moved
                else:
                    print(f"[DRY RUN] Would move {item.name} -> {destination_file}") #prints where the file would be moved to

            else: 
                destination_folder.mkdir(exist_ok=True) #creates the destination folder if it doesn't exist already


                if destination_file.exists(): #checks if a file with  same name already exists in destination folder
                    print(f"Skipping {item.name} (already exists in {destination_folder})") #indicates file is being skipped due to a name conflict
                    skipped_count += 1 #increments skipped count by 1
                    continue #skips to the next iteration of loop, preventing overwriting of existing files

                shutil.move(str(item), str(destination_file)) #moves the file to the new destination using shutil.move() method, converting both paths to strings
                print(f"Moved {item.name} -> {destination_file}") #prints message confirming  file has been moved, showing the original file name + new destination path
                moved_count += 1 #increments moved count by 1
    
    print()
    print("Summary:")
    print(f"Processed: {processed_count}")
    print(f"Moved: {moved_count}")
    print(f"Skipped: {skipped_count}")

