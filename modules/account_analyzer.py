import re


def analyze_account(html: str):

    private = False
    verified = False
    business = False
    creator = False

    lower_html = html.lower()

    if '"is_private":true' in lower_html:

        private = True

    if '"is_verified":true' in lower_html:

        verified = True

    if '"is_business_account":true' in lower_html:

        business = True

    creator_keywords = [
        "digital creator",
        "creator"
    ]

    business_keywords = [
        "professional_account",
        "business",
        "entrepreneur",
        "brand"
    ]

    for keyword in creator_keywords:

        if keyword in lower_html:

            creator = True
            break

    for keyword in business_keywords:

        if keyword in lower_html:

            business = True
            break

    return {
        "private": private,
        "verified": verified,
        "business_account": business,
        "creator_account": creator
    }
