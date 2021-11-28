from datetime import datetime


def parse_json_date_time(json_date_time: str) -> datetime:
    if not json_date_time:
        raise ValueError('json date time cannot be empty.')
    return datetime.strptime(json_date_time, '%Y-%m-%dT%H:%M:%S.%fZ')
