def data_quality_summary(df):
    """Returns basic checks: missing values, duplicates, and unique values counts."""
    
    print("Missing values per column:")
    print(df.isnull().sum())
    print("\nNumber of duplicate rows:")
    print(df.duplicated().sum())
    print("\nUnique values per column:")
    print(df.nunique())
 
