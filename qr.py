import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qr_code(data, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, fill_color="black", back_color="white"):
    # Generate QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img

def save_qr_code(img, filename):
    # Save the image to the specified file
    img.save(filename)

def generate_qr_from_gui():
    def generate_qr():
        # Get input values from sliders and entry widget
        data = website_entry.get()
        error_correction = error_correction_mapping[error_correction_var.get()]
        box_size = box_size_slider.get()
        border = border_slider.get()
        fill_color = fill_color_entry.get()
        back_color = back_color_entry.get()

        # Generate QR code
        qr_code = generate_qr_code(data, error_correction, box_size, border, fill_color, back_color)

        # Save QR code to file
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            save_qr_code(qr_code, filename)
            print(f"QR code saved as '{filename}'")

    # Create main window
    root = tk.Tk()
    root.title("QR Code Generator")

    # Error correction mapping
    error_correction_mapping = {'L': qrcode.constants.ERROR_CORRECT_L,
                                'M': qrcode.constants.ERROR_CORRECT_M,
                                'Q': qrcode.constants.ERROR_CORRECT_Q,
                                'H': qrcode.constants.ERROR_CORRECT_H}

    # Website link entry
    website_label = tk.Label(root, text="Enter website link:")
    website_label.grid(row=0, column=0, padx=10, pady=5)
    website_entry = tk.Entry(root, width=50)
    website_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

    # Error correction level selection
    error_correction_label = tk.Label(root, text="Select error correction level:")
    error_correction_label.grid(row=1, column=0, padx=10, pady=5)
    error_correction_var = tk.StringVar(root, "M")
    error_correction_options = ["L", "M", "Q", "H"]
    error_correction_dropdown = tk.OptionMenu(root, error_correction_var, *error_correction_options)
    error_correction_dropdown.grid(row=1, column=1, padx=10, pady=5)

    # Box size slider
    box_size_label = tk.Label(root, text="Box Size:")
    box_size_label.grid(row=2, column=0, padx=10, pady=5)
    box_size_slider = tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, length=200)
    box_size_slider.set(10)  # Default value
    box_size_slider.grid(row=2, column=1, padx=10, pady=5)

    # Border size slider
    border_label = tk.Label(root, text="Border Size:")
    border_label.grid(row=3, column=0, padx=10, pady=5)
    border_slider = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, length=200)
    border_slider.set(4)  # Default value
    border_slider.grid(row=3, column=1, padx=10, pady=5)

    # Fill color entry
    fill_color_label = tk.Label(root, text="Fill Color:")
    fill_color_label.grid(row=4, column=0, padx=10, pady=5)
    fill_color_entry = tk.Entry(root)
    fill_color_entry.insert(0, "black")  # Default value
    fill_color_entry.grid(row=4, column=1, padx=10, pady=5)

    # Background color entry
    back_color_label = tk.Label(root, text="Background Color:")
    back_color_label.grid(row=5, column=0, padx=10, pady=5)
    back_color_entry = tk.Entry(root)
    back_color_entry.insert(0, "white")  # Default value
    back_color_entry.grid(row=5, column=1, padx=10, pady=5)

    # Generate button
    generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
    generate_button.grid(row=6, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    generate_qr_from_gui()
