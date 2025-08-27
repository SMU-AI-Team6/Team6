import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="다문화 레시피 변환 AI", page_icon="🍲", layout="wide")

# 메인 타이틀
st.markdown(
    """
    <h1 style='text-align: center; color: #ff7f50;'>
        🍲 다문화 레시피 변환 AI
    </h1>
    """,
    unsafe_allow_html=True
)

# 서브헤더
st.markdown(
    """
    <h3 style='text-align: center; color: gray;'>
        세계 각국의 요리를 경험해보세요!
    </h3>
    """,
    unsafe_allow_html=True
)

# 이미지나 배너
st.image("https://images.unsplash.com/photo-1600891964599-f61ba0e24092", use_container_width=True)

# 2열 레이아웃
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✨ 주요 기능")
    st.markdown("- 내가 가진 재료로 다른 문화권 음식으로 레시피 변환")
    st.markdown("- 사진 업로드 -> 레시피 변환, 음식 설명")
    st.markdown("- 입맛 입력 -> 여러나라 음식 추천, 이미지 생성")

with col2:
    st.markdown("### 🌍 활용 예시")
    st.markdown("- 한국 요리를 외국 스타일로 변환")
    st.markdown("- 입맛에 맞는 여러나라 음식 경험")
