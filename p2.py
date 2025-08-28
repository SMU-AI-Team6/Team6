import os
import streamlit as st
from openai import OpenAI
from PIL import Image
import base64
from dotenv import load_dotenv

# --------------------------
# 페이지 스타일 설정
# --------------------------
page_bg = """
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #FFF7E6; /* 배경 색 (연한 크림색) */
    }
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0); /* 헤더 투명하게 */
    }
    [data-testid="stSidebar"] {
        background-color: #FFE4B5; /* 사이드바 배경 (모카색) */
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --------------------------
# 환경 변수에서 OpenAI API 키 로드
# --------------------------
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --------------------------
# 페이지 제목 및 설명
# --------------------------
st.sidebar.markdown("👩‍🍳 음식 변환 페이지")
st.title("🍕외국 음식 → 한국식 레시피 변환")

# --------------------------
# 파일 업로드 (이미지)
# --------------------------
uploaded_img = st.file_uploader("외국 음식 사진을 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_img is not None:
    # 이미지 표시
    image = Image.open(uploaded_img)
    st.image(image, caption="업로드된 음식 사진", use_container_width=True)

    # 이미지 base64 인코딩
    img_bytes = uploaded_img.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    # 이미지에 대한 설명 및 변환 프롬프트
    prompt = """
    1. 업로드된 사진 속 음식이 무엇인지 알려주세요.
    2. 그 음식이 어떤 외국 음식인지 간단히 설명해주세요.
    3. 그 음식을 한국식으로 바꾼 레시피를 제안해주세요.
       - 한국에서 쉽게 구할 수 있는 재료 사용
       - 조리법은 간단명료하게
       - 원래 음식의 특징을 유지하면서 한국적인 맛을 살리기
    """

    try:
        # --------------------------
        # OpenAI Chat Completions (최신 방식)
        # --------------------------
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # 최신 경량 모델 (텍스트 전용)
            messages=[
                {"role": "system", "content": "너는 음식 전문가야."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=700
        )

        result = response.choices[0].message.content.strip()

        # 결과 출력
        st.subheader("📖 변환 결과")
        st.write(result)

    except Exception as e:
        st.error(f"API 호출 중 오류 발생: {e}")
