from bs4 import BeautifulSoup
import re


def parse_metadata(profile_data: dict):

    html = profile_data.get(
        "html_content",
        ""
    )

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    title = "Not Found"

    if soup.title:

        title = soup.title.string

    description = ""

    meta_desc = soup.find(
        "meta",
        attrs={
            "name": "description"
        }
    )

    if meta_desc:

        description = meta_desc.get(
            "content",
            ""
        )

    bio = "Not Found"

    bio_match = re.search(
        r'Instagram:\s*"([^"]*)"',
        description
    )

    if bio_match:

        extracted_bio = bio_match.group(
            1
        ).strip()

        if extracted_bio:

            bio = extracted_bio

    return {
        "title": title,
        "description": description,
        "bio": bio
    }
