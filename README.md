# 🍷 OnemoreSip Analytics

### Machine Learning-Based Wine Quality Prediction System

A web-based machine learning application that predicts wine quality using physicochemical properties such as acidity, alcohol content, sulphates, density, and pH. The system was developed using Python, Scikit-learn, Pandas, and Streamlit.

---

## Project Overview

Wine quality assessment traditionally relies on expert tasting and laboratory analysis. While effective, manual evaluation can be subjective, time-consuming, and difficult to scale.

OnemoreSip Analytics provides a data-driven alternative by using machine learning models trained on physicochemical wine properties to predict wine quality scores automatically.

The system allows users to:

* Explore the wine dataset
* Predict wine quality from user inputs
* Compare machine learning model performance
* Visualize wine quality insights
* Understand feature importance in predictions

---

## Features

### Dashboard

* Dataset overview
* Dataset preview
* Quality score distribution
* Key dataset statistics

### Wine Quality Prediction

* User-friendly prediction form
* Instant wine quality prediction
* Quality category classification

### Model Evaluation

* Logistic Regression vs Random Forest comparison
* Accuracy visualization
* Performance metrics summary

### Wine Insights

* Alcohol vs Quality analysis
* Volatile Acidity vs Quality analysis
* Feature Importance visualization

---

## Technology Stack

### Programming Language

* Python 3.12+ (Recommended)

### Libraries

* Pandas
* Scikit-learn
* Streamlit
* Matplotlib
* Joblib

### Machine Learning Models

* Logistic Regression
* Random Forest Classifier

---

## Project Structure

```text
CI-WineQuality-main
│
├── dataset
│   └── WineQT.csv
│
├── images
│   └── wine.jpg
│
├── model
│   ├── feature_columns.pkl
│   └── wine_quality_model.pkl
│
├── notebooks
│   ├── data_check.py
│   └── train_model.py
│
├── system
│   └── app.py
│
├── README.md
│
└── venv
```

---

## Dataset Information

### Dataset

WineQT.csv

### Records

1,143 wine samples

### Input Features

* Fixed Acidity
* Volatile Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Free Sulfur Dioxide
* Total Sulfur Dioxide
* Density
* pH
* Sulphates
* Alcohol

### Target Variable

```text
quality
```

Wine quality scores range from:

```text
3 - 8
```

---

## Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 45.85%   |
| Random Forest       | 65.50%   |

The Random Forest Classifier achieved the highest accuracy and was selected as the final deployed model.

---

# Installation Guide

## Prerequisites

Install the following software:

### Python

Recommended:

```text
Python 3.12.x
```

Download:
https://www.python.org/downloads/

### Visual Studio Code

Download:
https://code.visualstudio.com/

---

## Step 1 - Clone Repository

```bash
git clone https://github.com/your-username/CI-WineQuality-main.git
```

Or download the ZIP file and extract it manually.

---

## Step 2 - Open Project

Open the project folder using VS Code:

```text
File → Open Folder
```

Select:

```text
CI-WineQuality-main
```

---

## Step 3 - Open Terminal

Open a terminal inside the project folder.

### Recommended

Use:

```text
Command Prompt (CMD)
```

instead of PowerShell.

This avoids common activation and execution policy issues when working with Python virtual environments.

---

## Step 4 - Create Virtual Environment

```cmd
python -m venv venv
```

Wait until the command completes.

Do not interrupt the process.

---

## Step 5 - Activate Virtual Environment

### Windows CMD

```cmd
venv\Scripts\activate
```

Successful activation will display:

```text
(venv) C:\Path\To\Project>
```

---

## Step 6 - Install Required Packages

```cmd
pip install pandas scikit-learn matplotlib streamlit joblib
```

---

## Step 7 - Launch Application

```cmd
streamlit run system\app.py
```

If Streamlit is not recognized:

```cmd
python -m streamlit run system\app.py
```

---

## Step 8 - Open Application

After launching, Streamlit will display:

```text
Local URL: http://localhost:8501
```

Open the URL in your browser.

---

# Troubleshooting

## Virtual Environment Activation Fails

### Error

```text
activate is not recognized
```

### Solution

Ensure you are:

1. Inside the project root folder
2. Using Command Prompt
3. Running:

```cmd
venv\Scripts\activate
```

---

## Streamlit Not Found

### Error

```text
'streamlit' is not recognized
```

### Solution

```cmd
pip install streamlit
```

or

```cmd
python -m streamlit run system\app.py
```

---

## Missing Package Error

### Example

```text
ModuleNotFoundError
```

### Solution

Install required packages:

```cmd
pip install pandas scikit-learn matplotlib streamlit joblib
```

---

## Missing Files Error

Verify the following files exist:

```text
dataset/WineQT.csv
images/wine.jpg
model/wine_quality_model.pkl
model/feature_columns.pkl
system/app.py
```

---

# Machine Learning Workflow

```text
WineQT.csv
        ↓
Data Exploration
        ↓
Data Preprocessing
        ↓
Train Logistic Regression
        ↓
Train Random Forest
        ↓
Compare Performance
        ↓
Select Best Model
        ↓
Save Model (.pkl)
        ↓
Deploy Using Streamlit
        ↓
Predict Wine Quality
```

---

# Future Improvements

Potential enhancements for future versions:

* Hyperparameter tuning
* Additional machine learning models
* Deep learning implementation
* Prediction confidence scores
* Batch CSV prediction
* Export prediction reports
* Improved visual analytics
* Model explainability using SHAP

---

# Academic Purpose

This project was developed as part of a Computer Intelligence / Machine Learning coursework project.

The system demonstrates:

* Data preprocessing
* Model training
* Model evaluation
* Model deployment
* Interactive machine learning applications

---

# Team

### Group Name

**OnemoreSip**

### Members

| Name                          | Role                       |
| ----------------------------- | -------------------------- |
| Khairullah Bin Khairul Hisyam | Project Leader             |
| Akina Aishah Yeap             | System Developer           |
| Hussein Nazif Ar Rifai        | Machine Learning Developer |
| Muhammad Azim Bin Adanan      | Documentation Manager      |

---

## License

This project is intended for educational and research purposes.

