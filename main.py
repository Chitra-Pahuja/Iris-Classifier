from flask import Flask, request, jsonify
from predict import predict_iris
import os

app = Flask(__name__)

# Map numeric model output to human-readable class
label_map = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    sepal_length = float(data['sepal_length'])
    sepal_width  = float(data['sepal_width'])
    petal_length = float(data['petal_length'])
    petal_width  = float(data['petal_width'])

    print(sepal_length, sepal_width, petal_length, petal_width)

    # Call model and get prediction + probabilities
    prediction, probabilities = predict_iris(sepal_length, sepal_width, petal_length, petal_width)

    # Convert numeric class to label string for frontend
    try:
        pred_int = int(prediction)
        pred_label = label_map.get(pred_int, str(pred_int))
    except Exception:
        pred_label = str(prediction)

    # Return prediction with confidence scores
    return jsonify({
        'prediction': pred_label,
        'confidence_scores': {
            'Iris-setosa': float(probabilities[0]),
            'Iris-versicolor': float(probabilities[1]),
            'Iris-virginica': float(probabilities[2])
        }
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Iris ML API is running'})

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )