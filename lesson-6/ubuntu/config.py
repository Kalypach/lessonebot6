import os
from pathlib import Path

TOKEN = os.getenv("TOKEN")
admin_id = int(os.getenv("ADMIN_ID"))
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
lp_token = os.getenv("LIQPAY_TOKEN")
host = os.getenv("IP")

I18N_DOMAIN = 'testbot'
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'
