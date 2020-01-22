import requests
import bs4 as bs
import re


def con_check(con):
    """
    :param con: requests status code
    :return: if status code is greater or equal to 400 the script will be prematurely terminated
    """
    if con >= 400:
        print("Connection error")
        quit()


def get_word(rae_url: str):
    """
    :param rae_url: RAE url to parse
    :return: one word string
    """
    r = requests.get(rae_url)

    # if status code is 400 or higher, exit scrip
    con_check(r.status_code)

    # Parsing web page looking for featured word.
    soup = bs.BeautifulSoup(r.text, "lxml")
    raw = soup.find("p", {"class": "words"})

    # Cleaning word, removing extra characters
    clean_word = re.findall(r'data-eti=\"([a-z]+)\"', str(raw))[0]

    # clean_word = raw.text.split(",")[0]
    # clean_word = re.search(r"[a-z]+", clean_word.group())

    # if no word was found, exit code
    if len(clean_word) < 1:
        print("Word error")
        quit()

    return clean_word


def get_meaning(word: str):
    """
    :param word: today's featured word, it could ne any word
    :return: string with the word's meaning
    """
    r2 = requests.get(f"https://dle.rae.es/{word}")

    # if status code is 400 or higher, exit scrip
    con_check(r2.status_code)

    # looks for all possible results and stores it in a list
    soup = bs.BeautifulSoup(r2.text, "lxml")
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
        if start and i.startswith(word):
            result.append("\n" + i)
        elif start and len(i) > 1:
            result.append(i)

    # flipping the list back to normal and joining each element making a string
    clean_meaning = "\n".join(result[::-1])
    return clean_meaning
