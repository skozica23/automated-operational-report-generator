def calculate_basic_kpis(df):

    total_shipments = len(df)

    total_emissions = df["Carbon_Emission_kgCO2e"].sum()

    average_emissions = (
        df["Carbon_Emission_kgCO2e"].mean()
    )

    average_distance = df["Distance_KM"].mean()

    return {
        "total_shipments": total_shipments,
        "total_emissions": total_emissions,
        "average_emissions": average_emissions,
        "average_distance": average_distance
    }

def detect_high_emissions(df):

    df["Emission_per_KM"] = (
        df["Carbon_Emission_kgCO2e"]
        / df["Distance_KM"]
    )

    threshold = (
        df["Emission_per_KM"].mean() * 2
    )

    anomalies = df[
        df["Emission_per_KM"] > threshold
    ]

    return anomalies