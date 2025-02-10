import pandas as pd

# Without_manager
class Without_manager:
    def __init__(self, db):
        self.db = db

    def get_str(self):
        data = self.db.get_member_need_enter()

        return data if data else None
