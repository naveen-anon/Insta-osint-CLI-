from bs4 import BeautifulSoup


def extract_links(html: str):
    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    links = []

    for tag in soup.find_all("a", href=True):
        links.append(tag["href"])

    return list(set(links))
