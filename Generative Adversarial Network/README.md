# Generative Adversarial Network (GAN) – MNIST Image Generation

## 1. Aim

To implement and train a Generative Adversarial Network (GAN) to generate synthetic handwritten digit images using the MNIST dataset by training a Generator and a Discriminator in an adversarial learning framework.

## 2. Overview

A Generative Adversarial Network (GAN) is a deep learning model consisting of two neural networks: a Generator and a Discriminator.

The Generator creates synthetic images from random noise vectors, while the Discriminator identifies whether the given images are real or generated.

Both networks compete with each other during training, helping the Generator learn to produce realistic synthetic images.

## 3. Dataset

The MNIST handwritten digit dataset is used for this experiment.

- Training images: 60,000
- Testing images: 10,000
- Image dimensions: 28 × 28 pixels
- Image type: Grayscale
- Number of classes: 10 (digits 0–9)

The images are normalized from the original pixel range of 0–255 to -1 to +1 before training.

## 4. Technologies Used

- Python
- TensorFlow and Keras
- NumPy
- Matplotlib
- Google Colab
- GitHub

## 5. GAN Architecture

### Generator

The Generator takes a 100-dimensional random noise vector as input and transforms it into a 28 × 28 grayscale image.

Layers used:
- Dense
- Batch Normalization
- LeakyReLU
- Reshape
- Conv2DTranspose
- Tanh activation

### Discriminator

The Discriminator receives an image and predicts whether it is real or generated.

Layers used:
- Conv2D
- LeakyReLU
- Dropout
- Flatten
- Dense
- Sigmoid activation

## 6. Training Configuration

| Parameter | Value |
|---|---|
| Dataset | MNIST |
| Noise Dimension | 100 |
| Batch Size | 256 |
| Epochs | 30 |
| Optimizer | Adam |
| Learning Rate | 0.0002 |
| Beta 1 | 0.5 |
| Loss Function | Binary Cross-Entropy |
| Image Size | 28 × 28 × 1 |

## 7. Implementation Steps

1. Import the required libraries.
2. Load and explore the MNIST dataset.
3. Normalize and reshape the images.
4. Build the Generator model.
5. Build the Discriminator model.
6. Combine both models to construct the GAN.
7. Define loss functions and optimizers.
8. Train the Discriminator using real and generated images.
9. Train the Generator to produce realistic images.
10. Monitor Generator and Discriminator losses.
11. Generate synthetic images and compare them with original images.
12. Save the trained models.

## 8. Experimental Results

The GAN was trained successfully for 30 epochs.

Final loss values:

| Model | Final Loss |
|---|---:|
| Generator | 0.8998 |
| Discriminator | 1.2493 |

The Generator produced synthetic handwritten digit images from random noise vectors.

The generated images showed recognizable digit patterns with some variations and distortions.

## 9. Observations

- The Generator learned to produce synthetic handwritten digit images.
- The Discriminator learned to distinguish between real and generated images.
- Different random noise vectors produced different synthetic images.
- The generated images were compared with original MNIST samples.
- The loss graph demonstrated the changing performance of both networks during adversarial training
  
## 11. Conclusion

A Generative Adversarial Network was successfully implemented and trained using the MNIST handwritten digit dataset. The Generator learned to produce synthetic images from random noise, while the Discriminator learned to distinguish between real and generated images.

The experiment demonstrated the working of adversarial learning, image generation, loss monitoring and visualization of synthetic images.
