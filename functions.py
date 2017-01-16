import requests
import json
import re
import numpy as np
import pandas as pd
import time
from data import countries


def countryParser(country):
    for i in range(len(countries)):
        if country.lower() in countries[i]:
            country = countries[i][0]
    return country.lower()


def dateParser(date):
    date = date.split('-')
    if len(date) == 1 and len(date[0]) == 4:
        date = [date[0] + '/1', date[0] + '/12']
    elif len(date) == 1 and (len(date[0]) in (6, 7)):
        date = [date[0], date[0]]
    elif len(date) == 2 and len(date[0]) == 4 and len(date[1]) == 4:
        date = [date[0] + '/1', date[1] + '/12']
    elif len(date) == 2 and len(date[0]) == 4 and (len(date[1]) in (6, 7)):
        date = [date[0] + '/1', date[1]]
    elif len(date) == 2 and (len(date[0]) in (6, 7)) and len(date[1]) == 4:
        date = [date[0], date[1] + '/12']
    return date


def getYearInflat(arr, i=0, yearInflat=np.array(['date', 'rate'])):
    if i < len(arr) - 1:
        monthRate = np.array([])
        year = arr[i][0][:4]
        while arr[i][0][:4] == year and i < len(arr) - 1:
            monthRate = np.append(monthRate, 1 + float(arr[i][1]) / 100)
            i += 1
        yearInflat = np.vstack([yearInflat, [year, (round(np.prod(monthRate), 4) - 1) * 100]])
        return getYearInflat(arr, i, yearInflat=yearInflat)
    else:
        return yearInflat[1:]  # without ['date', 'rate']


def CalculateInflationRate(country, start, end):
    url = 'https://www.statbureau.org/calculate-inflation-rate-json'
    payload = {
        'country': country,
        'start': start,
        'end': end
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.content.decode('utf-8')[1:-1]


def CalculatePriceChange(country, start, end, amount):
    url = 'https://www.statbureau.org/calculate-inflation-price-json'
    payload = {
        'country': country,
        'start': start,
        'end': end,
        'amount': amount,
        # 'denominationsToApply': denominationsToApply
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.content.decode('utf-8')


def CalculateValueChange(country, start, end, amount):
    url = 'https://www.statbureau.org/calculate-inflation-value-json'
    payload = {
        'country': country,
        'start': start,
        'end': end,
        'amount': amount,
        # 'denominationsToApply': denominationsToApply
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.content.decode('utf-8')


def getDenominations(country):
    url = 'https://www.statbureau.org/get-denominations-json'
    payload = {'country': country}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    data = response.content.decode('utf-8')
    arr = np.array(['date', 'denomitation from', 'denomination to', 'ISO code from', 'ISO code to'])
    if len(data) == 0:
        arr = np.vstack((arr, ['NULL'] * 5))
    else:
        for i in data[2:-2].split('},{'):
            denomDate = time.ctime(int(re.findall(r'Date\(\d+', i)[0][5:-3]))
            denomDate = time.strftime("%Y/%m/%d", time.strptime(denomDate))
            denFrom = re.findall(r'DenominationFrom":\d+', i)[0][18:]
            denTo = re.findall(r'DenominationTo":\d+', i)[0][16:]
            IsoCodeFrom = re.findall(r'CurrencyFromIso3Code":"\w+', i)[0][23:]
            IsoCodeTo = re.findall(r'CurrencyToIso3Code":"\w+', i)[0][21:]
            arr = np.vstack((arr, [denomDate, denFrom, denTo, IsoCodeFrom, IsoCodeTo]))
    return arr


def getData(country, byMonth=True):
    url = 'https://www.statbureau.org/get-data-json'
    payload = {'country': country}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    data = response.content.decode('utf-8')[2:-2]

    country = re.search(r'"Country":\d+', data).group(0)[10:]
    month = re.findall(r'\d\d\d\d-\d\d-\d\d', data)
    inflationRate = re.findall(r'"InflationRateFormatted":"-?\d+.\d\d"', data)
    for i in range(len(inflationRate)):
        inflationRate[i] = inflationRate[i][26:-1]
    arr = np.column_stack((month, inflationRate))
    if not byMonth:
        arr = getYearInflat(arr)

    return pd.DataFrame(arr, columns=['date', 'rate']).to_csv()
