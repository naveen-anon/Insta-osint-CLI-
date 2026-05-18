import re


def extract_links(text: str):
    pattern = r'https?://(?:[-\\w.]|(?:%[\\da-fA-F]{2}))+[^\\s]*'

    links = re.findall(pattern, text)

    return list(set(links))
