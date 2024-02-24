tools = [
    {
        "type": "function",  #获取当前时间
        "function": {
            "name": "get_current_date",
            "description": "Get the current time,or get today's date",
            "parameters": {
                "type": "object",
                "properties": {
                },
                "required": [],
            },
        }
    },
    {
        "type": "function",  #获取当前地址
        "function": {
            "name": "get_location",
            "description": "Get the current address",
            "parameters": {
                "type": "object",
                "properties": {
                },
                "required": [],
            },
        }
    },
    {
        "type": "function",  #获取当前天气
        "function": {
            "name": "get_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "object",
                "properties": {
                },
                "required": [],
            },
        }
    },
    {
        "type": "function",  #获取几天的天气预报
        "function": {
            "name": "get_weather_n",
            "description": "Get an N-day weather forecast",
            "parameters": {
                "type": "object",
                "properties": {
                    "num_days": {
                        "type": "string",
                        "description": "The number of days to forecast",
                    }
                },
                "required": ["num_days"],
            },
        }
    },
    {
        "type": "function",  #获取问题,并google搜索返回
        "function": {
            "name": "get_web",
            "description": "Get the question's answer from web search",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "user's question",
                    }
                },
                "required": ["question"],
            },
        }
    },
    {
        "type": "function",  #发送电子邮件
        "function": {
            "name": "get_email",
            "description": "Send a email to some address",
            "parameters": {
                "type": "object",
                "properties": {
                    "receiver": {
                        "type": "string",
                        "description": "email address",
                    },
                    "content": {
                        "type": "string",
                        "description": "the contents of the email ",
                    },
                },
                "required": ["receiver", "content"],
            },
        }
    }
]