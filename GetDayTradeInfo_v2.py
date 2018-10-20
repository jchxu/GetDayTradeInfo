# conding=utf-8

from WindPy import w
from datetime import datetime
import os

codelist = ['RB.SHF','HC.SHF','I.DCE','J.DCE','JM.DCE']
code = ','.join(codelist)

rt_date = {}
rt_time = {}
rt_last = {}
rt_last_vol = {}
rt_nature = {}
codefile = {}
yearmonth = '_' + str(datetime.now().year) + str(datetime.now().month)
for item in codelist:
    rt_date[item] = ''
    rt_time[item] = ''
    rt_last[item] = ''
    rt_last_vol[item] = ''
    rt_nature[item] = 0
    filename = item + yearmonth + ".csv"
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

