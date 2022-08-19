import random
import re
import wikipedia

def get_facts(topic: str) -> list:
    facts = []
    try:
        wikipedia.set_lang("en")
        valid_topic = wikipedia.search(topic)[0]

        summary = wikipedia.summary(valid_topic, sentences=50)

        summary_wo_headings = re.sub(r"==.*==", "", summary)
        summary_wo_blanks = re.sub(r"\n", " ", summary_wo_headings)
        
        facts = summary_wo_blanks.split(". ")

        random_indices = [random.randint(0, len(facts)-1) for i in range(5)]

        return [facts[i] for i in random_indices]

    except wikipedia.exceptions.DisambiguationError as e:
        print(e)
        return None

    except Exception as e:
        print(e)
        return None