from Managers import Database, Select_manager
import streamlit as st

# --Managers--

db = Database()
select_manager = Select_manager(db)

# --UI--

st.title("점심 메뉴 데이터")
st.sidebar.markdown("Select Lunch Menu")
st.table(select_manager.get_lunch_menus())

# --Logic--

db.close_connection()
