def get_split_date(date_str: str) -> list[int]:
    date: list[str] = date_str.split("-")
    return [int(date[0]), int(date[1]), int(date[2])]

