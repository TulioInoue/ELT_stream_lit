from google.cloud import bigquery
from datetime import datetime, timedelta
from google.oauth2 import service_account

from dotenv import load_dotenv
import os
import ast

def get_database(date):

    load_dotenv()  # Carrega as variáveis do .env
    google_cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    print("google_cred_path:", google_cred_path)

    credential = ast.literal_eval(google_cred_path)

    print("credential:", credential, type(credential))

    client = bigquery.Client(
        credentials = service_account.Credentials.from_service_account_info(
            credential
        )
    )

    # Converter para objeto datetime
    date_after = datetime.strptime(
        str(date),
        "%Y-%m-%d"
    ) + timedelta(
        days = 1
    )

    date_after_str = date_after.strftime("%Y-%m-%d")

    query = f"""SELECT
        *
    FROM
        `dulcet-cable-412812.AulaPython.api-atmosfera`
    WHERE
        localtime >= '{date}' AND localtime < '{date_after_str}'"""

    result = client.query(
        query = query
    )

    return result.to_dataframe()