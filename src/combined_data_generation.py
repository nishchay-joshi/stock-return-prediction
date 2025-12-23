import os
import numpy as np
import pandas as pd

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
combined_dir = os.path.join(project_root, "data", "combined")
os.makedirs(combined_dir, exist_ok=True)

file_name = "combined_data_stocks.csv"
full_file_path = os.path.join(combined_dir, file_name)

processed_data = os.path.join(project_root, "data", "processed")

dfs = []

for file in os.listdir(processed_data):
    df = pd.read_csv(os.path.join(processed_data, file))
    df["stock"] = file.replace("_features.csv", "")
    dfs.append(df)

final_df = pd.concat(dfs)
final_df = final_df.replace([np.inf, -np.inf], np.nan)
final_df = final_df.dropna()

final_df.to_csv(full_file_path, index=False)
