from Managers import Database, Preferred_manager
import streamlit as st

# --Managers--

db = Database()
preferred_manager = Preferred_manager(db)

# --Properties--

table = preferred_manager.get_table()

# --UI--

st.title("요일별 선호 음식")
st.sidebar.markdown("Preferred Lunch Menu by day of the week")
st.table(table)

# --Logic--

db.close_connection()
