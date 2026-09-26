import os
import shutil

def organize_files(directory_path):
    """
    Scans a directory and organizes files into subfolders based on 
    their extensions (.pdf, .png, .docx, .xlsx).
    """
    # 1. Validate that the target directory exists
    if not os.path.exists(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    # 2. Define target extensions and their respective folder names
    extension_mapping = {
        '.pdf': 'PDFs',
        '.png': 'Images_PNG',
        '.docx': 'Word_Documents',
        '.xlsx': 'Excel_Spreadsheets'
    }

    print(f"Scanning directory: '{directory_path}'...")
    files_moved = 0

    # 3. Iterate through all items in the target directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Skip subdirectories, process files only
        if os.path.isdir(file_path):
            continue

        # Extract and lowercase the file extension
        _, ext = os.path.splitext(filename)
        ext_lower = ext.lower()

        # Check if the file extension matches our supported list
        if ext_lower in extension_mapping:
            folder_name = extension_mapping[ext_lower]
            destination_folder = os.path.join(directory_path, folder_name)

            # 4. Create the target folder if it doesn't already exist
            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(destination_folder, filename)

            # 5. Handle name collisions (if a file with the same name already exists)
            if os.path.exists(destination_path):
                base, extension = os.path.splitext(filename)
                counter = 1
                while os.path.exists(destination_path):
                    new_filename = f"{base}_{counter}{extension}"
                    destination_path = os.path.join(destination_folder, new_filename)
                    counter += 1

            # 6. Move the file to its destination folder
            shutil.move(file_path, destination_path)
            print(f"Moved: '{filename}' -> '{folder_name}/{os.path.basename(destination_path)}'")
            files_moved += 1

    print(f"Organization complete! Total files moved: {files_moved}")

if __name__ == "__main__":
    # Replace './my_files' with the path to the folder you want to clean up
    target_directory = "./my_files"
    organize_files(target_directory)