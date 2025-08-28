import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI
from PIL import Image
import base64

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")
    st.stop()

client = OpenAI(api_key=api_key)

st.markdown("""
<style>
  [data-testid="stAppViewContainer"] { background-color: #FFF7E6; }
  [data-testid="stHeader"] { background-color: rgba(0,0,0,0); }
  [data-testid="stSidebar"] { background-color: #FFE4B5; }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("👩‍🍳 음식 변환 페이지")
st.title("🍕 외국 음식 → 한국식 레시피 변환")

uploaded_img = st.file_uploader("외국 음식 사진을 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_img:
    image = Image.open(uploaded_img)
    st.image(image, caption="업로드된 음식 사진", width=800)

    img_bytes = uploaded_img.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode()
    data_url = f"data:image/png;base64,{img_base64}"

    messages = [
        {
            "role": "system",
            "content": "당신은 외국 음식을 한국식으로 재해석하는 요리사입니다. 결과는 한국어로만 작성해주세요."
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": """
1. 업로드된 사진 속 음식이 무엇인지 알려주세요.
2. 그 음식이 어떤 외국 음식인지 간단히 설명해주세요.
3. 한국식 레시피를 제안해주세요.
   - 한국에서 쉽게 구할 수 있는 재료 사용
   - 조리법은 간단명료하게
   - 원래 음식의 특징 유지 + 한국적 맛 반영
                """},
                {"type": "image_url", "image_url": {"url": data_url}}
            ]
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=700
    )

    st.subheader("📖 변환 결과")
    st.write(response.choices[0].message.content)