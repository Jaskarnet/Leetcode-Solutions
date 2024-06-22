import os
import re

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
        source_code_file = f"{problem_dir}/{problem_dir}.cpp"
        readme_content += f"""
## {problem_name}

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
"""

    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    generate_readme()
