from google.cloud import bigquery
import os

# ✅ Step 1: Authenticate using your service account JSON
client = bigquery.Client.from_service_account_json("service_account.json")

# ✅ Step 2: Define your GCP project and dataset
project_id = "supply-chain-project-467705"
dataset_id = "supply_chain_data"

# ✅ Step 3: Define a function to upload CSVs to BigQuery

def upload_csv_to_bigquery(csv_file, table_name):
    table_id = f"{project_id}.{dataset_id}.{table_name}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True  # BigQuery will auto-detect columns and types
    )

    # Open the CSV file in binary read mode and upload to BigQuery
    with open(csv_file, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file, table_id, job_config=job_config
        )

    load_job.result()  # Wait until upload completes
    print(f"✅ Uploaded {os.path.basename(csv_file)} to table: {table_id}")

# ✅ Step 4: Upload raw CSVs to staging/raw tables in BigQuery
data_files = {
    "data/orders.csv": "orders",
    "data/inventory.csv": "inventory",
    "data/returns.csv": "returns",      
    "data/people.csv": "people"          
}

# ✅ Step 5: Loop and upload only if file exists
for filepath, tablename in data_files.items():
    if os.path.exists(filepath):
        upload_csv_to_bigquery(filepath, tablename)
    else:
        print(f"⚠️ File not found: {filepath} — skipping upload.")
