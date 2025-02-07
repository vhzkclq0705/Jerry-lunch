import pandas as pd

# Statistics_manager
class Statistics_manager:
    def __init__(self, data):
        self.data = data
        self.initial_df = pd.DataFrame(data, columns=['menu_name', 'member_name', 'date'])

    def get_initial_df(self) -> pd.DataFrame:
        return self.initial_df.sort_values(by='date', ascending=False)

    def get_grouped_df(self) -> pd.DataFrame:
        melted_df = self.initial_df.melt(
            id_vars=['member_name'],
            value_vars=['date'],
            value_name='menu'
        )

        grouped_df = self.melted_df.groupby('member_name')['menu'].count().reset_index()
        return grouped_df
