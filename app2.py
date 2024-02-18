import streamlit as st
import cv2
import numpy as np

# Function to find the dissimilarity position and bounding boxes
def find_dissimilarity(img1, img2):
    # Convert images to grayscale
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Calculate absolute difference between images
    diff_img = cv2.absdiff(gray_img1, gray_img2)
    
    # Threshold the difference image to create a mask
    _, mask = cv2.threshold(diff_img, 30, 255, cv2.THRESH_BINARY)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find bounding boxes around contours
    bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours]
    
    return bounding_boxes

def main():
    st.title("Image Dissimilarity Detection")
    
    # Upload images
    uploaded_files = st.file_uploader("Choose two images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    if uploaded_files is not None and len(uploaded_files) == 2:
        st.write("### Selected Images:")
        st.image([file for file in uploaded_files], width=300)
        
        # Read images using OpenCV
        img1 = cv2.imdecode(np.frombuffer(uploaded_files[0].read(), np.uint8), cv2.IMREAD_COLOR)
        img2 = cv2.imdecode(np.frombuffer(uploaded_files[1].read(), np.uint8), cv2.IMREAD_COLOR)
        
        # Find dissimilarity position and bounding boxes
        bounding_boxes = find_dissimilarity(img1, img2)
        
        # Draw bounding boxes on the images
        for bbox in bounding_boxes:
            x, y, w, h = bbox
            cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Display images with bounding boxes
        st.write("### Images with Bounding Boxes Around Dissimilar Regions:")
        st.image([img1, img2], caption=["Image 1", "Image 2"], width=300)

if __name__ == "__main__":
    main()
