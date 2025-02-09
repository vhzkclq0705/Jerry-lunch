import pandas as pd

# Preferred_manager
class Preferred_manager:
    def __init__(self, db):
        self.db = db

    def get_table(self) -> pd.DataFrame:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        data = self.db.get_lunch_menus()
        
        df = pd.DataFrame(data, columns=['menu_name', 'date'])
        df['date'] = pd.to_datetime(df['date'])
        df['day_of_week'] = df['date'].dt.day_name()
        df = df.groupby(['day_of_week', 'menu_name']).size().reset_index(name='count')
        df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=weekdays, ordered=True)
        df = df.loc[df.groupby('day_of_week')['count'].idxmax()].reset_index(drop=True)

        return df
