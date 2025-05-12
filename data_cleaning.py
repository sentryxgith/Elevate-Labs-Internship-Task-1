import pandas as pd

# Load the dataset
file_path = 'Mall_Customers.csv'  # Update path if needed
df = pd.read_csv(file_path)

# Step 1: Check for missing values
print("Missing values before cleaning:\n", df.isnull().sum())

# Step 2: Remove duplicate rows
df = df.drop_duplicates()

# Step 3: Standardize 'Gender' column
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.strip().str.lower().replace({'f': 'female', 'm': 'male'})

# Step 4: Rename columns (lowercase, underscores, remove special chars)
df.columns = [col.strip().lower().replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_') for col in df.columns]

# Step 5: Convert 'age' column to integer
if 'age' in df.columns:
    df['age'] = df['age'].astype(int)

# Step 6: Save the cleaned dataset
cleaned_file_path = 'cleaned_mall_customers.csv'
df.to_csv(cleaned_file_path, index=False)

# Step 7: Output summary info (for README)
print("Columns after cleaning:", df.columns.tolist())
print("Final row count:", len(df))
print("Cleaned file saved as:", cleaned_file_path)
