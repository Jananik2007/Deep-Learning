#  CNN Image Classification using CIFAR-10

A Convolutional Neural Network (CNN) based image classification project that classifies images into 10 different categories using the **CIFAR-10 benchmark dataset**. The project covers the complete machine learning workflow, from dataset preparation and preprocessing to model training, evaluation, and performance analysis.

---

##  Project Overview

Image classification is a fundamental computer vision task where a machine learning model learns to identify the category of an image.

In this project, a **Convolutional Neural Network (CNN)** is developed using **TensorFlow/Keras** to classify CIFAR-10 images into 10 classes.

The project focuses on understanding how convolutional layers extract visual features and how a CNN can learn hierarchical representations for image recognition.

---

##  Objectives

* Understand the architecture and working of Convolutional Neural Networks.
* Prepare and preprocess an image dataset for CNN training.
* Build a CNN model using TensorFlow/Keras.
* Train the model using an appropriate optimizer and loss function.
* Evaluate model performance using accuracy and loss.
* Analyze predictions using a confusion matrix.
* Visualize correctly and incorrectly classified images.
* Identify the strengths and limitations of CNN-based image classification.

---

##  Dataset

### CIFAR-10

The **CIFAR-10 dataset** contains 60,000 color images belonging to 10 different classes.

| Class | Description |
| ----- | ----------- |
| 0     | Airplane    |
| 1     | Automobile  |
| 2     | Bird        |
| 3     | Cat         |
| 4     | Deer        |
| 5     | Dog         |
| 6     | Frog        |
| 7     | Horse       |
| 8     | Ship        |
| 9     | Truck       |

### Dataset Split

| Dataset    | Number of Images |
| ---------- | ---------------: |
| Training   |           45,000 |
| Validation |            5,000 |
| Testing    |           10,000 |
| **Total**  |       **60,000** |

The original CIFAR-10 images have a resolution of **32 × 32 pixels** with **3 RGB channels**.

---

##  Technologies Used

* **Python**
* **TensorFlow / Keras**
* **NumPy**
* **Matplotlib**
* **Scikit-learn**
* **Google Colab**
* **CIFAR-10 Dataset**

---

##  Project Workflow

```text
CIFAR-10 Dataset
       ↓
Dataset Loading
       ↓
Data Exploration
       ↓
Train / Validation / Test Split
       ↓
Image Preprocessing
       ↓
Normalization
       ↓
CNN Architecture
       ↓
Model Compilation
       ↓
Model Training
       ↓
Validation
       ↓
Testing
       ↓
Performance Analysis
       ↓
Confusion Matrix
       ↓
Sample Predictions
       ↓
Misclassified Images
```

---

##  Data Preprocessing

The dataset undergoes preprocessing before being provided to the CNN.

### 1. Train-Validation-Test Split

The original training dataset is divided into:

* 45,000 training images
* 5,000 validation images

The original 10,000-image test set is kept separate for final evaluation.

### 2. Image Resizing

Images can be resized to a consistent input size when required by the model architecture.

### 3. Pixel Normalization

Pixel values originally range from:

```text
0 – 255
```

They are normalized to:

```text
0 – 1
```

using:

```python
x = x / 255.0
```

Normalization helps improve numerical stability and makes model training more efficient.

---

#  CNN Architecture

The CNN consists of convolutional layers for feature extraction followed by fully connected layers for classification.

```text
Input Image
64 × 64 × 3
      ↓
Conv2D
32 Filters, 3 × 3
      ↓
ReLU
      ↓
Max Pooling
2 × 2
      ↓
Conv2D
64 Filters, 3 × 3
      ↓
ReLU
      ↓
Max Pooling
2 × 2
      ↓
Flatten
      ↓
Dense
128 Neurons
      ↓
ReLU
      ↓
Dense
10 Neurons
      ↓
Softmax
      ↓
Class Prediction
```

---

##  Model Components

### Convolutional Layers

Convolutional layers use filters to automatically extract important visual features such as:

* Edges
* Textures
* Shapes
* Patterns

### ReLU Activation

ReLU introduces non-linearity into the network and helps the model learn complex patterns.

```text
ReLU(x) = max(0, x)
```

### Max Pooling

Max Pooling reduces the spatial dimensions of feature maps while retaining important features.

### Flatten Layer

The extracted feature maps are converted into a one-dimensional vector before being passed to the fully connected layers.

### Fully Connected Layer

The Dense layer learns relationships between the extracted features and the target classes.

### Softmax Output

The final Softmax layer produces probability values for all 10 CIFAR-10 classes.

The class with the highest probability is selected as the predicted class.

---

# ⚙️ Model Compilation

The CNN is compiled using:

| Component     | Configuration                    |
| ------------- | -------------------------------- |
| Optimizer     | Adam                             |
| Loss Function | Sparse Categorical Cross-Entropy |
| Metric        | Accuracy                         |

### Adam Optimizer

Adam updates the model weights during training and provides adaptive learning rates for efficient optimization.

### Sparse Categorical Cross-Entropy

This loss function is suitable for multi-class classification when class labels are represented as integers.

---

#  Model Training

The model is trained using the training dataset while the validation dataset is used to monitor generalization performance.

Important training parameters include:

* Number of epochs
* Batch size
* Learning rate
* Number of convolution filters
* Kernel size
* Dense layer size

The training history is recorded to analyze the model's learning behavior.

---

#  Performance Evaluation

The model is evaluated using:

### Training Accuracy

Measures the percentage of training images correctly classified by the model.

### Validation Accuracy

Measures how well the model performs on unseen validation data during training.

### Testing Accuracy

Measures the final classification performance on the independent test dataset.

### Training and Validation Loss

Loss values indicate how closely the model's predictions match the actual labels.

---

##  Training Curves

The project visualizes:

### Accuracy vs Epoch

The graph compares training accuracy and validation accuracy across epochs.

It helps determine whether the model is learning effectively and whether overfitting is occurring.

### Loss vs Epoch

The graph compares training loss and validation loss across epochs.

A decreasing training loss generally indicates that the model is learning from the training data.

---

#  Confusion Matrix

A confusion matrix is used to analyze class-wise classification performance.

It compares:

```text
Actual Class
     vs
Predicted Class
```

The diagonal elements represent correctly classified images, while off-diagonal elements represent misclassifications.

The confusion matrix also helps identify classes that the CNN frequently confuses with one another.

---

#  Sample Predictions

The project displays sample test images along with:

```text
Actual: Cat
Predicted: Cat
```

This provides a visual understanding of how well the CNN recognizes different classes.

---

#  Misclassified Images

Images where:

```text
Actual Class ≠ Predicted Class
```

are identified and visualized.

Analyzing these images helps understand why the model makes incorrect predictions.

Common causes include:

* Low-resolution images
* Visually similar classes
* Complex backgrounds
* Unusual object orientations
* Insufficient training
* Model overfitting or underfitting

---

#  Results



| Metric              |     Result |
| ------------------- | ---------: |
| Training Accuracy   | **94.00%** |
| Validation Accuracy | **67.26%** |
| Training Loss       | **0.1775** |
| Validation Loss     | **1.4986** |
| Testing Accuracy    | **66.39%%** |

> **Note:** Results may vary depending on the training configuration, number of epochs, hardware, and model architecture.

---

#  Strengths

* Automatically learns visual features from images.
* Preserves spatial relationships between pixels.
* Uses parameter sharing, reducing the number of parameters compared with fully connected networks.
* Performs well on image classification tasks.
* Learns hierarchical features from simple edges to complex patterns.

---

#  Limitations

* CNNs may require large amounts of labeled training data.
* Training can require significant computational resources.
* Deeper CNN architectures can take longer to train.
* Models can suffer from overfitting.
* Low-resolution or visually similar images can be difficult to classify.
* CNN predictions can be difficult to interpret.

---

#  Future Improvements

The model can be improved using:

1. **Data Augmentation**

   Apply random rotation, flipping, zooming, and cropping to increase training data diversity.

2. **Batch Normalization**

   Add Batch Normalization layers to improve training stability and convergence.

3. **Dropout**

   Introduce Dropout to reduce overfitting.

4. **Deeper CNN Architecture**

   Add additional convolutional blocks to learn more complex visual features.

5. **Hyperparameter Tuning**

   Experiment with learning rate, batch size, number of filters, kernel size, and number of epochs.

6. **Transfer Learning**

   Use pretrained architectures such as ResNet, VGG, or MobileNet to potentially achieve better classification performance.

---

#  Project Structure

```text
CNN-Image-Classification/
│
├── CNN_Image_Classification.ipynb
├── README.md
│
├── plots/
   ├── results(graphs and images)

```

---

#  How to Run

### Option 1 — Google Colab

1. Open the `.ipynb` notebook in Google Colab.
2. Select **Runtime → Change runtime type**.
3. Select **GPU** if available.
4. Run the notebook cells sequentially.

### Option 2 — Local Environment

Install the required libraries:

```bash
pip install tensorflow numpy matplotlib scikit-learn
```

Then open the notebook using Jupyter Notebook or JupyterLab.

---

#  Key Takeaway

This project demonstrates the complete workflow of building an image classification system using a Convolutional Neural Network.

The CNN learns visual features directly from CIFAR-10 images and uses these learned representations to classify images into 10 categories. Performance is evaluated using accuracy, loss, confusion matrix, sample predictions, and misclassified images.

The project provides a foundation for exploring more advanced computer vision techniques such as **data augmentation, transfer learning, deeper CNN architectures, and hyperparameter optimization**.


