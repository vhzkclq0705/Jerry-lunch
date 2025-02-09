import matplotlib.pyplot as plt
import pandas as pd

# Statistics_manager
class Statistics_manager:
    def __init__(self, db):
        self.db = db
        self.df = self.convert_to_df()

    def convert_to_df(self) -> pd.DataFrame:
        lunch_menus = self.db.get_lunch_menus()
        lunch_menus_dict = [vars(lunch_menu) for lunch_menu in lunch_menus]

        df = (
            pd.DataFrame(lunch_menus_dict)
            .drop(columns=['id'])
            .groupby('member_name').size().reset_index(name='menu')
        )

        return df
   
    def get_table(self) -> pd.DataFrame:
        return self.df
    
    def get_chart(self):
        if self.df.empty:
            return None
        fig, ax = plt.subplots()
        self.df.plot(x='member_name', y='menu', kind='bar', ax=ax)
        ax.set_xticklabels(self.df['member_name'], rotation=45)
        return fig
