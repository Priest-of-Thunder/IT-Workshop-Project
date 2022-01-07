import pdftables_api

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
     c = pdftables_api.Client('zgj4kmh68dbj')
     c.xml('C:/IT Workshop Project/Downloaded Papers/PDF/2015/Document'+str(i)+'.pdf', 'C:/IT Workshop Project/Downloaded Papers/XML/2015/Document'+str(i)) 