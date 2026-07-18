class EntityRelationExtractor:

    def __init__(self, tokens, pos_tags):
        self.tokens = tokens
        self.pos_tags = pos_tags

    def extract_entities(self):
        entities = []

        for word, tag in self.pos_tags:
            if tag.startswith('NN'):  
                entities.append(word)

        return entities

    def extract_relations(self):
        relations = []

        for word, tag in self.pos_tags:
            if tag.startswith('VB'):  
                relations.append(word)

        return relations