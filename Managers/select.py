import pandas as pd

# Select_manager
class Select_manager:
    def __init__(self, db):
        self.db = db

    def get_table(self) -> pd.DataFrame:
        data = self.db.get_lunch_menus()

        df = (
            pd.DataFrame(data)
            .drop(columns=['id'])
            .sort_values(by='date', ascending=False)
            .reset_index(drop=True)
        )

        return df
