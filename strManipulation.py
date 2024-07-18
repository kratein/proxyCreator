def remove_digits(input_string: str) -> str:
    result = "".join([char for char in input_string if not char.isdigit()])
    return result
