import pickle
from bs4 import BeautifulSoup

datafile = open("piyush.txt", "rb+")
data = pickle.load(datafile)
datafile.close()
soup = BeautifulSoup(data, "html.parser")
divs = soup.find_all("textarea")
for d in divs:
    print(d.text)