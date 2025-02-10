from Managers import Database, Rank_manager
import streamlit as st

# --Managers--

db = Database()
rank_manager = Rank_manager(db)

# --Properteis--

table = rank_manager.get_table()

## --UI--

st.title("점심 메뉴별 인기 순위")
st.sidebar.markdown("Lunch Menu Rank")
st.table(table)

## --Logic--
db.close_connection()
