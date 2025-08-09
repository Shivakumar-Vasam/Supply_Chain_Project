# Supply Chain Data Integration System

## Overview

The **Supply Chain Data Integration System** is an end-to-end data engineering and analytics pipeline designed to process, integrate, and visualize supply chain data from multiple sources — including an Excel dataset (Global Superstore) and a REST API (Fake Store API).  
It simulates inventory movements, loads the data into **Google BigQuery**, models it into a **Star Schema**, and finally visualizes it through **Streamlit** and **Looker Studio dashboards**.

---

## Objectives

- Extract, clean, and integrate data from multiple sources.
- Simulate daily inventory changes and restocking.
- Store and model data in BigQuery using dimensional modeling.
- Calculate core supply chain KPIs.
- Build dashboards for real-time analytics.

---

## Project Structure

```
supply_chain_project/
├── data/                     # Raw Excel & generated CSVs
│   └── Global_Superstore.xlsx, orders.csv, inventory.csv, returns.csv, people.csv
├── src/                      # Python ETL scripts
│   ├── load_global_superstore.py
│   ├── inventory_simulator.py
│   └── etl_pipeline.py
├── bigquerry/                # BigQuery interaction scripts
│   ├── bq_loader.py
│   └── create_star_schema.py
├── dashboard/                # Streamlit dashboard script
│   └── dashboard.py
├── service_account.json      # Google Cloud credentials
└── README.md                 # Project documentation
```

---

## System Architecture

```
┌──────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│ Excel Data (XLSX)│    │ API (Fake Store) │    | Inventory Simulation│
└──────────────────┘    └──────────────────┘    └─────────────────────┘
        │                      │                         │
        ▼                      ▼                         ▼
┌────────────────────────────────────────────────────────────────┐
│ ETL Pipeline                                                    
│ (load_global_superstore.py, inventory_simulator.py, etl_pipeline.py) 
└────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────┐
│ Google BigQuery Storage │
└─────────────────────────┘
          │
          ▼
┌───────────────────────────┐
│ Star Schema & Data Marts  │
└───────────────────────────┘
          │
          ▼
┌───────────────────────┐
│ Analytics & Dashboards│
└───────────────────────┘
```

---

## Features

### 1. Data Extraction & Integration
- Load **Orders, Returns, People** sheets from the Global Superstore Excel file.
- Fetch product data from the Fake Store API.
- Simulate daily inventory levels for 30 days with restocking every 7 days.
- Save all processed data as `.csv` for further loading.

### 2. Data Storage & Modeling
- Upload CSVs into Google BigQuery tables.
- Create a **Star Schema**:
  - **Fact Tables**: Orders, Inventory
  - **Dimension Tables**: Product, Customer, Date
- Partition and cluster tables for query performance.

### 3. Supply Chain Metrics
- Lead Time: Time from order to shipment.
- Order Cycle Time: Time from order to delivery.
- Inventory Turnover & Days on Hand.
- On-Time Delivery Rate & Order Fill Rate.
- Sales by Category, Country, and Product.

### 4. Data Marts & Analytics
- Vendor Performance
- Inventory Analysis
- Order Fulfillment
- Product Category Performance
- Shipping and Logistics Performance

### 5. Visualization & Monitoring
- **Streamlit Dashboard**: KPIs, inventory trends, category sales.
- **Looker Studio**: Geographic shipping performance, interactive category & country-level analytics.

---

## Tech Stack

- Python (pandas, requests, streamlit, google-cloud-bigquery)
- Google BigQuery (Data Warehouse)
- Excel (Global Superstore dataset)
- REST API (Fake Store API)
- Streamlit (Web Dashboard)
- Looker Studio (Data Visualization)
- Git (Version Control)

---

## How to Run

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/supply_chain_project.git
cd supply_chain_project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run ETL Pipeline
```bash
python src/etl_pipeline.py
```

### 4. Upload to BigQuery
```bash
python bigquerry/bq_loader.py
```

### 5. Create Star Schema
```bash
python bigquerry/create_star_schema.py
```

### 6. Run Dashboard
```bash
streamlit run dashboard/dashboard.py
```

---

## Example Dashboards

**Streamlit**
- Sales by category
- Inventory restocking
- Total sales and orders KPIs

**Looker Studio**
- Geographic sales map
- Product category performance
- Country-wise sales trend

---

## Project Status

- Data Extraction - Completed
- Inventory Simulation - Completed
- BigQuery Loading - Completed
- Star Schema Modeling - Completed
- KPI Calculation - Completed
- Streamlit Dashboard - Completed
- Looker Studio Dashboard - Completed
