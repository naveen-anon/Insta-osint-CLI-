import re


def extract_profile_stats(metadata: dict):
    description = metadata.get(
        "description",
        ""
    )

    followers = 0
    following = 0
    posts = 0

    numbers = re.findall(
        r'[\d,]+',
        description
    )

    try:

        if len(numbers) >= 3:

            followers = numbers[0]
            following = numbers[1]
            posts = numbers[2]

    except:

        pass

    return {
        "followers": followers,
        "following": following,
        "posts": posts
    }
