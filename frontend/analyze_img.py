import cv2
import numpy as np
import sys

image_path = 'C:/Users/photoshop/.gemini/antigravity/brain/eb8d473b-c8a0-41ee-a9f4-604aaa497258/.user_uploaded/media_1791351792157.png'
img = cv2.imread(image_path)
if img is None:
    print("Could not load image")
    sys.exit()

height, width, _ = img.shape
print(f"Image dimensions: {width}x{height}")

# Let's sample a horizontal line across the middle of the tabs to see if there's a gap
# Assuming tabs are roughly in the middle of the image vertically
middle_y = height * 2 // 3 # adjust if needed
row = img[middle_y, :]

# Print some color values across the width
for x in range(0, width, width // 10):
    print(f"x={x}: {row[x]}")

