# Brain Tumor Classification Using Transfer Learning

## Overview

This project implements transfer learning using a pre-trained **ResNet-50** model for classifying brain MRI images into four categories:

- Glioma Tumor
- Meningioma Tumor
- No Tumor
- Pituitary Tumor

A pre-trained Vision Transformer (ViT) from Hugging Face is also explored for image classification.

## Technologies Used

- Python
- TensorFlow / Keras
- ResNet-50
- Hugging Face Transformers
- Google Colab
- Kaggle
- Matplotlib
- NumPy

## Methodology

1. Downloaded and prepared the Brain Tumor MRI dataset.
2. Resized and preprocessed the images.
3. Split the dataset into training, validation, and testing sets.
4. Loaded a pre-trained ResNet-50 model.
5. Replaced the original classification layer with a custom four-class classifier.
6. Froze the pre-trained feature extraction layers.
7. Trained and evaluated the model.
8. Visualized accuracy and loss across epochs.
9. Tested a pre-trained Hugging Face Vision Transformer on sample images.

## Results

| Metric | Result |
|---|---:|
| Training Accuracy | 91.46% |
| Validation Accuracy | 84.49% |
| Test Accuracy | 74.87% |

## Hugging Face Comparison

The generic Hugging Face Vision Transformer produced ImageNet-based predictions such as **"nematode"** for the MRI images. This occurs because the model was not fine-tuned for brain tumor classification.

In contrast, ResNet-50 was trained specifically for the four brain tumor classes and was therefore more suitable for this task.

## Conclusion

The experiment demonstrates that transfer learning can effectively adapt pre-trained vision models to domain-specific image classification. ResNet-50 achieved a test accuracy of **74.87%** on the brain tumor dataset.

## Author

**Janani K.**  
AI & Data Science Student
