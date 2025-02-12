from jerry_lunch.managers import Database, Without_manager
import streamlit as st

# --Managers--

db = Database()
without_manager = Without_manager(db)

# --Properties--

str = without_manager.get_str()

# --UI--

st.title("오늘 메뉴 기입 안 한 사람")
st.sidebar.markdown("Who???")

is_tapped_refer_button = st.button("조회")

# --Logic--

if is_tapped_refer_button:
    if str:
        st.warning(str)
    else:
        st.success("모두 기입하였습니다!")

db.close_connection()
