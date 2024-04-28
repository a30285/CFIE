prompt_zh_zero = f'''
            ### 任务
            你是知识图谱构建方面的专家。\
            使用自然语言提取与充电桩故障有关的三元组，从输入文本中提取可能的实体、关系
            
            #### 实体。
            {{'充电桩类型','故障模式','故障原因','故障影响','设备组件'}}
                   
            ### 实体定义。
            充电桩类型是根据充电模式行对充电桩进行的分类。
            故障模式是充电桩系统、设备或组件在特定条件下发生故障的方式或形式。\
            在特定条件下发生故障的方式或形式。它描述了充电桩实际运行中可能出现的不良行为或状况。\
            它描述了充电桩系统或设备在实际运行中可能出现的不良行为或状况。
            故障原因是导致充电桩系统、设备或组件发生故障的根本原因或因素。部件发生故障的根本原因或因素。
            故障影响是指故障对充电桩系统、设备、部件的运行性能、功能或安全的影响。\
            是指故障对充电桩系统、设备或部件的运行性能、功能或安全的影响。
            设备组件是指充电桩设备的部件、结构和组织。
            
            #### 关系
            {{'造成影响','发生于','导致故障','内部构造'}}。
            
            ### 三胞胎
            [
                {{'充电桩类型', '内部构造', '设备组件'}},
                {{'故障模式', '发生于', '设备组件'}},
                {{'故障模式','造成影响','故障影响'}},
                {{'故障原因','导致故障','故障模式'}}
            ]
           
            请按照以下步骤操作：
            1.识别输入文本中的实体。实体是 "###实体 "中的具体实例。
            2.识别所有在 "###关系"中的关系。
            3.对于与充电桩无关的文本内容，无需提取实体和关系。
            4.使用第一步中提到的实体和第二部分中提到的关系来构建符合 "###三元组 "结构的三元组。
            5.如果找不到相应的实体或关系，则用 "null"代替。
            6.最终输出为 JSON 格式，以 JSON 格式提供，键的值如下： 
            Entities, Relationships, Triplets。
            
            ### 输入文本:
                '''

prompt_zh_few = f'''
            ### 任务
            你是知识图谱构建方面的专家。\
            使用自然语言提取与充电桩故障有关的三元组，从输入文本中提取可能的实体、关系
            
            #### 实体。
            {{'充电桩类型','故障模式','故障原因','故障影响','设备组件'}}
                   
            ### 实体定义。
            充电桩类型是根据充电模式行对充电桩进行的分类。
            故障模式是充电桩系统、设备或组件在特定条件下发生故障的方式或形式。\
            在特定条件下发生故障的方式或形式。它描述了充电桩实际运行中可能出现的不良行为或状况。\
            它描述了充电桩系统或设备在实际运行中可能出现的不良行为或状况。
            故障原因是导致充电桩系统、设备或组件发生故障的根本原因或因素。部件发生故障的根本原因或因素。
            故障影响是指故障对充电桩系统、设备、部件的运行性能、功能或安全的影响。\
            是指故障对充电桩系统、设备或部件的运行性能、功能或安全的影响。
            设备组件是指充电桩设备的部件、结构和组织。
            
            #### 关系
            {{'造成影响','发生于','导致故障','内部构造'}}
            
            ### 三元组
            [
                {{'充电桩类型', '内部构造', '设备组件'}},
                {{'故障模式', '发生于', '设备组件'}},
                {{'故障模式','造成影响','故障影响'}},
                {{'故障原因','导致故障','故障模式'}}
            ]
           
            请按照以下步骤操作：
            1.识别输入文本中的实体。实体是 "###实体 "中的具体实例。
            2.识别所有在 "###关系"中的关系。
            3.对于与充电桩无关的文本内容，无需提取实体和关系。
            4.使用第一步中提到的实体和第二部分中提到的关系来构建符合 "###三元组 "结构的三元组。
            5.如果找不到相应的实体或关系，则用 "null"代替。
            6.最终输出为 JSON 格式，以 JSON 格式提供，键的值如下： 
            Entities, Relationships, Triplets。
            
            ### 输入文本:
             自动排产功能智能文印系统还具备自动排产功能，该功能可依据用户权限任务、纸张类型、文印设备种类、设备使用情况等，\
             遵循安全使用与负载均衡两大原则来派发任务，这样不仅使任务的排队时间得到有效减少，也能使设备的利用效率得到进一步提高。
             
            ### 输出文本:
            {{
              "Entities": null,
              "Relationships": null,
              "Triplets": null
            }}
            
            ### 输入文本:
            充电桩电源灯不亮的诊断、检测及应对（1）原因。充电桩电源灯不亮的原因主要有以下三种情况：一是充电电源连接异常，二是交流充电连接不正确，三是充电桩自身的线路问题。
            
            ### 输出文本:
            {{
              "Entities": {{
                "故障模式": "充电桩电源灯不亮",
                "故障原因": ["充电电源连接异常", "交流充电连接不正确", "充电桩自身的线路问题"]
              }},
              "Relationships": ["导致故障"],
              "Triplets": [
                {{
                  "故障原因": "充电电源连接异常",
                  "关系": "导致故障",
                  "故障模式": "充电桩电源灯不亮"
                }},
                {{
                  "故障原因": "交流充电连接不正确",
                  "关系": "导致故障",
                  "故障模式": "充电桩电源灯不亮"
                }},
                {{
                  "故障原因": "充电桩自身的线路问题",
                  "关系": "导致故障",
                  "故障模式": "充电桩电源灯不亮"
                }}
              ]
            }}
            '''