# Resume Parser

A beginner-friendly, modular Deep Learning application designed to recognize handwritten digits using the famous MNIST dataset. This project provides a hands-on introduction to neural networks using TensorFlow/Keras.

## 🚀 Features
- **Automated Dataset Handling:** Seamlessly downloads and prepares the MNIST dataset for training.

- **Neural Network Architecture:** Implements a multi-layer perceptron with Flatten, Dense, and Softmax output layers.

- **Model Persistence:** Trains the model and saves it as a .keras file for future use.

- **Interactive Prediction:** A terminal-based menu to test the model on specific images from the test set.

- **Image Visualization:** Uses Matplotlib to display the actual digits and verify model predictions.
## 📂 Project Structure
```text
Resume_Parser/
│
├── main.py              # Application entry point and menu
├── parser.py            # Handles file reading and orchestration
├── extractor.py         # Core logic using Regex and string matching
├── sample_resume.txt    # Sample resume file for testing
├── requirements.txt     # List of project dependencies
├── .gitignore
└── README.md            # Project documentation
