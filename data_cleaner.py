import os
import pandas as pd

def clean_csv_data(input_file='input_data.csv', output_file='clean_output.csv', email_col='email'):
    """
    Reads a messy CSV file, cleans whitespace from text columns, lowercases emails,
    removes duplicate rows based on the email column, and exports the clean data.
    """
    # 1. Error handling for missing file
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' was not found. Please ensure it is in the correct directory.")
        return

    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        print(f"Successfully loaded '{input_file}' with {len(df)} initial rows.")

        # 2. Strip leading/trailing white spaces from all text (object/string) columns
        text_columns = df.select_dtypes(include=['object', 'string']).columns
        for col in text_columns:
            df[col] = df[col].astype(str).str.strip()

        # 3. Locate and clean the email column (case-insensitive column name matching)
        target_email_col = None
        for col in df.columns:
            if col.strip().lower() == email_col.lower():
                target_email_col = col
                break

        if target_email_col:
            # Convert email addresses to lowercase
            df[target_email_col] = df[target_email_col].str.lower()
            
            # 4. Remove duplicate rows based on the email column
            initial_count = len(df)
            df.drop_duplicates(subset=[target_email_col], keep='first', inplace=True)
            removed_count = initial_count - len(df)
            print(f"Removed {removed_count} duplicate rows based on '{target_email_col}'.")
        else:
            print(f"Warning: Could not find an email column matching '{email_col}'. Skipping lowercasing and duplicate removal.")

        # 5. Save the clean result to a new CSV file
        df.to_csv(output_file, index=False)
        print(f"Cleaned data successfully saved to '{output_file}'. Total rows remaining: {len(df)}")

    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")

if __name__ == "__main__":
    clean_csv_data()