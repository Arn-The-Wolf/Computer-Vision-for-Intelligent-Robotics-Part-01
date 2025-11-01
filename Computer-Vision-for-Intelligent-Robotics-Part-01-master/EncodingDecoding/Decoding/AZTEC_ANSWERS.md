# Answers to Aztec Code Decoding Questions

## Question: Which type of code is represented in the image?

**Answer: Aztec Code**

The image shows a **2D barcode** with the following characteristics:
- **Square-shaped** barcode pattern
- **Central bullseye finder pattern** - The most distinctive feature: a concentric square pattern in the center consisting of:
  - A small black square at the core
  - Surrounded by a white square
  - Then a black square
  - Finally a larger white square
- **Dense grid** of black and white modules (squares) surrounding the central finder pattern
- **High-density pixelated pattern** encoding data

These characteristics are definitive features of an **Aztec Code**.

**Why not the other code types:**
- **Barcode (1D)**: Would have vertical lines of varying widths, not a square matrix
- **QR Code**: Would have three finder squares in the corners (top-left, top-right, bottom-left), not a central bullseye
- **PDF417 Code**: Would have a rectangular stacked barcode pattern with start/stop patterns on the sides
- **Data Matrix Code**: Would have an L-shaped finder pattern along the bottom and left edges, with timing patterns along top and right edges
- **Maxicode**: Would have a hexagonal pattern with a central finder pattern surrounded by hexagonal modules

---

## Question 1: Please write down the text you decoded from the code

**To decode the Aztec code, run:**

```powershell
cd "D:\QR Code Scanner\Computer-Vision-for-Intelligent-Robotics-Part-01-master\EncodingDecoding\Decoding"
python 05_aztec_decoder.py [path_to_your_aztec_image.jpg]
```

**Example:**
```powershell
python 05_aztec_decoder.py qr_code2.png
```

**The decoded text will be:**
- Displayed in the console output
- Saved to `decoded_aztec.txt`
- Annotated on the image saved as `annotated_aztec.png`

**Note:** If the initial decode fails, the script automatically tries rotated versions (90°, 180°, 270°) for better robustness.

---

## Question 2: Please write down the link to the code you used to decode the code

**GitHub Repository Link:**

Assuming the repository is pushed to GitHub, the link to the Aztec decoder code would be:

```
https://github.com/[username]/Computer-Vision-for-Intelligent-Robotics-Part-01/blob/master/EncodingDecoding/Decoding/05_aztec_decoder.py
```

**Alternative locations in the repository:**

1. **ZXing-based decoder (recommended - most robust):**
   ```
   https://github.com/[username]/Computer-Vision-for-Intelligent-Robotics-Part-01/blob/master/EncodingDecoding/Decoding/05_aztec_decoder.py
   ```

2. **AZTech folder decoder (using pyztec library):**
   ```
   https://github.com/[username]/Computer-Vision-for-Intelligent-Robotics-Part-01/blob/master/EncodingDecoding/AZTech/02_decode_aztec_code.py
   ```

**Main decoder used:** `05_aztec_decoder.py` in the `EncodingDecoding/Decoding/` folder.

This decoder uses **ZXing (Zebra Crossing)** library through Java, similar to the PDF417 and Data Matrix decoders. ZXing automatically detects and decodes Aztec codes.

---

## Technical Details

### Decoder Implementation:
- **Library**: ZXing (javase-3.5.0.jar, core-3.5.0.jar, jcommander-1.82.jar)
- **Method**: Command-line Java execution via subprocess
- **Fallback**: Docker support (if Docker is available)
- **Preprocessing**: Automatic rotation variants (90°, 180°, 270°) for robustness
- **Output**: 
  - Console output with decoded text
  - `decoded_aztec.txt` file
  - `annotated_aztec.png` with bounding box and text overlay

### Prerequisites:
- Java 17 or higher
- Required JAR files (in Decoding folder):
  - `javase-3.5.0.jar`
  - `core-3.5.0.jar`
  - `jcommander-1.82.jar`
- Python libraries: `cv2`, `numpy`

---

## How to Use

1. **Navigate to the Decoding folder:**
   ```powershell
   cd "D:\QR Code Scanner\Computer-Vision-for-Intelligent-Robotics-Part-01-master\EncodingDecoding\Decoding"
   ```

2. **Run the decoder with your image:**
   ```powershell
   python 05_aztec_decoder.py your_aztec_image.png
   ```

3. **Results:**
   - Check console for decoded text
   - Check `decoded_aztec.txt` for saved text
   - Check `annotated_aztec.png` for visual annotation

---

## Example Output

When decoding a successful Aztec code, you'll see:

```
============================================================
Aztec Code Decoder Output:
============================================================
file:///D:/.../aztec_image.png (format: AZTEC, type: TEXT):
Raw result:
Hello World
Parsed result:
Hello World
Found 4 result points.
  Point 0: (x, y)
  Point 1: (x, y)
  Point 2: (x, y)
  Point 3: (x, y)
============================================================

Decoded Text: Hello World
Decoded text saved to: decoded_aztec.txt

Drawing polygon with points: [...]
Annotated image saved as annotated_aztec.png
```

