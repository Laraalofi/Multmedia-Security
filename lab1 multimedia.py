from PIL import Image  # Import the Image module from the Python Imaging Library (PIL), allowing image manipulation
import numpy as np  # Import the numpy library for numerical computing and give it the alias 'np'
from PIL import ImageFont  # Import the ImageFont module from PIL for working with fonts in images
from PIL import ImageDraw  # Import the ImageDraw module from PIL for drawing 2D graphics on images

# Task 1 Read an image 
# Open the original image
# First Define the path to the original image file
path = "shara.jpg"  
# Seconed Open the image file specified by the 'path' variable and assign the resulting Image object to 'image'
image = Image.open(path) 
# Print the size and format of the original image to the console
print(' image size=', image.size, ', image format=', image.format)
image.show()

# Task 2 write in image 
path2 = "shara2.jpg"  # Define the path to the second image file
image2 = Image.open(path2)  # Open the second image file specified by 'path2' and assign the resulting Image object to 'image2'

# Add text to the second image and save it as shara2_Writing.jpg
text = "shahad and lara"  # Define the text to be added to the image
font = ImageFont.truetype("arial.ttf", 20)  # Specify the font and size for the text
draw = ImageDraw.Draw(image2)  # Create a drawing object for the second image

# Draw the text on the second image 
#represents the coordinates (x, y) where the text will be drawn on the image
#specifies the top-left corner of the image as the starting point for drawing the text. 
#The first value 0 represents the x-coordinate (horizontal position), 
#and the second value 0 represents the y-coordinate (vertical position). 
draw.text((0, 0), text, (0, 0, 255), font=font) 
image2.save("shara2_Writing.jpg")  # Save the modified second image as shara2_Writing.jpg
image2.show()

# Task 3 Resize the original image to desired width and height
image3 = Image.open(path)  # Open the original image again
DESIRED_WIDTH = 600  # Define the desired width for resizing
height = 600  # Define the height for resizing
image3 = image3.resize((DESIRED_WIDTH, height))  # Resize the image to the specified width and height
output_file = "Resizing_Image.jpg"  # Define the output file name
image3.save(output_file)  # Save the resized image as Resizing_Image.jpg
image = Image.open("Resizing_Image.jpg")  # Open the resized image file named "Resizing_Image.jpg"
print(' image size=', image.size, ', image format=', image.format)  # Print the size and format of the resized image to the console
image3.show()

# Task 4 Rotate the original image by a specified angle
ROTATION = 60  # Define the rotation angle
image4 = Image.open(path)  # Open the original image again
image4 = image4.rotate(ROTATION, expand=True)  # Rotate the image by the specified angle while expanding the image canvas
output_file = "Rotation_Image.jpg"  # Define the output file name
image4.save(output_file)  # Save the rotated image as Rotation_Image.jpg
image4.show()

# Task 5: XOR two images
# Open the original and modified images, convert them to arrays, perform XOR operation, and save the encrypted and decrypted images
path1 = "shara.jpg"  # Define the path to the original image
image1 = Image.open(path1)  # Open the original image
array1 = np.array(image1)  # Convert the original image to a NumPy array
array2 = np.array(image2.resize(image1.size))  # Resize and convert the modified image to match the shape of the original image
encrypted_array = np.bitwise_xor(array1, array2)  # Perform XOR operation between the two arrays
encrypted_image = Image.fromarray(encrypted_array)  # Convert the resulting array back to an image
encrypted_filename = "encrypted_Image.jpg"  # Define the output file name for the encrypted image
encrypted_image.save(encrypted_filename)  # Save the encrypted image
encrypted_image.show()

decrypted_array = np.bitwise_xor(encrypted_array, array2)  # Perform XOR operation between the encrypted image and the modified image to decrypt
decrypted_image = Image.fromarray(decrypted_array)  # Convert the resulting array back to an image
decrypted_filename = "decrypted_Image.jpg"  # Define the output file name for the decrypted image
decrypted_image.save(decrypted_filename)  # Save the decrypted image
decrypted_image.show()
