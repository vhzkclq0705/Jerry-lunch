import pandas as pd

# Rank_manager
class Rank_manager:
    def __init__(self, db):
        self.db = db

    def get_table(self) -> pd.DataFrame:
        data  = self.db.get_lunch_menus()

        df = (
            pd.DataFrame(data)
            .groupby('menu_name').size().reset_index(name='count')
            .sort_values(by='count', ascending=False)
            .reset_index(drop=True)
        )

        return df
