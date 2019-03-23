import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("/Users/ethanzh/Code/recorda-ml/food-model")
# nlp = spacy.load('en')

# Process whole documents
text = "My pizza from The Counter was bad"
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
