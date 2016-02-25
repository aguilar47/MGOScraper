from bs4 import BeautifulSoup
import requests

BASE_URL = "http://www.mgo.com"


def get_movie_lists():
    html = requests.get(BASE_URL).text

    soup = BeautifulSoup(html, "html.parser")
    list_container = soup.findAll("section", attrs={"class": "home-list-container"})

    lists_text = []
    for movie_list in list_container:
        list_title = movie_list.h2.a.string
        list_description = movie_list.h3.string

        lists_text.append(list_title + " - " + list_description + "\n")

        for movie_li in movie_list.div.ul.findAll("li"):
            if movie_li.i:
                movie_info = movie_li.i
                title = movie_info["data-title"]
                lists_text.append("\t"+title + "\n")
        lists_text.append("\n")

    return ''.join(lists_text)

print(get_movie_lists())