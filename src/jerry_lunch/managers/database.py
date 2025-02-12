import psycopg
from psycopg.rows import dict_row
from jerry_lunch.config.db_config import db_config
from jerry_lunch.models import LunchMenu

# Database
class Database:
    def execute_query(self, query, data=None) -> list:
        with psycopg.connect(**db_config, row_factory=dict_row) as conn:
            cur = conn.execute(query)
            row = cur.fetchall()
            return row

    def insert_data(self, lunch_menu: LunchMenu):
        members = self.get_member_dict()
        data = (lunch_menu.menu_name, members[lunch_menu.member_name], lunch_menu.date)
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
        results = self.cursor.fetchall()

        return ',  '.join([record[0] for record in results])

    def select_data(self) -> list:
        query = "SELECT * FROM view_select_all"
        data = self.execute_query(query)
        return data

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
