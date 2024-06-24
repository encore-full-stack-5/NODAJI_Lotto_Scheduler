from apscheduler.schedulers.background import BackgroundScheduler
from utils.generate_lotto_num import lotto_result
import requests

scheduler = BackgroundScheduler(timezone='Asia/Seoul')
analytics_url = 'http://localhost:8000/api/v1/lotto'
lotto_result_url = 'http://localhost:8080/api/v1/lotto/result'
headers = {'Content-Type': 'application/json'}

def lotto_num_result_job():
    print(lotto_result())
    data = lotto_result()
    requests.post(analytics_url, json=data, headers=headers)
    requests.post(lotto_result_url, json=data, headers=headers)


scheduler.add_job(lotto_num_result_job, 'interval', seconds=30)