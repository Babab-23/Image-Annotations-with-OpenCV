import cv2
import matplotlib.pyplot as plt

# Load image
image_path = "image.png"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, _ = image_rgb.shape

# Draw horizontal bi-directional arrow for width
arrow_start = (20, height - 50)
arrow_end = (width - 20, height - 50)

cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.03)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.03)

# Add width label
font = cv2.FONT_HERSHEY_SIMPLEX
label_position = ((arrow_start[0] + arrow_end[0]) // 2 - 120, height - 70)

cv2.putText(
    image_rgb,
    f"Width: {width}px",
    label_position,
    font,
    0.9,
    (255, 255, 0),
    2,
    cv2.LINE_AA
)

# Display image
plt.figure(figsize=(10, 6))
plt.imshow(image_rgb)
plt.title("Annotated Image Width")
plt.axis("off")
plt.show()
