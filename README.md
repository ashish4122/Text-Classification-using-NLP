
   DATASET-[IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

  ## Overview

This project involves building a text classification model to categorize input statements as either positive or negative. The model was developed using the **Bag of Words** approach, combined with a **Random Forest Classifier** to achieve robust and accurate predictions.

## Approach

### Bag of Words

The **Bag of Words (BoW)** technique is used to represent text data in a format that machine learning algorithms can process. Each word in the text is treated as a feature, and the frequency of each word is recorded to create a vector that represents the text. This simple yet effective approach allows the model to capture the key characteristics of the text.

### Random Forest Classifier

The **Random Forest Classifier** is a powerful ensemble learning method that combines multiple decision trees to make predictions. It enhances the model's accuracy and generalization capabilities by reducing the risk of overfitting. In this project, the classifier was trained on the BoW vectors to classify the sentiment of the text accurately.

## Results

The model was trained and tested on a dataset of labeled text samples. It demonstrated a significant improvement in accuracy over baseline models, making it a reliable tool for sentiment analysis.

## Future Work

Further improvements could involve exploring advanced techniques like **TF-IDF** or deep learning models such as **LSTM** for more nuanced text representations and potentially higher accuracy.
