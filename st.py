import streamlit as st
from main import main

st.title("💬 AI助理")
st.caption("🚀 由OPENAI提供大模型支持的AI助理")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "您好，有什么可以帮您?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "您好，有什么可以帮您?"}]
st.sidebar.button('清空聊天记录', on_click=clear_chat_history)


if (prompt := st.chat_input()):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = main(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

