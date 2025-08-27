import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
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

# .env 파일에서 API 키 불러오기
load_dotenv()
google_api_key = os.getenv("OPENAI_API_KEY")

# 이미지 저장 폴더 생성
if not os.path.exists("img"):
    os.makedirs("img")

# 페이지 제목 및 설명
st.sidebar.markdown("🍜음식 추천 및 이미지 생성")
st.title("🍽️입맛 기반 음식 추천 시스템")
st.write("입맛과 원하는 나라를 입력하면 음식과 이미지를 추천해드립니다.")

# 사용자 입력
user_input = st.text_area("입맛을 입력하세요", placeholder="예: 매콤한 국물 추천해 줘 ")
country = st.selectbox("원하는 나라를 선택하세요", ["한국", "일본", "이탈리아", "중국", "인도", "미국", "멕시코"])
image_name = st.text_input("저장할 이미지 파일 이름", placeholder="예: spicy_soup")
num_images = st.number_input("생성할 이미지 개수", min_value=1, max_value=5, step=1)

# 추천 및 생성 버튼
if st.button("음식 추천 & 이미지 생성"):
    if user_input and image_name:
        st.info(f"입력하신 입맛: {user_input}")
        st.info(f"선택한 나라: {country}")

        with st.spinner("음식을 추천하고 이미지를 생성 중입니다..."):

            # Step 1: 음식 추천 프롬프트
            prompt = f"""
            너는 음식 추천 전문가야.
            사용자가 '{user_input}' 라고 말했어.
            이 입맛에 딱 맞는 {country} 음식 하나를 추천해줘.
            음식 이름만 간단히 출력해.
            """

            try:
                # 최신 API 방식에 맞춰 음식 추천 요청
                response = openai.ChatCompletion.create(
                    model="gpt-4",  # 모델 이름을 확인하세요.
                    messages=[{"role": "user", "content": prompt}],  # Prompt가 user 역할로 전달되도록
                    max_tokens=100
                )
                food_name = response['choices'][0]['message']['content'].strip()
                st.success(f"추천 음식: {food_name}")
            except Exception as e:
                st.error(f"음식 추천 실패: {e}")
                st.stop()

            # Step 2: 음식 이미지 생성 프롬프트
            # 음식에 대한 구체적인 프롬프트 작성 (기존 이미지 생성 방식을 더 구체화)
            image_prompt = f"""
            A high-quality, realistic image of a traditional {country} dish called {food_name}. 
            The dish should feature the signature elements of spicy, stir-fried noodles with a rich, red sauce. 
            The noodles should be thick, slightly wavy, and coated with a vibrant red sauce. 
            Include common ingredients like a fried egg on top, sliced green onions, and sesame seeds. 
            The image should focus on the texture of the noodles, the creamy, runny yolk of the egg, and the glossy sheen of the spicy sauce. 
            The food should look appetizing, with a professional food photography style that emphasizes its vibrant colors and delicious appeal.
            """

            # 이미지 생성
            for i in range(num_images):
                try:
                    img_response = openai.Image.create(
                        prompt=image_prompt,
                        n=1,
                        size="512x512"
                    )
                    img_url = img_response['data'][0]['url']

                    # 이미지 저장
                    img_data = requests.get(img_url).content
                    filename = f"img/{image_name}_{i}.png"
                    with open(filename, "wb") as f:
                        f.write(img_data)

                    # 이미지 표시 및 다운로드 버튼
                    st.image(Image.open(BytesIO(img_data)), caption=f"{food_name} (이미지 {i+1})")
                    with open(filename, "rb") as file:
                        st.download_button(
                            label=f"Download {image_name}_{i}.png",
                            data=file,
                            file_name=f"{image_name}_{i}.png",
                            mime="image/png"
                        )

                except Exception as e:
                    st.error(f"이미지 생성 실패: {e}")

    else:
        st.warning("입맛과 이미지 이름을 모두 입력해주세요.")
