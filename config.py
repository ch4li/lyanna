DB_URL = 'mysql://root:@localhost:3306/test?charset=utf8'

try:
    from local_settings import *   # noqa
except ImportError:
    pass  