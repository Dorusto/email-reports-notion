import requests

class NotionAPI:
    def __init__(self, api_key, database_id):
        self.api_key = api_key
        self.database_id = database_id
        self.base_url = "https://api.notion.com/v1/databases/"

    def fetch_data(self):
        url = f"{self.base_url}{self.database_id}/query"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()