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
        return self.container.find("div", class_="WI9k4c")\
                             .find("span", attrs={"data-dobid": "hdw"})\
                             .text

    def fetch_phonetic(self):
        """
        Method to fetch phonetic from the passed DOM
        :param container: Container DOM
        """
        return self.container.find("div", class_="WI9k4c")\
                             .find("div", class_="S23sjd")\
                             .find("span").text

    def fetch_audio_link(self):
        """
        Method to fetch audio link from the passed DOM
        :param container: Container DOM
        """
        return self.container.find("div", class_="gycwpf D5gqpe")\
                             .find("source")\
                             .attrs.get('src')

    def fetch_definitions(self):
        """
        Method to fetch the context of the word along with Definitions
        :param container: Container DOM
        """
        contexts = []
        for context in self.container.find("div", class_="vmod"):
            if not context.find("div", class_="vmod"):
                continue
            definitions = []
            context_title = context.find("div", class_="vpx4Fd")\
                                   .find("div", class_="pgRvse vdBwhd")\
                                   .find("i").text
            list_items = context.find("div").find("ol").find_all("li")
            for item in list_items:
                container = item.find("div", class_="thODed Uekwlc XpoqFe")\
                                .find("div", attrs={"jsname": "cJAsRb"})\
                                .find("div", class_="QIclbb XpoqFe")
                context_definition = container.find("div", attrs={"data-dobid": "dfn"}).text
                context_example = container.find("div", class_="vk_gy").text
                definitions.append({
                    "definition": context_definition,
                    "example": context_example
                })
            contexts.append({
                context_title: definitions
            })
        return contexts
