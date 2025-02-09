import psycopg
from config.db_config import db_config
from Model.lunch_menu import LunchMenu

# Database
class Database:
    def __init__(self):
        self.conn = psycopg.connect(**db_config)
        self.cursor = self.conn.cursor()
        self.lunch_menus = self.select_data()

    def get_lunch_menus(self) -> list:
        return self.lunch_menus

    def execute_query(self, query, data=None):
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, lunch_menu: LunchMenu):
        data = (lunch_menu.menu_name, lunch_menu.member_id, lunch_menu.date)
        query = '''
        INSERT INTO lunch_menu (menu_name, member_id, dt)
        VALUES (%s, %s, %s)
        '''
        self.execute_query(query, data)

    def get_member_need_enter(self) -> list:
        query = '''
        select
            m.name
        from
            member m
        left join lunch_menu l
            on m.id = l.member_id and l.dt = current_date
        where
            l.member_id is null
        '''
        self.execute_query(query)

        return ', '.join([record[0] for record in self.cursor.fetchall()])

    def select_data(self) -> list:
        query = '''
        SELECT
            l.id,
            menu_name,
            name,
            dt
        FROM lunch_menu l
        JOIN member m ON l.member_id = m.id
        '''
        self.execute_query(query)

        results = self.cursor.fetchall()
        lunch_menus = [LunchMenu(menu_name=row[1], member_name=row[2], date=row[3], id=row[0]) for row in results]

        return lunch_menus

    # TODO
    def delete_data(self):
        query = f'DELETE INTO lunch_menu'

    # TODO
    def update_data(self):
        query = f'UPDATE INTO lunch_menu'

    def get_member_dict(self) -> dict:
        query = '''
        SELECT jsonb_object_agg(name, id)
        FROM member;
        '''
        self.execute_query(query)
        return self.cursor.fetchone()[0]

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
