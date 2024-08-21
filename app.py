
from flask import Flask, request, render_template
import pickle

# Load the trained model and vectorizer
model_path = 'random_forest_model1.pkl'
vectorizer_path = 'count_vectorizer.pkl'

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, 'rb') as vectorizer_file:
    cv = pickle.load(vectorizer_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Safely access form data
    user_input = request.form.get('input_text')
    if not user_input:
        return render_template('index.html', prediction_text="No input provided")

    # Preprocess input and predict
    transformed_input = cv.transform([user_input])
    prediction = model.predict(transformed_input)
    output = 'Positive' if prediction[0] == 1 else 'Negative'

    return render_template('index.html', prediction_text=f'Prediction: {output}')

if __name__ == "__main__":
    app.run(debug=True)
