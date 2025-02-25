import json
import os
import sys

def extract_image_and_file_paths(notebook_path):
    """
    Extracts image and file paths from a Jupyter Notebook.
    """
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_data = json.load(f)

    missing_files = []
    referenced_files = set()

    for cell in notebook_data.get("cells", []):
        if cell["cell_type"] in ["markdown", "code"]:
            for line in cell.get("source", []):
    
                if "![" in line and "](" in line:
                    start = line.find("](") + 2
                    end = line.find(")", start)
                    file_path = line[start:end]
                    referenced_files.add(file_path)

                
                if '<img src="' in line:
                    start = line.find('<img src="') + 10
                    end = line.find('"', start)
                    file_path = line[start:end]
                    referenced_files.add(file_path)

                if 'open("' in line or 'read_csv("' in line:
                    start = line.find('("') + 2
                    end = line.find('"', start)
                    file_path = line[start:end]
                    referenced_files.add(file_path)

    for file in referenced_files:
        if not os.path.exists(file):
            missing_files.append(file)

    return missing_files

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_notebook_assets.py <notebook.ipynb>")
        sys.exit(1)

    notebook_path = sys.argv[1]

    if not os.path.exists(notebook_path):
        print(f"Notebook file '{notebook_path}' not found.")
        sys.exit(1)

    missing_files = extract_image_and_file_paths(notebook_path)

    if missing_files:
        print("❌ Missing files:")
        for file in missing_files:
            print(f"- {file}")
    else:
        print("✅ All referenced images and files are present!")
