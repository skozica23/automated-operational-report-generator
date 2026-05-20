def generate_text_report(
    kpis,
    anomalies
):

    with open(
        "reports/operational_report.txt",
        "w"
    ) as report:

        report.write(
            "=== OPERATIONAL REPORT ===\n\n"
        )

        report.write(
            f"Total Shipments: "
            f"{kpis['total_shipments']}\n"
        )

        report.write(
            f"Total Emissions: "
            f"{kpis['total_emissions']:.2f}\n"
        )

        report.write(
            f"Average Emissions: "
            f"{kpis['average_emissions']:.2f}\n"
        )

        report.write(
            f"Average Distance: "
            f"{kpis['average_distance']:.2f}\n"
        )

        report.write("\n")

        report.write(
            "=== HIGH EMISSION ANOMALIES ===\n\n"
        )

        report.write(
            anomalies[
                [
                    "Transaction_ID",
                    "Vehicle_Type",
                    "Distance_KM",
                    "Carbon_Emission_kgCO2e",
                    "Emission_per_KM"
                ]
            ]
            .head(10)
            .to_string()
        )