from Model.lunch_menu import LunchMenu

# Insert_manager
class Insert_manager:
    def __init__(self, db):
        self.db = db
        self.member_dict = db.get_member_dict()

    def get_members(self) -> list:
        return list(self.member_dict.keys())

    def save_lunch_menu(self, menu_name: str, member_name: str, dt: str):
        lunch_menu = LunchMenu(menu_name=menu_name, member_name=member_name, date=dt)
        self.db.insert_data(lunch_menu)
