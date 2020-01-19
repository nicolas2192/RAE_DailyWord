import requests
import bs4 as bs


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
    r = requests.get("https://dle.rae.es/")

    # if status code is 400 or higher, exit scrip
    con_check(r.status_code)

    # Parsing web page looking for featured word.
    soup = bs.BeautifulSoup(r.text, "lxml")
    raw = soup.find("p", {"class": "words"})
    clear_word = raw.text.split(",")[0]

    # if no word was found, exit code
    if len(clear_word) < 1:
        print("Word error")
        quit()

    return clear_word


def get_meaning(word: str):
    """
    :param word: today's featured word, it could ne any word
    :return: string with the word's meaning
    """
    r2 = requests.get(f"https://dle.rae.es/{word}")

    # if status code is 400 or higher, exit scrip
    con_check(r2.status_code)

    soup = bs.BeautifulSoup(r2.text, "lxml")
    raw_results = soup.find("div", {"id": "resultados"})
    lst_results = raw_results.text.split("\n")
    start = False
    result = []
    for i in lst_results:
        if len(i) > 1:
            start = True
        if start:
            if len(i) > 1:
                result.append(i)
            else:
                break

    result = "\n".join(result)
    return result

