# Colab to Markdown Converter

This project provides a Python script to convert Jupyter/Colab notebooks (.ipynb files) to Markdown (.md) format.

## Features

- Converts Jupyter/Colab notebooks to Markdown
- Supports command-line usage
- Allows specifying custom output paths

## Requirements

- Python 3.6+
- nbformat
- nbconvert

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/mikelaaron/colab-converter-project.git
   cd colab-converter-project
   ```

2. Install the required packages:
   ```
   pip install nbformat nbconvert
   ```

## Usage

Run the script from the command line:

```
python colab-to-markdown-converter.py path/to/your/notebook.ipynb
```

To specify a custom output path:

```
python colab-to-markdown-converter.py path/to/your/notebook.ipynb -o path/to/output.md
```

## Example

```
python colab-to-markdown-converter.py '/Users/username/Documents/Projects/ColabConverter/MyNotebook.ipynb'
```

This will create a Markdown file named 'MyNotebook.md' in the same directory as the input notebook.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

License Pending.