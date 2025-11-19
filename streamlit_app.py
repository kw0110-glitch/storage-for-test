import streamlit as st
import base64
from openai import OpenAI

st.write("Hello World")
st.set_page_config(page_title="GPT-5-mini Chat")

st.title("GPT 챗봇")

api_key = st.text_input("OpenAI API Key를 입력하세요", type="password")

user_question = st.text_input("질문을 입력하세요")

if st.button("질문 보내기"):
    if not api_key:
        st.error("먼저 OpenAI API Key를 입력하세요.")
    elif not user_question:
        st.error("질문을 입력하세요.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_question},
                ],
            )

            answer = response.choices[0].message.content
            st.subheader("답변:")
            st.write(answer)

        except Exception as e:
            st.error(f"에러 발생: {e}")

 
st.subheader("이미지 생성")

prompt = st.text_input("이미지 프롬프트를 입력하세요", key="prompt")

if st.button("이미지 생성하기"):
    if not api_key:
        st.error("먼저 OpenAI API Key를 입력하세요.")
    elif not image_prompt:
        st.error("이미지 프롬프트를 입력하세요.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            img = client.images.generate(
                model="gpt-image-1-mini",
                prompt=prompt)

            image_bytes = base64.b64decode(img.data[0].b64_json)

            st.image(image_bytes)

        except Exception as e:
            st.error(f"이미지 생성 중 에러 발생: {e}")