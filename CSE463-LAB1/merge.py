import os
import nbformat

# Define the folder path where your notebooks are located
folder_path = './'  # Replace with the folder path if necessary
output_file = 'merged_output.ipynb'

# List all the .ipynb files in the folder
notebooks = [f for f in os.listdir(folder_path) if f.endswith('.ipynb')]

# Create an empty list to collect all cells from all notebooks
merged_cells = []

# Read each notebook and add its cells to the merged_cells list
for notebook in notebooks:
    notebook_path = os.path.join(folder_path, notebook)
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        merged_cells.extend(nb.cells)  # Append the cells

# Create a new notebook to store the merged content
merged_nb = nbformat.v4.new_notebook()
merged_nb.cells = merged_cells

# Write the merged notebook to the output file
with open(output_file, 'w', encoding='utf-8') as f:
    nbformat.write(merged_nb, f)

print(f"Notebooks merged successfully into {output_file}")
