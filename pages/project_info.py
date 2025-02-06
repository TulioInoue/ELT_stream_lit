import streamlit as st

st.write(f"""
<h2>Project Overview</h2>
<p>This ETL (Extract, Transform, Load) project aims to collect, store, and analyze atmospheric conditions in the 50 most famous cities worldwide. The main objective is to raise awareness of air pollution's impact on human health and the environment by monitoring toxic gas concentrations (O3, SO2, NO2, CO) and their potential risks. The project is entirely developed in Python and leverages various Google Cloud services to automate data collection and visualization.</p>
<p>The dataset was collected from the beginning to the end of May 2024 and is available for download on Kaggle: <a href="https://www.kaggle.com/datasets/tuliocarvalho/air-condition-dataset/data">Air Condition Dataset</a>.</p>

<h2>Project Workflow</h2>
<p>This project follows a structured ETL pipeline using the following technologies:</p>

<h3>1. Extract - Data Collection from Weather API</h3>
<ul>
    <li>The <strong>Weather API</strong> is used to collect real-time weather and air quality data for 50 major cities worldwide.</li>
    <li>The API provides details such as temperature, humidity, wind speed, and concentrations of harmful gases (O3, SO2, NO2, CO).</li>
    <li>The Python script fetches data every hour for continuous monitoring.</li>
</ul>

<h3>2. Transform - Processing Data for Storage</h3>
<ul>
    <li>The retrieved data is pre-processed to clean and structure it properly.</li>
    <li>Data transformations include converting timestamps, handling missing values, and normalizing units for consistency.</li>
    <li>Additional geographic metadata is integrated to provide context on the city's environment.</li>
</ul>

<h3>3. Load - Storing Data in Google Cloud BigQuery</h3>
<ul>
    <li>The processed data is stored in <strong>Google Cloud BigQuery</strong>, allowing efficient querying and analysis.</li>
    <li>BigQuery's scalability ensures that large datasets can be handled with ease, making it ideal for long-term monitoring.</li>
</ul>

<h3>4. Automating Data Collection with Google Cloud Functions & Scheduler</h3>
<ul>
    <li>The Python script responsible for querying the Weather API is deployed as a <strong>Google Cloud Function</strong>.</li>
    <li><strong>Google Cloud Scheduler</strong> is used to trigger this function every hour via an HTTP request, ensuring automated data updates without manual intervention.</li>
</ul>

<h3>5. Visualization and Dashboard with Streamlit</h3>
<ul>
    <li>A <strong>Streamlit dashboard</strong> provides an interactive visualization of air quality trends and weather conditions.</li>
    <li>Users can filter data by city, date, and specific pollutants to understand how air quality varies over time.</li>
    <li>The dashboard also includes insights into the potential health risks of different pollution levels, helping raise awareness of air quality's impact on human health.</li>
</ul>

<h2>Importance of the Project in Data Science</h2>
<p>This project demonstrates the core principles of an ETL pipeline, which is essential for data engineering and data science careers. Key takeaways include:</p>
<ul>
    <li><strong>API Integration</strong>: Automating real-time data collection from an external API.</li>
    <li><strong>Cloud Computing</strong>: Using Google Cloud services for efficient data storage, processing, and scheduling.</li>
    <li><strong>Big Data Management</strong>: Storing large datasets in BigQuery and optimizing query performance.</li>
    <li><strong>Data Visualization</strong>: Creating meaningful insights through interactive dashboards.</li>
    <li><strong>Environmental and Health Awareness</strong>: Understanding how air pollution impacts public health and advocating for cleaner urban environments.</li>
</ul>

<h2>Conclusion</h2>
<p>This project bridges environmental science and data analytics by providing a comprehensive view of air quality in major cities. By leveraging cloud technologies and automation, it presents a scalable and insightful solution for tracking atmospheric conditions and their health implications. The dataset is publicly available on Kaggle, allowing researchers, policymakers, and citizens to explore air pollution trends and make informed decisions.</p>
""", unsafe_allow_html=True)