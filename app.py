import streamlit as st

page_main = st.Page("main.py", title="Main Page")
page_1 = st.Page("p1.py", title="Page 1")
page_2 = st.Page("p2.py", title="Page 2")
page_3 = st.Page("p3.py", title="Page 3")
page_4 = st.Page("p4.py", title="Page 4")

page = st.navigation([page_main, page_1, page_2,
                      page_3, page_4])
page.run()