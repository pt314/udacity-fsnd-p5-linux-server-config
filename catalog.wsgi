import sys

app_path = "/var/www/catalog"
if not app_path in sys.path:
    sys.path.insert(0, app_path)

from catalog import app as application
