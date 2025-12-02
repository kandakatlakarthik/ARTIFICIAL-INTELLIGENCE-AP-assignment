import pandas as pd
import numpy as np # This line was missing during execution
import os
from utils.preprocessing import preprocess_stock_data, load_data_from_csv

# --- 1. Create a dummy data file if it doesn't exist ---
# In a real scenario, you would already have this file.
try:
    # Try to load the data
    raw_df = load_data_from_csv('data/aapl_stock.csv')
    print("Loaded existing data/aapl_stock.csv")
except FileNotFoundError:
    print("data/aapl_stock.csv not found. Creating a sample file.")
    # Create sample data and save it
    data = {
        'date': pd.to_datetime(pd.date_range(start='2023-01-01', periods=20)),
        'closing_price': [150.5, 152.3, 151.9, np.nan, 153.2, 155.0, 154.5, 156.8, 157.2, 155.5, 158.0, 159.1, 161.5, 160.9, 159.8, np.nan, 163.4, 185.0, 164.0, 165.2],
        'volume': [1.2e6, 1.5e6, 1.4e6, 1.3e6, np.nan, 1.8e6, 1.7e6, 2.1e6, 2.2e6, 1.9e6, 2.5e6, 2.6e6, 3.0e6, 2.8e6, 2.7e6, 3.2e6, 3.5e6, 4.5e6, 3.8e6, 3.9e6]
    }
    raw_df = pd.DataFrame(data)
    if not os.path.exists('data'):
        os.makedirs('data')
    raw_df.to_csv('data/aapl_stock.csv', index=False)
    # Now load it properly with the function
    raw_df = load_data_from_csv('data/aapl_stock.csv')


# --- 2. Preprocess the data ---
processed_df = preprocess_stock_data(raw_df)

# --- 3. Continue with your analysis or modeling ---
print("\nPreprocessing complete. Data is ready for modeling.")
print(processed_df.head())
