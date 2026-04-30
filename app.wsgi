import sys
import site
import os

site.addsitedir('/var/www/test/heavenly-semester/env/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/test/heavenly-semester')

os.chdir('/var/www/test/heavenly-semester')

os.environ['VIRTUAL_ENV'] = '/var/www/test/heavenly-semester/env'
os.environ['PATH'] = '/var/www/test/heavenly-semester/env/bin:' + os.environ['PATH']

from app import app as application

