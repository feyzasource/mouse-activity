import numpy as np
import ast
import math
import pandas as pd

def extract_mouse_features_from_row(row):
    try:
        
        if pd.isna(row['x']) or pd.isna(row['y']):
            raise ValueError("Empty coordinates")
            
            
        # Süslü parantezleri listeye çeviriyoruz
        x_raw = row['x'].replace("{", "[").replace("}", "]")
        y_raw = row['y'].replace("{", "[").replace("}", "]")

        x_list = ast.literal_eval(x_raw)
        y_list = ast.literal_eval(y_raw)

        if isinstance(x_list, set):
            x_list = list(x_list)
        if isinstance(y_list, set):
            y_list = list(y_list)

    except Exception as e:
        print(f"Row parsing error: {e}")
        return {
            'avg_speed': 0,
            'avg_acceleration': 0,
            'avg_direction': 0,
            'avg_direction_change': 0,
            'mouse_box_area': 0
        }

    if len(x_list) < 2 or len(y_list) < 2:
        return {
            'avg_speed': 0,
            'avg_acceleration': 0,
            'avg_direction': 0,
            'avg_direction_change': 0,
            'mouse_box_area': 0
        }

    speeds = []
    directions = []

    for i in range(1, len(x_list)):
        dx = x_list[i] - x_list[i - 1]
        dy = y_list[i] - y_list[i - 1]
        dist = math.sqrt(dx ** 2 + dy ** 2)
        speed = dist / 0.2  # 200 ms
        direction = math.atan2(dy, dx)
        speeds.append(speed)
        directions.append(direction)

    accelerations = [(speeds[i] - speeds[i - 1]) / 0.2 for i in range(1, len(speeds))]
    direction_changes = [abs(directions[i] - directions[i - 1]) for i in range(1, len(directions))]

    mouse_box_area = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list)) if len(x_list) > 1 else 0

    return {
        'avg_speed': np.mean(speeds),
        'avg_acceleration': np.mean(accelerations) if accelerations else 0,
        'avg_direction': np.mean(directions),
        'avg_direction_change': np.mean(direction_changes) if direction_changes else 0,
        'mouse_box_area': mouse_box_area
    }


# Optional helper: extract all from a dataframe
def extract_features_dataframe(df):
    feature_rows = df.apply(extract_mouse_features_from_row, axis=1)
    return pd.DataFrame(feature_rows.tolist())
