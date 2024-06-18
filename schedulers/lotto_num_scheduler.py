from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(timezone='Asia/Seoul')

def lotto_num_result_job():
    print('hello')
    
scheduler.add_job(lotto_num_result_job, 'interval', seconds=5)