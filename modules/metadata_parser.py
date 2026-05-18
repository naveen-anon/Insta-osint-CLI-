from bs4 import BeautifulSoup


def parse_metadata(profile_data: dict):
    html = profile_data.get("html_content", "")

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    title = soup.title.string if soup.title else "Not Found"

    description = ""

    meta_desc = soup.find(
        "meta",
        attrs={"name": "description"}
    )

    if meta_desc:
        description = meta_desc.get(
            "content",
            ""
        )

    return {
        "title": title,
        "description": description
    }
