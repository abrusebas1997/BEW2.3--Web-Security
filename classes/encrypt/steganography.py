from PIL import Image
import base64

    # Loop over the range of x_size (`x`)
        # Loop over the range of y_size (`y`)
            # Get RGB values from red_channel via `getpixel(x, y)`
            # Convert red value in returned tuple to a binary string via `bin()`
            # Grab the LSB (right-most value) from the binary string
            # Perform a check to see if resulting LSB value is `1`
            #   Write `pixels[x, y]` to to black `(0, 0, 0)`
            # Otherwise
            #   Write `pixels[x, y]` to white `(255, 255, 255)`
    # Save the decoded image as `decoded_image.png`

def decode_image(file_location):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
​
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
​
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
​
    #TODO: Fill in decoding functionality
    # Loop over the range of x_size (`x`)
    for x in range(x_size):
        # Loop over the range of y_size (`y`)
        for y in range(y_size):
            # Get RGB values from red_channel via `getpixel(x, y)`
            r,g,b = red_channel.getpixel((x,y))

​




    decoded_image.save("images/encoded_sample.png")

#
#
#
# def write_text():
#     pass
#
# def encoded_image():
#     pass
