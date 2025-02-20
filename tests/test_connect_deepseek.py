# 安装必要库（如果未安装）
# pip install langchain-openai

import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# 设置环境变量
os.environ["DEEPSEEK_API_KEY"] = "sk-Y8JXzmhnP6Ij7bbP3SAaHsxkUXV4hnXgoAeCWh9lbIQqqK9w"  # 替换为你的实际API密钥

# 创建DeepSeek客户端
# 注意：需要确认DeepSeek的API端点地址，这里假设为官方提供的地址
chat = ChatOpenAI(
    model_name="deepseek-chat",  # 根据实际模型名称调整
    openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"  # 请确认实际API地址
)

# 构造测试消息
messages = [HumanMessage(content="你好，请介绍一下你自己")]

try:
    # 调用API
    response = chat.invoke(messages)
    
    # 打印结果
    print("API调用成功！响应内容：")
    print(response.content)
    
except Exception as e:
    print("API调用失败，错误信息：")
    print(str(e))