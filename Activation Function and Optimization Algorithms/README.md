## Objective

To analyze the impact of different activation functions and optimization
algorithms on the performance of Artificial Neural Networks (ANNs) and to
learn best practices for managing deep learning experiments using
cloud-based tools and version control.

## Software Requirements

- Python
- TensorFlow
- Google Colab
- Google Drive
- GitHub
- NumPy
- Pandas
- Matplotlib

## Experiments

### Task A - Activation Function Visualization

The following activation functions were implemented and visualized:

- Sigmoid
- Tanh
- ReLU

Their output range, saturation regions, gradient behavior,
computational efficiency, and typical applications were compared.

**Notebook:** `visualization.ipynb`

### Task B - Performance Comparison of Activation Functions

Identical Artificial Neural Network architectures were trained using:

- Sigmoid
- Tanh
- ReLU

Training accuracy, validation accuracy, training loss,
validation loss, and convergence behavior were compared.

**Notebook:** `performance.ipynb`

### Task C - Comparison of Optimization Algorithms

The same ANN architecture was trained using:

- SGD
- Momentum
- RMSProp
- Adam

Training loss, validation loss, convergence speed, training accuracy,
and validation accuracy were compared.

**Notebook:** `comparison.ipynb`

## Dataset

The MNIST handwritten digit dataset was used for the experiments.

The dataset contains grayscale images of handwritten digits from 0 to 9,
with each image having a size of 28 × 28 pixels.

## Experiment Management

Google Colab was used as a cloud-based environment for running
deep learning experiments.

Google Drive was used for persistent storage of notebooks,
trained models, and experiment results.

GitHub was used for storing the experiment notebooks,
documenting the experiments, and maintaining version history
through Git commits.

## Repository Structure

```text
deep-learning-experiments/
│
├── README.md
│
└── notebooks/
    ├── visualization.ipynb
    ├── performance.ipynb
    └── comparison.ipynb
