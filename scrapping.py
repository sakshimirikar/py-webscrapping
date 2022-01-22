import requests
from bs4 import BeautifulSoup
import csv

url="https://coreyms.com/"
page=requests.get(url , verify=True)

soup=BeautifulSoup(page.content,'html5lib')
# print(soup.prettify())

csv_file=open('webscrape.csv', 'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline' , 'summary' , 'video_link'])

for article in soup.find_all('article'):
# print(article.prettify())
    headline=article.a.text
    print(headline)

    summary=article.find('div' , class_='entry-content').p.text
    print(summary)
    
    try:
        vid_source=article.find('iframe' , class_='youtube-player')['src']
        # print(vid_source)
        vid_id=vid_source.split('/')[4]
        # print(vid_id)

        vid_id=vid_id.split('?')[0]

        yt_link=f'https://youtube.com/watch?v={vid_id}'
    except Exception as e: 
        yt_link=None   
    print(yt_link)

    print( )

    csv_writer.writerow([headline , summary , yt_link])

csv_file.close()