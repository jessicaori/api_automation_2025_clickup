import os
from dotenv import load_dotenv

api_data = {}
load_dotenv()
secret_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
team_id = os.getenv('TEAM_ID')
headers = {
    "Authorization": f"{secret_key}",
    "accept": "application/json",
    "content-type": "application/json"
}
api_data['headers'] = headers
api_data['base_url'] = base_url
api_data['team_id'] = team_id