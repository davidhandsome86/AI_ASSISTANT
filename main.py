import json
from Get_time import *
from Get_location import *
from Get_weather import *
from Get_web import *
from Get_email import *
import Tools
from chat_completion_request import chat_completion_request

def main(question):
    messages = []
    messages.append({"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."})
    messages.append({"role": "user", "content": question})
    chat_response = chat_completion_request(
            messages, tools=Tools.tools, tool_choice="auto", 
    )
    message_origin = messages
    try:
        assistant_message = chat_response.json()["choices"][0]["message"]
        tool_call = assistant_message.get("tool_calls")
        if tool_call:
            messages.append(assistant_message)
            name = tool_call[0].get("function").get("name")
            arguments = tool_call[0].get("function").get("arguments")
            arguments = json.loads(arguments)
            para = ''
            if arguments:
                for value in arguments.values():
                    para = para + '"' + value + '"' +','
            if para:
                para = para[:-1]
                name = name + '(' +  para  + ')'
            else:
                name = name + '()'
            tool_response = eval(name)
            messages.append({"tool_call_id": tool_call[0]["id"], "role": "tool", "name": tool_call[0]["function"]["name"], "content": tool_response})
            second_response = chat_completion_request(
                    messages, tools=Tools.tools, tool_choice=None, 
            )
            try:
                content = second_response.json()["choices"][0]["message"]["content"]
            except Exception as e:
                #content = "Sorry, please ask in other way"
                content = "不好意思,请换个方式提问"
        else:
            chat_response = chat_completion_request(
                message_origin, 
            ) 
            content = chat_response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        chat_response = chat_completion_request(
                message_origin, 
        ) 
        content = chat_response.json()["error"]["message"]
    return content