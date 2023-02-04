import sys

sys.path.insert(0, './djangoTest/djangoTest')
from djangoTest.djangoTest import wsgi


app = wsgi.application
