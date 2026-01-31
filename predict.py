import pickle
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl')

with open(model_path, 'rb') as f:
    iris_model = pickle.load(f)

def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    """
    Predict iris class and return probabilities
    
    Args:
        sepal_length: Length of sepal in cm
        sepal_width: Width of sepal in cm
        petal_length: Length of petal in cm
        petal_width: Width of petal in cm
    
    Returns:
        prediction: Class index (0, 1, or 2)
        probabilities: Array of probabilities for each class
    """
    features = [sepal_length, sepal_width, petal_length, petal_width]
    
    # Make prediction
    prediction = iris_model.predict([features])[0]
    
    # Get probability scores
    probabilities = iris_model.predict_proba([features])[0]
    
    return prediction, probabilities