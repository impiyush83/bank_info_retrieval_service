import datetime
from decimal import Decimal

from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=10000
)

date_format = '%Y-%m-%d %H:%M:%S UTC'


def parse_date(date_str, _format=date_format):
    try:
        if date_str is None:
            return None
        date_time = datetime.strptime(date_str, _format)
    except ValueError:
        return None
    else:
        return date_time


def date_to_str(date):
    return date and date.strftime(date_format)


def parse_int(int_str):
    try:
        return int(int_str)
    except ValueError:
        return None
    except TypeError:
        return None


def parse_float(float_str):
    try:
        return float(float_str)
    except ValueError:
        return None
    except TypeError:
        return None
    except:
        return None


def parse_decimal(decimal_str):
    try:
        return Decimal(decimal_str)
    except ValueError:
        return None
    except TypeError:
        return None
    except:
        return None


def encrypt_password(password):
    return pwd_context.hash(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)


def row_to_dict(row):
    temp = row.__dict__
    temp.pop('_sa_instance_state', None)
    return temp


def rows_to_list(rows):
    ret_rows = []
    for row in rows:
        ret_rows.append(row_to_dict(row))
    return ret_rows
