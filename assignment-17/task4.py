from sklearn.preprocessing import MinMaxScaler
import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_movie_reviews_final(df: pd.DataFrame, max_tfidf_features: int = 100) -> (pd.DataFrame, object):
    """
    Cleans and preprocesses a DataFrame of movie reviews.

    Args:
        df (pd.DataFrame): Input DataFrame with 'review' and 'rating' columns.
        max_tfidf_features (int): The maximum number of features for TF-IDF vectorization.

    Returns:
        tuple: A tuple containing:
            - pd.DataFrame: The cleaned DataFrame.
            - scipy.sparse.csr_matrix: The TF-IDF feature matrix.
    """
    # Work on a copy to avoid modifying the original DataFrame (Side Effect)
    df_clean = df.copy()

    # --- 1. Standardize Text (Review Column) ---
    # Use a pre-compiled regex for slight performance improvement on large datasets
    html_tag_re = re.compile('<.*?>')
    df_clean['review'] = df_clean['review'].str.lower()
    df_clean['review'] = df_clean['review'].apply(lambda x: re.sub(html_tag_re, '', x))
    # Also remove extra whitespace that might be left by tags
    df_clean['review'] = df_clean['review'].str.strip().str.replace(' +', ' ', regex=True)

    # --- 2. Handle Missing Ratings (Rating Column) ---
    # Calculate median *before* making any changes
    median_rating = df_clean['rating'].median()
    
    # First, fill the missing values in the 'rating' column.
    # Reassigning the column is the recommended practice over inplace=True on a slice.
    df_clean['rating'] = df_clean['rating'].fillna(median_rating)
    # Now, create the 'rating_original' column from the now-filled 'rating' column.
    df_clean['rating_original'] = df_clean['rating']
    # --- 3. Normalize Ratings (Rating Column) ---
    # Using MinMaxScaler is more robust than simple division. It can handle
    # any scale, not just 0-10. We reshape for the scaler's 2D input requirement.
    scaler = MinMaxScaler(feature_range=(0, 1))
    df_clean['rating_normalized'] = scaler.fit_transform(df_clean[['rating']])

    # --- 4. Vectorize Text using TF-IDF ---
    # TF-IDF is great for turning text into meaningful numerical representations.
    # It weighs words by how important they are to a document in a collection.
    tfidf_vectorizer = TfidfVectorizer(
        max_features=max_tfidf_features,
        stop_words='english' # A common practice to remove generic words
    )
    tfidf_matrix = tfidf_vectorizer.fit_transform(df_clean['review'])

    return df_clean, tfidf_matrix

# --- 5. Generate Before vs. After Summary Report ---
def generate_summary_report(original_df, cleaned_df):
    """Generates a summary report comparing data before and after cleaning."""
    print("="*50)
    print("      DATA CLEANING SUMMARY REPORT")
    print("="*50)

    print("\n--- Missing Values Analysis ---")
    print(f"Missing ratings before: {original_df['rating'].isnull().sum()}")
    print(f"Missing ratings after:  {cleaned_df['rating'].isnull().sum()}")
    print(f"Imputation value (median): {original_df['rating'].median()}")


    print("\n--- Rating Scale Analysis ---")
    print(f"Rating scale before: {original_df['rating'].min()} - {original_df['rating'].max()}")
    print(f"Rating scale after (normalized): {cleaned_df['rating_normalized'].min():.1f} - {cleaned_df['rating_normalized'].max():.1f}")

    print("\n--- Text Standardization Example ---")
    print("Review before:")
    print(f"  '{original_df.loc[1, 'review']}'")
    print("Review after:")
    print(f"  '{cleaned_df.loc[1, 'review']}'")
    print("="*50)

# --- Helper functions for demonstration and testing ---
def get_sample_data():
    """Creates a sample DataFrame for testing."""
    data = {
        'review': [
            'This movie was EXCELLENT!',
            'A terrible film. <br /><br />Not recommended.',
            'Just okay, nothing special.',
            'An absolute masterpiece.',
            'I fell asleep halfway through.'
        ],
        'rating': [9.0, 2.0, 5.0, 10.0, np.nan] # Includes a missing rating
    }
    return pd.DataFrame(data)

def run_tests(cleaned_df):
    """Runs assertions to check the quality of the cleaned data."""
    print("--- Running Test Cases ---")
    
    # Test Case 1: Check for lowercase and HTML tag removal
    expected_review = 'a terrible film. not recommended.'
    actual_review = cleaned_df.loc[1, 'review']
    assert actual_review == expected_review, f"Test 1 Failed: Expected '{expected_review}', got '{actual_review}'"
    print("✅ Test 1 Passed: Text is lowercased and HTML tags are removed.")

    # Test Case 2: Check if missing rating is filled with the median
    # Median of [9.0, 2.0, 5.0, 10.0] is (5.0 + 9.0) / 2 = 7.0
    expected_rating_original_scale = 7.0
    actual_rating_original_scale = cleaned_df.loc[4, 'rating'] # Check the column that was actually filled
    assert actual_rating_original_scale == expected_rating_original_scale, f"Test 2 Failed: Expected {expected_rating_original_scale}, got {actual_rating_original_scale}"
    print("✅ Test 2 Passed: Missing rating correctly filled with median.")

    # Test Case 3: Check if ratings are normalized to a 0-1 scale
    assert np.isclose(cleaned_df.loc[1, 'rating_normalized'], 0.0), f"Test 3 Failed: Rating for '2.0' was not normalized correctly."
    print("✅ Test 3 Passed: Rating correctly normalized to 0-1 scale.")
    print("--- All tests passed successfully! ---\n")

# --- Main Execution Block ---
if __name__ == '__main__':
    # Get original data
    df_original = get_sample_data()

    # Run the final cleaning function
    df_cleaned, review_features = clean_movie_reviews_final(df_original)

    # Run tests on the cleaned data
    # Note: The test function needs a small adjustment for the improved cleaning logic
    run_tests(df_cleaned)

    # Generate the summary report
    generate_summary_report(df_original, df_cleaned)

    print("\n--- Cleaned DataFrame Head ---")
    print(df_cleaned.head())

    print("\n--- TF-IDF Matrix Shape ---")
    print(f"(Documents, Features): {review_features.shape}")
