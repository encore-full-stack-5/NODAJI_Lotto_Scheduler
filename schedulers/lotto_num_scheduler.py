from apscheduler.schedulers.background import BackgroundScheduler
from utils.generate_lotto_num import lotto_result
import requests, json

scheduler = BackgroundScheduler(timezone='Asia/Seoul')
analytics_url = 'http://localhost:8000/api/v1/lotto'

def lotto_num_result_job():
    print(lotto_result())
    requests.post(analytics_url, json=lotto_result())
# minutes=1
scheduler.add_job(lotto_num_result_job, 'interval', seconds=15)