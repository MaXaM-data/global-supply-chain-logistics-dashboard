import pandas as pd

df = pd.read_csv("DataCoSupplyChainDataset.csv", encoding="latin-1")

pii_columns = [
    "Customer Email",
    "Customer City",
    "Customer Password",
    "Customer Fname",
    "Customer Lname",
    "Customer Street",
    "Customer State",
    "Customer Zipcode",
    "Order Zipcode",
    "Product Image"
]

df_clean = df.drop(columns=pii_columns, errors="ignore")

df_clean.to_csv("Global_Logistics_Anonymised.csv", index=False)

print("GDPR cleaning complete. Saved as Global_Logistics_Anonymised.csv")
print(f"Original columns: {len(df.columns)}")
print(f"Cleaned columns: {len(df_clean.columns)}")
