from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from visualizations import (
    generate_best_selling_graph, 
    generate_sales_by_product_graph, 
    generate_behavior_analysis_graph, 
    generate_region_sales_graph
)
from data_processing import load_data, filter_by_region, filter_by_date

# Load data
data = load_data()

# Initialize the app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Analysis Dashboard"),
    
    # Region-wise Best Selling Product
    html.Div([
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': region, 'value': region} for region in data['Region'].unique()],
            placeholder="Select a Region",
        ),
        dcc.Graph(id='best-selling-graph'),
    ]),
    
    # Best Selling Product on Selected Date
    html.Div([
        dcc.Dropdown(
            id='date-dropdown',
            options=[{'label': str(date), 'value': str(date)} for date in data['Date'].dt.date.unique()],
            placeholder="Select a Date",
        ),
        dcc.Graph(id='daily-best-selling-graph'),
    ]),
    
    # Sales by Product, Behavior Analysis, Regional Sales
    html.Div([
        dcc.Graph(id='sales-by-product-graph'),
        dcc.Graph(id='behavior-analysis-graph'),
        dcc.Graph(id='region-sales-graph'),
    ])
])

# Callbacks

# Update Best Selling Graph based on Region
@app.callback(
    Output('best-selling-graph', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_best_selling_graph(region):
    filtered_data = filter_by_region(data, region) if region else data
    return generate_best_selling_graph(filtered_data, region)  # Pass region as argument

# Update Best Selling Product Graph based on Date
@app.callback(
    Output('daily-best-selling-graph', 'figure'),
    [Input('date-dropdown', 'value')]
)
def update_daily_best_selling_graph(date):
    if date:
        filtered_data = filter_by_date(data, date)
        return generate_sales_by_product_graph(filtered_data)
    else:
        return generate_sales_by_product_graph(data)  # Show overall sales when no date is selected

# Update Sales by Product Graph based on Region
@app.callback(
    Output('sales-by-product-graph', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_sales_by_product_graph(region):
    filtered_data = filter_by_region(data, region) if region else data
    return generate_sales_by_product_graph(filtered_data)

# Update Behavior Analysis Graph based on Region
@app.callback(
    Output('behavior-analysis-graph', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_behavior_analysis_graph(region):
    filtered_data = filter_by_region(data, region) if region else data
    return generate_behavior_analysis_graph(filtered_data)

# Update Regional Sales Graph based on Region
@app.callback(
    Output('region-sales-graph', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_region_sales_graph(region):
    filtered_data = filter_by_region(data, region) if region else data
    return generate_region_sales_graph(filtered_data)

if __name__ == '__main__':
    app.run_server(debug=True)
