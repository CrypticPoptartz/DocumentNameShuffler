import os
import random

def get_document_files():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_directory, "Documents")
    
    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # Get all files in the folder
        files = os.listdir(folder_path)
        
        # Filter only the files with certain extensions, you can modify this as needed
        document_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        
        # Print or use the list as needed
        print("Documents in the 'Documents' folder:")
        for document_file in document_files:
            print(document_file)
        
        return document_files
    else:
        print("The 'Documents' folder does not exist.")
        return []

def randomize_list(input_list):
    # Use the random.sample function to shuffle the list
    randomised_list = random.sample(input_list, len(input_list))
    
    # Print or use the randomised list as needed
    print("Randomised List:")
    for item in randomised_list:
        print(item)
    
    return randomised_list

def move_and_rename_to_temp(original_list, new_list):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_directory, "Documents")
    temp_folder_path = os.path.join(folder_path, "temp")
    
    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # Create a temporary folder if it doesn't exist
        if not os.path.exists(temp_folder_path):
            os.makedirs(temp_folder_path)
        
        # Iterate through the original list and move files to the temp folder before renaming
        for original_file, new_name in zip(original_list, new_list):
            original_file_path = os.path.join(folder_path, original_file)
            new_temp_file_path = os.path.join(temp_folder_path, new_name)
            
            try:
                # Move the file to the temp folder and rename it
                os.rename(original_file_path, new_temp_file_path)
                print(f"Moved and renamed file to temp: {original_file} to {new_name}")
            except Exception as e:
                print(f"Error processing file: {original_file}. Error: {e}")
        
        print("Finished moving and renaming files to temp.")
    else:
        print("The 'Documents' folder does not exist.")

def move_temp_to_original():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_directory, "Documents")
    temp_folder_path = os.path.join(folder_path, "temp")

    # Check if the 'temp' folder exists
    if os.path.exists(temp_folder_path) and os.path.isdir(temp_folder_path):
        try:
            # Iterate through files in the 'temp' folder and move them back to the original folder
            for file_name in os.listdir(temp_folder_path):
                temp_file = os.path.join(temp_folder_path, file_name)
                original_file = os.path.join(folder_path, file_name)
                
                # Move the file back to the original folder
                os.rename(temp_file, original_file)
                print(f"Moved file back to original: {file_name}")

            # Remove the 'temp' folder
            os.removedirs(temp_folder_path)
            print("Removed temp folder.")
        except Exception as e:
            print(f"Error moving files back or removing temp folder. Error: {e}")
    else:
        print("The 'temp' folder does not exist.")

# Example usage
document_files_list = get_document_files()
randomised_list = randomize_list(document_files_list)
move_and_rename_to_temp(document_files_list, randomised_list)
move_temp_to_original()
input("Press Enter to exit...")