from jerry_lunch.managers import Database, Statistics_manager
import streamlit as st

# --Managers--

db = Database()
statistics_manager = Statistics_manager(db)

# --Properteis--

chart = statistics_manager.get_chart()
table = statistics_manager.get_table()

# --UI--

st.title("점심 입력 수 통계")
st.sidebar.markdown("Statistics Lunch Menu")

st.markdown("## Chart")
if chart:
    st.pyplot(chart)
else:
    st.warning("데이터가 존재하지 않아 통계를 확인할 수 없습니다.")

st.markdown("""
---

## Table
""")
st.table(table)

# --Logic--

db.close_connection()
