# LunchMenu Data Model
class LunchMenu:
    def __init__(self, id: int, menu_name: str, member_name: str, date: str):
        self.id = id
        self.menu_name = menu_name
        self.member_name = member_name
        self.date = date
