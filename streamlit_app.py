import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Iris Classifier Pro",
    page_icon="flower",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS FOR MODERN STYLING
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        height: 50px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .title-main {
        text-align: center;
        color: #667eea;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# SESSION STATE FOR HISTORY
if 'prediction_history' not in st.session_state:
    st.session_state.prediction_history = []

# SIDEBAR CONFIGURATION
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/1200px-Iris_versicolor_3.jpg", 
             caption="Iris Versicolor", use_column_width=True)
    
    st.title("About This App")
    st.info(
        """
        Iris Species Classifier Pro
        
        Advanced ML model for predicting iris flower species based on measurements.
        
        Species:
        - Setosa - Smaller, delicate flowers
        - Versicolor - Medium-sized flowers
        - Virginica - Larger, robust flowers
        
        Features Analyzed:
        - Sepal length and width
        - Petal length and width
        """
    )
    
    st.divider()
    st.caption("Enhanced with Confidence Scores and Visualizations")

# MAIN HEADER
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1 style='text-align: center; color: #667eea;'>Iris Species Predictor Pro</h1>", 
                unsafe_allow_html=True)

st.markdown("**Adjust the measurements below to classify the iris flower.**", unsafe_allow_html=True)
st.divider()

# CREATE TABS
tab1, tab2, tab3 = st.tabs(["Prediction", "Statistics", "History"])

# TAB 1: PREDICTION
with tab1:
    # Input section with better layout
    st.subheader("Flower Measurements")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        sepal_length = st.slider('Sepal Length in cm', 4.0, 8.0, 5.5, step=0.1)
    with col2:
        sepal_width = st.slider('Sepal Width in cm', 2.0, 4.5, 3.0, step=0.1)
    with col3:
        petal_length = st.slider('Petal Length in cm', 1.0, 7.0, 4.0, step=0.1)
    with col4:
        petal_width = st.slider('Petal Width in cm', 0.1, 2.5, 1.3, step=0.1)
    
    st.divider()
    
    # Prediction button
    col_button1, col_button2, col_button3 = st.columns([1, 2, 1])
    with col_button2:
        predict_button = st.button('Classify Iris', use_container_width=True)
    
    if predict_button:
        with st.spinner('Analyzing flower measurements...'):
            data = {
                'sepal_length': sepal_length,
                'sepal_width': sepal_width,
                'petal_length': petal_length,
                'petal_width': petal_width
            }
            
            try:
                # API Call - Update this with your Cloud Run URL
                API_URL = "https://iris-app-1091239832875.us-east1.run.app"
                response = requests.post(f'{API_URL}/predict', json=data, timeout=10)
                
                if response.status_code == 200:
                    result = response.json()
                    prediction = result['prediction']
                    confidence_scores = result.get('confidence_scores', {})
                    
                    # Add to history
                    st.session_state.prediction_history.append({
                        'timestamp': datetime.now(),
                        'prediction': prediction,
                        'sepal_length': sepal_length,
                        'sepal_width': sepal_width,
                        'petal_length': petal_length,
                        'petal_width': petal_width,
                        'confidence': confidence_scores
                    })
                    
                    # Success message
                    st.success(f"Classified as: {prediction}")
                    
                    # Display prediction with columns
                    pred_col1, pred_col2 = st.columns([1, 2])
                    
                    # Image mapping
                    images = {
                        "Iris-setosa": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/640px-Kosaciec_szczecinkowaty_Iris_setosa.jpg",
                        "Iris-versicolor": "https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg",
                        "Iris-virginica": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1200px-Iris_virginica_2.jpg"
                    }
                    
                    with pred_col1:
                        img_url = images.get(prediction, images["Iris-versicolor"])
                        st.image(img_url, use_column_width=True, caption=f"This is a {prediction}")
                    
                    with pred_col2:
                        st.markdown(f"### It is an {prediction}")
                        st.markdown(f"""
                        Input Measurements:
                        - Sepal: {sepal_length} times {sepal_width} cm
                        - Petal: {petal_length} times {petal_width} cm
                        """)
                    
                    st.divider()
                    
                    # Confidence Scores Section
                    if confidence_scores:
                        st.subheader("Model Confidence Analysis")
                        
                        # Create bar chart with Plotly
                        fig = go.Figure(data=[
                            go.Bar(
                                x=list(confidence_scores.keys()),
                                y=list(confidence_scores.values()),
                                marker=dict(
                                    color=['#667eea' if k == prediction else '#d3d3d3' 
                                           for k in confidence_scores.keys()],
                                    line=dict(color='#333', width=2)
                                ),
                                text=[f'{v:.1%}' for v in confidence_scores.values()],
                                textposition='outside',
                                textfont=dict(size=14, color='black', family='Arial Black')
                            )
                        ])
                        
                        fig.update_layout(
                            title="Model Confidence Scores by Class",
                            xaxis_title="Iris Species",
                            yaxis_title="Confidence Score",
                            yaxis=dict(range=[0, 1.0]),
                            height=400,
                            showlegend=False,
                            template="plotly_white",
                            font=dict(size=12)
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Confidence metrics
                        col1, col2, col3 = st.columns(3)
                        for i, (species, score) in enumerate(confidence_scores.items()):
                            with [col1, col2, col3][i]:
                                st.metric(
                                    species.replace("Iris-", ""),
                                    f"{score:.1%}",
                                    delta=f"{score*100:.1f}" if score > 0.5 else None
                                )
                        
                        st.balloons()
                else:
                    st.error(f'Server Error: {response.status_code}')
                    
            except requests.exceptions.RequestException as e:
                st.error('Connection Error: Could not reach the prediction service.')
                st.info("Make sure the API is deployed and the URL is correct in the code.")

# TAB 2: STATISTICS
with tab2:
    st.subheader("Input Data Statistics")
    
    # Create sample data visualization
    iris_ranges = pd.DataFrame({
        'Feature': ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'],
        'Min': [4.3, 2.0, 1.0, 0.1],
        'Max': [7.9, 4.4, 6.9, 2.5],
        'Mean': [5.8, 3.0, 3.8, 1.2]
    })
    
    st.dataframe(iris_ranges, use_container_width=True)
    
    # Visualization of ranges
    st.subheader("Feature Ranges")
    fig = go.Figure()
    
    for idx, row in iris_ranges.iterrows():
        fig.add_trace(go.Bar(
            name=row['Feature'],
            x=['Min', 'Mean', 'Max'],
            y=[row['Min'], row['Mean'], row['Max']],
            marker=dict(color=['#ff6b6b', '#667eea', '#51cf66'])
        ))
    
    fig.update_layout(
        title="Iris Feature Statistics",
        barmode='group',
        height=400,
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""
    Dataset Info:
    - Total Samples: 150
    - Features: 4 (Sepal Length, Sepal Width, Petal Length, Petal Width)
    - Classes: 3 (Setosa, Versicolor, Virginica)
    - Training Accuracy: approximately 96 percent
    """)

# TAB 3: HISTORY
with tab3:
    st.subheader("Prediction History")
    
    if st.session_state.prediction_history:
        # Display history as dataframe
        history_data = []
        for pred in st.session_state.prediction_history:
            history_data.append({
                'Time': pred['timestamp'].strftime("%H:%M:%S"),
                'Prediction': pred['prediction'],
                'Sepal Length': f"{pred['sepal_length']:.2f}",
                'Sepal Width': f"{pred['sepal_width']:.2f}",
                'Petal Length': f"{pred['petal_length']:.2f}",
                'Petal Width': f"{pred['petal_width']:.2f}",
            })
        
        history_df = pd.DataFrame(history_data)
        st.dataframe(history_df, use_container_width=True)
        
        # Clear history button
        if st.button('Clear History'):
            st.session_state.prediction_history = []
            st.rerun()
    else:
        st.info("No predictions yet. Make a prediction to see history!")

st.divider()
st.caption("Customized Iris Classifier - Enhanced Dashboard with Confidence Scores and Visualizations")