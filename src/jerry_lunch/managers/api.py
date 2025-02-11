import requests
from jerry_lunch import constants as cons

# API_manager
class API_manager:
    def __init__(self, db):
        self.db = db
        self.headers = {
            'accept': 'applicaation/json'
        }
    
    def get_age(self, date):
        url = f'{cons.API_AGE}/{date}'
        print(url)
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            data = response.json()
            age = data['age']
            k_age = data['kage']
            
            return (age, k_age)
        else:
            return None
    