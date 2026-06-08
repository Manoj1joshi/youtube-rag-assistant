from urllib.parse import (
    urlparse,
    parse_qs
)

def extract_video_id(url):

    try:

        parsed = urlparse(url)

        if parsed.hostname in [
            "youtube.com",
            "www.youtube.com"
        ]:

            return parse_qs(
                parsed.query
            ).get("v", [None])[0]

        elif parsed.hostname == "youtu.be":

            return parsed.path[1:]

    except Exception:
        return None

    return None


def get_video_id(user_input):

    if len(user_input) == 11:
        return user_input

    return extract_video_id(
        user_input
    )
