
from tqdm import tqdm
import requests
import urllib.request as ur
from bs4 import BeautifulSoup

print("Enter the page link:")
page_link = input()
page = ur.urlopen(page_link)
soup = BeautifulSoup(page, 'html.parser')

for link in soup.find_all('a'):
    tar_link = link.get('href')
    if tar_link.endswith('.tar'):
        url = 'https://archive.org/download/archiveteam-twitter-stream-2018-06/' + tar_link
        don = requests.get(url, stream=True)
        with open(tar_link, 'wb') as file_name:
            for part in tqdm(don.iter_content()):
                if part:
                    file_name.write(part)

