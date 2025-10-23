from datetime import *
from random import *
import time 
stday="1/1/2025"
enday="12/31/2025"
x=random()
dateformat='%m/%d/%Y'
startime=time.mktime(time.strptime(stday,dateformat))
endtime=time.mktime(time.strptime(enday,dateformat))
rantime=startime+x*(endtime-startime)
randate=time.strftime(dateformat,time.localtime(rantime))
print(f"Random date is {randate}.")