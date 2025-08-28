import streamlit as st
from langchain.adapters import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

from MyLCH import OPENAI_API_KEY
from MyLLM import openAiModel, makeMsg, openAiModelArg

# .env 파일에서 API 키 불러오기
load_dotenv()
openai.api_key= os.getenv("OPENAI_API_KEY")


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

# OpenAI Client 불러오기
def openAiModel():
    client = OpenAI(api_key=OPENAI_API_KEY)
    return client

def makeMsg(system, user):
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]
    return messages

def openAiModelArg(model, msgs):
    client = openAiModel()
    response = client.chat.completions.create(
        model=model,
        messages=msgs
    )
    return response.choices[0].message.content

# Streamlit UI 시작
st.set_page_config(page_title="🌍 나라별 레시피 추천 AI", page_icon="🍳", layout="wide")

st.title("🌍 나라별 레시피 추천 AI")
st.markdown("입력한 재료와 나라를 기반으로 만들 수 있는 요리를 추천하고 레시피를 알려드립니다!")

# 사용자 입력
ingredient = st.text_input("🍅 사용할 주요 재료를 입력하세요 (예: 닭고기, 감자, 두부 등)")
country = st.text_input("나라를 입력하세요 (예: 한국, 일본, 이탈리아 등)")

if st.button("레시피 추천받기"):
    if ingredient.strip() == "" or country.strip() == "":
        st.warning("⚠️ 재료와 나라를 모두 입력해주세요!")
    else:
        with st.spinner("AI가 레시피를 준비 중입니다... 🍴"):
            prompt = f"""
            사용자가 {country} 요리를 원합니다. 주요 재료는 {ingredient} 입니다.
            1) 이 재료로 만들 수 있는 {country} 전통 또는 현지 스타일 요리 이름을 알려주세요.
            2) 그 요리의 상세 레시피를 단계별로 알려주세요.
            3) 필요하면 대체 재료나 요리 팁도 알려주세요.
            출력은 요리 이름과 레시피만 깔끔하게 보여주세요.
            """
            msgs = makeMsg("당신은 전문 셰프입니다.", prompt)
            recipe = openAiModelArg("gpt-4o-mini", msgs)
            st.success("✅ 레시피 추천이 완료되었습니다!")
            st.markdown(recipe)
