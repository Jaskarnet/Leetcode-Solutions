import os
import urllib.parse

# GitHub details
github_username = "Jaskarnet"
github_repo = "Leetcode-Solutions"
github_branch = "main"

# Root directory where problem folders are located
root_dir = "./"

# Output README file
readme_file = os.path.join(root_dir, "README.md")

# Initialize the README content with introduction and table of contents header
readme_content = "# LeetCode Solutions\n\n"
readme_content += "This repository contains my solutions to various LeetCode problems, implemented in C++ using Visual Studio. Each problem is stored in its own folder, with only the source code included.\n\n"
readme_content += "## Table of Contents\n"

# List to store sections for each problem
problem_sections = []

# Log file to record found subfolders
log_file = os.path.join(root_dir, "found_subfolders.log")
log_content = "Subfolders found:\n"

# Iterate through folders in the root directory
for folder in sorted(os.listdir(root_dir)):
    folder_path = os.path.join(root_dir, folder)
    
    # Check if the item is a directory and not a hidden folder or this script itself
    if os.path.isdir(folder_path) and not folder.startswith('.') and folder != "__pycache__":

        # Log the found subfolder
        log_content += f"{folder}\n"
        
        # Assume each folder has a description.md file
        description_file = os.path.join(folder_path, "description.md")
        if os.path.exists(description_file):
            # Read the description.md file
            with open(description_file, 'r', encoding='utf-8') as f:
                description_content = f.read().strip()

            # Extract problem name for generating anchor link
            problem_name = folder.split(' - ', 1)[1]

            # Append to Table of Contents
            readme_content += f"- [{problem_name}](#{problem_name.lower().replace(' ', '-')})\n"

            # Construct problem section
            problem_section = f"## {problem_name}\n\n"
            problem_section += description_content + "\n\n"
            
            # Add the description comment to the .cpp file and construct GitHub link
            solution_folder = os.path.join(folder_path, folder)
            for file in os.listdir(solution_folder):
                if file.endswith(".cpp"):
                    cpp_file = os.path.join(solution_folder, file)
                    
                    # Read the current content of the .cpp file
                    with open(cpp_file, 'r', encoding='utf-8') as cpp:
                        cpp_content = cpp.read()
                    
                    # Prepare the description comment
                    description_comment = "\n".join([f"// {line}" for line in description_content.split("\n")])
                    description_comment = f"// Description:\n{description_comment}\n\n"
                    
                    # Check if the comment already exists in the .cpp file
                    if description_comment not in cpp_content:
                        # Write the new content with the description at the top
                        with open(cpp_file, 'w', encoding='utf-8') as cpp:
                            cpp.write(description_comment + cpp_content)
                    
                    # Encode the file path for URL
                    encoded_file_path = urllib.parse.quote(f"{folder}/{folder}/{file}")
                    file_link = f"https://github.com/{github_username}/{github_repo}/blob/{github_branch}/{encoded_file_path}"
                    
                    # Add the link to the problem section
                    problem_section += f"**Solution:** [Solution Code]({file_link})\n\n"
                    
                    break
            
            # Add problem section to list
            problem_sections.append(problem_section)
            
# Combine Table of Contents and problem sections
readme_content += "\n\n".join(problem_sections)

# Write the README content to README.md
with open(readme_file, 'w', encoding='utf-8') as readme:
    readme.write(readme_content)

print(f"README.md has been generated in {readme_file}")

# Write found subfolders to log file
with open(log_file, 'w', encoding='utf-8') as log:
    log.write(log_content)

print(f"List of found subfolders has been logged in {log_file}")
