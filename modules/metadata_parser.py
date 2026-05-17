def parse_metadata(profile_data: dict):
    return {
        "username": profile_data.get("username"),
        "reachable": profile_data.get("reachable"),
        "status_code": profile_data.get("status_code")
    }
