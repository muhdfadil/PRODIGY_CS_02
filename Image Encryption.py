from PIL import Image
import numpy as np


def encrypt_image(input_path, output_path, key=50):
    try:
        # Open the image and convert it to RGB
        image = Image.open(input_path).convert("RGB")
        # Convert the image to a NumPy array
        pixels = np.array(image)
        # Apply encryption by adding the key value to each pixel
        encrypted_pixels = (pixels + key).clip(0, 255)
        # Convert back to an image
        encrypted_image = Image.fromarray(np.uint8(encrypted_pixels))
        # Save the encrypted image
        encrypted_image.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error encrypting image: {e}")

def decrypt_image(input_path, output_path, key=50):
    try:
        # Open the encrypted image and convert it to RGB
        image = Image.open(input_path).convert("RGB")
        # Convert the image to a NumPy array
        pixels = np.array(image)
        # Apply decryption by subtracting the key value from each pixel
        decrypted_pixels = (pixels - key).clip(0, 255)
        # Convert back to an image
        decrypted_image = Image.fromarray(np.uint8(decrypted_pixels))
        # Save the decrypted image
        decrypted_image.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error decrypting image: {e}")

def main():
    print_ascii_heading()
    print("Welcome to Geny: Simple Image Encryption Tool")
    option = input("Enter 'e' for encryption or 'd' for decryption: ").lower()

    if option == 'e':
        input_path = input("Enter the path of the image to encrypt (e.g., image.png): ")
        output_path = input("Enter the output path for the encrypted image (e.g., encrypted.png): ")
        try:
            key = int(input("Enter encryption key (numeric value, default is 50): ") or 50)
            encrypt_image(input_path, output_path, key)
        except ValueError:
            print("Invalid key. Please enter a numeric value.")
    elif option == 'd':
        input_path = input("Enter the path of the image to decrypt (e.g., encrypted.png): ")
        output_path = input("Enter the output path for the decrypted image (e.g., decrypted.png): ")
        try:
            key = int(input("Enter decryption key (numeric value, default is 50): ") or 50)
            decrypt_image(input_path, output_path, key)
        except ValueError:
            print("Invalid key. Please enter a numeric value.")
    else:
        print("Invalid option. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
