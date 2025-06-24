import pandas as pd  # Import pandas

def format_date_column(data, column_name):
    """Format a column to datetime."""
    data[column_name] = pd.to_datetime(data[column_name])
    return data
