# Pixel Manipulation for Image Encryption

This project implements a simple image encryption tool using pixel manipulation techniques in Python. The tool performs operations like swapping pixel values or applying a basic mathematical transformation to encrypt and decrypt images.

## Features

- **Pixel-level encryption**: Alters pixel values of an image using defined operations.
- **Customizable encryption**: Allows for different mathematical operations or pixel swapping techniques.
- **Image decryption**: Reverses the manipulation to restore the original image.
- **Support for common image formats**: The tool can handle images in formats like PNG, JPEG, etc.

## How It Works

1. The user selects an image file to encrypt.
2. The program performs pixel manipulation by altering the pixel values (e.g., shifting RGB values or applying bitwise operations).
3. The encrypted image is saved to a new file.
4. The user can choose to decrypt the image using the same algorithm to restore the original image.

## Example Usage

### Encryption
```bash
$ python3 pixel_manipulation.py --mode encrypt --input input_image.png --output encrypted_image.png
