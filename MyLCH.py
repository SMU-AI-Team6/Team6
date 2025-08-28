import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
import os
import time
from openai import OpenAI
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

from p4 import client

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI LLM
def getOpenAI():
    llm = ChatOpenAI(temperature=0, model_name='gpt-4o')
    return llm

# Progress Bar
def progressBar(txt):
    progress_text = txt
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.08)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    return my_bar

# TTS 생성
def openAiModel():
    client = OpenAI(api_key=OPENAI_API_KEY)
    return client

def makeAudio(text, path):
    # path: 최종 파일 경로 (ex: "audio/temp.mp3")
    path = "audio/temp.mp3"
    folder = os.path.dirname(path)
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = client.audio.speech.create(
        model="tts-1",
        input=text,
        voice="echo",
        response_format="mp3",
        speed=1.2,
    )
    response.stream_to_file(path)


# --------------------------
# 페이지 제목 및 사이드바
# --------------------------
st.markdown("## 🍲 나라별 음식문화 Q&A")
st.sidebar.markdown("### 🌏 음식문화 질의응답")

# --------------------------
# 사용자 입력
# --------------------------
country = st.selectbox(
    "질문할 나라를 선택하세요",
    ["한국", "일본", "중국", "인도", "이탈리아", "미국", "멕시코", "프랑스", "태국"],
    key="country_select"
)

text = st.text_area(
    label="질문 입력:",
    placeholder=f"{country}의 전통 음식이나 음식문화를 물어보세요.",
    key="question_input"
)

# --------------------------
# SEND 버튼 클릭 시
# --------------------------
if st.button("SEND", key="send_button"):
    if text:
        st.info(f"질문: {text}")

        # 입력한 질문 음성 변환
        makeAudio(text, "temp.mp3")
        st.audio("audio/temp.mp3", autoplay=True, format="audio/mp3", key="audio_input")

        # OpenAI LLM과 도구 초기화
        openllm = getOpenAI()
        tools = load_tools(['wikipedia'], llm=openllm)
        agent = initialize_agent(
            tools,
            openllm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False,
            handle_parsing_errors=True
        )

        # 진행 표시
        my_bar = progressBar("답변 생성 중...")

        # 질문 실행
        result = agent.run(text)

        # 결과 표시 및 음성 변환
        st.subheader("💬 답변")
        st.info(result)
        makeAudio(result, "result.mp3")
        st.audio("audio/result.mp3", autoplay=True, format="audio/mp3", key="audio_result")

        # 진행바 제거
        my_bar.empty()
    else:
        st.warning("질문을 입력해주세요.", key="warning_no_text")
