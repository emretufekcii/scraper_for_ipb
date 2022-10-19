from datetime import datetime, timedelta

import time 
import os 

while 1:
    os.system('C:\\Users\\dell\scraper-for-ipb\\igneiplikscrap\\igneiplikreq.py')

    dt =  datetime.now() + timedelta(hours=1)
    

    while datetime.now() < dt:
        time.sleep(1)