from jerry_lunch.managers import Database, Sync_manager
import streamlit as st

## --Managers--

db = Database()
sync_manager = Sync_manager(db)

## --UI--

st.title("Sync")
st.sidebar.markdown("Sync")
st.markdown(""" 
### 모두의 점심 데이터를 비교하고 합칩니다.
""")

is_tapped_sync_button = st.button("데이터 동기화")

## --Logic--

if is_tapped_sync_button:
    df, success_cnt, new_data_cnt, duplcated_data_cnt = sync_manager.get_data()
    if not df.empty:
        st.success(f"동기화 완료 - 새로운 원천 {success_cnt} 곳에서 총 {new_data_cnt} 건을 새로 추가하였습니다.")
        if duplcated_data_cnt:
            st.warning(f"중복 데이터 제거 완료 - {duplcated_data_cnt} 건")
        st.dataframe(df)
    else:
        st.error("시스템 에러가 발생했습니다.")
        