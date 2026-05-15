import instaloader
from exports.json_export import save_json

L = instaloader.Instaloader()

def scan_profile(username):
    try:
        profile = instaloader.Profile.from_username(
            L.context,
            username
        )

        data = {
            "username": profile.username,
            "full_name": profile.full_name,
            "bio": profile.biography,
            "followers": profile.followers,
            "following": profile.followees,
            "posts": profile.mediacount,
            "is_private": profile.is_private,
            "external_url": profile.external_url
        }

        save_json(username, "profile", data)

        return data

    except Exception as e:
        return {
            "error": str(e)
        }
