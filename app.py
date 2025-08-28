import streamlit as st

page_main = st.Page("main.py", title="다문화 레시피 변환 AI", icon="🍲")
page_1 = st.Page("p1.py", title="나라별 레시피 추천", icon="🧀")
page_2 = st.Page("p2.py", title="한국식 레시피 변환", icon="🧀")
page_3 = st.Page("p3.py", title="지역 기반 맛집 추천", icon="🧀")
page_4 = st.Page("p4.py", title="입맛 기반 음식 추천", icon="🧀")
page_5 = st.Page("p5.py", title="나라별 음식 문화 탐방", icon="🧀")


page = st.navigation([page_main, page_1, page_2,
                      page_3, page_4, page_5])
page.run()