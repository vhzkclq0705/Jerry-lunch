import pandas as pd
import requests
from .api import API_manager
from .database import Database
from jerry_lunch import constants as cons

# Sync_manager
class Sync_manager:
    def __init__(self, db):
        self.db = db
        self.headers = {
            'accept': 'application/json'
        }
        
    def get_my_data(self) -> pd.DataFrame:
        my_data = self.db.select_data()
        df = pd.DataFrame(my_data)
        return df
                             
    def get_data(self):
        cur_df = self.get_my_data()
        endpoints = self.get_endpoints()
        
        success_cnt = 0
        total_data_cnt = 0
        duplicated_data_cnt = 0
        
        for endpoint in endpoints:
            response = requests.get(endpoint['url'], headers=self.headers)
            if response.status_code == 200:
                success_cnt += 1
                data = response.json()
                new_df = pd.DataFrame(data)
                cur_df, cnt = self.calculate_data(cur_df, new_df)
                
                total_data_cnt += len(new_df)
                duplicated_data_cnt += cnt
                
        cur_df['dt'] = cur_df['dt'].astype(str)
        df = cur_df.sort_values(by='dt', ascending=False).reset_index(drop=True)
        
        return (df, success_cnt, total_data_cnt - duplicated_data_cnt, duplicated_data_cnt)
    
    def get_endpoints(self):
        response = requests.get(cons.ENDPOINTS_URL, headers=self.headers)
        if response.status_code == 200:
            return response.json()['endpoints']
    
    def calculate_data(self, df1: pd.DataFrame, df2: pd.DataFrame):
        df2['name'] = df2['name'].str.upper()
        duplicated_data_cnt = len(pd.merge(df1, df2, on=['menu_name', 'name', 'dt'], how="inner"))
        df = pd.concat([df1, df2], ignore_index=True).drop_duplicates()
        
        return (df, duplicated_data_cnt)
        

