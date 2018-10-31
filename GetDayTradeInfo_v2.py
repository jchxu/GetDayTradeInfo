# conding=utf-8

from WindPy import w
from datetime import datetime,timedelta
import os

codelist = ['RB.SHF','HC.SHF','I.DCE','J.DCE','JM.DCE']
code = ','.join(codelist)

rt_date = {}
rt_time = {}
rt_last = {}
rt_last_vol = {}
rt_oi_change = {}
rt_nature = {}
codefile = {}
oldline = {}

nowdate = '_' + str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day)

for item in codelist:
    rt_date[item] = ''
    rt_time[item] = ''
    rt_last[item] = 0
    rt_last_vol[item] = 0
    rt_oi_change[item] = 0
    rt_nature[item] = 0
    oldline[item] = []

    #filename = item + nowdate + ".csv"
    #if os.path.isfile(filename):
    #    codefile[item] = open(filename, 'a')
    #else:
    #    codefile[item] = open(filename, 'a')
    #    print('code','rt_date','rt_time','rt_last','rt_last_vol','rt_oi_change','rt_nature',sep=',',file=codefile[item])
    #    codefile[item].flush()

def  MyWSQCallback(indata):
    #print(indata)
    global oldline
    ticktime = indata.Times[0]
    today = ticktime.strftime('%Y%m%d')
    endtime = datetime.strptime((today + ' 15:30:00'),'%Y%m%d %H:%M:%S')
    newdaytime = datetime.strptime((today + ' 20:30:00'),'%Y%m%d %H:%M:%S')
    datestr = today
    if (ticktime < endtime):
        datestr = today
    elif (ticktime > newdaytime):
        if ticktime.weekday() == 4:
            datestr = (ticktime + timedelta(days = 3)).strftime('%Y%m%d')
        else:
            datestr = (ticktime + timedelta(days = 1)).strftime('%Y%m%d')
    else:
        datestr = 'none'
    for i in range(len(indata.Codes)):
        rt_code = indata.Codes[i]
        filename = rt_code + '_' + datestr + ".csv"
        codefile[rt_code] = open(filename, mode = 'w')
        for j in range(len(indata.Fields)):
            if (indata.Fields[j] == "RT_DATE"):
                rt_date[rt_code] = str(indata.Data[j][i]).split('.')[0]
            if (indata.Fields[j] == "RT_TIME"):
                rt_time[rt_code] = str(indata.Data[j][i]).split('.')[0]
            if (indata.Fields[j] == "RT_LAST"):
                rt_last[rt_code] = int(indata.Data[j][i])
            if (indata.Fields[j] == "RT_LAST_VOL"):
                rt_last_vol[rt_code] = int(indata.Data[j][i])
            if (indata.Fields[j] == "RT_OI_CHANGE"):
                rt_oi_change[rt_code] = int(indata.Data[j][i])
            if (indata.Fields[j] == "RT_NATURE"):
                rt_nature[rt_code] = int(indata.Data[j][i])
        line = [rt_code,rt_date[rt_code],rt_time[rt_code],rt_last[rt_code],rt_last_vol[rt_code],rt_oi_change[rt_code],rt_nature[rt_code]]
        if line != oldline[rt_code]:
            print(rt_code,rt_date[rt_code],rt_time[rt_code],rt_last[rt_code],rt_last_vol[rt_code],rt_oi_change[rt_code],rt_nature[rt_code])
            print(rt_code,rt_date[rt_code],rt_time[rt_code],rt_last[rt_code],rt_last_vol[rt_code],rt_oi_change[rt_code],rt_nature[rt_code],sep=',',file=codefile[rt_code])
            oldline[rt_code] = line
        codefile[rt_code].close()

w.start()

tradeinfo = w.wsq("RB.SHF,HC.SHF,I.DCE,J.DCE,JM.DCE", "rt_date,rt_time,rt_last,rt_last_vol,rt_oi_change,rt_nature",func=MyWSQCallback)

#w.cancelRequest(0)

