# Mental-health-prediction
Machine learning–based mental health risk prediction using Random Forest with data preprocessing, feature analysis, and Flask-based deployment for real-time predictions.
📌 Mental Health Prediction – Project Overview

This project focuses on predicting mental health risk using machine learning techniques based on survey and behavioral data.

#📊 Dataset
Source: Kaggle
Link: https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset
The dataset contains multiple attributes related to mental health conditions, work environment, and personal factors.
(Dataset file not included in the repository due to size constraints.)
#🧠 Models Used
I experimented with multiple machine learning algorithms:
Naive Bayes
Logistic Regression
Random Forest (Final Model)
Although Naive Bayes and Logistic Regression provided reasonable results, Random Forest achieved higher accuracy and better generalization, so it was selected as the final model.
#📘 What is Random Forest?
Random Forest is an ensemble machine learning algorithm that builds multiple decision trees and combines their outputs to improve prediction accuracy and reduce overfitting. It performs well on complex datasets with nonlinear relationships.
#⚙️ Project Workflow
Data Loading – Dataset imported from Kaggle.
Data Preprocessing – Handling missing values, encoding categorical features, and cleaning data.
Feature Selection & Scaling – Important features identified for better model performance.
Model Training – Naive Bayes, Logistic Regression, and Random Forest models trained and evaluated.
Model Selection – Random Forest chosen based on accuracy and stability.
Model Serialization – Trained model saved as a .pkl file.
API Development – Flask APIs created to serve real-time predictions.
Deployment – Model integrated with a web interface for user input and prediction.
#💾 Why Convert the Model to a Pickle File?
Pickle is used to serialize the trained model.
It allows the model to be saved and reused without retraining.
Essential for deploying the model in production or APIs.
Improves efficiency and response time in real-time applications.
#🔗 API Integration
Flask APIs are used to:
Accept user input
Load the trained pickle model
Return mental health risk predictions in real time
#🚀 Technologies Used
Python
Pandas, NumPy
Scikit-learn
Random Forest, Logistic Regression, Naive Bayes
Flask
Pickle
