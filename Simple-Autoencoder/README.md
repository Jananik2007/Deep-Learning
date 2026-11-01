# Autoencoder for Dimensionality Reduction and Feature Learning

## 1. Project Overview

This project demonstrates the implementation of a Dense Autoencoder using TensorFlow and Keras for dimensionality reduction and feature learning. The model is trained using the MNIST handwritten digits dataset to learn compact representations of input images and reconstruct them with minimum information loss.

The Encoder compresses the input images into a lower-dimensional latent representation, while the Decoder reconstructs the original images from the learned features.

## 2. Aim

To implement and train a simple Autoencoder for dimensionality reduction and feature learning by compressing input data into a lower-dimensional representation and reconstructing the original data from the learned features.

## 3. Dataset Description

The experiment uses the **MNIST Handwritten Digits Dataset**, which consists of grayscale images of handwritten digits from 0 to 9.

| Dataset Property | Description |
|---|---|
| Training samples | 60,000 |
| Testing samples | 10,000 |
| Image dimensions | 28 × 28 pixels |
| Number of classes | 10 |
| Original pixel range | 0–255 |
| Normalized pixel range | 0–1 |

Each image was converted into a one-dimensional vector containing 784 features before being passed to the Autoencoder.

## 4. Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Pandas
- Scikit-learn
- Google Colab
- GitHub

## 5. Autoencoder Architecture

The Autoencoder consists of three main components:

**Encoder:** Extracts important features and compresses the input data.

**Bottleneck:** Stores the compressed representation using 32 neurons.

**Decoder:** Reconstructs the original input using the compressed representation.

### Architecture Details

| Layer | Number of Neurons | Activation |
|---|---:|---|
| Input | 784 | - |
| Encoder Layer 1 | 128 | ReLU |
| Encoder Layer 2 | 64 | ReLU |
| Bottleneck | 32 | ReLU |
| Decoder Layer 1 | 64 | ReLU |
| Decoder Layer 2 | 128 | ReLU |
| Output | 784 | Sigmoid |

**Model Configuration:**

- Optimizer: Adam
- Loss Function: Mean Squared Error (MSE)
- Epochs: 20
- Batch Size: 256
- Total Parameters: 222,384
- Trainable Parameters: 222,384
- Non-trainable Parameters: 0

## 6. Implementation Workflow

The experiment was carried out through the following stages:

1. **Dataset Preparation:** Loaded the MNIST dataset, explored sample images, normalized pixel values and reshaped images into 784-dimensional vectors.

2. **Model Implementation:** Designed a Dense Autoencoder using an Encoder, Bottleneck and Decoder with suitable activation functions.

3. **Model Training:** Trained the Autoencoder using the original images as both input and target output.

4. **Performance Evaluation:** Evaluated the trained model using reconstruction MSE and visualized training and validation loss.

5. **Dimensionality Reduction:** Extracted 32-dimensional latent representations using the trained Encoder.

6. **Feature Visualization:** Applied Principal Component Analysis (PCA) to visualize the latent representations in two dimensions.

7. **Image Reconstruction:** Used the Decoder to reconstruct images from their compressed representations.

## 7. Experimental Results

### 7.1 Training and Validation Performance

The Autoencoder was trained for 20 epochs.

| Metric | Initial Value | Final Value |
|---|---:|---:|
| Training Loss | 0.0633 | 0.0097 |
| Validation Loss | 0.0354 | 0.0095 |

**Test Reconstruction MSE: 0.00948364**

The training and validation losses decreased consistently throughout the training process, indicating that the model progressively improved its reconstruction performance.

### 7.2 Dimensionality Reduction Results

The Encoder successfully compressed the original input data into a lower-dimensional representation.

| Parameter | Dimensions |
|---|---|
| Original Test Data | (10000, 784) |
| Compressed Test Data | (10000, 32) |
| Original Features | 784 |
| Latent Features | 32 |
| Dimensionality Reduction | 95.92% |

The model reduced the number of input features by approximately 95.92% while retaining information useful for image reconstruction.

### 7.3 Feature Visualization

Principal Component Analysis (PCA) was applied to transform the 32-dimensional latent representations into two dimensions for visualization.

The resulting plot showed overlapping distributions among different digit classes, with some visible groupings in the latent feature space.

## 8. Observations

1. The MNIST dataset was successfully preprocessed by normalizing pixel values and converting the images into 784-dimensional input vectors, making them suitable for Autoencoder training.

2. The implemented Autoencoder successfully learned a compact representation of the input images through its Encoder and Bottleneck layers, reducing the feature dimensions from 784 to 32.

3. The Decoder effectively reconstructed the input images from their compressed representations, retaining the major visual patterns and structures of the handwritten digits.

4. During training, the training loss decreased from 0.0633 to 0.0097, while the validation loss decreased from 0.0354 to 0.0095 over 20 epochs, indicating consistent improvement in reconstruction performance.

5. The model achieved a test reconstruction Mean Squared Error (MSE) of 0.00948364, demonstrating its ability to reconstruct the input images with relatively low error.

6. The latent representations were visualized using PCA. The visualization showed overlapping distributions among different digit classes, with some visible groupings in the learned feature space.

7. Overall, the experiment demonstrated that an Autoencoder can effectively perform dimensionality reduction while preserving important features required for data reconstruction.

## 9. Conclusion

The Dense Autoencoder was successfully implemented and trained using the MNIST handwritten digits dataset. The Encoder compressed the original 784-dimensional input into a 32-dimensional latent representation, achieving approximately 95.92% dimensionality reduction. The Decoder reconstructed the original images from the learned features, achieving a test reconstruction MSE of 0.00948364. The experiment demonstrated the effectiveness of Autoencoders in dimensionality reduction, feature learning and image reconstruction.

