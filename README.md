Problem Overview:

1. Goal: Develop a model to detect differences between two images and draw bounding boxes around the detected differences.

2. Objective: 
    - Utilize computer vision techniques to identify disparities between two input images.
    - Implement a model that takes two images as input, identifies areas with differences, and draws bounding boxes around those areas.
    - Calculate and print a similarity score to evaluate the model's performance.

3. Evaluation Criteria:
    - Quantitative metrics will be used to evaluate the model's performance.
    - The model should be capable of working on any image for ranking purposes.

4. Sample Input and Output:
    - Sample input consists of two images.
    - Sample output includes images with bounding boxes drawn around the areas of dissimilarity, along with a similarity score.

My Solution:

1. App 1: Image Comparison with Bounding Boxes:
    - This Streamlit app takes two images as input.
    - It employs a pre-trained computer vision model to detect differences between the images.
    - The app then overlays bounding boxes on the dissimilar regions and returns the modified image.
  

      Website : 
       ![image](https://github.com/SudipDharaCode/Image-Dissimilarity-Detection/assets/127935611/7f7f653b-82ff-4be4-8c7f-70ed4538561e)

      Selected Images:
        ![image](https://github.com/SudipDharaCode/Image-Dissimilarity-Detection/assets/127935611/8d4e11ef-52eb-42c1-9fea-5aedf417707f)
      
      Image with Bounding Box Around Dissimilar Regions:
        ![image](https://github.com/SudipDharaCode/Image-Dissimilarity-Detection/assets/127935611/0b6724ab-c896-45aa-bde5-80a3cb507665)



2. App 2: Side-by-Side Image Comparison:
    - Another Streamlit app designed to compare two images side by side.
    - Users upload two images for comparison.
    - The app uses a similar underlying model to identify differences between the images.
    - Bounding boxes are drawn around the dissimilar areas in both images.
    - It returns two images, each displaying the original image with bounding boxes around the dissimilar regions.
    - This facilitates a direct visual comparison between the two images.
  
      Website : 
       ![image](https://github.com/SudipDharaCode/Image-Dissimilarity-Detection/assets/127935611/7f7f653b-82ff-4be4-8c7f-70ed4538561e)

      Selected Images:
        ![image](https://github.com/SudipDharaCode/Image-Dissimilarity-Detection/assets/127935611/8d4e11ef-52eb-42c1-9fea-5aedf417707f)
      
      Image with Bounding Box Around Dissimilar Regions:
        ![image](https://github.com/SudipDharaCode/Image-Dissimilarity-Detection/assets/127935611/cf6c6de2-5758-4f4b-86d6-3882699faf6d)


Key Features of My Solution:

 Flexibility: Both apps are designed to handle any pair of input images, ensuring versatility and applicability.
 User-Friendly Interface: Streamlit provides a simple and intuitive interface for users to interact with the model.
 Effective Visualization: Bounding boxes help users quickly identify the dissimilar areas between the images.
 Scalability: The model can be further improved or replaced with more advanced techniques for better performance.
 Documentation: Well-commented code and clear documentation accompany the deliverables for ease of understanding and future development.
