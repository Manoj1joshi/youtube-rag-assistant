def retrieve_by_time(
        target_time,
        docs,
        window=300
):

    results = []

    # RANGE QUERY
    if isinstance(target_time, tuple):

        range_start, range_end = target_time

        for doc in docs:

            start = doc.metadata["start"]
            end = doc.metadata["end"]

            if (
                start < range_end
                and end > range_start
            ):
                results.append(doc)

        return sorted(
            results,
            key=lambda x: x.metadata["start"]
        )

    # POINT QUERY
    for doc in docs:

        start = doc.metadata["start"]
        end = doc.metadata["end"]

        if (
            start <= target_time <= end
            or abs(start - target_time) <= window
        ):

            results.append(doc)

    return results