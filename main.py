from bs4 import BeautifulSoup
import requests
import lxml

header = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
url = 'https://select.by/kurs/'
req = requests.get(url, headers=header)
#scr = req.text

# with open('index.html', 'w', encoding='utf-8') as file:
#      file.write(scr)
with open('index.html', encoding='utf-8') as file:
    scr = file.read()
soup = BeautifulSoup(scr, 'lxml')
sum_dollars = int(input('Введите сумму в долларах:'))
sum_b_rub = soup.find('td', class_="align-bottom")\
    .find_next()\
    .find_next()\
    .find_next()\
    .text\
    .strip('\n                    \n                ')\
    .replace(',', '.')

try:
  print(f'Sum:{float(sum_b_rub) * sum_dollars}')
except:
    print('value error')



