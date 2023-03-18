import sys
import urllib3
import HTMLPaser
from BeautifulSoup import BeautifulSoup
URL = sys.argv[1]

XFN_TAGS = set([
    'colleague',
    'kolade', 
    ''
])