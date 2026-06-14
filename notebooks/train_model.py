import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("../dataset/WineQT.csv")

# Drop Id column because it is only an identifier, not a useful feature
df = df.drop(columns=["Id"])

# Separate features and target
X = df.drop(columns=["quality"])
y = df["quality"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model 1: Logistic Regression
logistic_model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=2000, class_weight="balanced"))
])

# Model 2: Random Forest
random_forest_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

# Train models
logistic_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)

# Make predictions
logistic_pred = logistic_model.predict(X_test)
random_forest_pred = random_forest_model.predict(X_test)

# Evaluate models
logistic_accuracy = accuracy_score(y_test, logistic_pred)
random_forest_accuracy = accuracy_score(y_test, random_forest_pred)

print("Logistic Regression Accuracy:", logistic_accuracy)
print("Random Forest Accuracy:", random_forest_accuracy)

print("\nLogistic Regression Classification Report:")
print(classification_report(y_test, logistic_pred, zero_division=0))

print("\nRandom Forest Classification Report:")
print(classification_report(y_test, random_forest_pred, zero_division=0))

print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, random_forest_pred))

# Save the better model
os.makedirs("../model", exist_ok=True)

if random_forest_accuracy >= logistic_accuracy:
    best_model = random_forest_model
    best_model_name = "Random Forest"
else:
    best_model = logistic_model
    best_model_name = "Logistic Regression"

joblib.dump(best_model, "../model/wine_quality_model.pkl")
joblib.dump(list(X.columns), "../model/feature_columns.pkl")

print(f"\nBest model saved: {best_model_name}")
print("Model saved to: ../model/wine_quality_model.pkl")
print("Feature columns saved to: ../model/feature_columns.pkl")