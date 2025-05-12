# Elevate-Labs-Internship-Task-1

## Data Cleaning Summary

**Dataset:** Mall_Customers.csv (Mall Customer Segmentation Data)

**Steps Performed:**

- **Missing Values:**  
  The dataset was checked for missing values in all columns. No missing values were found in any column.

- **Duplicate Rows:**  
  The dataset was examined for duplicate rows. No duplicates were found, so no rows were removed.

- **Standardization of Text Values:**  
  The `Gender` column was standardized by converting all entries to lowercase and ensuring consistent labeling (`male`, `female`).

- **Date Formats:**  
  No date columns were present in the dataset, so this step was not applicable.

- **Column Header Renaming:**  
  All column headers were converted to lowercase, spaces were replaced with underscores, and special characters were removed for consistency and ease of use.  
  - Original columns:  
    `CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, `Spending Score (1-100)`
  - New columns:  
    `customerid`, `gender`, `age`, `annual_income_k$`, `spending_score_1-100`

- **Data Type Corrections:**  
  The `age` column was explicitly converted to integer type to ensure consistency.

- **Rows After Cleaning:**  
  The dataset contains **200 rows** after cleaning, which matches the original size since no rows were removed.

---

### Key Cleaning Statistics

| Step                    | Result                |
|-------------------------|-----------------------|
| Missing values handled  | 0 found               |
| Duplicates removed      | 0 found               |
| Columns renamed         | Yes                   |
| Gender standardized     | Yes                   |
| Date columns processed  | Not applicable        |
| Final row count         | 200                   |

---

**The cleaned dataset is saved as `cleaned_mall_customers.csv`.**

---

#### Example of Cleaned Data

| customerid | gender  | age | annual_income_k$ | spending_score_1-100 |
|------------|---------|-----|------------------|----------------------|
| 1          | male    | 19  | 15               | 39                   |
| 2          | male    | 21  | 15               | 81                   |
| 3          | female  | 20  | 16               | 6                    |

---

**No data was lost during cleaning. The dataset is now ready for analysis.**
