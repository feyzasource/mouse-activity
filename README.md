# Mouse Activity Analysis with AI

## 🎯 Project Overview

This project is part of a senior design initiative aimed at detecting fraudulent mouse behavior — such as the use of mouse jigglers or bots — by analyzing mouse activity patterns. We leverage Artificial Intelligence (AI) techniques to distinguish between genuine human movement and automated scripts. The ultimate goal is to embed this capability into a desktop-based productivity analysis platform used in professional environments.

---

## 📌 Key Features

- **Mouse Data Collection**  
  C++ agent records raw X-Y coordinates every 200 ms and saves them into timestamped text files.

- **Synthetic vs Real Data**  
  Real data is collected from human users. Synthetic data is generated using mouse jigglers or programmatic simulation to imitate human-like patterns.

- **AI-based Fraud Detection**  
  Machine learning models are trained on feature-engineered datasets to detect anomalies and fraudulent behavior.

- **Model Integration**  
  The AI model will be embedded in an existing desktop analytics application with cloud/on-prem licensing options.

---

## 🧰 Technologies Used

- **Languages**: C++, Python, R
- **Machine Learning**: scikit-learn, TensorFlow (planned)
- **Data Visualization**: matplotlib, seaborn, ggplot2 (R)
- **IDE**: Visual Studio (for C++), Jupyter Notebook

---

## 🗂️ Project Structure

```
km-stat-fake-detection/
│
├── notebooks/
│   └── Logistic Regression Paths.ipynb     # Main ML pipeline
│
├── data/
│   └── real/
│       └── km_stat_1_processed.csv ...     # Real human mouse activity
│
├── processed/
│   └── fake/
│       └── profile_guid=*/*.csv            # Scripted/fake mouse activity
│
├── unused/
│   └── 20250416/
│       └── km_stat_acer_20250416_processed.csv  # Unseen real test set
│
├── main.cpp                                # Mouse activity recorder (C++)
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- **Windows machine** with Visual Studio for running `main.cpp`
- **Python 3.8+** with:  
  `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `seaborn`
- **R** (optional, for visualization):  
  `ggplot2`, `caret`, etc.

### 🔧 Running the C++ Mouse Recorder

```bash
g++ main.cpp -o mouse_activity
./mouse_activity
```

This will generate files like:

```
mouse_coordinates_2024109_205723.txt
mouse_coordinates_2024112_1412.txt
```

---

## 🧠 AI Workflow

### 1. Data Collection
- Real and fake mouse activities are gathered and stored as `.csv` files after preprocessing.

### 2. Feature Engineering
Each movement sample is processed to extract meaningful behavioral features:
- `x_direction_changes`, `y_direction_changes`
- `min/max x and y`
- `bounding_box_area`, `avg_speed`, `mouse_idle_ratio`, etc.

### 3. Data Labeling
- Real data → `label = 1`
- Fake data → `label = 0`

### 4. Preprocessing
- Data is normalized using `StandardScaler` (Z-score normalization).
- Dimensionality reduction using:
  - `SelectKBest`
  - `Recursive Feature Elimination (RFE)`

### 5. Model Training
- Trained a **Logistic Regression** model.
- High performance on internal test set:  
  Accuracy, Precision, Recall ≈ 1.00
- Overfitting was observed and actively addressed via:
  - Feature selection
  - Normalization
  - External testing with **unseen real data** (`2025-04-16`)

---

## 📊 Evaluation Metrics

- **Accuracy**
- **Precision**
- **Recall**
- **Specificity**
- **Confusion Matrix**

We also tested the model with a completely **unseen real day** to measure generalization performance.

---

## 🧪 Current Status

✅ Data Pipeline Complete  
✅ Logistic Regression Model Trained  
✅ Feature Selection Applied  
✅ Overfitting Identified and Addressed  
✅ External Test Case Evaluated  
🔄 Next: Try SVM, Random Forest, or Neural Networks  

---

## 🚧 Future Enhancements

- Use more complex models (SVM, MLP, XGBoost)
- Extend detection to **keyboard activity**
- Evaluate performance in real-time scenarios
- Package model for **desktop deployment**
- Explore applications in **cybersecurity** and **HCI**

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE)

---

## 🙌 Acknowledgment

This project is supervised as part of our senior capstone course and will be shared on GitHub for academic evaluation and presentation.
