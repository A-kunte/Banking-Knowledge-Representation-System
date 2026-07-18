def extract_entities_relations(pos_tags):

    entities = []
    relations = []

    for word, tag in pos_tags:

        if tag.startswith("NN"):
            entities.append(word)

        elif tag.startswith("VB"):
            relations.append(word)

    return entities, relations