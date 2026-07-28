import qrcode
import argparse
from pathlib import Path

def generate_qr(data, filename="qrcode.png", size=10, border=4):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved to: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="Text or URL to encode")
    parser.add_argument("-o", "--output", default="qrcode.png", help="Output filename")
    parser.add_argument("-s", "--size", type=int, default=10, help="Box size")
    args = parser.parse_args()
    
    generate_qr(args.data, args.output, args.size)
