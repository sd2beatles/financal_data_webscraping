import numpy as np
import urllib
import requests
from bs4 import BeautifulSoup
import datetime


import sys
import datetime

class individualStock(object):
    def __init__(self,codes):
        self.codes=codes
        self.url='https://finance.naver.com/item/main.nhn?code={}'
    
    def getScript(self,code):
        url=self.url.format(code)
        r=requests.get(url)
        re=BeautifulSoup(r.content,'html.parser')
        return re
    
    def currentPrice(self,re):
        s=re.select('div > p > em')
        todayPrice=s[0].find('span',class_='blind').text
        return todayPrice
    
    def candleData(self,re):
        summary=list()
        trs=re.findAll('tr')
        for i in range(2):
            for j in range(2):
                tr=trs[i]
                tds=tr.findAll('td')
                td=tds[j].find('span',class_='blind').text
                summary.append(td)
        return summary
    
    def finalReport(self):
        reports=list()
        for code in self.codes:
            re=self.getScript(code)
            cprice=self.currentPrice(re)
            csummary=self.candleData(re)
            time=now.strftime("%Y/%m/%d %H:%M:%S")
            temp=[time,cprice]+csummary
            reports.append(temp)
        reports=pd.DataFrame(reports,index=self.codes,columns=['updated_time','current_price','close','high','start','low'])
        return reports
    
def main():
    codes=['005930','066570','068270','252670','017670 ','035720 ']
    results=individualStock(codes).finalReport()
    display(results.head())
    
if __init__=="__main__":
    main()
    

            
