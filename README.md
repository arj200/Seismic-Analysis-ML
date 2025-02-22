Seismic Analysis of Buckling-Restrained Braced Frames using Machine Learning

📌 Project Overview

This project applies Machine Learning (ML) techniques to predict seismic response parameters for Buckling-Restrained Braced Frames (BRBFs). The study compares XGBoost and a Multi-Layer Perceptron (MLP) Neural Network, with MLP achieving better accuracy after feature scaling corrections.

📊 Project Features

Implemented ML Models:

✅ XGBoost (Baseline Model)

✅ Multi-Layer Perceptron (MLP Neural Network) (Improved Model)

Seismic Input Parameters: PGA, PGV, PGD, Spectral Accelerations, Structural Features, and Seismic Features.

Predicted Outputs (EDPs):

🔹 Inter-Storey Drift Ratio (IDR)

🔹 Residual Drift Ratio (RDR)

🔹 Maximum Ductility Demand

🔹 Cumulative Ductility Demand

GUI Application: A PySimpleGUI-based tool allows users to input seismic parameters and get real-time predictions.

Performance:

XGBoost (R² Score: 0.7645)

MLP Neural Network (R² Score: 0.7681) ✅ (Best Model)

📂 Project Structure

├── ML-BRBF-All-EDPs-Database.xlsx  # Dataset
├── BRBF_IDR_Optimised_Model.ipynb  # Jupyter Notebook with model training
├── MLP_Trained_Model.pkl           # Trained MLP model for predictions
├── scaler.pkl                      # Feature Scaler for consistent input processing
├── app.py                          # GUI Application (PySimpleGUI)
├── README.md                       # Project Documentation

🚀 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/Seismic-Analysis-ML.git
cd Seismic-Analysis-ML

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the GUI Application

python app.py

📌 How to Use the GUI?

Enter seismic parameters (e.g., Peak Ground Acceleration, Magnitude, etc.)

Click "Predict" to get the EDPs (IDR, RDR, Max Ductility, Cumulative Ductility)

View results instantly in the output fields.

📊 Visualizations

Scatter Plot: Actual vs. Predicted Values

(Insert scatter_plot.png here)

Feature Importance (Permutation Importance Method)

(Insert feature_importance.png here)

Feature Distribution of Input Parameters

(Insert feature_distribution.png here)

📌 Future Improvements

🔹 Further Hyperparameter Optimization

🔹 Expand Dataset for Better Generalization

🔹 Integrate Real-Time Seismic Monitoring

📜 License

This project is for educational and research purposes only.
