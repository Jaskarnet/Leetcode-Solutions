import os
import re

def parse_cpp_file(file_path):
    metadata = {
        'Title': '',
        'Difficulty': '',
        'Topics': '',
        'Description': '',
        'Examples': '',
        'Constraints': '',
        'Follow-up': '',
        'Hint': ''
    }
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    inside_comment = False
    current_key = None
    
    for line in lines:
        line = line.strip()
        if line.startswith("/*"):
            inside_comment = True
            continue
        if line.endswith("*/"):
            inside_comment = False
            continue
        if inside_comment:
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                if key in metadata:
                    current_key = key
                    metadata[key] = value
                else:
                    if current_key:
                        metadata[current_key] += f'\n{line}'
            else:
                if current_key:
                    metadata[current_key] += f'\n{line}'
    return metadata

def generate_readme():
    readme_content = """# LeetCode Solutions

This repository contains my solutions to various LeetCode problems, implemented in C++ using Visual Studio. Each problem is stored in its own folder, with only the source code included.

## Table of Contents
"""
    root_dir = '.'
    problem_dirs = [d for d in os.listdir(root_dir) if os.path.isdir(d) and re.match(r'\d+ - ', d)]
    
    for problem_dir in problem_dirs:
        problem_name = problem_dir.split(' - ', 1)[1]
        readme_content += f"- [{problem_name}](#{problem_name.lower().replace(' ', '-')})\n"

    for problem_dir in problem_dirs:
        problem_name = problem_dir.split(' - ', 1)[1]
        source_code_file = f"{problem_dir}/{problem_dir}/{problem_dir}.cpp"
        
        metadata = parse_cpp_file(source_code_file)
        
        readme_content += f"""
## {metadata['Title']}

**Difficulty:** {metadata['Difficulty']}  
**Topics:** {metadata['Topics']}  

**Description:**  
{metadata['Description']}

**Examples:**  
{metadata['Examples']}

**Constraints:**  
{metadata['Constraints']}

**Follow-up:**  
{metadata['Follow-up']}

**Hint:**  
{metadata['Hint']}

**Solution:**  
[Solution Code]({source_code_file})
"""

    readme_content += """
## How to Use

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourrepositoryname.git
    ```
2. Navigate to the problem folder you are interested in.
3. Open the solution file in Visual Studio to view and run the code.

## Contributing

Feel free to contribute by submitting a pull request. Please ensure your solutions are well-documented and follow the repository's structure.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
"""

    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    generate_readme()
