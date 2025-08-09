from load_global_superstore import load_orders
from inventory_simulator import get_products, simulate_inventory

# Load historical order and return data
orders, returns,people = load_orders()

# Get product data from Fake Store API
products = get_products()

# Simulate 30 days of inventory data for all products
inventory_df = simulate_inventory(products, days=30)

# Save the processed data to CSV files for further use
orders.to_csv('./data/orders.csv', index=False)
returns.to_csv('./data/returns.csv', index=False)
people.to_csv('./data/people.csv', index=False)
inventory_df.to_csv('./data/inventory.csv', index=False)

print(" ETL process complete. Data saved to CSV.")
