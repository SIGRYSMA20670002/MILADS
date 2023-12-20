import streamlit as st
import pandas as pd

# Sample data
data = {
    'id': [842302, 842517, 84300903, 84348301, 84358402],
    'diagnosis': ['M', 'M', 'M', 'M', 'M'],
    'radius_mean': [17.99, 20.57, 19.69, 11.42, 20.29],
    'texture_mean': [10.38, 17.77, 21.25, 20.38, 14.34],
    'perimeter_mean': [122.80, 132.90, 130.00, 77.58, 135.10],
    'area_mean': [1001.0, 1326.0, 1203.0, 386.1, 1297.0],
    'smoothness_mean': [0.11840, 0.08474, 0.10960, 0.14250, 0.10030],
    'compactness_mean': [0.27760, 0.07864, 0.15990, 0.28390, 0.13280],
    'concavity_mean': [0.30010, 0.08690, 0.19740, 0.24140, 0.19800],
    'concave_points_mean': [0.14710, 0.07017, 0.12790, 0.10520, 0.10430],
    # ... add other columns here
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app
def main():
    st.title('Breast Cancer Prediction App')

    # Display the sample data
    st.write('Sample Data:')
    st.write(df)

    # Collect user input
    st.sidebar.header('Input Parameters')
    user_input = {}

    for col in df.columns:
        if col != 'id' and col != 'diagnosis':
            user_input[col] = st.sidebar.number_input(col, min_value=df[col].min(), max_value=df[col].max(), value=df[col].mean())

    st.sidebar.markdown('---')

    if st.sidebar.button('Predict'):
        prediction = predict(user_input)
        st.success(f'The prediction is: {prediction}')

def predict(user_input):
    # Replace this with your actual model prediction logic
    # For example, using a dummy model
    radius_mean = user_input['radius_mean']
    if radius_mean > 15:
         return 'Malignant (Cancer Detected)'
    else:
        return 'Benign (No Cancer Detected)'

if _name_ == '_main_':
    main()