import re
from text_to_num import alpha2digit
import re

def normalize_ordinal_hours(question):

    ordinal_map = {
        "first": 1,
        "second": 2,
        "third": 3,
        "fourth": 4,
        "fifth": 5,
        "sixth": 6,
        "seventh": 7,
        "eighth": 8,
        "ninth": 9,
        "tenth": 10,
        "eleventh": 11,
        "twelfth": 12,
        "thirteenth": 13,
        "fourteenth": 14,
        "fifteenth": 15,
        "sixteenth": 16,
        "seventeenth": 17,
        "eighteenth": 18,
        "nineteenth": 19,
        "twentieth": 20,
    }

    for word, num in ordinal_map.items():
        question = re.sub(
            rf"\b{word}\s+hour\b",
            f"{num} hour",
            question
        )

    return question
def detect_time_query(question):

    question = question.lower()
    question = normalize_ordinal_hours(question)
    patterns = [
        r"(\d+)(?:st|nd|rd|th)\s*hour",
        r"(\d+)\s*hour",
        r"(\d+)\s*hours",
        r"(\d+):(\d+):(\d+)",
        r"(\d+):(\d+)"
    ]

    for pattern in patterns:

        match = re.search(pattern, question)

        if match:

            # 3 hour
            if "hour" in pattern:

                hour = int(match.group(1))

                if "start" in question:
                    return (hour - 1) * 3600

                elif "middle" in question:
                    return (hour - 1) * 3600 + 1800

                elif "end" in question:
                    return hour * 3600 - 1

                else:
                    return ((hour - 1) * 3600,hour * 3600)
            # hh:mm:ss
            if len(match.groups()) == 3:

                h = int(match.group(1))
                m = int(match.group(2))
                s = int(match.group(3))

                return h * 3600 + m * 60 + s

            # mm:ss
            if len(match.groups()) == 2:

                m = int(match.group(1))
                s = int(match.group(2))

                return m * 60 + s

    return None

question = "what is discussed during the start second hour . only 2 line answer"
question = normalize_ordinal_hours(question)
target_time = detect_time_query(question)
print(target_time) 
print(question)

