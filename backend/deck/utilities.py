import wikipedia

def get_facts(topic: str) -> list:
    facts = []
    try:
        wikipedia.set_lang("en")
        valid_topic = wikipedia.search(topic)[0]

        summary = wikipedia.summary(valid_topic, sentences=5)
        
        facts = summary.split(". ")
        return facts

    except wikipedia.exceptions.DisambiguationError as e:
        print(e)
        return None