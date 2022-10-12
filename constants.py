from datetime import timedelta
from datetime import datetime


YESTERDAY = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
