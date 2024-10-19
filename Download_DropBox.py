import os
import dropbox

# Initialize Dropbox client
ACCESS_TOKEN = 'sl.B_FiErGoCqHp6wWzxc8848XWJMwcp-C6m0GkZ0qe_ds669HXKm3AY86UOAJrxYhQHHq1AcjAggPt2vwhHqvqdbXSJlED9ECShaoaV5QDj4HHQieztB3KKfjjss5nZRfubmUFE48gM6zq'
dbx = dropbox.Dropbox(ACCESS_TOKEN)

def upload_file(local_path, dropbox_path):
    with open(local_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.add)

def upload_directory(local_folder, dropbox_folder):
    for root, dirs, files in os.walk(local_folder):
        # Calculate the relative path and the corresponding Dropbox path
        relative_path = os.path.relpath(root, local_folder)
        dropbox_path = os.path.join(dropbox_folder, relative_path).replace("\\", "/")

        # Create folder in Dropbox
        try:
            dbx.files_create_folder_v2(dropbox_path)
        except dropbox.exceptions.ApiError as e:
            if e.error.is_conflict() and e.error.get_conflict().is_folder():
                print(f"Folder already exists: {dropbox_path}")
            else:
                print(f"Failed to create folder: {dropbox_path}, Error: {e}")

        # Upload files in the current directory
        for file_name in files:
            local_file_path = os.path.join(root, file_name)
            dropbox_file_path = os.path.join(dropbox_path, file_name).replace("\\", "/")
            print(f"Uploading {local_file_path} to {dropbox_file_path}")
            upload_file(local_file_path, dropbox_file_path)

def upload_to_dropbox(path):
    dropbox_base_folder = '/Linux'  # All uploads will go into the "Linux" folder

    if os.path.isfile(path):
        dropbox_path = os.path.join(dropbox_base_folder, os.path.basename(path)).replace("\\", "/")
        print(f"Uploading file: {path} to {dropbox_path}")
        upload_file(path, dropbox_path)
    elif os.path.isdir(path):
        dropbox_folder = os.path.join(dropbox_base_folder, os.path.basename(path)).replace("\\", "/")
        print(f"Uploading directory: {path} to {dropbox_folder}")
        upload_directory(path, dropbox_folder)
    else:
        print(f"Path does not exist: {path}")

# Usage
path_to_upload = '/home/JS_Console'  # Provide either a file or folder path
upload_to_dropbox(path_to_upload)
