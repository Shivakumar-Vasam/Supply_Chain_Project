from google.cloud import bigquery

# ✅ Step 1: Authenticate with your service account JSON
client = bigquery.Client.from_service_account_json("service_account.json")

# ✅ Step 2: Helper to run SQL

def run_query(sql, label):
    job = client.query(sql)
    job.result()
    print(f"✅ {label} created.")

# ✅ Step 3: Create FACT TABLES

# FACT ORDERS
run_query("""
CREATE OR REPLACE TABLE `supply-chain-project-467705.supply_chain_data.fact_orders` AS
SELECT
  `Order ID` AS order_id,
  `Order Date` AS order_date,
  `Ship Date` AS ship_date,
  `Product ID` AS product_id,
  `Customer ID` AS customer_id,
  Sales
FROM `supply-chain-project-467705.supply_chain_data.orders`
""", "fact_orders")

# ✅ Step 4: Create DIMENSION TABLES

# DIM PRODUCT
run_query("""
CREATE OR REPLACE TABLE `supply-chain-project-467705.supply_chain_data.dim_product` AS
SELECT DISTINCT
  `Product ID` AS product_id,
  `Product Name` AS product_name,
  Category,
  `Sub-Category` AS sub_category
FROM `supply-chain-project-467705.supply_chain_data.orders`
""", "dim_product")

# DIM CUSTOMER
run_query("""
CREATE OR REPLACE TABLE `supply-chain-project-467705.supply_chain_data.dim_customer` AS
SELECT DISTINCT
  `Customer ID` AS customer_id,
  `Customer Name` AS customer_name,
  Segment,
  Country,
  City,
  State,
  `Postal Code` AS postal_code,
  Region
FROM `supply-chain-project-467705.supply_chain_data.orders`
""", "dim_customer")

# DIM DATE
run_query("""
CREATE OR REPLACE TABLE `supply-chain-project-467705.supply_chain_data.dim_date` AS
WITH dates AS (
  SELECT 
    DATE_ADD(DATE '2016-01-01', INTERVAL day DAY) AS date
  FROM UNNEST(GENERATE_ARRAY(0, 1460)) AS day
)
SELECT 
  date,
  EXTRACT(DAY FROM date) AS day,
  EXTRACT(MONTH FROM date) AS month,
  EXTRACT(YEAR FROM date) AS year,
  FORMAT_DATE('%B', date) AS month_name,
  FORMAT_DATE('%A', date) AS day_name
FROM dates
""", "dim_date")

# ✅ Step 5: Create a View for Sales by Category
run_query("""
CREATE OR REPLACE VIEW `supply-chain-project-467705.supply_chain_data.sales_by_category` AS
SELECT 
  p.category,
  SUM(f.sales) AS total_sales
FROM `supply-chain-project-467705.supply_chain_data.fact_orders` f
JOIN `supply-chain-project-467705.supply_chain_data.dim_product` p
  ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC
""", "sales_by_category view")
