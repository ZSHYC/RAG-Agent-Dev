from openai import OpenAI

# 1. 获取client对象，配置API Key和Base URL，用于请求阿里云百炼大模型服务，openai库对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 2. 构造请求参数，调用chat.completions.create接口，发起对话式大模型请求
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是一个循循善诱的python编程专家，擅长解决leetcode的题目"},
        {"role": "assistant", "content": "好的，我是一个python专家，请开始回答吧！"},
        {"role": "user", "content": "请用python代码完成冒泡排序算法，并给出详细注释"},
    ]
)

# 3. 打印响应结果，输出对话内容
print(response.choices[0].message.content)