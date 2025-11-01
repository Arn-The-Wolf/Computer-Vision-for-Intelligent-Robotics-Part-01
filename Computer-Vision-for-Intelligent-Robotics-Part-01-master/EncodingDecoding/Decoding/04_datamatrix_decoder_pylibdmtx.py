"""
Data Matrix Decoder using pylibdmtx library
This is a Python-native approach for decoding Data Matrix codes
"""
from pylibdmtx.pylibdmtx import decode
from PIL import Image
import sys
import cv2
import numpy as np

# Allow passing the image path via CLI
image_path = sys.argv[1] if len(sys.argv) > 1 else "datamatrix_image.jpg"

def decode_datamatrix(image_path):
    """Decode Data Matrix code from an image file."""
    try:
        # Load the image using PIL
        image = Image.open(image_path)
        
        # Try to decode
        decoded = decode(image)
        
        if decoded:
            decoded_text = decoded[0].data.decode('utf-8')
            print("=" * 60)
            print("Data Matrix Decoded Successfully!")
            print("=" * 60)
            print(f"Decoded Text: {decoded_text}")
            print("=" * 60)
            
            # Save decoded text to file
            with open("decoded_datamatrix.txt", "w", encoding="utf-8") as f:
                f.write(decoded_text)
            print("\nDecoded text saved to: decoded_datamatrix.txt")
            
            # Try to visualize with bounding box
            try:
                img_cv = cv2.imread(image_path)
                if img_cv is not None:
                    # Get rectangle coordinates if available
                    rect = decoded[0].rect
                    if rect:
                        # Draw rectangle
                        points = [
                            (rect.left, rect.top),
                            (rect.left + rect.width, rect.top),
                            (rect.left + rect.width, rect.top + rect.height),
                            (rect.left, rect.top + rect.height)
                        ]
                        points_array = np.array(points, dtype=np.int32).reshape((-1, 1, 2))
                        cv2.polylines(img_cv, [points_array], isClosed=True, color=(0, 255, 0), thickness=2)
                        
                        # Add text
                        cv2.putText(img_cv, decoded_text, (rect.left, rect.top - 10), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                        
                        # Save annotated image
                        cv2.imwrite("annotated_datamatrix.png", img_cv)
                        print("Annotated image saved as: annotated_datamatrix.png")
                        
                        # Display
                        cv2.imshow("Detected Data Matrix Code", img_cv)
                        print("Press any key to close the window.")
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
            except Exception as e:
                print(f"Note: Could not visualize bounding box: {e}")
            
            return decoded_text
        else:
            print("=" * 60)
            print("No Data Matrix code found in the image.")
            print("=" * 60)
            
            # Try image preprocessing for better detection
            print("\nAttempting image preprocessing...")
            try:
                img_cv = cv2.imread(image_path)
                if img_cv is not None:
                    # Convert to grayscale
                    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
                    
                    # Apply threshold
                    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
                    
                    # Try decoding thresholded image
                    img_pil = Image.fromarray(thresh)
                    decoded = decode(img_pil)
                    
                    if decoded:
                        decoded_text = decoded[0].data.decode('utf-8')
                        print("Successfully decoded after preprocessing!")
                        print(f"Decoded Text: {decoded_text}")
                        with open("decoded_datamatrix.txt", "w", encoding="utf-8") as f:
                            f.write(decoded_text)
                        return decoded_text
            except Exception as e:
                print(f"Preprocessing failed: {e}")
            
            return None
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found!")
        return None
    except Exception as e:
        print(f"Error decoding Data Matrix: {e}")
        return None

if __name__ == "__main__":
    result = decode_datamatrix(image_path)

