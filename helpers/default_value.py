def default_value(defaultValue, value, callback) -> str:
    result = value
    if not value.strip():
        result = defaultValue

    return callback(result)
