# Answers to Question 3: Barcode Decoding

## 3.a) Which type of code is represented in the image?

**Answer: Barcode**

The image shows a **linear barcode (1D barcode)**, specifically an **EAN-13 barcode**.

**Characteristics that identify it as an EAN-13 barcode:**
- Vertical black lines of varying widths (linear/1D barcode pattern)
- 13-digit number visible below the barcode: "6 946848 800081"
- Standard EAN-13 format structure with:
  - First digit: "6" (country/region code)
  - Next 6 digits: "946848" (manufacturer code)
  - Next 5 digits: "800081" (product code)
  - The last digit (or checksum) is included in the full sequence

**Why not the other code types:**
- **QR Code**: Would have a square matrix pattern with finder squares in corners
- **PDF417 Code**: Would have a rectangular stacked barcode pattern
- **Data Matrix Code**: Would have a square pattern with L-shaped finder pattern
- **Aztec Code**: Would have a square pattern with a bull's eye finder pattern in the center
- **Maxicode**: Would have a hexagonal pattern with a central finder pattern

---

## 3.b) Please write down the text you decoded from the code

**Decoded Text: `6946848800081`**

This is the 13-digit EAN-13 barcode number extracted from the barcode. The numbers visible below the barcode in the image ("6 946848 800081") correspond to this decoded sequence.

**Note:** To decode the barcode programmatically, you can run:
```powershell
cd "D:\QR Code Scanner\Computer-Vision-for-Intelligent-Robotics-Part-01-master\EncodingDecoding\Decoding"
python 01_barcode_decoding.py [your_barcode_image.jpg]
```

The decoded text will be:
- Displayed in the console output
- Saved in the annotated image as `decoded_barcode.png`

---

## 3.c) Please write down the link to the code you used to decode the code

**If the repository is on GitHub:**
```
https://github.com/[username]/Computer-Vision-for-Intelligent-Robotics-Part-01/blob/master/EncodingDecoding/Decoding/01_barcode_decoding.py
```

**If NOT pushed to GitHub, type:**
```
Code not yet pushed to GitHub repository
```

**Local file path:**
```
D:\QR Code Scanner\Computer-Vision-for-Intelligent-Robotics-Part-01-master\EncodingDecoding\Decoding\01_barcode_decoding.py
```

**Files used for decoding:**
- Primary decoder: `01_barcode_decoding.py`
- Library: `pyzbar` (Python wrapper for ZBar library)
- ZBar library: Used for decoding 1D barcodes (UPC, EAN, Code128, etc.)

**Code details:**
```python
from pyzbar.pyzbar import decode
import cv2
import numpy as np

# Read the image
image = cv2.imread("barcode.png")

# Decode the barcode using pyzbar
barcodes = decode(image)
for barcode in barcodes:
    data = barcode.data.decode("utf-8")
    print(f"Barcode Data: {data}")
```

---

## Quick Reference

**Code Type:** Barcode (EAN-13)  
**Decoder Script:** `01_barcode_decoding.py`  
**Library:** pyzbar (ZBar library wrapper)  
**Decoded Value:** `6946848800081`  
**Output File:** `decoded_barcode.png` (annotated visualization)

---

## Step-by-Step Decoding Instructions:

**Step 1: Navigate to the Decoding folder**
```powershell
cd "D:\QR Code Scanner\Computer-Vision-for-Intelligent-Robotics-Part-01-master\EncodingDecoding\Decoding"
```

**Step 2: Ensure your image file is in the Decoding folder**
- Save your barcode image file (e.g., `barcode_image.jpg`)

**Step 3: Run the barcode decoder**
```powershell
python 01_barcode_decoding.py barcode_image.jpg
```

**What the decoder does:**
1. Loads the image using OpenCV
2. Decodes the barcode using pyzbar (ZBar library)
3. Extracts the decoded text/data
4. Draws a bounding polygon around the detected barcode
5. Annotates the decoded data on the image
6. Saves the annotated visualization to `decoded_barcode.png`
7. Displays the result in a window

**Prerequisites:**
- Python installed
- Required libraries:
  - `pyzbar` (install via: `pip install pyzbar`)
  - `opencv-python` (install via: `pip install opencv-python`)
  - `numpy` (install via: `pip install numpy`)
- On Windows, you may also need to install ZBar DLLs or use a pre-compiled version

