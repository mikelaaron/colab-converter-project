import nbformat
import nbconvert
import os
import sys
import argparse

def convert_notebook_to_markdown(notebook_path, output_path=None):
    """
    Convert a Jupyter notebook to a Markdown file.

    Args:
    notebook_path (str): Path to the input notebook file (.ipynb)
    output_path (str, optional): Path for the output Markdown file. If not provided,
                                 it will use the same name as the notebook with .md extension.

    Returns:
    str: Path to the created Markdown file
    """
    # Ensure the notebook file exists
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"Notebook file not found: {notebook_path}")

    # If output_path is not provided, create one based on the input file
    if output_path is None:
        output_path = os.path.splitext(notebook_path)[0] + '.md'

    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = notebook_file.read()

    # Parse the notebook JSON
    notebook = nbformat.reads(notebook_content, as_version=4)

    # Configure and create the exporter
    markdown_exporter = nbconvert.MarkdownExporter()

    # Convert the notebook to markdown
    markdown_content, _ = markdown_exporter.from_notebook_node(notebook)

    # Write the markdown content to the output file
    with open(output_path, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_content)

    return output_path

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert Colab/Jupyter notebooks to Markdown.")
    parser.add_argument("notebook_path", help="Path to the input notebook file (.ipynb)")
    parser.add_argument("-o", "--output", help="Path for the output Markdown file (optional)")

    # Parse arguments
    args = parser.parse_args()

    try:
        output_file = convert_notebook_to_markdown(args.notebook_path, args.output)
        print(f"Conversion successful. Markdown file created: {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()