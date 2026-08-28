# How to make a basic web scraping programme using Beautiful Soup

<br>

## Project Summary
Within this tutorial i will be guiding you step-by-step on how to create a basic Web Scraping Programme using python.
The Website that we will be using in this tutorial is <https://www.timesjobs.com/>. TimesJobs is basically an employment portal designed to connect job seekers with recruiters and hiring companies across diverse industries. The platform offers candidates to search for job vacancies by role, location and specific skill set. 

<br>

So our goal is to filter out job applications under "Python" skill set that was "Posted a few days ago". 
Unironically using Python to find Python developer jobs. ;)

### **Step 1: Installing BeautifulSoup and using the request library to see a Websites HTML**

Firstly we need to install BeautifulSoup,requests library and lxml.

    pip install beautifulsoup4
    pip install requests
    pip install lxml

<u>Why do we need the BeautifulSoup and the request library installed?</u>

The main purpose of BeautifulSoup is to parse HTML and XML files so developers can easily extract, navigate and clean data from web pages, and the primary purpose of the Python requests library is to send HTTP requests and interact with web resources in a simple and human-friendly way.


