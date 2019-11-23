class Meaning(object):
    def __init__(self, container):
        self.container = container

    @property
    def word(self):
        return self.fetch_word()

    @property
    def phonetic(self):
        return self.fetch_phonetic()

    @property
    def audio_link(self):
        return self.fetch_audio_link()

    @property
    def definitions(self):
        return self.fetch_definitions()

    def fetch_word(self):
        """
        Method to fetch word from the passed DOM
        :param container: Container DOM
        """
        return self.container.find("div", class_="entryHead primary_homograph")\
                   .header.h2.span.text.capitalize()

    def fetch_phonetic(self):
        """
        Method to fetch phonetic from the passed DOM
        :param container: Container DOM
        """
        return self.container.find("section", class_="pronSection etym")\
                             .div.span.text 

    def fetch_audio_link(self):
        """
        Method to fetch audio link from the passed DOM
        :param container: Container DOM
        """
        return self.container.find("section", class_="pronSection etym")\
                             .div.a.audio.get("src") 

    def fetch_definitions(self):
        """
        Method to fetch the context of the word along with Definitions
        :param container: Container DOM
        """
        # Fetching Part of Speech
        part_of_speech = self.container.find("section", class_="gramb")\
                                       .h3.span.text.capitalize()

        # Fetchings Meanings List
        meanings = []
        meanings_list = self.container.find("section", class_="gramb")\
                                      .find("ul", class_="semb")\
                                      .find_all("li", recursive=False)
        for meaning_dict in meanings_list:
            parent_meaning_dict = meaning_dict.find("div", class_="trg")
            
            # Fetching Definition
            definition = parent_meaning_dict.p.find("span", class_="ind").text
            
            # Fetching Examples
            examples = []
            examples_dict = parent_meaning_dict.find_all("div", class_="exg", recursive=False)
            for example in examples_dict:
                examples.append(example.div.em.text[1:-1].capitalize())
            
            # Fetching Synonyms
            synonyms = []
            try:
                synonyms_dict = parent_meaning_dict.find("div", class_="synonyms")\
                                                   .find("div", class_="exg")\
                                                   .find_all("div", recursive=False)
            except:
                pass
            else:
                for synonym in synonyms_dict:
                    try:
                        synonyms.append(synonym.strong.text.capitalize())
                        synonyms.extend([s.capitalize() for s in synonym.span.text[2:].split(", ")])
                    except:
                        continue

            meanings.append({
                "definition": definition,
                "examples": examples,
                "synonyms": synonyms
            })

        return meanings
