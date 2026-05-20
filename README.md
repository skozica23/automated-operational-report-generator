# Automated Operational Report Generator

Python-based operational analytics and sustainability reporting tool for logistics datasets.

This project simulates a real-world operational reporting pipeline used in logistics and supply chain environments.  
The application automatically analyzes transport operations, calculates KPIs, detects operational anomalies, generates charts, and creates automated reports.

---

# Features

## Operational KPI Analysis
- Total shipments
- Total CO₂ emissions
- Average emissions per shipment
- Average delivery distance

## Sustainability Analytics
- Vehicle emission comparison
- Route efficiency analysis
- Traffic impact on emissions
- Emission-per-kilometer metrics

## Operational Anomaly Detection
The system automatically detects:
- unusually high-emission deliveries
- inefficient transport operations
- abnormal emission-per-distance ratios

## Automated Reporting
The application automatically:
- loads logistics datasets
- processes operational data
- generates charts
- creates operational reports

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- OpenPyXL
- Jupyter Notebook

---

# Example Business Insights

- Heavy trucks generate the highest average CO₂ emissions
- Traffic congestion significantly increases transport emissions
- Certain route types are less eco-efficient
- Emission-per-kilometer analysis helps identify inefficient operations

---

# Project Structure

```text
automated-operational-report-generator/
│
├── data/
│   └── ecommerce_logistics_carbon_emissions_v1.csv
│
├── reports/
│   └── operational_report.txt
│
├── charts/
│   └── vehicle_emissions.png
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── analyzer.py
│   ├── visualizer.py
│   └── report_generator.py
│
├── README.md
├── requirements.txt
└── main.py