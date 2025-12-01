# Data notes

This project uses the **DataCo Supply Chain** dataset from Kaggle as its source.

- No real customer data is used.
- The raw file contains customer PII such as emails, names and addresses.
- A Python script (`scripts/data_anonymiser.py`) is used to strip these PII fields and export `Global_Logistics_Anonymised.csv` for BI use.

In the Power BI file (`Global_Supply_Chain_Logistics.pbix`), the anonymised data is modelled as:

- `Fact_Orders` – one row per order
- `Dim_Customer` – anonymised customer ID and segment
- `Dim_Product` – product card and category
- `Dim_Geography` – market, region, country, city
- `Dim_ShippingMode` – shipping mode (Same Day, Standard, etc.)
- `Dim_Date` – calendar table

You can reuse the model by pointing Power Query at your own orders file with the same structure.
