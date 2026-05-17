import re


def extract_links(metadata: dict):
    text = str(metadata)
    return re.findall(r'https?://[^\\s]+', text)
  
