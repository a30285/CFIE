import json
from main import muti_segment
from prompts.prompt_zh_v1 import prompt_zh_few
from text2neo import faultjson2neo
from py2neo import Graph, Node, Relationship, NodeMatcher

model = "gpt-3.5-turbo"

# 获得本地文本
file_path = "./pdf2text/dataset.txt"  # 将 "your_file_path.txt" 替换为实际的文件路径

# 处理大模型生成结果，json格式化
def res2faultjson(raw_data):
    # 查找第一个 '{' 和最后一个 '}' 的索引
    start_index = raw_data.find('{')
    end_index = raw_data.rfind('}')

    # 获取两个索引之间的字符串内容
    json_content = raw_data[start_index:end_index + 1]
    return json_content

# # 打开文件并读取单行字符串
# with open(file_path, 'r', encoding='utf-8') as file:
#     raw_data = file.readline().strip()

# 使用大模型得到故障相关信息的JSON变量
res_list = muti_segment(prompt_zh_few, model, file_path)

# 连接neo4j数据库
graph = Graph('bolt://localhost:7687', auth=("neo4j", "123456"))

# 创建
for i in res_list:
    cleaned_i = res2faultjson(i)
    faultjson2neo(cleaned_i, graph)

