import numpy as np
import urllib
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

class dailyQuota(object):
    def __init__(self,code,page_limit=10):
        self.code=code
        self.page_limit=page_limit
    
    def getAcess(self,page):
        url='https://finance.naver.com/item/sise_day.nhn?code={}&page={}'.format(self.code,page)
        r=requests.get(url)
        re=BeautifulSoup(r.content,'html.parser')
        return re
    
    def getDailyInfo(self):
        results=list()
        for i in range(self.page_limit):
            try:
                re=self.getAcess(i)
                trs=re.findAll('tr')
            except:
                logging.error('The page is over the limt.Check out the maximum number of pages')
            for j in range(2,len(trs)-3):
                temp=[data.text.strip() for data in trs[j].findAll('span')]
                results.append(temp)
        results=list(filter(lambda x:len(x)!=0,results)) 
        results=pd.DataFrame(results).drop(2,axis=1)
        results.columns=['date','close','start','high','low','trade(quant)']
        return results
    
    
def main():
    dailyQuota(code='005930').getDailyInfo()    
    
if __name__=='__main__':
    main()
