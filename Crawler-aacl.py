from bs4 import BeautifulSoup
import requests
import os

yearacl = input("Enter year: ")
if yearacl == '2015':
     a = 5
elif yearacl == '2016':
     a = 4
elif yearacl == '2017':
     a = 3
elif yearacl == '2018':
     a = 2
elif yearacl == '2019':
     a = 1
elif yearacl == '2020':
     a = 0

main_doc = requests.get('https://aclanthology.org/venues/aacl')
soup = BeautifulSoup(main_doc.text, 'html.parser')
total_conf = (soup.find_all(class_='row'))
total_conferences_in_2021 = len(total_conf[a].find_all('a', class_='align-middle'))
# (soup1.find_all('a', class_='badge badge-primary align-middle mr-1')
# total_conferences_in_2021 = soup.find_all('a',class_="badge badge-primary align-middle mr-1")
conferences_in_2021 = []

print("There are ",total_conferences_in_2021," conferences in ",yearacl,".")


for i in range(0, total_conferences_in_2021):
    conferences_in_2021.append('https://aclanthology.org/'+total_conf[a].find_all('a', class_='align-middle')[i].get('href'))

document_number = 0
for i in range(0, total_conferences_in_2021):
    conference = requests.get(conferences_in_2021[i])
    soup_new = BeautifulSoup(conference.text, 'html.parser')
    total_pdfs_in_the_conference = len(soup_new.find_all('a', class_='badge badge-primary align-middle mr-1'))
    for j in range(0, total_pdfs_in_the_conference):
        url = (soup_new.find_all('a', class_='badge badge-primary align-middle mr-1')[j].get('href'))
        response = requests.get(url)
        file_path = os.path.join("C:/IT Workshop Project/Downloaded Papers/PDF/2020/AACL", f"Document{document_number + 1}.pdf")
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Document{document_number + 1} is downloaded.")
        document_number += 1
print("All documents downloaded successfully.")

