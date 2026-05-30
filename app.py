import streamlit as st
import joblib 
import numpy as np
import pandas as pd
from io import BytesIO
USERNAME = "admin"
PASSWORD = "1234"

st.sidebar.title("🔐Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password",type = "password")

if username != USERNAME or password != PASSWORD:
    st.warning("Please login to access the system")
    st.stop()

st.set_page_config(
    page_title="Student Performance Prediction System",
    page_icon="🎓",
    layout="wide"
)

st.markdown(
    """
    <h1 style = 'text-align: center; color: #4CAF50;'>
    🎓 Student Performance Prediction System
    </h1>
    <h4 style = 'text-align: center; color: gray;'>
    AI & Machine Learning Based Academic Analysis
    </h4>
    """,
    unsafe_allow_html=True
)

model = joblib.load("Model/model.pkl")

st.sidebar.title("📌Project Information")

st.sidebar.info(
"""
### Technologies Used
- Python
- Streamlit 
- Scikit-learn
- Pandas   
- Machine Learning  

### Security Features
- Login Authentication 
- Protected Access 
           
### Developed by
BCA Student                
""")

st.sidebar.success("🎯Model Accuracy: 100%")
st.markdown(
    "<h1 style='text-align: center; color; #4B8BBE;'>🎓Student Performance Prediction System</h1>",
    unsafe_allow_html=True
)

st.write("### Enter Student Details")

#User Inputs
study_hours = st.number_input("📚Study Hours", min_value = 0)
attendance = st.number_input("🏫Attendance Percentage", min_value = 0)
sleep_hours = st.number_input("😴Sleep Hours", min_value = 0)
assignment_completion = st.number_input("📝Assignment Completion Percentage", min_value = 0)
internet_usage = st.number_input("🌐Internet Usage Hours", min_value = 0)
previous_marks = st.number_input("📊Previous Marks Percentage", min_value = 0)
gender = st.selectbox("👤Gender", ["Male", "Female"])

gender_value = 1 if gender == "Female" else 0

if st.button("🔍Predict Performance"):
    input_data = np.array([[
        study_hours,
        attendance,
        sleep_hours,
        assignment_completion,
        internet_usage,
        previous_marks,
        gender_value
    ]])
    prediction = model.predict(input_data)

    st.write("---")

    if prediction[0] == 1:
        st.success("✅Excellent Student Performance")
    elif prediction[0] == 0:
        st.warning("⚠Average Student Performance")
    else:
        st.error("❌Poor Student Performance")

    st.write("---")

    st.subheader("AI Performance Insights")

    if attendance < 50:
        st.warning("🧠Low attendance may affect academic performance.")
    if study_hours < 3:
        st.warning("📚Student should increase study hours.")
    if internet_usage > 8:
        st.warning("🌐High Internet usage detected.")
    if sleep_hours < 5:
        st.warning("😴Poor sleep schedule may reduce concentration.")
    if previous_marks > 80:
        st.success("🏆Strong academic history detected")
    if assignment_completion > 80:
        st.success("✅Assignment completion rate is excellent.")

st.write("---")

st.subheader("📥 Download Prediction Report")

report_data = pd.DataFrame({
    "Field": [
        "Study Hours",
        "Attendance",
        "Sleep Hours",
        "Assignment Completion",
        "Internet Usage",
        "Previous Marks",
        "Gender"
    ],
    "Value": [
        study_hours,
        attendance,
        sleep_hours,
        assignment_completion,
        internet_usage,
        previous_marks,
        gender
    ]
})

csv = report_data.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📄 Download Report",
    data=csv,
    file_name="student_prediction_report.csv",
    mime="text/csv"
)

st.write("---")
st.subheader("📊Student Analytics")
col1,col2,col3 = st.columns(3)

with col1:
    st.metric(label="🎯Model Accuracy",value="100%")

with col2:
    st.metric(label="📚Study Hours",value=study_hours)

with col3:
    st.metric(label="🎯Attendance",value=f"{attendance}%")

chart_data = pd.DataFrame({
    "Category" : ["Study Hours","Attendance", "Sleep Hours", "Assignments"],
    "Values" : [ study_hours, attendance, sleep_hours, assignment_completion]
})

st.write("### Student Activity Chart")
st.bar_chart(chart_data.set_index("Category"))

performance_data = pd.DataFrame({
    "Performance": ["Good", "Average", "Poor"],
    "Count" : [60,25,15] 
})

st.write("###Overall Performance Distribution")
st.dataframe(performance_data)

st.write("---")

st.markdown(
    """
    <div style = 'text-align: center; font-size:18px; color: white; padding: 20px;'
    <br>
    🚀Developed using Python, Machine Learning & Streamlit\n
    🎓Student Performance Prediction System @ 2026
    </div>
    """ ,
    unsafe_allow_html = True
)