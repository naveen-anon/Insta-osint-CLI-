def analyze_account(html: str):

    private = False
    verified = False
    business = False

    if '"is_private":true' in html:

        private = True

    if '"is_verified":true' in html:

        verified = True

    if '"is_business_account":true' in html:

        business = True

    return {
        "private": private,
        "verified": verified,
        "business_account": business
    }
