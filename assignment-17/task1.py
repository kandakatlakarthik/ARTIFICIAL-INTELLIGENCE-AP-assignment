import pandas as pd
import numpy as np
import re
import string
import nltk

# --- 1. SETUP: Download NLTK stopwords (only needs to be done once) ---
try:
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
except LookupError:
    print("NLTK stopwords not found. Downloading...")
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))

# --- 2. SAMPLE DATA: Create a raw DataFrame ---
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'text': [
        "Hello world!! This is my #firstpost. So excited :)",
        "Check out this awesome deal @ www.example.com!",
        "Just enjoying a beautiful sunset. #blessed",
        "What are your thoughts on the new update? Let me know!",
        np.nan, # Missing post text
        "Check out this awesome deal @ www.example.com!", # Duplicate post
        "Feeling sad today... need some motivation 😔",
        "Another great day at the office. #worklife"
    ],
    'likes': [150, 25, 300, 55, 10, 28, 90, np.nan],
    'shares': [20, 5, 45, 12, 2, 6, np.nan, 5],
    'timestamp': [
        '2023-10-27 09:15:00', '2023-10-27 10:30:00', '2023-10-27 18:45:00',
        '2023-10-28 11:00:00', '2023-10-28 12:00:00', '2023-10-28 14:20:00',
        '2023-10-29 19:05:00', '2023-10-30 17:30:00'
    ]
}
df = pd.DataFrame(data)
print("----------- Raw Dataset -----------")
print(df)
print("\n")


# --- 3. DATA CLEANING & PREPROCESSING ---

# Step 3.1: Handle missing text values
# We'll fill any missing post text with an empty string.
df['text'].fillna('', inplace=True)

# Step 3.2: Clean the 'text' column
def clean_text(text):
    """
    Removes punctuation, special symbols, URLs, and stopwords from text.
    Converts text to lowercase.
    """
    # Convert to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove special symbols and numbers (optional, depends on use case)
    text = re.sub(r'[^a-z\s]', '', text)
    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

df['cleaned_text'] = df['text'].apply(clean_text)

# Step 3.3: Handle missing values in 'likes' and 'shares'
# A common strategy is to fill with 0, assuming no recorded value means no engagement.
# Alternatively, you could use the median: df['likes'].fillna(df['likes'].median(), inplace=True)
df['likes'].fillna(0, inplace=True)
df['shares'].fillna(0, inplace=True)
# Convert to integer type for cleaner data
df['likes'] = df['likes'].astype(int)
df['shares'] = df['shares'].astype(int)


# Step 3.4: Convert timestamp and extract features
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour_of_day'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.day_name()


# Step 3.5: Detect and remove spam/duplicate posts
# We identify duplicates based on the original 'text' column.
# `keep='first'` ensures we keep the first occurrence and remove subsequent ones.
df.drop_duplicates(subset='text', keep='first', inplace=True)


# --- 4. FINALIZE THE DATAFRAME ---

# Select and reorder columns for the final cleaned dataset
final_df = df[[
    'post_id', 'cleaned_text', 'likes', 'shares',
    'timestamp', 'hour_of_day', 'day_of_week'
]].reset_index(drop=True)


print("----------- Cleaned Dataset -----------")
print(final_df)
