
# Lab 2 Lara and Shahad
from PIL import Image  # Import the Image module from the PIL library for image processing
import cv2  # Import the OpenCV library for image processing
import numpy as np  # Import the NumPy library for numerical operations
from imwatermark import WatermarkEncoder  # Import WatermarkEncoder from imwatermark module for watermark encoding
from imwatermark import WatermarkDecoder# Import WatermarkDecoder from imwatermark module for watermark decoding

# Watermark encoding
bgr = cv2.imread('lab2.png')  # Read the input image in BGR format using OpenCV
wm = 'lab2'  # Watermark text

encoder = WatermarkEncoder()  # Create a WatermarkEncoder object
encoder.set_watermark('bytes', wm.encode('utf-8'))  # Set the watermark text
bgr_encoded = encoder.encode(bgr, 'dwtDct')  # Encode the watermark onto the image

cv2.imwrite('Watermarked.png', bgr_encoded)  # Save the watermarked image
image = Image.open("Watermarked.png")  # Open the resized image
print('image size=', image.size, ', image format=', image.format)  # Print the size and format of the image

# Watermark decoding
bgr = cv2.imread('Watermarked.png')  # Read the watermarked image
decoder = WatermarkDecoder('bytes', 32)  # Create a WatermarkDecoder object
watermark = decoder.decode(bgr, 'dwtDct')  # Decode the watermark from the image

decoded_message = watermark.decode('utf-8')  # Decode the watermark message

# Check if the decoded watermark matches the expected watermark
if decoded_message == wm:
    print("Watermark decoding passed.")  # Print message indicating decoding success
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark:", decoded_message)  # Print the decoded watermark message
else:
    print("Watermark decoding failed.")  # Print message indicating decoding failure
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark: is empty.")  # Print a message indicating that the decoded watermark is empty


#Attack1: Crop operation
print("\nAttack1: crop operation")
image = cv2.imread("Watermarked.png")  # Read the input image
cropped = image[65:292, 37:564]  # Crop the image using specified coordinates
cv2.imwrite("cropped.png", cropped)  # Save the cropped image

# Watermark decoding
bgr = cv2.imread('cropped.png')  # Read the watermarked image
decoder = WatermarkDecoder('bytes', 32)  # Create a WatermarkDecoder object
watermark = decoder.decode(bgr, 'dwtDct')  # Decode the watermark from the image

decoded_message = watermark.decode('utf-8')  # Decode the watermark message

# Check if the decoded watermark matches the expected watermark
if decoded_message == wm:
    print("Watermark decoding after cropping passed.")  # Print message indicating decoding success
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark:", decoded_message)  # Print the decoded watermark message
else:
    print("Watermark decoding after cropping failed.")  # Print message indicating decoding failure
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark: is empty.")  # Print a message indicating that the decoded watermark is empty
    

#Attack2 Rotation
print("\nAttack2: Rotation")
ROTATION = 60  # Define the rotation angle
image4 = Image.open("Watermarked.png")  # Open the image
image4 = image4.rotate(ROTATION, expand=True)  # Rotate the image
output_file = "Rotation.png"  # Define the output file name
image4.save(output_file)  # Save the rotated image

# Watermark decoding
bgr = cv2.imread('Rotation.png')  # Read the watermarked image
decoder = WatermarkDecoder('bytes', 32)  # Create a WatermarkDecoder object
watermark = decoder.decode(bgr, 'dwtDct')  # Decode the watermark from the image

decoded_message = watermark.decode('utf-8')  # Decode the watermark message

# Check if the decoded watermark matches the expected watermark
if decoded_message == wm:
    print("Watermark decoding after Rotation passed.")  # Print message indicating decoding success
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark:", decoded_message)  # Print the decoded watermark message
else:
    print("Watermark decoding after Rotation failed.")  # Print message indicating decoding failure
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark: is empty.")  # Print a message indicating that the decoded watermark is empty


#Attack3: Resize
print("\nAttack3: Resize")
image3 = Image.open("Watermarked.png")  # Open the image
DESIRED_WIDTH = 600  # Define the desired width
height = 600  # Define the height
image3 = image3.resize((DESIRED_WIDTH, height))  # Resize the image
output_file = "Resizing.png"  # Define the output file name
image3.save(output_file)  # Save the resized image
image = Image.open("Resizing.png")  # Open the resized image
print('image size=', image.size, ', image format=', image.format)  # Print the size and format of the image
    
# Watermark decoding
bgr = cv2.imread('Resizing.png')  # Read the watermarked image
decoder = WatermarkDecoder('bytes', 32)  # Create a WatermarkDecoder object
watermark = decoder.decode(bgr, 'dwtDct')  # Decode the watermark from the image

decoded_message = watermark.decode('utf-8')  # Decode the watermark message

# Check if the decoded watermark matches the expected watermark
if decoded_message == wm:
    print("Watermark decoding after Resize passed.")  # Print message indicating decoding success
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark:", decoded_message)  # Print the decoded watermark message
else:
    print("Watermark decoding after Resize failed.")  # Print message indicating decoding failure
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark: is empty.")  # Print a message indicating that the decoded watermark is empty
   

#Attack4: Masking
print("\nAttack4: Masking")
image = cv2.imread('Watermarked.png')  # Read the input image
mask = np.zeros(image.shape, dtype=np.uint8)  # Create a binary mask
mask = cv2.circle(mask, (260, 300), 225, (255, 255, 255), -1)  # Draw a white circle on the mask
result = cv2.bitwise_and(image, mask)  # Apply the mask to the input image
result[mask == 0] = 255  # Color the background white
cv2.imwrite('Masking.png', result)  # Save the masked image

# Watermark decoding
bgr = cv2.imread('Masking.png')  # Read the watermarked image
decoder = WatermarkDecoder('bytes', 32)  # Create a WatermarkDecoder object
watermark = decoder.decode(bgr, 'dwtDct')  # Decode the watermark from the image

decoded_message = watermark.decode('utf-8')  # Decode the watermark message

# Check if the decoded watermark matches the expected watermark
if decoded_message == wm:
    print("Watermark decoding after Masking passed.")  # Print message indicating decoding success
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark:", decoded_message)  # Print the decoded watermark message
else:
    print("Watermark decoding after Masking failed.")  # Print message indicating decoding failure
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark: is empty.")  # Print a message indicating that the decoded watermark is empty
   

#Attack5: Overlaying
print("\nAttack5: Overlaying")

# Watermark encoding
bgr = cv2.imread('background.png')  # Read the input image in BGR format using OpenCV
wm = 'lab2'  # Watermark text

encoder = WatermarkEncoder()  # Create a WatermarkEncoder object
encoder.set_watermark('bytes', wm.encode('utf-8'))  # Set the watermark text
bgr_encoded = encoder.encode(bgr, 'dwtDct')  # Encode the watermark onto the image
cv2.imwrite('backgroundWatermarked.png', bgr_encoded)  # Save the watermarked image

img1 = Image.open(r"backgroundWatermarked.png")  # Open the watermark background image
img2 = Image.open(r"lab2.png")  # Open the overlay image
img1.paste(img2, (0, 0), mask=img2)  # Paste the overlay image on top of the background image
img1.save("Overlaying.png")  # Save the altered image

# Watermark decoding
bgr = cv2.imread('Overlaying.png')  # Read the watermarked image
decoder = WatermarkDecoder('bytes', 32)  # Create a WatermarkDecoder object
watermark = decoder.decode(bgr, 'dwtDct')  # Decode the watermark from the image

decoded_message = watermark.decode('utf-8')  # Decode the watermark message

# Check if the decoded watermark matches the expected watermark
if decoded_message == wm:
    print("Watermark decoding after overlaying passed.")  # Print message indicating decoding success
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark:", decoded_message)  # Print the decoded watermark message
else:
    print("Watermark decoding after overlaying failed.")  # Print message indicating decoding failure
    print("Expected Watermark:", wm)  # Print the expected watermark message
    print("Decoded Watermark: is empty.")  # Print a message indicating that the decoded watermark is empty


