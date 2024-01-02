import schedule
import time
from statistics_and_analytics.dataloader import dataloader

schedule.every(30).minutes.do(dataloader)


while True:
    schedule.run_pending()
