from tika import parser 
from pathlib import Path
import re

yearacl = input("Enter a year: ")

if yearacl == '2000':
    yearc = 101
elif yearacl == '2015':
    yearc = 55
elif yearacl == '2016':
    yearc = 55
elif yearacl == '2017':
    yearc = 89
elif yearacl == '2018':
    yearc = 101
elif yearacl == '2019':
    yearc = 115
elif yearacl == '2020':
    yearc = 204
    yearc1 = 63
elif yearacl == '2021':
    yearc = 53

for i in range(1,yearc+1):
     raw = parser.from_file('C:/IT Workshop Project/Downloaded Papers/PDF/2021/Document'+str(i)+'.pdf')
     a = raw['content']
     with Path('C:/IT Workshop Project/Downloaded Papers/TXT/2021/Document'+str(i)+'.txt').open(mode='w',encoding='utf-8') as output_file:
          output_file.write(a)