# import requests
# from bs4 import BeautifulSoup
# import pprint
#
# res = requests.get('https://www.thehindu.com/news/international/')
# # res2 = requests.get('https://news.ycombinator.com/news?p=2')
# soup = BeautifulSoup(res.text, 'html.parser')
# # soup2 = BeautifulSoup(res2.text, 'html.parser')
#
# links = soup.select('.story4-3x33-text')
# def stp(links):
#     li = []
#     for i in range(3):
#         title = links[i].getText()
#         href = links[i].get('href', None)
#         li.append({title:href})
#     return li
# print(stp(links))
# # subtext = soup.select('.subtext')
# # links2 = soup2.select('.storylink')
# # subtext2 = soup2.select('.subtext')
#
# # mega_links = links + links2
# # mega_subtext = subtext + subtext2
#
# # def scrape(links, # subtext):
# #     hn = []
# #     for idx, item in enumerate(links):
# #         title = item.getText()
# #         href  = item.get('href', None)
# #         point = subtext[idx].select('.score')
# #         if len(point):
# #             votes = int(point[0].getText().replace(' points', ''))
# #             if votes > 99:
# #                 hn.append({'title': title, 'link': href, 'points': votes})
# #         with open(r"C:\Users\appu\Desktop\charm.py\test.txt", 'w') as f:
# #             for i in hn:
# #                 f.write(f"{i['title']}:{i['link']}\n")
# #     print('"Created"')
# #     return sorted(hn, key= lambda k:k['points'], reverse=True)
# # pprint.pprint(scrape(mega_links, mega_subtext))
# price = soup.select(".a-price-whole")
# stars = soup.select(".a-icon.a-icon-star-small.a-star-small-4.aok-align-bottom")
# name = soup.select(".pa-size-medium.a-colr-base.a-text-normal")
# links = soup.select(".a-link-normal.a-text-normal")
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# m,j = input("Enter from and to pages you want to scrap: ").split(" ")
# v = int(input("Enter price of mobile you want to search: "))

k = "https://www.snapdeal.com/search?keyword=phones&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=true&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=mobiles&url=&utmContent=&dealDetail=&SRPID=Recent&sort=rlvncy"
res = requests.get(k) # requests the servers
soup = BeautifulSoup(res.text, "html.parser") # crawls through the link
price = soup.select(".lfloat.product-desc-price.strike") #soup.find_all('span', class_="lfloat product-price")
dis = soup.select(".lfloat.product-price")
name = soup.select(".product-title") # selects the name of the product
links = soup.select(".dp-widget-link.noUdLine")
# print(dis[1].getText().replace("% Off",""))

def my_own(links,price):
    sd = []
    for idx, items in enumerate(links[::2]):
        title = name[idx].getText().replace("\n","")
        m = re.sub(r'[^A-Za-z0-9 ]+', '', title)
        href = items.get('href', None)
        original_price = price[idx].getText()
        discount = dis[idx].getText()
        sd.append({"title": m, "href": href, "original_price": original_price, "discount": discount})
        print(sorted(sd, key= lambda sd:sd['discount']))
        with open(r"C:\Users\appu\Desktop\charm.py\data.txt", 'a') as file:
            file.write(f"{m}, {original_price},price after discount {discount}\n {href}\n")
    print("Done dana done")

my_own(links,price)
res2 = requests.get('https://www.amazon.in/s?k=phones&rh=n%3A1389401031&ref=nb_sb_noss')
