import version_query


def get_version() -> str:
    return version_query.predict_version_str()
