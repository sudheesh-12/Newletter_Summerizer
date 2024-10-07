# import requests
# from bs4 import BeautifulSoup
#
#
# url = "https://bbc.com/"
# result = requests.get(url).text
# soup = BeautifulSoup(result,"html.parser")
# img = soup.find_all("img")
# sourse = [x.get("src") for x in img]
# x = sourse[1::2]
# # print(sourse[1::2])
#
# print(type(x))