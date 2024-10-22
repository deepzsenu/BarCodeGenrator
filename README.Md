
# Barcode Generator

A Python-based desktop application that generates barcodes in multiple formats. Users can select a barcode type, input data, and save the generated barcode as a PNG file. The application is built using `Tkinter` for the graphical user interface (GUI) and `python-barcode` for barcode generation. The project also includes a standalone `.exe` application for Windows, making it easy to run without requiring Python.

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
- Standalone Windows executable version available.

## Technologies Used

- **Python**: The main programming language.
- **Tkinter**: Used for building the desktop GUI application.
- **python-barcode**: For generating barcodes in different formats.
- **Pillow**: (PIL) used for image handling and resizing the barcode image.
- **PyInstaller**: Used to package the application into a standalone `.exe` for Windows.

## Prerequisites (For Running from Python Source Code)

- Python 3.6 or higher
- Virtual Environment (optional but recommended)

### Python Libraries

You will need to install the following Python libraries if running from source:

- `python-barcode`
- `Pillow` (for image handling)

You can install them using the following command:

```bash
pip install python-barcode Pillow
```

## Installation & Setup (For Running from Source)

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

   To run the Barcode Generator application from Python source, execute:

   ```bash
   python barcode_app.py
   ```

## Installation & Setup (For Running the Executable)

1. Download the pre-built `.exe` file from the [releases page](https://github.com/deepzsenu/barcode-generator/releases).
2. Double-click the `.exe` to run the Barcode Generator application without needing Python installed.

## Usage

1. **Running from Source**: 
   - Select the barcode type from the dropdown menu.
   - Enter the data to be encoded in the input field.
   - Click the **"Generate Barcode"** button.
   - A file dialog will prompt you to save the barcode as a PNG image.
   - The generated barcode will be displayed within the application window.

2. **Running the Executable**:
   - The usage is the same as running from source, but without needing to install any dependencies. Simply open the `.exe`, follow the same steps, and generate barcodes.

## How to Create the Executable (Optional)

To create the Windows executable yourself, use `PyInstaller`. Here's how you can package the Python script into a `.exe`:

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Run the following command to generate a standalone executable:

   ```bash
   pyinstaller --onefile --windowed --name "MyBarcodeApp" --icon=assets/icon.ico barcode_app.py
   ```

   This will create the `MyBarcodeApp.exe` file in the `dist` folder.

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

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/deepzsenu/barcode-generator/issues) if you want to contribute.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

