import cv2

# Read the image
image = cv2.imread("C:\\Users\\KESHAV TRIKHA\\OneDrive\\Desktop\\TWD\\aw.jpg")

# Rotate the image by 90 degrees
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Save the rotated image
cv2.imwrite("rotated_image.jpg", rotated_image)
cv2.imshow("image",rotated_image)
cv2.waitKey(0)
