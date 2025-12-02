import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# --- 1. Simulate Raw IoT Sensor Data ---
# In a real-world scenario, you would load this from a CSV, database, or stream.
# pd.read_csv('your_iot_data.csv')
print("--- 1. Creating a sample raw IoT dataset ---")
data = {
    'timestamp': pd.to_datetime([
        '2023-10-27 10:00:00', '2023-10-27 10:01:00', '2023-10-27 10:02:00',
        '2023-10-27 10:03:00', '2023-10-27 10:04:00', '2023-10-27 10:05:00',
        '2023-10-27 10:00:00', '2023-10-27 10:01:00', '2023-10-27 10:02:00',
        '2023-10-27 10:03:00', '2023-10-27 10:04:00', '2023-10-27 10:05:00'
    ]),
    'sensor_id': [
        'sensor_A', 'sensor_A', 'sensor_A', 'sensor_A', 'sensor_A', 'sensor_A',
        'sensor_B', 'sensor_B', 'sensor_B', 'sensor_B', 'sensor_B', 'sensor_B'
    ],
    'temperature': [
        22.1, 22.2, np.nan, 22.5, 22.6, 22.8, # sensor_A data with a missing value
        30.1, 30.2, 30.3, np.nan, 30.5, 30.6  # sensor_B data with a missing value
    ],
    'humidity': [
        45.2, 45.2, 45.4, np.nan, 45.5, 45.7,
        60.1, np.nan, 60.3, 60.4, 60.5, 60.7
    ]
}
df = pd.DataFrame(data)
# Introduce a slight upward drift to sensor_A's temperature for demonstration
df.loc[df['sensor_id'] == 'sensor_A', 'temperature'] += np.linspace(0, 0.5, 6)

print("Original Data with missing values and drift:")
print(df)
print("\n")


# --- 2. Handle Missing Values using Forward Fill ---
# Forward fill is great for time-series data as it assumes the most recent
# valid observation is the best estimate until a new one arrives.
# We group by 'sensor_id' to prevent data from one sensor filling gaps in another.
print("--- 2. Handling missing values with forward fill (per sensor) ---")
df['temperature'] = df.groupby('sensor_id')['temperature'].transform(lambda x: x.ffill())
df['humidity'] = df.groupby('sensor_id')['humidity'].transform(lambda x: x.ffill())

print("Data after forward fill:")
print(df)
print("\n")


# --- 3. Remove Sensor Drift using a Rolling Mean ---
# Sensor drift is a slow, gradual change in sensor readings over time.
# We can mitigate this by subtracting a rolling average from the signal.
# This highlights short-term fluctuations, which is often where anomalies lie.
print("--- 3. Removing sensor drift with a rolling mean (window=3) ---")
window_size = 3
# Calculate rolling mean for each sensor
rolling_mean_temp = df.groupby('sensor_id')['temperature'].transform(lambda x: x.rolling(window=window_size, min_periods=1).mean())
rolling_mean_hum = df.groupby('sensor_id')['humidity'].transform(lambda x: x.rolling(window=window_size, min_periods=1).mean())

# Subtract the rolling mean to detrend the data
df['temp_detrended'] = df['temperature'] - rolling_mean_temp
df['hum_detrended'] = df['humidity'] - rolling_mean_hum

print("Data after detrending (notice the new columns):")
# Displaying relevant columns for clarity
print(df[['timestamp', 'sensor_id', 'temperature', 'temp_detrended']])
print("\n")


# --- 4. Normalize Numerical Readings using Standard Scaling ---
# StandardScaler transforms data to have a mean of 0 and a standard deviation of 1.
# This is crucial for many anomaly detection algorithms that are sensitive to feature scales.
print("--- 4. Normalizing numerical features with StandardScaler ---")
scaler = StandardScaler()
numerical_cols = ['temperature', 'humidity', 'temp_detrended', 'hum_detrended']
# Fit and transform the data, creating new scaled columns
df[[f'{col}_scaled' for col in numerical_cols]] = scaler.fit_transform(df[numerical_cols])

print("Data after scaling (notice the new scaled columns):")
print(df[['timestamp', 'sensor_id', 'temperature_scaled', 'temp_detrended_scaled']].head())
print("\n")


# --- 5. Encode Categorical Sensor IDs ---
# Machine learning models require numerical input. We convert the categorical
# 'sensor_id' into numerical format using one-hot encoding.
print("--- 5. Encoding categorical 'sensor_id' ---")
# Using pandas get_dummies is a straightforward way to do one-hot encoding
sensor_dummies = pd.get_dummies(df['sensor_id'], prefix='sensor')

# Concatenate the new dummy variables with the main dataframe
processed_df = pd.concat([df, sensor_dummies], axis=1)

# --- 6. Final Structured Dataset ---
# Let's create the final, clean dataset ready for a model.
# We select the timestamp and all the new, engineered features.
print("--- 6. Assembling the final, structured dataset ---")
final_cols = [
    'timestamp',
    'temperature_scaled',
    'humidity_scaled',
    'temp_detrended_scaled',
    'hum_detrended_scaled'
] + list(sensor_dummies.columns)

final_df = processed_df[final_cols]

# Set timestamp as index, which is common for time-series analysis
final_df = final_df.set_index('timestamp')

print("Final dataset optimized for anomaly detection:")
print(final_df)
