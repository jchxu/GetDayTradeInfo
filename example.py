from WindPy import *

w.start()

# open a file to write.
pf = open('example.txt', 'w')


# define the callback function
def myCallback(indata):
    if indata.ErrorCode != 0:
        print('error code:' + str(indata.ErrorCode) + '\n')
        return ()

    global begintime
    lastvalue = ""
    for k in range(0, len(indata.Fields)):
        if (indata.Fields[k] == "RT_TIME"):
            begintime = indata.Data[k][0]
        if (indata.Fields[k] == "RT_LAST"):
            lastvalue = str(indata.Data[k][0])

    string = str(begintime) + " " + lastvalue + "\n"
    pf.writelines(string)
    print(string)


# to subscribe if14.CFE
w.wsq("RB.SHF", "rt_time,rt_last", func=myCallback)
'''
20181015.0
.ErrorCode=0
.StateCode=1
.RequestID=11
.Codes=[I.DCE,RB.SHF]
.Fields=[RT_DATE,RT_TIME,RT_LAST,RT_LAST_VOL,RT_OI_CHANGE,RT_NATURE]
.Times=[20181015 11:00:43]
.Data=[[20181015.0,20181015.0],[110122.0,110122.0],[512.0,4148.0],[2.0,424.0],[0.0,278.0],[6.0,4.0]]
110123.0
.ErrorCode=0
.StateCode=1
.RequestID=11
.Codes=[RB.SHF]
.Fields=[RT_TIME,RT_LAST,RT_LAST_VOL,RT_OI_CHANGE,RT_NATURE]
.Times=[20181015 11:00:44]
.Data=[[110123.0],[4146.0],[6.0],[0.0],[3.0]]
110123.0
.ErrorCode=0
.StateCode=1
.RequestID=11
.Codes=[I.DCE,RB.SHF]
.Fields=[RT_TIME,RT_LAST,RT_LAST_VOL,RT_OI_CHANGE,RT_NATURE]
.Times=[20181015 11:00:45]
.Data=[[110123.0,110124.0],[511.5,4147.0],[2.0,46.0],[0.0,16.0],[8.0,1.0]]
4147.0
.ErrorCode=0
.StateCode=1
.RequestID=11
.Codes=[RB.SHF]
.Fields=[RT_LAST,RT_LAST_VOL,RT_OI_CHANGE,RT_NATURE]
.Times=[20181015 11:00:45]
.Data=[[4147.0],[110.0],[-2.0],[2.0]]
110124.0
.ErrorCode=0
.StateCode=1
.RequestID=11
.Codes=[I.DCE]
.Fields=[RT_TIME,RT_LAST,RT_LAST_VOL,RT_OI_CHANGE]
.Times=[20181015 11:00:45]
.Data=[[110124.0],[511.5],[2.0],[-2.0]]
110125.0
.ErrorCode=0
.StateCode=1
.RequestID=11
.Codes=[RB.SHF]
.Fields=[RT_TIME,RT_LAST,RT_LAST_VOL,RT_OI_CHANGE,RT_NATURE]
.Times=[20181015 11:00:46]
.Data=[[110125.0],[4147.0],[56.0],[12.0],[4.0]]
0.0
.ErrorCode=0
.StateCode=1
.RequestID=11
.Codes=[I.DCE]
.Fields=[RT_OI_CHANGE]
.Times=[20181015 11:00:46]
.Data=[[0.0]]
4147.0
.ErrorCode=0
.StateCode=1
.RequestID=11
.Codes=[RB.SHF]
.Fields=[RT_LAST,RT_LAST_VOL,RT_OI_CHANGE]
.Times=[20181015 11:00:46]
.Data=[[4147.0],[124.0],[46.0]]
0.0
.ErrorCode=0
.StateCode=1
.RequestID=11
.Codes=[I.DCE]
.Fields=[RT_OI_CHANGE]
.Times=[20181015 11:00:46]
.Data=[[0.0]]
110126.0
.ErrorCode=0
.StateCode=1
.RequestID=11
.Codes=[RB.SHF]
.Fields=[RT_TIME,RT_LAST,RT_LAST_VOL,RT_OI_CHANGE]
.Times=[20181015 11:00:47]
.Data=[[110126.0],[4147.0],[30.0],[22.0]]
w.cancelRequest(0)
'''