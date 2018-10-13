# conding=utf-8

from WindPy import w
from Functions import *
import time,gc

#timelist = ["9:00","11:30","15:00","17:30","21:00","23:59"]
#timeinterval = 0.1
codelist = ['RB.SHF','HC.SHF','I.DCE','J.DCE','JM.DCE']
#codelist = ['RB.SHF']

code = ','.join(codelist)
w.start()

def  MyWSQCallback(indata):
    if indata.ErrorCode != 0:
        print('error code:' + str(indata.ErrorCode))
        return ()
    for i in range(len(indata.Codes)):
        rt_code = indata.Codes[i]
        rt_date = str(indata.Data[0][i]).split('.')[0]
        rt_time = str(indata.Data[1][i]).split('.')[0]
        rt_last = indata.Data[2][i]
        rt_last_vol = indata.Data[3][i]
        rt_oi_change = indata.Data[4][i]
        rt_nature = int(indata.Data[5][i])
        tradeinfolist = [rt_code,rt_date,rt_time,rt_last,rt_last_vol,rt_oi_change,rt_nature]
        tradeline = ','.join(tradeinfolist)
        print(tradeline)

tradeinfo = w.wsq(code, "rt_date,rt_time,rt_last,rt_last_vol,rt_oi_change,rt_nature",func=MyWSQCallback)
#tradeinfo = w.wsq(code, "rt_date,rt_time,rt_last,rt_last_vol,rt_oi_change,rt_nature")
print(tradeinfo)

#while CheckTime(timelist):  #检查是否在交易时间段内
#    interval = CalcInterval(timeinterval, timelist)    #返回读取当天交易数据的时间间隔
#    time.sleep(interval)    #暂停时间间隔后再进行操作
#    tradedata = ReadTradeInfo(codelist)  #获取各品种的实时交易数据
#    WriteTick(codelist,tradedata)   #保存实时交易数据
#    clearvalue(tradedata)
#w.stop()