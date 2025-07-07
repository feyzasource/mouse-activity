
# Mouse Activity Analysis with AI

## Project Overview

This project is part of a senior design initiative focused on analyzing mouse activity to detect fraudulent behaviors, such as the use of mouse jigglers or bots. The objective is to build an AI-powered classifier that can reliably distinguish between real human behavior and synthetic patterns. The models and features developed here can be integrated into employee productivity monitoring software.

---

## Key Features

- **Mouse Data Collection**: C++ program to record real-time mouse activity (X-Y coordinates every 200ms).
- **Synthetic (Fake) Data Generation**: Automatically generated mouse activity using scripts and templates simulating fake behaviors (constant movement, low entropy, etc.).
- **Data Preprocessing & Feature Engineering**: Directional changes, entropy, bounding box area, idle ratio, speed, etc. calculated via Python.
- **Automated Feature Processing**: Using `Papermill`, all `.ipynb` notebooks are executed across real and fake datasets with batch automation.
- **Partitioned Dataset Management**: Large-scale mouse activity data was divided into daily partitions for better manageability and parallel processing.
- **Model Training**: Logistic Regression and K-Nearest Neighbors (KNN) were trained to classify real vs. fake data.
- **Overfitting Currently Observed**: Current results show very high accuracy, indicating possible overfitting due to synthetic data similarity. This is being actively addressed by increasing dataset diversity.

---

## Technologies Used

| Category         | Tools / Libraries                                 |
|------------------|---------------------------------------------------|
| Programming      | C++, Python, Jupyter Notebooks                    |
| AI / ML          | scikit-learn (Logistic Regression, KNN)           |
| Automation       | Papermill (for batch notebook execution)          |
| Data Handling    | Pandas, NumPy                                     |
| Visualization    | Matplotlib, Seaborn                               |
| Deployment Plan  | Integration into a desktop productivity analyzer  |

---

## Repository Structure

```
mouse-activity/
├── analysis/                     # Feature engineering + ML notebooks
│   ├── knn_paths.ipynb
│   ├── logistic_regression_paths.ipynb
│   └── run_all_features.py       # Papermill executor script
├── processed/                    # Output of real + fake processed features
├── data/                         # Raw mouse activity (not pushed to GitHub)
├── poster/                       # Final presentation poster and A1 layout
├── README.md                     # Project summary and instructions
```

---

## How Fake Data Was Handled

- **Data Simulation**: Fake data mimicking mouse movement was generated using custom scripts.
- **Daily Partitioning**: Fake data was saved under folders like `profile_guid=*/2025-04-16/*.parquet` to simulate per-day activity.
- **Papermill Execution**: Feature extraction notebooks were parameterized and executed over each daily partition using `papermill`, ensuring scalable processing of hundreds of profiles.
- **Consistency Checks**: Fake datasets were kept structurally consistent with real data: each entry includes timestamp, x/y coordinates, and timezone info.
- **Labeling**: Real data was labeled with `1`, fake with `0`, enabling binary classification.

---

## Getting Started

### Prerequisites

- Python 3.10+ with the following libraries:
  ```bash
  pip install -r requirements.txt
  ```
- A Windows machine with mouse activity capture enabled via C++ if collecting new data.

### Run Notebooks

```bash
# Feature engineering using real and fake partitioned data
cd analysis/
python run_all_features.py
```

---

## Example Features Used

- `x_direction_changes`, `y_direction_changes`
- `bounding_box_area`
- `avg_speed`, `avg_acceleration`
- `mouse_idle_ratio`
- `movement_entropy`
- `linearity`

These features are extracted and selected via `SelectKBest` and passed to classifiers.

---

## Evaluation Metrics

| Metric       | Value (Initial Test) |
|--------------|----------------------|
| Accuracy     | 100% (overfit)       |
| Precision    | 100%                 |
| Recall       | 100%                 |
| Specificity  | 100%                 |

🚨 **Note**: These perfect results indicate overfitting due to the current synthetic data patterns being too simplistic. This is being improved by increasing diversity and realism in fake data.

---

## Future Work

- Add keyboard activity and idle time modeling.
- Integrate deep learning models (CNN, LSTM).
- Add time-series anomaly detection.
- Finalize integration into employee productivity application.

---

## License

MIT License. See [LICENSE](./LICENSE) for full terms.
