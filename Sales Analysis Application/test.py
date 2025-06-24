#1. Best-Selling Product Analysis

import pandas as pd
from data_processing import find_best_selling, load_data

def test_find_best_selling_with_real_data():
    # Load the actual dataset
    data = load_data()
    
    # Calculate the best-selling product
    best_selling = find_best_selling(data)
    
    expected_product = "Tea Powder"  
    assert best_selling == expected_product, f"Expected '{expected_product}', got '{best_selling}'"

#2. Customer Behavior Analysis

from data_processing import find_behavior_patterns, load_data

def test_find_behavior_patterns_with_real_data():
    # Load the actual dataset
    data = load_data()
    
    # Find customer behavior patterns
    patterns = find_behavior_patterns(data)
    
    expected_count = 247 
    assert len(patterns) == expected_count, f"Expected {expected_count} patterns, got {len(patterns)}"

#3. Product Performance Analysis

from visualizations import generate_sales_by_product_graph
from data_processing import load_data

def test_product_performance_with_real_data():
    data = load_data()
    
    # Generate graph data
    graph = generate_sales_by_product_graph(data)
    
    # Validate the top product sales data 
    expected_top_product = "Tea Powder"  
    expected_sales = 5166  
    
    x_values = graph.data[0]['x']
    y_values = graph.data[0]['y']

    
    assert expected_top_product in x_values, f"Expected product '{expected_top_product}' not found in graph"
    assert expected_sales in y_values, f"Expected sales '{expected_sales}' not found in graph data"

#4. Regional Sales Analysis

from visualizations import generate_region_sales_graph
from data_processing import load_data

def test_regional_sales_analysis_with_real_data():
    # Load the actual dataset
    data = load_data()

    # Generate graph data
    graph = generate_region_sales_graph(data)

    # Expected regions and sales values (adjust these based on your dataset)
    expected_regions = ['Central', 'East', 'North', 'South', 'West']  
    expected_sales = [13135.5, 13452. , 15335. , 17429.5, 11713.5]  
    # Get graph data
    x_values = graph.data[0]['x']  # Regions in the graph
    y_values = graph.data[0]['y']  # Sales values in the graph

    # Validate that all expected regions are in the graph regions
    assert set(expected_regions) == set(x_values), f"Expected regions {expected_regions}, but got {list(x_values)}"

    # Validate sales values match for corresponding regions
    sales_mapping = dict(zip(x_values, y_values))  # Create a mapping of regions to their sales
    for region, sales in zip(expected_regions, expected_sales):
        assert sales_mapping.get(region) == sales, f"Mismatch for {region}: expected {sales}, got {sales_mapping.get(region)}"
