import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from data_preprocessing import load_and_preprocess_csv, load_multiple_csvs_in_folder

# Load real and fake data
df_fake = load_and_preprocess_csv("../../data/fake/fake_activity_log.csv")
df_real = load_multiple_csvs_in_folder("../../data/real/")  # Loads all .csv files in the folder

# Add a new label column to identify real vs fake
df_fake["label"] = 1  # fake = 1
df_real["label"] = 0  # real = 0

# Combine datasets
df = pd.concat([df_real, df_fake], ignore_index=True)

# Select features and target
features = [
    'key_down', 'key_up', 'sys_key_down', 'sys_key_up',
    'total_x', 'total_y', 'left_click', 'right_click',
    'scroll_up', 'scroll_down', 'injected_key_down', 'injected_key_up',
    'injected_sys_key_down', 'injected_sys_key_up', 'injected_x', 'injected_y',
    'injected_left', 'injected_right', 'injected_scroll_up', 'injected_scroll_down',
    'x', 'y'
]
X = df[features]
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(clf, "../../models/fraud_detector.pkl")
