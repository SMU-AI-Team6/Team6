import streamlit as st
import textwrap

from MyLLM import geminiModel

st.set_page_config(page_title="맛집 추천 AI", page_icon="🍽️", layout="wide")

st.sidebar.markdown("🍽️ 맛집 추천 AI")

# 페이지 제목
st.title("지역 기반 맛집 추천 AI")
st.write("추천받을 지역을 입력하면 5가지 카테고리별 맛집을 추천해드립니다!")

# 지역 입력
location = st.text_input("📍추천받을 지역 입력:")

if location.strip():
    with st.spinner("추천 중... 🍴"):
        # 프롬프트 작성
        prompt = textwrap.dedent(f"""
            당신은 맛집 전문가입니다. 사용자가 입력한 지역 "{location}"을(를) 기준으로
            5가지 카테고리(한식, 양식, 일식, 카페/디저트, 이색음식)로 나누어
            각 카테고리별로 인기 맛집 2곳씩 추천해주세요.
            출력은 다음과 같이 해주세요:

            🍲 [카테고리명]
            - 가게 이름1: 간단 설명
            - 가게 이름2: 간단 설명
        """)

        try:
            # Gemini 모델 불러오기
            model = geminiModel()

            # Gemini는 문자열 프롬프트로 직접 요청
            response = model.generate_content(prompt)

            st.markdown("### 추천 결과")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"추천 중 오류가 발생했습니다: {e}")
