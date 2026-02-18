# 💳 Elif Bank – Credit Risk Decision System

A machine learning-based web application that evaluates credit applications and estimates default risk using logistic regression.

This project simulates a real-world banking credit scoring system developed as part of a data analytics and risk modeling study.

---

## Project Overview

The Elif Bank Credit Risk Decision System is an interactive web application built with **Streamlit**.  

It allows users to input applicant financial and demographic information and returns:

- Estimated default probability
- Decision threshold
- Credit approval / rejection result

The system is powered by a trained **Logistic Regression pipeline**.

---

## Model Details

- Algorithm: Logistic Regression
- Output: Probability of Default (PD)
- Decision Rule:  
  - If PD ≥ 37% → Reject  
  - If PD < 37% → Approve
- Threshold optimized for cost-sensitive credit risk evaluation
- Feature Engineering:
  - Loan-to-Income Ratio calculated dynamically inside the application
---
## Model Performance

The model was evaluated using classification metrics:

- Accuracy: (write your value)
- Precision: (write your value)
- Recall: (write your value)
- ROC-AUC: (write your value)

The decision threshold (37%) was selected to balance credit approval rate and risk exposure.

---
## 💼 Business Interpretation

This system simulates a real-world banking credit scoring process.

By estimating Probability of Default (PD), the model helps reduce credit risk exposure and supports data-driven lending decisions.

Threshold tuning allows balancing between:
- Risk reduction
- Loan approval rate
- Portfolio quality control

---

## Features Used

The model evaluates applicants based on:

- Age
- Annual Income
- Home Ownership Status
- Employment Length
- Loan Purpose
- Loan Amount
- Interest Rate
- Loan-to-Income Ratio (calculated automatically)
- Previous Default History
- Credit History Length

---

## Tech Stack

- Python
- scikit-learn
- pandas
- joblib
- Streamlit

---
##  My Contribution

- Performed data preprocessing and feature encoding
- Built a Logistic Regression pipeline using scikit-learn
- Optimized decision threshold for risk-sensitive classification
- Developed an interactive Streamlit web interface
- Integrated trained model into production-ready app structure

---


## How to Run Locally

1. Clone the repository:
   git clone https://github.com/elifeda/credit-risk-decision-app.git
cd credit-risk-decision-app
2. Install dependencies: pip install streamlit scikit-learn pandas joblib
3. Run the app: streamlit run app.py
4. Open your browser and go to:

   http://localhost:8501

⚠️ Make sure the model file `credit_risk_pipeline.joblib` is in the root directory before running the app.
---

## Author

Elif Eda Kul  
Mathematics Student – Data Analytics & Risk Modeling
