import matplotlib.pyplot as plt


def vehicle_emission_chart(df):

    vehicle_emissions = (
        df.groupby("Vehicle_Type")[
            "Carbon_Emission_kgCO2e"
        ]
        .mean()
        .sort_values(ascending=False)
    )

    vehicle_emissions.plot(kind="bar")

    plt.title(
        "Average CO2 Emissions by Vehicle Type"
    )

    plt.xlabel("Vehicle Type")

    plt.ylabel("Average CO2 Emissions")

    plt.tight_layout()

    plt.savefig(
        "charts/vehicle_emissions.png"
    )

    plt.close()