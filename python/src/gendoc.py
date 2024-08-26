import pydoc
import os

# Path to your project directory
project_dir = './python/src'

# Path to the desired output directory
output_dir = './docs'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Walk through the project directory and generate documentation for each Python file
for root, dirs, files in os.walk(project_dir):
    for file in files:
        if file.endswith('.py'):
            module_path = os.path.join(root, file)
            module_name = os.path.splitext(file)[0]
            
            # Generate HTML documentation
            html_doc = pydoc.HTMLDoc().docmodule(__import__(module_name))
            
            # Write to the specified path
            output_file = os.path.join(output_dir, f'{module_name}.html')
            with open(output_file, 'w') as f:
                f.write(html_doc)

print(f"Documentation generated in {output_dir}.")
