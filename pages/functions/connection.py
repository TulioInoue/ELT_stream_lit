from google.cloud import bigquery
from datetime import datetime, timedelta
from google.oauth2 import service_account

# from dotenv import load_dotenv
import os

def get_database(date):

    # load_dotenv()

    type = os.getenv("type")
    project_id = os.getenv("project_id")
    private_key_id = os.getenv("private_key_id")
    private_key = os.getenv("private_key")
    client_email = os.getenv("client_email")
    client_id = os.getenv("client_id")
    auth_uri = os.getenv("auth_uri")
    token_uri = os.getenv("token_uri")
    auth_provider_x509_cert_url = os.getenv("auth_provider_x509_cert_url")
    client_x509_cert_url = os.getenv("client_x509_cert_url")
    universe_domain = os.getenv("universe_domain")

    client = bigquery.Client(
        credentials = service_account.Credentials.from_service_account_info(
            {
                "type": type,
                "project_id": project_id,
                "private_key_id": private_key_id,
                "private_key": private_key,
                "client_email": client_email,
                "client_id": client_id,
                "auth_uri": auth_uri,
                "token_uri": token_uri,
                "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
                "client_x509_cert_url": client_x509_cert_url,
                "universe_domain": universe_domain
            }
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