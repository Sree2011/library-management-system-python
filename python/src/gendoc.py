import os
from lazydocs import generate_docs

# Define the path to your source directory
src_dir = './python/src'

# Get a list of all Python files in the source directory
modules = [f.replace('.py', '') for f in os.listdir(src_dir) if f.endswith('.py')]

# Generate documentation for all modules
generate_docs(modules, output_path='./')

print("Markdown documentation generated successfully for all modules!")
