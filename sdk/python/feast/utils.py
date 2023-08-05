from datetime import datetime

from pytz import utc


def make_tzaware(t: datetime) -> datetime:
    """ We assume tz-naive datetimes are UTC """
    return t.replace(tzinfo=utc) if t.tzinfo is None else t
