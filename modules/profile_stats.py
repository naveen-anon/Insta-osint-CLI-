import re


def extract_profile_stats(metadata: dict):

    description = metadata.get(
        "description",
        ""
    )

    followers = "Not Found"
    following = "Not Found"
    posts = "Not Found"

    matches = re.search(
        r'([\d,]+)\sFollowers,\s([\d,]+)\sFollowing,\s([\d,]+)\sPosts',
        description
    )

    if matches:

        followers = matches.group(
            1
        )

        following = matches.group(
            2
        )

        posts = matches.group(
            3
        )

    return {
        "followers": followers,
        "following": following,
        "posts": posts
    }
