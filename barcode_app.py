import tkinter as tk
from tkinter import messagebox, filedialog
import barcode  # Corrected import
from barcode.writer import ImageWriter
from PIL import Image, ImageTk

def generate_barcode():
    barcode_type = barcode_type_var.get()
    input_data = input_data_entry.get()
    
    # Dictionary of supported barcode formats
    barcode_formats = {
        'EAN13': barcode.get_barcode_class('ean13'),
        'EAN8': barcode.get_barcode_class('ean8'),
        'UPC-A': barcode.get_barcode_class('upca'),
        'Code128': barcode.get_barcode_class('code128'),
        'ISBN13': barcode.get_barcode_class('isbn13'),
        'ISBN10': barcode.get_barcode_class('isbn10'),
    }
    
    # Validate inputs
    if barcode_type not in barcode_formats:
        messagebox.showerror("Error", f"Barcode type '{barcode_type}' is not supported.")
        return
    if not input_data:
        messagebox.showerror("Error", "Input data cannot be empty.")
        return
    
    # Prompt user to choose save location
    output_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if not output_file:
        return
    
    # Generate barcode
    BarcodeClass = barcode_formats[barcode_type]
    try:
        barcode_obj = BarcodeClass(input_data, writer=ImageWriter())
        barcode_obj.save(output_file)
        
        # Display success message and show barcode
        messagebox.showinfo("Success", f"Barcode saved as {output_file}")
        display_barcode(output_file)
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate barcode: {str(e)}")

def display_barcode(filepath):
    img = Image.open(filepath)
    img = img.resize((300, 150), Image.ANTIALIAS)  # Resize to fit in the window
    img_tk = ImageTk.PhotoImage(img)
    
    # Update label with barcode image
    barcode_image_label.config(image=img_tk)
    barcode_image_label.image = img_tk

# Create main application window
app = tk.Tk()
app.title("Barcode Generator")
app.geometry("400x400")

# Create dropdown for barcode type
barcode_type_var = tk.StringVar(app)
barcode_type_var.set("EAN13")  # Default value
barcode_type_label = tk.Label(app, text="Select Barcode Type:")
barcode_type_label.pack(pady=10)
barcode_type_menu = tk.OptionMenu(app, barcode_type_var, "EAN13", "EAN8", "UPC-A", "Code128", "ISBN13", "ISBN10")
barcode_type_menu.pack()

# Create input field for barcode data
input_data_label = tk.Label(app, text="Enter Data to Encode:")
input_data_label.pack(pady=10)
input_data_entry = tk.Entry(app)
input_data_entry.pack()

# Create generate button
generate_button = tk.Button(app, text="Generate Barcode", command=generate_barcode)
generate_button.pack(pady=20)

# Label for displaying the barcode image
barcode_image_label = tk.Label(app)
barcode_image_label.pack(pady=10)

# Run the application
app.mainloop()
