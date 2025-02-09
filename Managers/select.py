import pandas as pd

# Select_manager
class Select_manager:
    def __init__(self, db):
        self.db = db

    def get_table(self) -> pd.DataFrame:
        lunch_menus = self.db.get_lunch_menus()
        lunch_menus_dict = [vars(lunch_menu) for lunch_menu in lunch_menus]

        df = (
            pd.DataFrame(lunch_menus_dict)
            .drop(columns=['id'])
            .sort_values(by='date', ascending=False)
            .reset_index(drop=True)
        )

        return df
