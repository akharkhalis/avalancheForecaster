#Play meteo station
import urllib.request
import urllib.parse
import re
from datetime import datetime


def pars():
    nowDateTS = datetime.now()
    nowDateT = str(nowDateTS)
#    nowDate = nowDateT[0:20]
    url='http://gmc.uzhgorod.ua/metdata.php?StNo=33638'
    values = {'s':'basics',
              'submit':'search'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    #print(respData)

    rows = re.findall(r'<td>(.*?)</td>',str(respData))
    #print(rows)
    #'Дата і час','Температура повітря','Температура точки роси', 'Опади','Атмосферний тиск','Напрямок вітру','Швидкість вітру'
    wData = []
    w1Data = {}
    for eachR in rows:
        wData = wData + [eachR]
#        print (eachR)

    fileNameNS = nowDateT[5:10]+ '_' + nowDateT[11:13] + nowDateT[14:16] + '.txt'
    fileName = str(fileNameNS)

    print(fileName)
#    print (wData)
    i = 0
    lenWD = len(wData)
    while lenWD > 0:
        w0Data = {wData[0] : wData[1:7]}
        w1Data.update(w0Data)
        del wData[0:7]
        lenWD = lenWD - 7
    #    print(w1Data)
#    print (w1Data)

    w1DataSTR = str(w1Data)

    file = open(fileName,"w+")
    file.write(w1DataSTR)
    file.close()