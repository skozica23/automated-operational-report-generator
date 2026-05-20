from src.data_loader import load_data

from src.analyzer import (
    calculate_basic_kpis,
    detect_high_emissions
)

from src.visualizer import (
    vehicle_emission_chart
)

from src.report_generator import (
    generate_text_report
)


df = load_data(
    "data/ecommerce_logistics_carbon_emissions_v1.csv"
)

# KPI Calculation
kpis = calculate_basic_kpis(df)

print("\n=== BASIC KPIs ===")

for key, value in kpis.items():
    print(f"{key}: {value}")


# Generate Charts
vehicle_emission_chart(df)


# Detect Operational Anomalies
anomalies = detect_high_emissions(df)

print("\n=== HIGH EMISSION ANOMALIES ===")

print(
    anomalies[
        [
            "Transaction_ID",
            "Vehicle_Type",
            "Distance_KM",
            "Carbon_Emission_kgCO2e",
            "Emission_per_KM"
        ]
    ].head(10)
)

print(
    "\nOperational report generation completed."
)

generate_text_report(
    kpis,
    anomalies
)