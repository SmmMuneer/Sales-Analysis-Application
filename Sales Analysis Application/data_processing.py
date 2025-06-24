import pandas as pd

def load_data():
    """Load and preprocess data."""
    file_path = 'modify.csv'
    data = pd.read_csv(file_path)
    
    # Convert Date column to datetime format with dayfirst=True
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True, errors='coerce')
    
    # Optionally, drop rows where the Date conversion failed (if any)
    data = data.dropna(subset=['Date'])
    
    return data

def filter_by_region(data, region):
    """Filter data by region."""
    return data[data['Region'] == region]

def filter_by_date(data, date):
    """Filter data by date."""
    # Ensure the input date is a datetime object
    date = pd.to_datetime(date)
    
    # Filter data by the exact date, ignoring time parts if present
    return data[data['Date'].dt.date == date.date()]

def find_best_selling(data):
    """Find the best-selling product."""
    return data.groupby('Product')['Total Sales'].sum().idxmax()

def find_behavior_patterns(data):
    """Find customer behavior patterns."""
    grouped = data.groupby(['Customer ID', 'Date'])
    patterns = grouped.size().reset_index(name='Count')
    return patterns[patterns['Count'] > 1]
