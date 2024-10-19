import requests
import os

def divide_file(url, parts=4):
    response = requests.get(url)
    content = response.text
    parent_file_name = url.split('/')[-1].split('.')[0]
    file_type = '.' + url.split('.')[-1]
    length = len(content)
    part_length = length // parts

    # Create a folder named after the parent file
    if not os.path.exists(parent_file_name):
        os.makedirs(parent_file_name)

    for i in range(parts):
        start = i * part_length
        end = (i + 1) * part_length if i != parts - 1 else length
        part_content = content[start:end]
        
        # Define the path for the part file
        part_file_path = os.path.join(parent_file_name, f"{parent_file_name}_part_{i}{file_type}")
        
        # Save the part content to a file
        with open(part_file_path, 'w') as part_file:
            part_file.write(part_content)
        
        print(f"Saved {part_file_path}")

# Replace the URL with your raw GitHub URL
url = "https://raw.githubusercontent.com/SUPREME-CONDEMNER/redesigned-octo-carnival/refs/heads/main/JS_Console.js"
divide_file(url)
  
