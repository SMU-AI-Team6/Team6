
import streamlit as st
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationSummaryMemory
from streamlit_chat import message
from MyLCH import getOpenAI  # 사용자 정의 OpenAI 래퍼

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

st.title("💬 AI와 함께하는 음식 문화 탐방")
st.sidebar.markdown("✈️ 나라별 음식 문화 및 예절")

# 메모리 초기화
if 'MEMORY' not in st.session_state:
    memory = ConversationSummaryMemory(
        llm = getOpenAI(),
        return_messages=True
    )
    st.session_state['MEMORY'] = memory

chain = ConversationChain(llm=getOpenAI(), memory=st.session_state['MEMORY'])

# 대화 실행 함수
def conversational_chat(query):
    result = chain.predict(input=query)
    st.session_state['chathistory'].append((query, result))
    # 오디오 생성 코드 (선택)
    # makeAudio(result, "audio/last_response.mp3")

# 채팅 이력 초기화
def init_chathistory():
    st.session_state['chathistory'] = [(
        "안녕하세요!",
        "안녕하세요! 저는 세계 각국의 음식 문화와 예절을 소개하는 챗봇이에요. 나라 이름을 입력해보세요! 예: 일본, 프랑스, 인도 등"
    )]

if 'chathistory' not in st.session_state:
    init_chathistory()

# 입력 영역
container = st.container()
response_container = st.container(border=True)

with container:
    with st.form(key='Conv_Question', clear_on_submit=True):
        user_input = st.text_input("나라 이름을 입력해 주세요", placeholder="예: 일본, 프랑스, 인도...", key='input')
        submit_button = st.form_submit_button(label='Send')
    if submit_button and user_input:
        conversational_chat(f"{user_input}의 음식 문화나 식사 예절에 대해 알려줘.")
    if st.button("Clear"):
        init_chathistory()

# 출력 영역
if st.session_state['chathistory']:
    with response_container:
        for i in range(len(st.session_state['chathistory']) - 1, -1, -1):
            message(st.session_state['chathistory'][i][1], key=str(i), avatar_style="bottts")
            message(st.session_state['chathistory'][i][0], is_user=True, key=str(i) + '_user', avatar_style="fun-emoji")

