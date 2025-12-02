import pandas as pd
import numpy as np

def preprocess_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses a stock market dataset by handling missing values,
    creating lag features, normalizing volume, and detecting outliers.

    Args:
        df: DataFrame with 'date', 'closing_price', and 'volume' columns.

    Returns:
        A preprocessed DataFrame ready for time-series analysis.
    """
    processed_df = df.copy()

    if not isinstance(processed_df.index, pd.DatetimeIndex):
        processed_df['date'] = pd.to_datetime(processed_df['date'])
        processed_df.set_index('date', inplace=True)

    processed_df['closing_price'].fillna(method='ffill', inplace=True)
    processed_df['volume'].fillna(0, inplace=True)

    processed_df['1_day_return'] = processed_df['closing_price'].pct_change(periods=1)
    processed_df['7_day_return'] = processed_df['closing_price'].pct_change(periods=7)

    processed_df['volume_log'] = np.log1p(processed_df['volume'])

    Q1 = processed_df['closing_price'].quantile(0.25)
    Q3 = processed_df['closing_price'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    processed_df['is_outlier'] = (processed_df['closing_price'] < lower_bound) | \
                                 (processed_df['closing_price'] > upper_bound)

    processed_df.dropna(inplace=True)

    return processed_df

def load_data_from_csv(filepath: str) -> pd.DataFrame:
    """Loads data from a CSV and sets a datetime index."""
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df
