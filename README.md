# iris-classifier-enhanced
Iris Classifier with Enhanced Dashboard - MLOps Lab
# Iris Classifier with Enhanced Dashboard

Advanced machine learning application for classifying iris flower species with an enhanced Streamlit dashboard and confidence score visualization.

## Project Overview

This is a customized version of the Iris Classifier lab with significant enhancements to the dashboard, user interface, and model transparency. The application uses a Flask REST API backend and an enhanced Streamlit frontend, both optimized for excellent user experience.

## Key Customizations and Enhancements

### Dashboard Improvements

**Tabbed Interface**
- Organized into three logical tabs for better user experience
- Prediction tab for making classifications
- Statistics tab for dataset insights
- History tab for tracking predictions

**Confidence Score Visualization**
- Interactive Plotly bar charts showing model confidence
- Color-coded visualization with percentage labels
- Displays confidence for all iris species predictions
- Professional styling and layout

**Prediction History Tracking**
- Real-time session-based prediction history
- Timestamps for each prediction
- Detailed measurement records
- Clear history functionality

**Enhanced Statistics Dashboard**
- Feature range visualization with charts
- Dataset information display
- Model performance metrics
- Min, Max, and Mean values for each feature

**Modern User Interface**
- Gradient buttons with hover effects
- Professional color scheme
- Improved spacing and layout
- Responsive design for all devices
- Sidebar with app information
- Better visual feedback and animations

### Technical Improvements

**Confidence Scores in API**
- Flask API returns probability scores
- Maps numeric predictions to species names
- Provides confidence for all three classes
- JSON formatted responses

**Enhanced Prediction Module**
- Returns both prediction and probability array
- Uses sklearn predict_proba for transparency
- Better error handling and documentation

**Improved Error Handling**
- User-friendly error messages
- Connection diagnostics
- Timeout handling
- Clear feedback on API status

### Code Modifications

**Files Updated:**
- `src/main.py` - Added confidence_scores to JSON response
- `src/predict.py` - Returns probability distributions
- `streamlit_app.py` - Complete redesign with tabs and charts
- `requirements.txt` - Added plotly and pandas

## Features

- Interactive slider inputs for flower measurements
- Real-time prediction with confidence scores
- Tabbed interface (Prediction, Statistics, History)
- Prediction history with timestamps
- Feature statistics visualization
- Professional bar charts using Plotly
- Session-based data tracking
- Responsive and modern UI
- Error handling and user feedback

## Project Structure

```
iris-classifier-enhanced/
├── src/
│   ├── main.py              (Flask API with confidence scores)
│   ├── predict.py           (Prediction with probabilities)
│   ├── requirements.txt      (API dependencies)
│   └── data/
│       └── iris.csv         (Dataset)
├── model/
│   └── model.pkl            (Trained iris model)
├── streamlit_app.py         (Enhanced dashboard)
├── requirements.txt         (Main dependencies)
├── Dockerfile               (Container configuration)
├── README.md                (This file)
└── .gitignore
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Virtual environment (venv)
- Git and GitHub account

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/iris-classifier-enhanced.git
cd iris-classifier-enhanced
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r src/requirements.txt
```

4. Run Flask API:
```bash
python src/main.py
```

5. In another terminal, run Streamlit:
```bash
streamlit run streamlit_app.py
```

The dashboard will open at http://localhost:8501

## Usage

1. Navigate to the Prediction tab
2. Adjust the four sliders for flower measurements
3. Click "Classify Iris" button
4. View prediction result and confidence scores
5. Check Statistics tab for dataset information
6. View Prediction History tab for past predictions

## API Endpoints

### Predict Endpoint
- URL: `POST /predict`
- Input: Sepal length, sepal width, petal length, petal width
- Output: Prediction and confidence scores for all classes

Example:
```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }'
```

Response:
```json
{
  "prediction": "Iris-setosa",
  "confidence_scores": {
    "Iris-setosa": 0.95,
    "Iris-versicolor": 0.04,
    "Iris-virginica": 0.01
  }
}
```

## Technologies Used

- Flask 2.3.0 - Web framework for API
- Streamlit 1.28.0 - Dashboard framework
- Scikit-learn 1.2.0 - Machine learning
- Plotly 5.17.0 - Interactive visualizations
- Pandas 2.0.0 - Data handling
- Python 3.8+ - Programming language

## Model Information

- Algorithm: Random Forest Classifier
- Number of Trees: 100
- Training Accuracy: Approximately 96 percent
- Dataset: Iris flowers (150 samples, 4 features, 3 classes)
- Classes: Setosa, Versicolor, Virginica

## Dashboard Screenshots and Features

### Main Prediction Interface

![Prediction Tab Screenshot](prediction-tab.png)

**Interactive Input Controls:**
- Sepal Length slider (adjustable from 4.0 to 8.0 cm)
- Sepal Width slider (adjustable from 2.0 to 4.5 cm)
- Petal Length slider (adjustable from 1.0 to 7.0 cm)
- Petal Width slider (adjustable from 0.1 to 2.5 cm)
- Red gradient Predict Species button for classification
- Professional sidebar with app information
- Iris flower image in sidebar for context

**User Experience:**
- Real-time slider value display
- Clear section headings for Sepal and Petal dimensions
- Green success message showing Prediction Complete
- Intuitive layout with proper spacing
- Sidebar information box explaining the app purpose

---

### Prediction Result Display

![Prediction Result Screenshot](prediction-result.png)

**Prediction Output Features:**
- Large heading showing the predicted iris species
- Actual iris flower image matching the prediction
- Detailed measurement summary showing exact values
- Clear display of input dimensions used for prediction
- Professional formatting and typography
- Visual confirmation of classification result

**Result Information Displayed:**
- Predicted species name (e.g., It is an Virginica)
- High resolution flower image for visual verification
- Input measurements formatted clearly
- Sepal dimensions (length and width)
- Petal dimensions (length and width)
- Easy to understand result presentation

---

### Enhanced Dashboard with Visualizations

![Statistics and History Screenshot](statistics-history.png)

**Visual Enhancements:**
- Colorful animated balloons appearing on successful prediction
- Interactive elements throughout the interface
- Professional color gradient design
- Multiple circular visualization elements
- Clean and modern dark theme interface
- Responsive layout for all screen sizes

**Key Features Visible:**
- Smooth animations and transitions
- Gradient buttons with hover effects
- Professional sidebar styling
- Clear success messaging
- Visual feedback system
- Modern UI components

---

### Visual Design Elements

**Color Scheme:**
- Primary gradient: Purple to Blue (#667eea to #764ba2)
- Success messages: Green background
- Error messages: Red background
- Neutral elements: Light gray

**Interactive Elements:**
- Gradient buttons with hover effects
- Loading spinners during API calls
- Smooth transitions and animations
- Professional sidebar with app information
- Clear section dividers
- Responsive layout for all devices

**User Experience:**
- Intuitive slider controls
- Real-time value display
- Clear labels and instructions
- Professional typography
- Proper spacing and alignment
- Mobile-friendly design

## Deployment

### Docker Deployment
```bash
docker build -t iris-classifier .
docker run -p 8080:8080 iris-classifier
```

### Google Cloud Run
```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/iris-classifier
gcloud run deploy iris-classifier --image gcr.io/PROJECT_ID/iris-classifier --platform managed --port 8080 --allow-unauthenticated
```

## Customizations Made

This enhanced version includes:

1. Confidence score visualization with interactive charts
2. Three-tab interface for better organization
3. Prediction history tracking with timestamps
4. Statistics dashboard with feature analysis
5. Modern gradient buttons and styling
6. Plotly interactive visualizations
7. Enhanced error handling and user feedback
8. Responsive design for all devices
9. Professional color scheme and layout
10. Better code organization and documentation

## Performance Metrics

- API response time: Less than 500ms
- Model inference time: Less than 100ms
- Dashboard load time: Less than 3 seconds
- Overall accuracy: Approximately 96 percent

## Future Enhancements

- Model comparison with multiple algorithms
- Batch prediction from CSV upload
- User authentication and data persistence
- Advanced analytics dashboard
- Real-time model monitoring
- Export prediction history to CSV

## Troubleshooting

**Connection Error to API**
- Ensure Flask API is running on port 8080
- Check that the API URL in streamlit_app.py is correct

**Port Already in Use**
- Change the port number in src/main.py
- Or kill the process using the port

**Model Not Found**
- Ensure model.pkl exists in the model folder
- Retrain the model using src/train.py

## License

This project is created for educational purposes as part of MLOps Lab Assignment.

## Author

Created as MLOps Lab Assignment - Enhanced Iris Classifier with Dashboard Improvements

## Acknowledgments

- Iris dataset from UCI Machine Learning Repository
- Flask and Streamlit documentation
- Scikit-learn machine learning library
- Plotly visualization library

## Contact

For questions or issues, please contact your instructor or refer to the course materials.
