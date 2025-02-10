from Managers import Database, Select_manager
import streamlit as st

# --Managers--

db = Database()
select_manager = Select_manager(db)

# --Properties--

table = select_manager.get_table()

# --UI--

st.title("점심 메뉴 데이터")
st.sidebar.markdown("Select Lunch Menu")
st.table(table)

# --Logic--

db.close_connection()
