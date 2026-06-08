from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)


def get_transcript(video_id):

    try:

        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        return transcript

    except (
        TranscriptsDisabled,
        NoTranscriptFound,
        VideoUnavailable
    ):

        return None