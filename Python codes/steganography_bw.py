from PIL import Image


def encode_message(img, message):
    """
    Encodes a message into an image using LSB steganography
    """
    width, height = img.size
    pixels = img.load()

    # Converting the message into binary
    binary_message = ''.join(format(ord(x), '08b') for x in message)
    binary_message += '00000000'  # padding the message with zeros

    # Replacing the least significant bit of each pixel with a bit of the message
    index = 0
    for i in range(width):
        for j in range(height):
            pixel = pixels[i, j][0]
            if index < len(binary_message):
                # Replacing the LSB of the pixel value with the corresponding bit of the message
                pixel = (pixel & 254) | int(binary_message[index])
                pixels[i, j] = (pixel,)
                index += 1
    return img


def decode_message(img):
    """
    Decodes a message from an image using LSB steganography
    """
    width, height = img.size
    pixels = img.load()

    binary_message = ''

    # Reading the least significant bit of each pixel
    for i in range(width):
        for j in range(height):
            pixel = pixels[i, j][0]
            binary_message += str(pixel & 1)

    # Removing the padding from the message
    binary_message = binary_message[:-8]

    # Converting the binary message back into the original message
    message = ''.join(chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8))
    return message


# Example usage:
img = Image.open("cameraman.tif")
encoded_img = encode_message(img, "hello")
encoded_img.save("encoded.tif")

decoded_img = Image.open("encoded.tif")
message = decode_message(decoded_img)
print("Decoded message:", message)
