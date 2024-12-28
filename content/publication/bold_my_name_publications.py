import os
import re

# Path to the directory containing your Hugo content
base_directory = "/Users/rargelaguet/test/hugoblox_test/content/publication"

# Your name to highlight in bold
your_name = "Ricard Argelaguet"

# Function to highlight name in bold
def highlight_name(file_path, name):
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Replace instances of your name with the bolded version
        updated_content = re.sub(rf"(?<!\*\*){re.escape(name)}(?!\*\*)", rf"**{name}**", content)

        # Write back the updated content if changes were made
        if content != updated_content:
            with open(file_path, "w") as file:
                file.write(updated_content)
            print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Walk through the directory and process each Markdown file
for root, dirs, files in os.walk(base_directory):
    for file in files:
        if file.endswith(".md"):  # Process only Markdown files
            file_path = os.path.join(root, file)
            highlight_name(file_path, your_name)

print("Processing completed.")