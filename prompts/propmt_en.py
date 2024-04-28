prompt_en_zero = f'''
            ### Task.
            Assume you are an expert in knowledge graph construction. \
            Use natural language to extract a triad related to charging pile faults, the following sentence is known, extract possible entities, relationships from the sentence
            
            ### Entities.
            {'Charging pile type', 'Failure mode', 'Failure cause', 'Failure effect', 'Equipment component'}        
            
            ### Entity definition.
            Charging pile type is the classification of the charging pile according to the charging mode row.
            Failure Mode is the manner or form in which a Charging Pile system, equipment or component fails \
            under specific conditions. It describes the undesirable behaviour or condition that may occur in \
            the actual operation of the Charging Pile system or equipment.
            Failure cause is the root cause or factor that causes the charging pile system, equipment, \
            or component to fail.
            Failure Impact is the effect of the failure on the operational performance, functionality, or safety \
            of the Charging Pile system, equipment, or component.
            Equipment component is the components, construction and organisation of the charging pile equipment.
            
            ### Relationships
            {'Cause effect','Happen at','Result in','consist of'}
            
            ### Triplets
            [
                {'Charging pile type','consist of','Equipment component'},
                {'Failure mode','Happen at','Equipment component'},
                {'Failure mode','Cause effect','Failure effect'},
                {'Failure cause','Result in','Failure mode'}
            ]
           
            Please follow the steps below:
            1.Identify the Entities in the input text.Entities are specific instances in '### Entities'.
            2.Identify all the relationships in '### Relationships', the entities of which you mentioned in first step.
            3.You do not need to extract entities and relationships for textual content that is not related to the charging pile.
            4.Use the entities you mentioned in the first step and the relations you mentioned in the second part \
            to construct triples that conform to the structure of '### Triplets'.
            5.If the corresponding entity or relationship is not found, replace it with 'null'.
            6.The final output is in JSON format, Provide them in JSON format with the following keys: 
            entities, relationships, triplets.
           
            '''

prompt_en_few = f'''
            ### Task.
            Assume you are an expert in knowledge graph construction. \
            Use natural language to extract a triad related to charging pile faults, the following sentence is known, extract possible entities, relationships from the sentence

            ### Entities.
            {'Charging pile type', 'Failure mode', 'Failure cause', 'Failure effect', 'Equipment component'}        

            ### Entity definition.
            Charging pile type is the classification of the charging pile according to the charging mode row.
            Failure Mode is the manner or form in which a Charging Pile system, equipment or component fails \
            under specific conditions. It describes the undesirable behaviour or condition that may occur in \
            the actual operation of the Charging Pile system or equipment.
            Failure cause is the root cause or factor that causes the charging pile system, equipment, \
            or component to fail.
            Failure Impact is the effect of the failure on the operational performance, functionality, or safety \
            of the Charging Pile system, equipment, or component.
            Equipment component is the components, construction and organisation of the charging pile equipment.

            ### Relationships
            {'Cause effect', 'Happen at', 'Result in', 'consist of'}

            ### Triplets
            [
                {'Charging pile type', 'consist of', 'Equipment component'},
                {'Failure mode', 'Happen at', 'Equipment component'},
                {'Failure mode', 'Cause effect', 'Failure effect'},
                {'Failure cause', 'Result in', 'Failure mode'}
            ]

            Please follow the steps below:
            1.Identify the Entities in the input text.Entities are specific instances in '### Entities'.
            2.Identify all the relationships in '### Relationships', the entities of which you mentioned in first step.
            3.You do not need to extract entities and relationships for textual content that is not related to the charging pile.
            4.Give the results for instances that satisfy the "### Triplets" structure.
            5.If the corresponding entity or relationship is not found, replace it with 'null'.
            6.The final output is in JSON format, Provide them in JSON format with the following keys: 
            entities, relationships, triplets.

            ### Input text:
            '''