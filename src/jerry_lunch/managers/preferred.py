import pandas as pd

# Preferred_manager
class Preferred_manager:
    def __init__(self, db):
        self.db = db

    def get_table(self) -> pd.DataFrame:
        weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일']
        weekdays_mapping = {
            "Monday": "월요일",
            "Tuesday": "화요일",
            "Wednesday": "수요일",
            "Thursday": "목요일",
            "Friday": "금요일"
        }
        data = self.db.get_lunch_menus()
        
        df = pd.DataFrame(data, columns=['menu_name', 'date'])
        df['date'] = pd.to_datetime(df['date']).dt.tz_localize('Asia/Seoul')
        df['day_of_week'] = df['date'].dt.day_name().map(weekdays_mapping)
        df = df.groupby(['day_of_week', 'menu_name']).size().reset_index(name='count')
        df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=weekdays, ordered=True)
        df = df.loc[df.groupby('day_of_week')['count'].idxmax()].reset_index(drop=True)

        return df
