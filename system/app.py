import base64
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# ===================== PAGE SETUP =====================
st.set_page_config(
    page_title="OnemoreSip Analytics",
    page_icon="🍷",
    layout="wide"
)


# ===================== FILE PATHS =====================
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "dataset" / "WineQT.csv"
MODEL_PATH = BASE_DIR / "model" / "wine_quality_model.pkl"
FEATURE_PATH = BASE_DIR / "model" / "feature_columns.pkl"
IMAGE_PATH = BASE_DIR / "images" / "wine.jpg"


# ===================== LOAD FILES =====================
@st.cache_data
def load_dataset():
    return pd.read_csv(DATA_PATH)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_data
def load_features():
    return joblib.load(FEATURE_PATH)


df = load_dataset()
model = load_model()
feature_columns = load_features()

df_display = df.drop(columns=["Id"]) if "Id" in df.columns else df.copy()


# ===================== HELPER FUNCTIONS =====================
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


def get_quality_category(score):
    if score <= 4:
        return "Low Quality", "Needs improvement", "#8b1e3f"
    elif score <= 6:
        return "Average Quality", "Acceptable wine quality", "#b76e22"
    elif score == 7:
        return "Good Quality", "Good wine quality", "#2f7d32"
    else:
        return "Premium Quality", "Excellent wine quality", "#5b2c83"


def show_metric_card(title, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <p class="metric-title">{title}</p>
            <h2 class="metric-value">{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_title(title, subtitle=None):
    st.markdown(f"<h2 class='page-title'>{title}</h2>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='page-subtitle'>{subtitle}</p>", unsafe_allow_html=True)


# ===================== HERO BACKGROUND =====================
if IMAGE_PATH.exists():
    image_base64 = image_to_base64(IMAGE_PATH)
    hero_background = f"""
        background-image:
        linear-gradient(rgba(8, 4, 5, 0.84), rgba(8, 4, 5, 0.84)),
        url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
    """
else:
    hero_background = "background: linear-gradient(135deg, #3b0d17, #7b1e3a);"


# ===================== CUSTOM CSS =====================
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: #f7f2ef;
        }}

        .block-container {{
            padding-top: 3rem;
            padding-bottom: 3rem;
        }}

        .block-container h1,
        .block-container h2,
        .block-container h3,
        .block-container h4,
        .block-container p,
        .block-container label,
        .block-container span {{
            color: #2b1d1d !important;
        }}

        section[data-testid="stSidebar"] {{
            background-color: #2f0d14;
        }}

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] div {{
            color: white !important;
        }}

        .hero {{
            {hero_background}
            border-radius: 22px;
            padding: 70px 50px;
            margin-bottom: 35px;
            box-shadow: 0 10px 28px rgba(0,0,0,0.22);
        }}

        .hero .hero-title {{
            color: #fff3ff !important;
            font-size: 52px;
            font-weight: 950;
            margin-bottom: 18px;
            letter-spacing: 0.5px;
            text-shadow:
                0px 0px 8px rgba(255, 255, 255, 0.45),
                0px 0px 18px rgba(255, 230, 255, 0.35),
                4px 4px 14px rgba(0, 0, 0, 1);
        }}

        .hero .hero-description {{
            color: #ffffff !important;
            font-size: 19px;
            line-height: 1.7;
            max-width: 900px;
            font-weight: 650;
            text-shadow:
                0px 0px 6px rgba(255, 255, 255, 0.25),
                3px 3px 10px rgba(0, 0, 0, 1);
        }}

        .page-title {{
            font-size: 32px;
            font-weight: 850;
            color: #3b0d17 !important;
            margin-top: 10px;
            margin-bottom: 5px;
        }}

        .page-subtitle {{
            color: #6b5b5b !important;
            font-size: 16px;
            margin-bottom: 25px;
        }}

        .metric-card {{
            background: white;
            padding: 22px;
            border-radius: 18px;
            box-shadow: 0 6px 16px rgba(0,0,0,0.08);
            border-left: 6px solid #7b1e3a;
            margin-bottom: 20px;
        }}

        .metric-title {{
            font-size: 15px;
            font-weight: 700;
            color: #6b5b5b !important;
            margin-bottom: 8px;
        }}

        .metric-value {{
            font-size: 34px;
            font-weight: 850;
            color: #7b1e3a !important;
            margin: 0;
        }}

        .content-card {{
            background: white;
            padding: 24px;
            border-radius: 18px;
            box-shadow: 0 6px 16px rgba(0,0,0,0.08);
            margin-top: 20px;
            margin-bottom: 20px;
        }}

        .content-card h3 {{
            color: #3b0d17 !important;
            margin-bottom: 8px;
        }}

        .content-card p {{
            color: #4a3b3b !important;
            font-size: 16px;
            line-height: 1.6;
        }}

        .result-box {{
            padding: 28px;
            border-radius: 20px;
            margin-top: 25px;
            box-shadow: 0 8px 22px rgba(0,0,0,0.15);
        }}

        .result-box h2,
        .result-box h3,
        .result-box p {{
            color: white !important;
        }}

        .result-score {{
            font-size: 42px;
            font-weight: 900;
            margin-bottom: 8px;
        }}

        .result-category {{
            font-size: 24px;
            font-weight: 750;
            margin-bottom: 8px;
        }}

        .stButton > button {{
            background-color: #7b1e3a;
            color: white !important;
            border: none;
            border-radius: 12px;
            padding: 12px 28px;
            font-weight: 750;
            font-size: 16px;
        }}

        .stButton > button:hover {{
            background-color: #5f162d;
            color: white !important;
        }}

        .stNumberInput label {{
            color: #2b1d1d !important;
            font-weight: 700;
        }}

        div[data-testid="stDataFrame"] {{
            border-radius: 14px;
            overflow: hidden;
        }}

        .stAlert p {{
            color: inherit !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


# ===================== HERO SECTION =====================
st.markdown(
    """
    <div class="hero">
        <h1 class="hero-title">OnemoreSip Analytics</h1>
        <p class="hero-description">
            A smart wine quality prediction that analyzes physicochemical properties
            such as alcohol, acidity, sugar level, sulphates, density, and pH to predict wine quality.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ===================== SIDEBAR =====================
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Predict Wine Quality", "Model Evaluation", "Wine Insights"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Project Info")
st.sidebar.markdown("**Group Name:** OnemoreSip")
st.sidebar.markdown("**Project:** Wine Quality Prediction")
st.sidebar.markdown("**Dataset:** WineQT.csv")
st.sidebar.markdown("**Best Model:** Random Forest")
st.sidebar.markdown("**Accuracy:** 65.50%")


# ===================== DASHBOARD PAGE =====================
if menu == "Dashboard":
    section_title(
        "Dashboard",
        "Overview of the wine quality dataset used for model training and analysis."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        show_metric_card("Total Samples", len(df))

    with col2:
        show_metric_card("Input Features", len(feature_columns))

    with col3:
        show_metric_card("Average Quality", round(df["quality"].mean(), 2))

    with col4:
        show_metric_card("Quality Range", f"{df['quality'].min()} - {df['quality'].max()}")

    st.markdown(
        """
        <div class="content-card">
            <h3>Dataset Summary</h3>
            <p>
                The dataset contains physicochemical properties of wine samples.
                The target variable is the wine quality score, which ranges from 3 to 8 in this dataset.
                The Id column is removed during model training because it is only an identifier.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Wine Quality Distribution")
    quality_counts = df["quality"].value_counts().sort_index()
    st.bar_chart(quality_counts)

    st.info(
        "Most samples are rated 5 and 6, while very few samples are rated 3 and 8. "
        "This means the dataset is slightly imbalanced."
    )


# ===================== PREDICTION PAGE =====================
elif menu == "Predict Wine Quality":
    section_title(
        "Predict Wine Quality",
        "Enter the wine chemical properties and let the trained model estimate its quality score."
    )

    st.markdown(
        """
        <div class="content-card">
            <h3>How This Prediction Works</h3>
            <p>
                The system uses a trained Random Forest classification model.
                After the user enters the wine properties, the model predicts a quality score
                and converts it into an easy-to-understand category.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    input_data = {}

    col1, col2 = st.columns(2)

    with col1:
        input_data["fixed acidity"] = st.number_input("Fixed Acidity", value=7.40, format="%.2f")
        input_data["volatile acidity"] = st.number_input("Volatile Acidity", value=0.70, format="%.2f")
        input_data["citric acid"] = st.number_input("Citric Acid", value=0.00, format="%.2f")
        input_data["residual sugar"] = st.number_input("Residual Sugar", value=1.90, format="%.2f")
        input_data["chlorides"] = st.number_input("Chlorides", value=0.076, format="%.3f")
        input_data["free sulfur dioxide"] = st.number_input("Free Sulfur Dioxide", value=11.0, format="%.1f")

    with col2:
        input_data["total sulfur dioxide"] = st.number_input("Total Sulfur Dioxide", value=34.0, format="%.1f")
        input_data["density"] = st.number_input("Density", value=0.9978, format="%.4f")
        input_data["pH"] = st.number_input("pH", value=3.51, format="%.2f")
        input_data["sulphates"] = st.number_input("Sulphates", value=0.56, format="%.2f")
        input_data["alcohol"] = st.number_input("Alcohol", value=9.40, format="%.2f")

    if st.button("Predict Wine Quality"):
        input_df = pd.DataFrame([input_data])
        input_df = input_df[feature_columns]

        prediction = model.predict(input_df)[0]
        category, description, badge_color = get_quality_category(prediction)

        st.markdown(
            f"""
            <div class="result-box" style="background: linear-gradient(135deg, {badge_color}, #2f0d14);">
                <p class="result-score">{prediction} / 10</p>
                <p class="result-category">{category}</p>
                <p>{description}</p>
                <p>
                    This prediction is based on the wine's physicochemical properties
                    using the trained Random Forest model.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ===================== MODEL EVALUATION PAGE =====================
elif menu == "Model Evaluation":
    section_title(
        "Model Evaluation",
        "Comparison of the machine learning models tested in this project."
    )

    st.markdown(
        """
        <div class="content-card">
            <h3>Evaluation Summary</h3>
            <p>
                Two classification models were tested: Logistic Regression and Random Forest.
                Random Forest performed better and was selected as the final model for the system.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    results = pd.DataFrame({
        "Model": ["Logistic Regression", "Random Forest"],
        "Accuracy": [0.4585, 0.6550],
        "Accuracy (%)": ["45.85%", "65.50%"]
    })

    st.subheader("Model Accuracy Table")
    st.dataframe(results, use_container_width=True)

    st.subheader("Accuracy Comparison")
    chart_data = pd.DataFrame({
        "Accuracy": [0.4585, 0.6550]
    }, index=["Logistic Regression", "Random Forest"])

    st.bar_chart(chart_data)

    col1, col2, col3 = st.columns(3)

    with col1:
        show_metric_card("Best Model", "Random Forest")

    with col2:
        show_metric_card("Accuracy", "65.50%")

    with col3:
        show_metric_card("Weighted F1", "0.65")

    st.markdown(
        """
        <div class="content-card">
            <h3>Why Random Forest Was Chosen</h3>
            <p>
                Random Forest achieved higher accuracy than Logistic Regression.
                It also performed better overall based on weighted precision, recall,
                and F1-score. Therefore, it was selected as the final prediction model.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    performance = pd.DataFrame({
        "Metric": ["Precision", "Recall", "F1-Score"],
        "Weighted Average": [0.66, 0.66, 0.65]
    })

    st.subheader("Random Forest Performance Summary")
    st.dataframe(performance, use_container_width=True)


# ===================== WINE INSIGHTS PAGE =====================
elif menu == "Wine Insights":
    section_title(
        "Wine Insights",
        "Simple analysis of wine properties and their relationship with wine quality."
    )

    st.markdown(
        """
        <div class="content-card">
            <h3>Insight Overview</h3>
            <p>
                This section helps explain the dataset visually.
                It shows how selected physicochemical properties change across different quality scores.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Average Alcohol by Quality Score")
    alcohol_quality = df.groupby("quality")["alcohol"].mean()
    st.bar_chart(alcohol_quality)

    st.markdown(
        """
        <div class="content-card">
            <p>
                Wines with higher quality scores usually show higher average alcohol content
                in this dataset.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Average Volatile Acidity by Quality Score")
    acidity_quality = df.groupby("quality")["volatile acidity"].mean()
    st.bar_chart(acidity_quality)

    st.markdown(
        """
        <div class="content-card">
            <p>
                Volatile acidity affects wine taste. In this dataset, lower volatile acidity
                is generally linked with better wine quality.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if hasattr(model, "feature_importances_"):
        st.subheader("Feature Importance")

        importance_df = pd.DataFrame({
            "Feature": feature_columns,
            "Importance": model.feature_importances_
        }).sort_values(by="Importance", ascending=False)

        st.dataframe(importance_df, use_container_width=True)
        st.bar_chart(importance_df.set_index("Feature"))

        st.markdown(
            """
            <div class="content-card">
                <p>
                    Feature importance shows which wine properties contributed most to the
                    Random Forest prediction model.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Feature importance is not available for this model.")