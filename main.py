import argparse
from organizer import organize_files #(organize_files) main function that will be called to organize the files in the specified folder. 

def main():#main function that will be called when the script is executed, sets up the command line argument parser 
    parser= argparse.ArgumentParser( #creates an ArgumentParser object to handle command line arguments
        description="Organize files into folders based on their file types." #description of the command line tool
    )

    #first required argument: the command to run, in this case "organize"
    parser.add_argument(
        "command",
        choices=["organize"],
        help="Command to run"
    )

    # second required argument: the path to the folder we want to organize
    parser.add_argument(
        "folder_path",
        help="Path to the folder you want to organize"
    )

    #creates optional flag: --dry-run, allowing users to preview the changes
    # if user includes --dry-run --> args.dry_run becomes True. If not included --> args.dry_run is False by default 
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without actually moving files"
    )

    #creates optional flag: --recursive, allowing users to organize files in subdirectories as well
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Organize files in subdirectories as well"
    )

    args = parser.parse_args() #reads user terminal input + stores inside args variable

    #if user typed "organize" --> runs organize function
    if args.command == "organize":
        organize_files(args.folder_path, args.dry_run, args.recursive) #allows user to specify folder path and whether to perform a dry run or organize subdirectories recursively

#ensures main() only runs when this script is executed directly, not when imported as a module in another script. This allows the script to be used as a standalone tool and as an importable module.
if __name__ == "__main__":
    main()