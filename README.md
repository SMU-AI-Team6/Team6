# 🍲 다문화 레시피 변환 AI 

---

## 📋 프로젝트 개요

앱 전체 Home 화면 예시  
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/6de6c40c-a6e8-4a0e-b616-8c05d362d6fc" />
**사용자 맞춤형 다문화 레시피 변환을 통해 음식으로 문화 교류 촉진**  
- 재료 →나라별레시피추천(텍스트, 이미지)
- 음식사진→한국식레시피변환
- 지역별맛집5개의 카테고리 추천
- 입맛에맞는 음식 추천→ 이미지 생성 및저장
- AI와 함께하는 음식문화탐방

---

## 🎯 주요 기능
### 🧀 나라별 레시피 추천
- 입력한 재료와 나라를 기반으로 만들 수 있는 요리 추천 후 레시피 추천
- 나라별 레시피 추천 메인 화면  
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e34f0479-3941-4cbc-80e2-9fed0d996572" />
  
- 나라와 재료 입력 후 레시피 추천 화면
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/50d32840-76ee-425a-aa17-dee5b931b529" />


### 🧀 한국식 레시피 변환
- 외국 음식 사진 업로드 후 한국식 레시피로 변환
- 한국식 레시피 변환 메인 화면  
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a7379496-6077-4068-8451-6a6da87bb346" />

- 사진 업로드 후 화면
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f7ed1a96-f462-4a0e-92f3-8dcf8264afba" />
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d3b68184-53e4-48de-ad43-93facb85d9e3" />

  
### 🧀 지역 기반 맛집 추천 AI
- 추천 지역을 입력하면 5가지 카테고리별 맛집 추천
- 지역 기반 맛집 추천 메인 화면  
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0ed0d22f-ad10-4c72-a0c8-0b2095c5f8a3" />

- 추천 결과 화면
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/24a171ab-0eda-4f16-9cea-25d1e99f7263" />


### 🧀 입맛 기반 음식 추천 시스템
- 입맛과 원하는 나를 입력하면 음식과 이미지 추천 
- 입맛 기반 음식 추천 메인 화면
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7d8a088f-6c42-4b3d-9751-98304ec050ba" />

- 입맛 입력 후 음식 추천 화면
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e2ee5968-ae53-453e-8c14-f50910982101" />


### 🧀 AI와 함꼐하는 음식 문화 탐방
- 나라를 입력하면 챗봇이 세계 각국의 음식 문화와 예절 소개
- AI와 함꼐하는 음식 문화 탐방 메인 화면  
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c16cc93f-512f-4d18-80b2-b34edc32c2ea" />

- 챗봇 대화 화면
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e5c97fef-bf88-4c08-8d5c-0520421a1070" />

---

## 🛠️ 기술 스택

### 📄 프론트엔드

- **Streamlit**: 빠르고 직관적인 웹 UI 프레임워크
- **Streamlit 멀티 페이지 구조**: 다양한 기능(챗봇)을 분리된 페이지로 구현
- **base64.b64encode**: 이미지 업로드 및 처리(리사이즈, 변환 등)

### 🌐 배포 및 협업

- **GitHub**: 코드 버전관리 및 팀원 협업 (커밋 컨벤션, 브랜치 등)
- **Streamlit Cloud/로컬 실행**: 빠른 배포·테스트 환경
- **README.md/사용자 설명서**: 기능, 사용법, 기술 스택 문서화

---

## 💡 사용 방법

1. 프로젝트 폴더에서 아래 명령어로 필수 패키지를 설치합니다.
- `pip install -r requirements.txt`

2. `.streamlit/secrets.toml` 파일에 본인의 OpenAI API 키를 입력합니다.
- OPENAI_API_KEY = “sk-…”

3. 프로젝트 루트에서 Streamlit 앱을 실행합니다.
- `streamlit run app.py`

4. 웹 브라우저에서 [http://localhost:8501](http://localhost:8501/)로 접속하여
음식 추천, 레시피 추천 등 다양한 기능을 직접 사용할 수 있습니다.

---

## 🚨 주의 사항

- **API 키(.streamlit/secrets.toml), 모델 파일(.h5), 환경 설정 등
주요 파일은 깃허브에 업로드하지 마세요!**
- `.gitignore`에 반드시 포함하여 보안 사고와 파일 크기 이슈를 예방하세요.

- 챗봇 AI 답변은 자동 생성된 결과이며, 정확하지 않을 수 있습니다.

- 알레르기는 반영이 안 되므로 주의하세요.

---

## 👨‍💻 개발자 소개

- 그린화학공학과 202321611 임예원
- 그린화학공학과 202321612 전이솔
- 소프트웨어학과 202421231 반시영
- 소프트웨어학과 202421009 조은비
