from flask import abort


def invalid_url_handler():
    error_message = (
        "Invalid URL: No scheme supplied. "
    )
    abort(400, description=error_message)
