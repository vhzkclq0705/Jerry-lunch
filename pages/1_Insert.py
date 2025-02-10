from Managers import Database, Insert_manager
import streamlit as st

# --Managers--

db = Database()
insert_manager = Insert_manager(db)

# --UI--

st.title("점심 메뉴 기입")
st.sidebar.markdown("Insert Lunch Menu")

menu_name = st.text_input("메뉴 이름", placeholder="ex) 설렁탕")
member_name = st.selectbox("먹은 사람", insert_manager.get_members())
dt = st.date_input("날짜")
is_tapped_save_button = st.button("저장")

# --Logic--

if is_tapped_save_button:
    if menu_name and member_name and dt:
        try:
            insert_manager.save_lunch_menu(menu_name, member_name, dt)
            st.success('저장 완료!')
        except Exception as e:
            st.error("중복된 데이터이거나 시스템 에러가 발생했습니다.")
            st.error(f'error message: {str(e)}')
    else:
        st.warning("모든 값을 입력해주세요.")

db.close_connection()
