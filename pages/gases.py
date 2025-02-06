import streamlit as st
from pages.functions.connection import get_database
from pages.functions.explanation import gas_explanation
from pages.functions.table import table_gas

st.title("Monitoring gases")

st.write("""
    <h3>Why monitor gases?</h3>
    <p>
        Air pollution is a critical global issue, impacting public health, ecosystems, and climate stability. Among the most concerning pollutants are carbon monoxide (CO), nitrogen dioxide (NO₂), ozone (O₃), and sulfur dioxide (SO₂)—each playing a significant role in urban air quality and environmental sustainability. Understanding and tracking these gases is essential for developing data-driven solutions to mitigate their effects.
    </p>
    <p>
        With the rise of real-time sensors, satellite data, and machine learning models, data science has become an indispensable tool for air pollution analysis. Predictive modeling, trend analysis, and geospatial visualization enable researchers, policymakers, and environmental organizations to make informed decisions to reduce emissions and improve air quality.
    </p>
    <h3>Searching for gas concentrations</h3>
    <p>
        Therefore, this page allows anybody to search for any of these gases in a specific date range. The data mining process has only take in considerantion the most 50 popular cities on May 2024.  
    </p>
    <p>
        If you want to see what cities has the most concentration of gases amount all others, you have to select a date and a specific gas and then make your request.
    </p>
         """,
    unsafe_allow_html = True
)

gas = st.selectbox(
    label = "Select a specific gas",
    options = ["co", "no2", "o3", "so2"]
)

st.write(table_gas(gas)["table"], unsafe_allow_html=True)

date = st.date_input(
    label="Select date",
    min_value = "2024-05-02",
    max_value = "2024-05-27"
)

if st.button("Query database"):
    df = get_database(date)

    df = df.sort_values(["name", gas], ascending = False).drop_duplicates("name", keep = "first")

    for row in df.index:
        value = df.loc[row, gas]
        if value < table_gas(gas)["range"]["medium"]:
            df.loc[row, f"{gas}_status"] = "#00FF0055"
        elif value < table_gas(gas)["range"]["high"]:
            df.loc[row, f"{gas}_status"] = "#FFDE2155"
        else: df.loc[row, f"{gas}_status"] = "#FF000055"

    newdf = df
    newdf["co"] = newdf['co']*100
    newdf["no2"] = newdf["no2"]*5000
    newdf["o3"] = newdf['o3']*2000
    newdf["so2"] = newdf["so2"]*1000

    st.header(f"Daily max of {gas.upper()} concentration")
    
    map_df = newdf[["name", "lat", "lon", f"{gas}_status", gas]].groupby(
        by = ["name", "lat", "lon", f"{gas}_status"]
    ).mean().reset_index()

    st.map(
        data = map_df,
        latitude = "lat",
        longitude = "lon",
        size = gas,
        color= f"{gas}_status"
    )

    st.write(gas_explanation(
        gas = gas
    ), unsafe_allow_html = True)