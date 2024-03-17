from bs4 import BeautifulSoup
import requests


def get_image_urls_list(url_chapter) -> list:
    """Flips all sorted images for a single chapter"""
    page = requests.get(url_chapter)
    soup = BeautifulSoup(page.text, "html.parser")
    image_list = soup.find_all("a")
    image_urls_list = [
        link.get("href") for link in image_list if ".jpg" in link.get("href")
    ]
    image_urls_list = sorted(
        image_urls_list, key=lambda x: int(x.split("/")[-1].replace(".jpg", ""))
    )
    if not image_urls_list:
        image_list = soup.find("div", class_="separator").find_all("img")
        image_urls_list = list(set([img.get("src") for img in image_list]))
        image_urls_list = sorted(
            image_urls_list, key=lambda x: int(x.split("/")[-1].replace(".jpg", ""))
        )
    return image_list


def get_chapters_info_list(
    url="https://w9.sololeveling-manwha.com/", availeble_chapters=[]
) -> list[tuple]:
    """Gets a list of already available partitions and returns new ones, if any"""
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    chapters_list_urls = soup.find("div", id="Chapters_List").find("ul").find_all("li")

    result_list = []

    for li in chapters_list_urls[1:]:
        try:
            urls_list = get_image_urls_list(li.a["href"])
            if urls_list and li.a.text not in availeble_chapters:
                result_list.append((li.a.text, urls_list))
        except Exception as a:
            print(a, print(li.a.text))

    return result_list
