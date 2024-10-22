# Barcode Generator

A Python-based desktop application that generates barcodes in multiple formats. Users can select a barcode type, input data, and save the generated barcode as a PNG file. The application is built using `Tkinter` for the graphical user interface (GUI) and `python-barcode` for barcode generation.

## Features

- Generate barcodes in the following formats:
  - EAN13
  - EAN8
  - UPC-A
  - Code128
  - ISBN13
  - ISBN10
- Save barcodes as PNG images.
- Display generated barcode in the application window.

## Technologies Used

- **Python**: The main programming language.
- **Tkinter**: Used for building the desktop GUI application.
- **python-barcode**: For generating barcodes in different formats.
- **Pillow**: (PIL) used for image handling and resizing the barcode image.

## Prerequisites

- Python 3.6 or higher
- Virtual Environment (optional but recommended)

### Python Libraries

You will need to install the following Python libraries:

- `python-barcode`
- `Pillow` (for image handling)

You can install them using the following command:

```bash
pip install python-barcode Pillow
```

## Installation & Setup

1. **Clone the Repository**

   Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/deepzsenu/barcode-generator.git
   cd barcode-generator
   ```

2. **Set up Virtual Environment** (optional but recommended)

   To create and activate a virtual environment:

   ```bash
   python -m venv barcode
   barcode\Scripts\activate   # On Windows
   source barcode/bin/activate  # On Mac/Linux
   ```

3. **Install Required Dependencies**

   Install the required packages using:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, use:

   ```bash
   pip install python-barcode Pillow
   ```

4. **Run the Application**

   To run the Barcode Generator application, execute:

   ```bash
   python barcode_app.py
   ```

## Usage

1. Select the barcode type from the dropdown menu.
2. Enter the data to be encoded in the input field.
3. Click the **"Generate Barcode"** button.
4. A file dialog will prompt you to save the barcode as a PNG image.
5. The generated barcode will be displayed within the application window.

## Screenshots

### Main Interface:
![Main Interface](screenshot.png)

### Example Barcode:
![Example Barcode](barcode_example.png)

## Troubleshooting

- **Error: "ModuleNotFoundError: No module named 'barcode'"**
  - Ensure that the `python-barcode` package is installed using `pip install python-barcode`.

- **Error: "File not found" when trying to save the barcode**
  - Ensure that you select a valid save location and filename for the output PNG file.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/username/barcode-generator/issues) if you want to contribute.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---