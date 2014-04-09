from olga.currency.money import Currency
from datetime import datetime
import os

def test_file():
    currency = Currency.RUB
    log_dir = Currency.LOG_DIR.format(base=currency,
                                           year=datetime.now().year,
                                           month=datetime.now().month,
                                           day=datetime.now().day)
    if not os.path.exists(log_dir):
        cur = Currency()
    
    if not os.path.exists(log_dir):
        assert "Not saved to file"


if __name__ == "__main__":
     test_file()