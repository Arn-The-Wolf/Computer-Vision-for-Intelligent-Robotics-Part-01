import cv2
import os
import time

# Create a folder for saved frames
save_folder = "captured_frames"
os.makedirs(save_folder, exist_ok=True)

# Load the face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the sunglasses images
sunglasses_male = cv2.imread('santa-glasses-02.png', cv2.IMREAD_UNCHANGED)
sunglasses_female = cv2.imread('santa-glasses-02.png', cv2.IMREAD_UNCHANGED)

# Load the hat image
hat = cv2.imread('santa-hat-01.png', cv2.IMREAD_UNCHANGED)

# Load the beard image
beard = cv2.imread('santa-beard-01.png', cv2.IMREAD_UNCHANGED)

# Load the gender detection model
genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"
genderNet = cv2.dnn.readNet(genderModel, genderProto)

# Define a scaling factor for the accessories
sunglass_accessory_scale = 0.8  # Adjust as needed
hat_accessory_scale = 1.8  # Adjust as needed
beard_accessory_scale = 1.5  # Adjust as needed

# Gender classification threshold
gender_threshold = 0.6  # Adjust as needed

# Start the webcam
cap = cv2.VideoCapture(0)

# Set the desired resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Prepare the input image for gender detection
        face_roi = frame[y:y+h, x:x+w]
        blob = cv2.dnn.blobFromImage(face_roi, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

        # Run gender detection
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()

        # Get the predicted gender and confidence
        gender = "Male" if genderPreds[0, 0] > gender_threshold else "Female"
        gender_confidence = genderPreds[0, 0]

        # Choose the accessory based on gender
        if gender == "Male":
            accessory = sunglasses_male
        else:
            accessory = sunglasses_female

        # Calculate the position and size of the accessory
        accessory_width = int(sunglass_accessory_scale * w)
        accessory_height = int(accessory_width * accessory.shape[0] / accessory.shape[1])

        # Resize the accessory image
        accessory_resized = cv2.resize(accessory, (accessory_width, accessory_height))

        # Create a mask for the accessory
        accessory_mask = accessory_resized[:, :, 3] / 255.0

        # Calculate the position to place the accessory

        # Move accessory slightly to the right or left
        x1 = x + int(w/2) - int(accessory_width/2)
        x2 = x1 + accessory_width

        # Move accessory slightly to the top or bottom
        y1 = y + int(0.6 * h) - accessory_height  
        y2 = y1 + accessory_height

        # Adjust for out-of-bounds positions
        x1 = max(x1, 0)
        x2 = min(x2, frame.shape[1])
        y1 = max(y1, 0)
        y2 = min(y2, frame.shape[0])

        frame_roi = frame[y1:y2, x1:x2]

        # Blend the accessory with the frame
        for c in range(0, 3):
            frame_roi[:, :, c] = (1.0 - accessory_mask) * frame_roi[:, :, c] + accessory_mask * accessory_resized[:, :, c]

        # Add the hat
        hat_width = int(hat_accessory_scale * w)
        hat_height = int(hat.shape[0] * hat_width / hat.shape[1])
        hat_resized = cv2.resize(hat, (hat_width, hat_height))

        # Create a mask for the hat
        hat_mask = hat_resized[:, :, 3] / 255.0
        hat_mask = cv2.resize(hat_mask, (hat_width, hat_height), interpolation=cv2.INTER_AREA)

        # Calculate the position to place the hat

        # Move hat slightly to the right or left
        x_hat1 = x + int(w/2) - int(hat_width/2) + int(0.275 * w)  
        x_hat2 = x_hat1 + hat_width

        # Move hat slightly to the top or bottom
        y_hat1 = y - int(-0.45 * h) - hat_height 
        y_hat2 = y_hat1 + hat_height

        # Adjust for out-of-bounds positions
        x_hat1 = max(x_hat1, 0)
        x_hat2 = min(x_hat2, frame.shape[1])
        y_hat1 = max(y_hat1, 0)
        y_hat2 = min(y_hat2, frame.shape[0])

        frame_roi_hat = frame[y_hat1:y_hat2, x_hat1:x_hat2]

        # Check if dimensions match before blending
        if frame_roi_hat.shape[0] == hat_resized.shape[0] and frame_roi_hat.shape[1] == hat_resized.shape[1]:
            # Blend the hat with the frame
            for c in range(0, 3):
                frame_roi_hat[:, :, c] = (1.0 - hat_mask) * frame_roi_hat[:, :, c] + hat_mask * hat_resized[:, :, c]
        else:
            print("Error: Dimensions mismatch between hat and frame_roi_hat")

        # Add the beard
        beard_width = int(beard_accessory_scale * w)
        beard_height = int(beard.shape[0] * beard_width / beard.shape[1])
        beard_resized = cv2.resize(beard, (beard_width, beard_height))

        # Create a mask for the beard
        beard_mask = beard_resized[:, :, 3] / 255.0
        beard_mask = cv2.resize(beard_mask, (beard_width, beard_height), interpolation=cv2.INTER_AREA)

        # Calculate the position to place the beard

        # Move beard slightly to the right or left
        x_beard1 = x + int(w/2) - int(beard_width/2)
        x_beard2 = x_beard1 + beard_width

        # Move beard slightly to the top or bottom
        y_beard1 = y + int(1.95 * h) - beard_height
        y_beard2 = y_beard1 + beard_height

        # Adjust for out-of-bounds positions
        x_beard1 = max(x_beard1, 0)
        x_beard2 = min(x_beard2, frame.shape[1])
        y_beard1 = max(y_beard1, 0)
        y_beard2 = min(y_beard2, frame.shape[0])

        frame_roi_beard = frame[y_beard1:y_beard2, x_beard1:x_beard2]

        # Check if dimensions match before blending
        if frame_roi_beard.shape[0] == beard_resized.shape[0] and frame_roi_beard.shape[1] == beard_resized.shape[1]:
            # Blend the beard with the frame
            for c in range(0, 3):
                frame_roi_beard[:, :, c] = (1.0 - beard_mask) * frame_roi_beard[:, :, c] + beard_mask * beard_resized[:, :, c]
        else:
            print("Error: Dimensions mismatch between beard and frame_roi_beard")

    cv2.imshow('Xmas Virtual Try-On', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Quit the application
        break
    elif key == ord('s'):  # Save the frame with a timestamp
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            save_path = os.path.join(save_folder, f"captured_frame_{timestamp}.png")
            cv2.imwrite(save_path, frame)
            print(f"Frame saved at {save_path}")
# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
