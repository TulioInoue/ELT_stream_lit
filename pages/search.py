import streamlit as st
import pandas as pd
import requests
from pages.functions.kpi import gases_kpi, temperature_kpi
import os


co = {
    "low": 0,
    "medium": 10_000,
    "high": 30_000
}

no2 = {
    "low": 0,
    "medium": 40,
    "high": 100
}

o3 = {
    "low": 0,
    "medium": 100,
    "high": 180
}

so2 = {
    "low": 0,
    "medium": 50,
    "high": 125
}

temperature = {
    "low": 59,
    "medium": 86,
    "high": 158
}

api_key = api_key = os.getenv("API_KEY")

st.title("Make your research")

st.write("""
    <h2>Explanation</h2>
    <p>
        In this page, you can easly get any city wheather status. Each request will generate a http response to a API, and this API will return the current city weather data in order to fulfill a dashboard.
    </p>
""", unsafe_allow_html = True)

city = st.text_input(label = "City name", placeholder = "eg. New York")

if st.button("search"):
    answer = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes")
    answer = answer.json()

    try:

        st.write(f"""
            <section style='background-color: #aaaaaa; height: max-content; display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; border-radius: 10px; box-shadow: 0px 0px 5px #aaaaaa; margin: 10px 0px'>
                <div style='height: 100%; border-radius: 10px; display:flex; flex-direction: column; align-items: center; justify-content: center; gap: 0px;'>
                    <b style='font-weight: bolder; padding: 5px; text-align: center; font-size: 24px'>
                        {answer["location"]["country"]}
                    </b>
                    <b style='font-weight: bolder; padding: 5px; text-align: center; font-size: 20px'>
                        {answer["location"]["name"]}
                    </b>
                </div>
                <div style='height: 100%; text-align: center; border-radius: 10px; display:flex; flex-direction: column; justify-content: center; gap: 10px;'>
                    <p style='padding: 0px; margin: 0px'><b>Date</b></p>
                    <p style='font-size: 20px; padding: 0px; margin: 0px'>
                        📅 {answer["location"]["localtime"].split(" ")[0].replace("-", "/")}
                    </p>
                </div>
                <div style='height: 100%; text-align: center; border-radius: 10px; display:flex; flex-direction: column; justify-content: center; gap: 10px;'>
                    <p style='padding: 0px; margin: 0px;'><b>Hour</b></p>
                    <p style='font-size: 20px; padding: 0px; margin: 0px'>
                        🕒 {answer["location"]["localtime"].split(" ")[1]}
                    </p>
                </div>
                <div style='height: 100%; text-align:center'>
                    <img src = '{answer["current"]["condition"]["icon"]}'/>
                    <p>{answer["current"]["condition"]["text"]}</p>
                </div>
            </section>
        """,
        unsafe_allow_html = True)

        st.map(
            data = pd.DataFrame(
                answer["location"],
                columns = ['country', 'lat', 'localtime', 'localtime_epoch', 'lon', 'name', 'region', 'tz_id'],
                index = [0]
            ),
            latitude = "lan",
            longitude = "lon",
            color = [0, 255, 0, 0.6],
            size = 200
        )

        col1, col2 = st.columns(2)

        col1.write(f"""
            <div style='background-color: #efefef; margin: 10px 0px; padding: 10px; border-radius: 5px; box-shadow: 0px 0px 5px lightgray'>
                <b style='font-size: 32px'>Concentrations:</b>
                <div>
                    <b>Carbon Monoxide (CO):</b>
                    <b>
                        {
                            gases_kpi(
                                value = answer["current"]["air_quality"]["co"],
                                range_dict = co
                            )["icon"]
                        }
                    </b>
                    <b style='color:{
                        gases_kpi(
                            value = answer["current"]["air_quality"]["co"],
                            range_dict = co
                        )["status"]}'>
                        {
                            answer['current']["air_quality"]["co"]
                        } μg/m³
                    </b>
                </div>
                <div>
                    <b>Nitrogen Dioxide (NO₂):</b>
                    <b>
                        {
                            gases_kpi(
                                value = answer["current"]["air_quality"]["no2"],
                                range_dict = no2
                            )["icon"]
                        }
                    </b>
                    <b style='color:{
                        gases_kpi(
                            value = answer["current"]["air_quality"]["no2"],
                            range_dict = no2
                        )["status"]}'>
                        {
                            answer['current']["air_quality"]["no2"]
                        } μg/m³
                    </b>
                </div>
                <div>
                    <b>Ozone (O₃):</b>
                    <b>
                        {
                            gases_kpi(
                                value = answer["current"]["air_quality"]["o3"],
                                range_dict = o3
                            )["icon"]
                        }
                    </b>
                    <b style='color:{
                        gases_kpi(
                            value = answer["current"]["air_quality"]["o3"],
                            range_dict = o3
                        )["status"]}'>
                        {
                            answer['current']["air_quality"]["o3"]
                        } μg/m³
                    </b>
                </div>
                <div>
                    <b>Sulfur Dioxide (SO₂):</b>
                    <b>
                        {
                            gases_kpi(
                                value = answer["current"]["air_quality"]["so2"],
                                range_dict = so2
                            )["icon"]
                        }
                    </b>
                    <b style='color:{
                        gases_kpi(
                            value = answer["current"]["air_quality"]["so2"],
                            range_dict = so2
                        )["status"]}'>
                        {
                            answer['current']["air_quality"]["so2"]
                        } μg/m³
                    </b>
                </div>
            </div>
        """, unsafe_allow_html = True)

        col2.write(f"""
            <div style='background-color: #efefef; margin: 10px 0px; padding: 10px; border-radius: 5px; box-shadow: 0px 0px 5px lightgray'>
                <b style='font-size: 32px'>Temperatures:</b>
                <div>
                    <b>Temperature:</b>
                    <b>
                        {
                            temperature_kpi(
                                value = answer["current"]["temp_f"],
                                range_dict = temperature
                            )["icon"]
                        }
                    </b>
                    <b style='color:{
                        temperature_kpi(
                            value = answer["current"]["temp_f"],
                            range_dict = temperature
                        )["status"]}'>
                        {
                            answer['current']["temp_f"]
                        } ºF
                    </b>
                </div>
                <div>
                    <b>Feels like:</b>
                    <b>
                        {
                            temperature_kpi(
                                value = answer["current"]["feelslike_f"],
                                range_dict = temperature
                            )["icon"]
                        }
                    </b>
                    <b style='color:{
                        temperature_kpi(
                            value = answer["current"]["feelslike_f"],
                            range_dict = temperature
                        )["status"]}'>
                        {
                            answer['current']["feelslike_f"]
                        } ºF
                    </b>
                </div>
                <div>
                    <b>Wind Chill:</b>
                    <b>
                        {
                            gases_kpi(
                                value = answer["current"]["windchill_f"],
                                range_dict = temperature
                            )["icon"]
                        }
                    </b>
                    <b style='color:{
                        gases_kpi(
                            value = answer["current"]["windchill_f"],
                            range_dict = temperature
                        )["status"]}'>
                        {
                            answer['current']["windchill_f"]
                        } ºF
                    </b>
                </div>
                <div>
                    <b>Dew point:</b>
                    <b>
                        {
                            gases_kpi(
                                value = answer["current"]["dewpoint_f"],
                                range_dict = temperature
                            )["icon"]
                        }
                    </b>
                    <b style='color:{
                        gases_kpi(
                            value = answer["current"]["dewpoint_f"],
                            range_dict = temperature
                        )["status"]}'>
                        {
                            answer['current']["dewpoint_f"]
                        } ºF
                    </b>
                </div>
            </div>
        """, unsafe_allow_html = True)



    except:
        st.write("""
            <p style="color:red;">Please, inform a valid city name.</p>
        """,
        unsafe_allow_html = True)
        



