# LunchMenu Data Model
class LunchMenu:
    def __init__(self, menu_name: str, member_name: str, date: str, id: int=None):
        self.id = id
        self.menu_name = menu_name
        self.member_name = member_name
        self.date = date
