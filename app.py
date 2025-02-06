import streamlit as st

pages = {
    "Info": [
        st.Page("./pages/project_info.py", title = "About this project")
    ],
    "Dashboards": [
        st.Page("./pages/gases.py", title="Gases"),
        st.Page("./pages/search.py", title="Searching")
    ],
}

pg = st.navigation(pages)
pg.run()
