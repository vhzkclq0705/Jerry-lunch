import pandas as pd
import pytz

# Preferred_manager
class Preferred_manager:
    def __init__(self, db):
        self.db = db

    def get_preferred_menu_by_weekdays(self) -> pd.DataFrame:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        data = db.select_data()
        df = pd.DataFrame(data, columns=['menu_name', 'dt'])
    
        df['date'] = pd.to_datetime(df['date'])
        df['day_of_week'] = df['date'].dt.day_name()

        grouped_df = df.groupby(['day_of_week', 'menu_name']).size().reset_index(name='count')
        grouped_df['day_of_week'] = pd.Categorical(grouped_df['day_of_week'], categories=weekdays, ordered=True)
        sorted_df = grouped_df.sort_values('day_of_week')

        return sorted_df
