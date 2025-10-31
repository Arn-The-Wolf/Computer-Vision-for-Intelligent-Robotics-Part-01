import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# --- Ensure aruco module available (requires: pip install opencv-contrib-python) ---
aruco_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_250)

# --- Parameters ---
marker_size = 100
padding = 20
text_space = 25
total_markers = 250

# Grid layout
grid_size = int(np.ceil(np.sqrt(total_markers)))
canvas_size = grid_size * (marker_size + padding + text_space) - padding

# --- Create canvas ---
grid_image = np.ones((canvas_size, canvas_size), dtype=np.uint8) * 255

font = cv.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
font_thickness = 2

# --- Generate markers ---
for marker_id in range(total_markers):
    marker_image = aruco_dict.generateImageMarker(marker_id, marker_size)
    row = marker_id // grid_size
    col = marker_id % grid_size
    y_start = row * (marker_size + padding + text_space)
    x_start = col * (marker_size + padding)
    grid_image[y_start:y_start + marker_size, x_start:x_start + marker_size] = marker_image

    text = str(marker_id)
    text_size = cv.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = x_start + (marker_size - text_size[0]) // 2
    text_y = y_start + marker_size + text_size[1] + 5
    cv.putText(grid_image, text, (text_x, text_y), font, font_scale, 0, font_thickness)

# --- Output paths ---
out_dir = os.path.abspath("./aruco_out")
os.makedirs(out_dir, exist_ok=True)
png_path = os.path.join(out_dir, "Aruco_DICT6X6_250.png")
pdf_path = os.path.join(out_dir, "Aruco_DICT6X6_250.pdf")

cv.imwrite(png_path, grid_image)

# --- Save to A4 PDF with LEFT margin (10 mm) ---
plt.figure(figsize=(8.27, 11.69), dpi=300)
plt.imshow(grid_image, cmap='gray', vmin=0, vmax=255)
plt.axis("off")

# left, right, top, bottom margins (in inches)
left_margin = 10 / 25.4  # 10 mm → inches
plt.subplots_adjust(left=left_margin / 8.27, right=1, top=1, bottom=0)
plt.savefig(pdf_path, format="pdf", bbox_inches="tight", pad_inches=0.05)
plt.close()

print("Saved successfully:")
print(" -", png_path)
print(" -", pdf_path)