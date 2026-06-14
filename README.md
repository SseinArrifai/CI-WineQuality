After extracting the ZIP file, open the WineQualityPrediction folder in VS Code.

Then open terminal in the main project folder and run these commands:

1. Create virtual environment:
   python -m venv venv

2. Activate virtual environment:
   venv\Scripts\activate

3. Install required packages:
   pip install pandas scikit-learn matplotlib streamlit joblib

4. Run the system:
   streamlit run system/app.py
