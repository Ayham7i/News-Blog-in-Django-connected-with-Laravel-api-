import requests

class ApiService:
    def __init__(self):
        self.base_url = 'http://127.0.0.1:8000/api/'  

    def get_articles(self):
        response = requests.get(f'{self.base_url}articles')
        if response.status_code == 200:
            return response.json()
        return []

    def get_article(self, article_id):
        response = requests.get(f'{self.base_url}articles/{article_id}')
        if response.status_code == 200:
            return response.json()
        return None
