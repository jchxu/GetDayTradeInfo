# conding=utf-8

#from WindPy import w
#from Functions import *
#import time,gc
#naturedict = {1:'空开',2:'空平',3:'空换',4:'多开',5:'多平',6:'多换',7:'双开',8:'双平'}
##timelist = ["9:00","11:30","15:00","17:30","21:00","23:59"]
##timeinterval = 0.1
#codelist = ['RB.SHF','HC.SHF','I.DCE','J.DCE','JM.DCE']
##codelist = ['RB.SHF']
#
#code = ','.join(codelist)
#w.start()
#w.isconnected()
#
#
#rt_code = ''
#rt_date = ''
#rt_time = ''
#rt_last = ''
#rt_last_vol = ''
#
#
##rt_oi_change =''
#
#
#
#def  MyWSQCallback(indata):
#    if indata.ErrorCode != 0:
#        print('error code:',str(indata.ErrorCode))
#        return ()
#    print(indata)
#    for i in range(len(indata.Codes)):
#        rt_code = indata.Codes[i]
#        rt_nature = 0
#        for j in range(len(indata.Fields)):
#            if (indata.Fields[j] == "RT_DATE"):
#                rt_date = str(indata.Data[j][i]).split('.')[0]
#            if (indata.Fields[j] == "RT_TIME"):
#                rt_time = str(indata.Data[j][i]).split('.')[0]
#            if (indata.Fields[j] == "RT_LAST"):
#                rt_last = indata.Data[j][i]
#            if (indata.Fields[j] == "RT_LAST_VOL"):
#                rt_last_vol = indata.Data[j][i]
#            if (indata.Fields[j] == "RT_NATURE"):
#                rt_nature = int(indata.Data[j][i])
#        print(rt_code,rt_date,rt_time,rt_last,rt_last_vol,rt_nature)
#    #    rt_code = indata.Codes[i]
#    #    rt_date = str(indata.Data[0][i]).split('.')[0]
#    #    rt_time = str(indata.Data[1][i]).split('.')[0]
#    #    rt_last = indata.Data[2][i]
#    #    rt_last_vol = indata.Data[3][i]
#    #    rt_oi_change = indata.Data[4][i]
#    #    rt_nature = int(indata.Data[5][i])
#    #    tradeinfolist = [rt_code,rt_date,rt_time,rt_last,rt_last_vol,rt_oi_change,rt_nature]
#    #    tradeline = ','.join(tradeinfolist)
#    #    print(tradeline)
#
#tradeinfo = w.wsq(code, "rt_date,rt_time,rt_last,rt_last_vol,rt_nature",func=MyWSQCallback)
##print(tradeinfo)
##tradeinfo = w.wsq("RB.SHF,HC.SHF,I.DCE,J.DCE,JM.DCE", "rt_date,rt_time,rt_last,rt_last_vol,rt_nature",func=MyWSQCallback)
##print(tradeinfo)
##while CheckTime(timelist):  #检查是否在交易时间段内
##    interval = CalcInterval(timeinterval, timelist)    #返回读取当天交易数据的时间间隔
##    time.sleep(interval)    #暂停时间间隔后再进行操作
##    tradedata = ReadTradeInfo(codelist)  #获取各品种的实时交易数据
#    WriteTick(codelist,tradedata)   #保存实时交易数据
#    clearvalue(tradedata)
#w.stop()

# w.cancelRequest(0)

''''''

from WindPy import w
import os
codelist = ['RB.SHF','HC.SHF','I.DCE','J.DCE','JM.DCE']
code = ','.join(codelist)

rt_date = {}
rt_time = {}
rt_last = {}
rt_last_vol = {}
rt_nature = {}
codefile = {}
for item in codelist:
    rt_date[item] = ''
    rt_time[item] = ''
    rt_last[item] = ''
    rt_last_vol[item] = ''
    rt_nature[item] = 0
    filename = item+".csv"
    if os.path.isfile(filename):
        codefile[item] = open(filename, 'a')
    else:
        codefile[item] = open(filename, 'a')
        print('rt_date','rt_time','rt_last','rt_last_vol','rt_nature',sep=',',file=codefile[item])
        codefile[item].flush()




w.start()

def  MyWSQCallback(indata):
    #print(indata)
    for i in range(len(indata.Codes)):
        rt_code = indata.Codes[i]
        for j in range(len(indata.Fields)):
            if (indata.Fields[j] == "RT_DATE"):
                rt_date[rt_code] = str(indata.Data[j][i]).split('.')[0]
            if (indata.Fields[j] == "RT_TIME"):
                rt_time[rt_code] = str(indata.Data[j][i]).split('.')[0]
            if (indata.Fields[j] == "RT_LAST"):
                rt_last[rt_code] = indata.Data[j][i]
            if (indata.Fields[j] == "RT_LAST_VOL"):
                rt_last_vol[rt_code] = indata.Data[j][i]
            if (indata.Fields[j] == "RT_NATURE"):
                rt_nature[rt_code] = int(indata.Data[j][i])
        print(rt_code,rt_date[rt_code],rt_time[rt_code],rt_last[rt_code],rt_last_vol[rt_code],rt_nature[rt_code])
        print(rt_code,rt_date[rt_code],rt_time[rt_code],rt_last[rt_code],rt_last_vol[rt_code],rt_nature[rt_code],sep=',',file=codefile[rt_code])
        codefile[rt_code].flush()
tradeinfo = w.wsq("RB.SHF,HC.SHF,I.DCE,J.DCE,JM.DCE", "rt_date,rt_time,rt_last,rt_last_vol,rt_nature",func=MyWSQCallback)
w.cancelRequest(0)

