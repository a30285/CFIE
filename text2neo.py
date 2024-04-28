import py2neo
# from main import muti_segment
import json
from py2neo import Graph, Node, Relationship, NodeMatcher


def node_exists(label, property_name, property_value, graph):
    query = f"MATCH (n:{label} {{{property_name}: '{property_value}'}}) RETURN n"
    result = graph.run(query).data()
    return bool(result)


text = f'''{{
          "Entities": {{
            "故障模式": ["动力蓄电池充电电流过流", "电池单体电压过高", "BMS管理系统与充电桩通讯故障", "网关通讯故障", "充电无数据", "通讯距离过远", "充电程序无法启动", "充电把松动", "充电设备标准不统一"],
            "故障原因": ["充电电源连接异常", "交流充电连接不正确", "充电桩自身的线路问题", "网关通讯故障", "通讯距离过远", "充电把松动", "充电设备标准不统一"],
            "故障影响": ["充电数据不能实时上传", "充电报表数据缺失", "计量计费准确性受影响", "充电无法启动", "充电线路短路", "设备运行不稳定"]
          }},
          "Relationships": ["导致故障", "造成影响"],
          "Triplets": [
            {{
              "故障模式": "动力蓄电池充电电流过流",
              "关系": "导致故障",
              "故障原因": "充电电源连接异常"
            }},
            {{
              "故障原因": "交流充电连接不正确",
              "关系": "导致故障",
              "故障模式": "电池单体电压过高"
              
              
            }},
            {{
              "故障原因": "充电桩自身的线路问题",
              "关系": "导致故障",
              "故障模式": "BMS管理系统与充电桩通讯故障"
            }},
            {{
              "故障原因": "网关通讯故障",
              "关系": "导致故障",
              "故障模式": "网关通讯故障"
            }},
            {{
              "故障模式": "充电无数据",
              "关系": "造成影响",
              "故障影响": "充电数据不能实时上传"
            }},
            {{
              "故障模式": "充电无数据",
              "关系": "造成影响",
              "故障影响": "充电报表数据缺失"
            }},
            {{
              "故障模式": "充电无数据",
              "关系": "造成影响",
              "故障影响": "计量计费准确性受影响"
            }},
            {{
              "故障模式": "充电程序无法启动",
              "关系": "造成影响",
              "故障影响": "充电无法启动"
            }},
            {{
              "故障原因": "通讯距离过远",
              "关系": "导致故障",
              "故障模式": "充电程序无法启动"
            }},
            {{
              "故障原因": "充电把松动",
              "关系": "导致故障",
              "故障模式": "充电把松动"
            }},
            {{
              "故障模式": "充电把松动",
              "关系": "造成影响",
              "故障影响": "充电线路短路"
            }},
            {{
              "故障原因": "充电设备标准不统一",
              "关系": "导致故障",
              "故障模式": "充电设备标准不统一"
            }},
            {{
              "故障模式": "充电设备标准不统一",
              "关系": "造成影响",
              "故障影响": "设备运行不稳定"
            }}
          ]
        }}
        '''


def faultjson2neo(text, graph):
    ##连接neo4j数据库，输入地址、用户名、密码
    ##注意：这句代码适用老版的py2neo，即适用于2021.1之前的
    # graph = Graph('http://localhost:7474', username='neo4j', password='')
    ##适用于新版
    matcher = NodeMatcher(graph)  # 创建关系需要用到

    # a = Node('owl_Class', name = 'banana') # 创建一个label = 'owl_Class'，属性name值为'banana'，此时节点并没有真的传到Neo4j
    # graph.create(a) # 将节点a创建到数据库

    parsed_outer = json.loads(text)
    print(parsed_outer)
    entities = parsed_outer['Entities']
    triplets = parsed_outer['Triplets']
    if entities is not None:
        for entity_type, entities_list in entities.items():
            if entities_list is not None:
                for entity in entities_list:
                    if not node_exists(entity_type, "name", entity, graph):
                        node = Node(entity_type, name=entity)
                        graph.create(node)
            # else:
            #     print(f"Node with label '{entity_type}' and name '{entity}' already exists.")
    if triplets is not None:
        for triplet in triplets:
            source_key = None

            target_key = None

            relation_type = triplet["关系"]

            # for key, value in triplet.items():
            #     if key != "关系":
            #         if not source_key:
            #             source_key = key
            #             source_label = key
            #             source_name = value
            #         else:
            #             target_key = key
            #             target_label = key
            #             target_name = value
            for key, value in triplet.items():
                if key != "关系":
                    if isinstance(value, list):  # 如果value是列表
                        for item in value:
                            if not source_key:
                                source_key = key
                                source_label = key
                                source_name = item
                            else:
                                target_key = key
                                target_label = key
                                target_name = item
                    else:
                        if not source_key:
                            source_key = key
                            source_label = key
                            source_name = value
                        else:
                            target_key = key
                            target_label = key
                            target_name = value

            if not node_exists(source_label, "name", source_name, graph):
                source_node = Node(source_label, name=source_name)
                graph.create(source_node)
            else:
                source_node = matcher.match(source_label, name=source_name).first()

            if not node_exists(target_label, "name", target_name, graph):
                target_node = Node(target_label, name=target_name)
                graph.create(target_node)
            else:
                target_node = matcher.match(target_label, name=target_name).first()
            relation = Relationship(source_node, relation_type, target_node)
            graph.create(relation)


def res2json(raw_data):
    # 查找第一个 '{' 和最后一个 '}' 的索引
    start_index = raw_data.find('{')
    end_index = raw_data.rfind('}')

    # 获取两个索引之间的字符串内容
    json_content = raw_data[start_index:end_index + 1]
    return json_content


def read_lines_from_output_file(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            lines.append(res2json(line))  # 去除每行末尾的换行符并添加到列表中
    return lines


data = read_lines_from_output_file('output.txt')

graph = Graph('bolt://localhost:7687', auth=("neo4j", "123456"))

for i in data:
    faultjson2neo(i, graph)
