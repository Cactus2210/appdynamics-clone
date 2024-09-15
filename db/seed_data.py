from backend.app import db
from backend.app.models import APIStatus

# Seed some initial API status data
api_status1 = APIStatus(url='https://example-api.com', status_code=200, latency=0.123)
api_status2 = APIStatus(url='https://another-api.com', status_code=500, latency=1.432)

db.session.add(api_status1)
db.session.add(api_status2)
db.session.commit()
