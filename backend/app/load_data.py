# backend/load_data.py
import pandas as pd
from db import db
import asyncio

async def load_csv_to_collection(file_path, collection_name):
    df = pd.read_csv(file_path)
    data = df.to_dict(orient="records")
    collection = db[collection_name]
    await collection.delete_many({})  # Clean existing
    result = await collection.insert_many(data)
    print(f"Inserted {len(result.inserted_ids)} records into {collection_name}")

async def main():
    await load_csv_to_collection("data/users.csv", "users")
    await load_csv_to_collection("data/products.csv", "products")
    await load_csv_to_collection("data/orders.csv", "orders")

if __name__ == "__main__":
    asyncio.run(main())
