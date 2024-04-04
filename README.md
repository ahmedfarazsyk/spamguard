# Spam Classification App using Streamlit (SpamGuard)

This project is a simple web application built with Streamlit that classifies text messages as spam or not spam using machine learning techniques.

## Overview

The application uses a Voting Classifier with three different estimators:
- Support Vector Classifier (SVC)
- Multinomial Naive Bayes (MultinomialNB)
- Extra Trees Classifier (ExtraTreesClassifier)

The model has been trained on a dataset and achieves high accuracy and precision scores (Accuracy: 0.9860681114551083, Precision: 0.984646878198567).

## Features

- Input text message into the app and get instant classification result.
- Easy to use interface.

## Installation

To run this application locally, follow these steps:

1. Clone this repository:
git clone <repository_url>

2. Navigate to the project directory:
cd spamguard

3. Install the required Python packages:
pip install -r requirements.txt

4. Run the Streamlit app:
streamlit run app.py

5. Access the app in your web browser at `http://localhost:8501`.

## Usage

- Input a text message into the provided text box.
- Click on the "Predict" button to get the classification result.

## File Structure

- `app.py`: Main Streamlit application script.
- `requirements.txt`: List of Python dependencies.
- `vectorizer.pkl`: Tfidf Vectorizer to vectorize your textual input.
- `voting.pkl`: Pre-trained machine learning model.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.


