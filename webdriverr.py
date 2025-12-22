from selenium import webdriver  
# Imports Selenium's webdriver to control a web browser

from selenium.webdriver.chrome.options import Options  
# Used to set custom options for the Chrome browser

import pickle  
# Used to save (serialize) Python data into a file

options = Options()  
# Creates an object to store Chrome configuration options

driver = webdriver.Chrome(options=options)  
# Launches the Chrome browser using Selenium with the given options

driver.get("https://ashutosh12mar.github.io/Ashutosh/ashu.html")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
# Opens the specified webpage in the browser

data = driver.page_source  
# Fetches the complete HTML source code of the loaded webpage

datafile = open("Ashu.txt", "wb+")  
# Opens (or creates) a file named Ashu.txt in binary write mode

pickle.dump(data, datafile)  
# Saves the webpage HTML source into the file using pickle

datafile.flush()  
# Forces any buffered data to be written to the file

datafile.close()  
# Closes the file to free system resources

print(data)  
# Prints the HTML source code to the terminal

driver.quit()  
# Closes the browser and ends the Selenium session
