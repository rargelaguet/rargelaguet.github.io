import os

# Path to the directory containing folders
base_directory = "/Users/rargelaguet/test/hugoblox_test/content/publication"

# Function to process each index.md file
def remove_draft_line(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        # Write back the file without the line containing "draft: true"
        with open(file_path, "w") as file:
            for line in lines:
                if "draft: true" not in line.strip():
                    file.write(line)
        print(f"Processed: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Walk through the directory and process each index.md
for root, dirs, files in os.walk(base_directory):
    for file in files:
        if file == "index.md":
            file_path = os.path.join(root, file)
            remove_draft_line(file_path)

print("Processing completed.")