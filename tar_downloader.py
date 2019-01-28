
from tqdm import tqdm
import requests
import urllib.request as ur
from bs4 import BeautifulSoup

print("Enter the page link:")
page_link = input()
page = ur.urlopen(page_link)
soup = BeautifulSoup(page, 'html.parser')

print('These files will be downloaded:')
for link in soup.find_all('a'):
    tarlink = link.get('href')
    if tarlink.endswith('.tar'):
        print(tarlink)

for link in soup.find_all('a'):
    tar_link = link.get('href')
    if tar_link.endswith('.tar'):
        url = page_link + '/' + tar_link
        print('\n' + tar_link + ' is being downloaded...')
        don = requests.get(url, stream=True)
        with open(tar_link, 'wb') as file_name:
            for part in tqdm(don.iter_content()):
                if part:
                    file_name.write(part)
