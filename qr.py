# First, make sure you have the qrcode library installed.
# You can install it using: pip install qrcode[pil]

import qrcode

# The URL to encode in the QR code.
data = "http://192.168.0.124:5000"

# Create a QRCode instance with settings:
qr = qrcode.QRCode(
    version=1,  # version 1 is a 21x21 matrix; adjust if you need a larger code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,  # each box will be 10x10 pixels
    border=4  # 4 boxes thick border
)

# Add your URL data to the QR code.
qr.add_data(data)
qr.make(fit=True)

# Generate the image (black QR code on a white background)
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file.
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")
