import cv2  
from pyzbar.pyzbar import decode  
import os

# Using raw string to handle backslashes
image_path = r'C:\Users\Olamzkid\NHS-projects\nhs-project\QRcode.PNG'
output_path = r'C:\Users\Olamzkid\NHS-projects\nhs-project\output_image.PNG'

# Function to load and process the image
def load_and_process_image(image_path, output_path):
    # Print the image path to ensure it's correct
    print(f"Image path: {image_path}")  # Error logging to help debug in case of errors with the image path

    # Load the image
    image = cv2.imread(image_path)  # This is a method from the imported cv2 that reads the image from the path

    # Check if the image was loaded successfully
    if image is None:  # Error handling
        print(f"Error: Unable to load image at {image_path}")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Decode the QR codes
    decoded_objects = decode(gray_image)

    # Check if any QR codes are found
    if not decoded_objects:
        print("No QR codes found in the image.")
        return

    # Extract and print the data from each QR code
    for obj in decoded_objects:
        print('Type:', obj.type)
        print('Data:', obj.data.decode('utf-8'))
        print()

    # Draw the detected QR codes on the image
    for obj in decoded_objects:
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(points)
            points = hull.reshape(-1, 2)
        for i in range(len(points)):
            cv2.line(image, tuple(points[i]), tuple(points[(i + 1) % len(points)]), (0, 255, 0), 3)

    # Save the image with detected QR codes
    cv2.imwrite(output_path, image)
    print(f"Output image saved at {output_path}")

# Call the function to load and process the image
load_and_process_image(image_path, output_path)
