import requests
import bs4
import re

"""
Version 01. Original
Version 02. Classes update
    scraper is now a class, independent functions were deprecated.
"""


class Scraper(object):
    """
    Daily word scraper.
    """

    def __init__(self, url: str):
        """
        Init function.

        Parameters:
            url: String.

        Attributes:
            url: String. RAE main webpage: https://dle.rae.es/
            word: String. Today's word.
            meaning: String. Today's word meaning.
        """

        self.url = url
        self.word = None
        self.word_url = None
        self.meaning = None

    def __repr__(self):
        """
        Visual representation.
        """

        return f"URL: {self.url}\nWord: {self.word}\nWord URL: {self.word_url}\nMeaning: {self.meaning}"

    def get_word(self) -> tuple:
        """
        Parse RAE main webpage and find out today's word and word url.

        Returns:
            Updates self.word attribute.
            Updates self.word_url attribute
            Tuple: (word: String. Today's word, word_url: String. Today's word url)
        """

        r = requests.get(self.url)
        soup = bs4.BeautifulSoup(r.content, "lxml")

        # Fetching word
        word = soup.find("a", attrs={"data-cat": "WOTD"})["data-eti"]
        self.word = word

        # Fetching word's link
        word_link = soup.find("a", attrs={"data-cat": "WOTD"})["href"]
        word_url = self.url + word_link[1:]
        self.word_url = word_url

        return word, word_url

    def get_meaning(self) -> str:
        """
        Parse RAE daily word page returning word's meaning.

        Returns:
            Updates self.meaning attribute
            clean_meaning: String.
        """

        r2 = requests.get(self.word_url)

        # looks for all possible results and stores it in a list
        soup = bs4.BeautifulSoup(r2.text, "lxml")
        raw_results = soup.find("div", {"id": "resultados"})
        lst_results = raw_results.text.split("\n")

        # Parsing the list and returning a clean list, check word 'carpa'
        start = False
        result = []
        # Inverting the list, turning it backwards
        for i in lst_results[::-1]:

            # Parsing starts at first definition
            if re.match(r"\d\d*\.", i):
                start = True

            # Improving readability and avoiding unnecessary characters
            if start and i.startswith(self.word):
                result.append("\n" + i)
            elif start and len(i) > 1:
                result.append(i)

        # flipping the list back to normal and joining each element making a string
        clean_meaning = "\n".join(result[::-1])

        self.meaning = clean_meaning
        return clean_meaning
