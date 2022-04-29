from datetime import datetime

from extensions import db

class StatusRepository:
    def uptime(self):
        rows = db.session.execute('SELECT (current_timestamp - pg_postmaster_start_time()) as uptime')
        uptime = rows.all()[0]['uptime']

        return str(uptime)