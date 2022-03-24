# ### Write a program anti_html.py that takes a URL as an argument, downloads the HTML from the web, and prints it after stripping HTML tags

#importing Libraries
from bs4 import BeautifulSoup
import urllib.request


#defining function
def strip_html(url):
    
    #open url to read
    html = urllib.request.urlopen(url).read()
    #initializing the beautifulsoup object
    soup = BeautifulSoup(html)

    #for loop to iterate on the tag strings in the list
    for script in soup(["script", "style"]):
        #emove the html code with the function decompose
        script.decompose()
        
     #return a list of the remaining string text   
    strips = list(soup.stripped_strings)
    return strips
