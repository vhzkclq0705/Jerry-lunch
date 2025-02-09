from Mocel.lunch_menu import LunchMenu

# Insert_manager
class Insert_manager:
    def __init__(self, db):
        self.db = db
        self.member_dict = db.get_member_dict()

    def get_members(self) -> list:
        return list(member_dict.keys())

    def save_lunch_menu(self, menu_name: str, member_name: str, dt: str):
        member_id = member_dict[member_name]
        lunch_menu = LunchMenu(member_name=member_name, member_id=member_id, dt=dt)

        self.db.insert_data(lunch_menu)
