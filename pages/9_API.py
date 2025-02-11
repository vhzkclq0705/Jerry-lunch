from Managers import Database, API_manager
import datetime
import streamlit as st

## --Managers--

db = Database()
api_manager = API_manager(db)

## --Properties--

min_date = datetime.date(1960, 1, 1)

## --UI--

st.title("API")
st.sidebar.markdown("API")
st.markdown("""
## 생년월일을 입력하고 나이를 얻어보자.            
""")

date = st.date_input("생일 입력", min_value=min_date)
is_tapped_check_button = st.button("나이 확인")

## --Logic--

if is_tapped_check_button:
    age = api_manager.get_age(date)
    if age:
        st.success(f"만 나이는 {age[0]}세, 연 나이는 {age[1]}세 입니다.")
    else:
        st.error(f"시스템 에러가 발생했습니다.")