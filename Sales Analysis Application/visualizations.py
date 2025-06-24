import plotly.express as px
import pandas as pd

def generate_best_selling_graph(data, region):
    """Generate a bar graph for the best-selling products in a region."""
    filtered_data = data if region is None else data[data['Region'] == region]
    best_selling = filtered_data.groupby('Product')['Total Sales'].sum().reset_index()
    best_selling = best_selling.sort_values('Total Sales', ascending=False)
    return px.bar(best_selling, x='Product', y='Total Sales', title='Best Selling Products')

def generate_sales_by_product_graph(data, region=None):
    """Generate a bar graph for sales by product."""
    filtered_data = data if region is None else data[data['Region'] == region]
    sales_data = filtered_data.groupby('Product')['Total Sales'].sum().reset_index()
    return px.bar(sales_data, x='Product', y='Total Sales', title='Sales by Product')

def generate_top_selling_graph_by_date(data, date):
    """Generate a bar graph for the top-selling product on a specific date."""
    if date:
        date_filtered = data[data['Date'] == pd.to_datetime(date)]
        top_product = date_filtered.groupby('Product')['Total Sales'].sum().reset_index()
        top_product = top_product.sort_values('Total Sales', ascending=False).head(1)
        return px.bar(
            top_product,
            x='Product',
            y='Total Sales',
            title=f"Top-Selling Product on {date}",
            text='Total Sales'
        )
    else:
        return px.bar(title="Select a Date to View the Graph")

def generate_behavior_analysis_graph(data):
    """Generate a bar graph for customer behavior analysis."""
    # Identify customers with multiple purchases on the same day
    behavior_data = data.groupby(['Customer ID', 'Date'])
    multi_purchase = behavior_data.size().reset_index(name='Count')
    multi_purchase = multi_purchase[multi_purchase['Count'] > 1]
    
    # Get product pairs for these customers
    product_pairs = []
    for _, row in multi_purchase.iterrows():
        customer_data = data[
            (data['Customer ID'] == row['Customer ID']) & (data['Date'] == row['Date'])
        ]
        products = customer_data['Product'].tolist()
        pairs = [(products[i], products[j]) for i in range(len(products)) for j in range(i + 1, len(products))]
        product_pairs.extend(pairs)

    # Convert pairs into a DataFrame
    pairs_df = pd.DataFrame(product_pairs, columns=['Product A', 'Product B'])
    pairs_df['Pair'] = pairs_df['Product A'] + " & " + pairs_df['Product B']
    pair_sales = pairs_df.groupby('Pair').size().reset_index(name='Count')

    # Create bar graph
    return px.bar(
        pair_sales,
        x='Pair',
        y='Count',
        title="Behavior Analysis: Product Pairs",
        text='Count'
    )

def generate_region_sales_graph(data, region=None):
    """Generate a bar graph for sales by region."""
    regional_sales = data.groupby('Region')['Total Sales'].sum().reset_index()
    return px.bar(regional_sales, x='Region', y='Total Sales', title='Regional Sales')
