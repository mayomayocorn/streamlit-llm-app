from dotenv import load_dotenv
load_dotenv()

"""
「app.py」にコードを記述してください。
画面に入力フォームを1つ用意し、入力フォームから送信したテキストをLangChainを使ってLLMにプロンプトとして渡し、回答結果が画面上に表示されるようにしてください。なお、当コースのLesson8を参考にLangChainのコードを記述してください。
ラジオボタンでLLMに振る舞わせる専門家の種類を選択できるようにし、Aを選択した場合はAの領域の専門家として、またBを選択した場合はBの領域の専門家としてLLMに振る舞わせるよう、選択値に応じてLLMに渡すプロンプトのシステムメッセージを変えてください。また用意する専門家の種類はご自身で考えてください。
「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数を定義し、利用してください。
Webアプリの概要や操作方法をユーザーに明示するためのテキストを表示してください。
Streamlit Community Cloudにデプロイする際、Pythonのバージョンは「3.11」としてください。
"""


import streamlit as st
input_message = st.text_input(label="子どもの教育・栄養に関するお悩みを相談してください")
expertise_area = st.radio("専門家の種類を選択してください", ["教育", "栄養"])

def get_llm_response(input_message, expertise_area):
    if expertise_area == "教育":
        system_message = "あなたは子どもの教育の専門家です。"
    elif expertise_area == "栄養":
        system_message = "あなたは子どもの栄養の専門家です。"
    
    from langchain_openai import ChatOpenAI
    from langchain.schema import SystemMessage, HumanMessage
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_message)
    ]
    
    result = llm(messages)
    return result
if st.button("送信"):
    st.divider()
    result = get_llm_response(input_message, expertise_area)
    st.write("回答結果：")
    st.write(result.content)
