import pandas as pd

# Rank_manager
class Rank_manager:
    def __init__(self, db):
        self.db = db

    def get_rank_of_lunch(self) -> pd.DataFrame:
        data = db.select_data()
        df = pd.DataFrame(data, columns=['menu_name'])
        grouped_df = df.groupby('menu_name').size().reset_index(name='count')
        sorted_df = grouped_df.sort_values(by='count', ascending=False)

        return sorted_df
