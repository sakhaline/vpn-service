from flask import abort


def invalid_url_handler():
    error_message = (
        "Invalid URL: No scheme supplied. "
        "Perhaps you meant https://sdsdsd?"
    )
    abort(400, description=error_message)
