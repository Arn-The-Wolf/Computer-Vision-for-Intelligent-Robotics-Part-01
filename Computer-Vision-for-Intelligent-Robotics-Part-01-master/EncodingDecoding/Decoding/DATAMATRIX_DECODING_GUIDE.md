# Data Matrix Code Decoding Guide

## Question 2.a: Which code type is this?

**Answer: Data Matrix Code**

Based on the image description:
- Square-shaped barcode
- L-shaped finder pattern along bottom and left edges
- Timing pattern along top and right edges
- Grid of black and white modules
- These are characteristic features of a **Data Matrix Code (ECC200)**

## Question 2: How to decode the image step by step

### Method 1: Using ZXing (Recommended - Most Robust)

This method uses ZXing library through Java, similar to the PDF417 decoder.

#### Prerequisites:
- Java 17 or higher (already installed on your system ✓)
- Docker (optional, for Docker-based decoding)
- Required JAR files (already in Decoding folder):
  - `javase-3.5.0.jar`
  - `core-3.5.0.jar`
  - `jcommander-1.82.jar`

#### Steps:

1. **Navigate to the Decoding folder:**
   ```powershell
   cd "D:\QR Code Scanner\Computer-Vision-for-Intelligent-Robotics-Part-01-master\EncodingDecoding\Decoding"
   ```

2. **Place your image in the Decoding folder:**
   - Save your Data Matrix image as `datamatrix_image.jpg` (or use the actual filename)

3. **Run the ZXing-based decoder:**
   ```powershell
   python 04_datamatrix_decoder.py datamatrix_image.jpg
   ```
   
   Or if the image is named differently:
   ```powershell
   python 04_datamatrix_decoder.py path\to\your\image.jpg
   ```

4. **The script will:**
   - Try to decode the original image
   - If that fails, try rotated versions (90°, 180°, 270°)
   - Extract the decoded text
   - Display bounding box around the code
   - Save decoded text to `decoded_datamatrix.txt`
   - Save annotated image to `annotated_datamatrix.png`

### Method 2: Using pylibdmtx (Python Native)

This method uses the Python `pylibdmtx` library.

#### Prerequisites:
- Install pylibdmtx: `pip install pylibdmtx`
- OpenCV: `pip install opencv-python`
- PIL/Pillow: `pip install Pillow`

#### Steps:

1. **Install dependencies (if not already installed):**
   ```powershell
   pip install pylibdmtx opencv-python Pillow
   ```

2. **Navigate to the Decoding folder:**
   ```powershell
   cd "D:\QR Code Scanner\Computer-Vision-for-Intelligent-Robotics-Part-01-master\EncodingDecoding\Decoding"
   ```

3. **Run the pylibdmtx-based decoder:**
   ```powershell
   python 04_datamatrix_decoder_pylibdmtx.py datamatrix_image.jpg
   ```

4. **The script will:**
   - Load and decode the image
   - Display the decoded text
   - Save to `decoded_datamatrix.txt`
   - Create an annotated visualization

### Method 3: Using Simple Script (Basic)

You can also use the existing simple decoder in the DataMatrix folder:

1. **Navigate to DataMatrix folder:**
   ```powershell
   cd "D:\QR Code Scanner\Computer-Vision-for-Intelligent-Robotics-Part-01-master\EncodingDecoding\DataMatrix"
   ```

2. **Modify the script to use your image:**
   - Edit `01_decode_ecc200.py`
   - Change `"ecc200_datamatrix.png"` to your image filename

3. **Run:**
   ```powershell
   python 01_decode_ecc200.py
   ```

## Question 3: Decoded Text

**To get the decoded text, you need to run the decoder on your actual image.**

Once you run the decoder, the decoded text will be:
- Displayed in the console output
- Saved to `decoded_datamatrix.txt` file

**Note:** Since I don't have access to the actual image file you're referring to, please run one of the decoders above with your image to get the decoded text.

## Question 4: GitHub Repository Link

The code used to decode the Data Matrix code is located in this codebase:

**Local Path:**
```
Computer-Vision-for-Intelligent-Robotics-Part-01-master/EncodingDecoding/Decoding/04_datamatrix_decoder.py
```

**If this codebase is pushed to GitHub, the link would be:**
```
https://github.com/[your-username]/Computer-Vision-for-Intelligent-Robotics-Part-01/tree/master/EncodingDecoding/Decoding
```

**Specific file:**
```
https://github.com/[your-username]/Computer-Vision-for-Intelligent-Robotics-Part-01/blob/master/EncodingDecoding/Decoding/04_datamatrix_decoder.py
```

**Note:** Replace `[your-username]` with your actual GitHub username, or if this repository is not yet pushed to GitHub, you would need to:
1. Initialize a git repository: `git init`
2. Add the files: `git add .`
3. Commit: `git commit -m "Add Data Matrix decoder"`
4. Create a GitHub repository and push: `git push origin main`

Otherwise, type: **"Code not yet pushed to GitHub repository"**

## Summary

- **Code Type:** Data Matrix Code
- **Decoder Script:** `04_datamatrix_decoder.py` (ZXing-based) or `04_datamatrix_decoder_pylibdmtx.py` (Python-native)
- **Output:** Decoded text saved to `decoded_datamatrix.txt`
- **Visualization:** Annotated image saved to `annotated_datamatrix.png`

