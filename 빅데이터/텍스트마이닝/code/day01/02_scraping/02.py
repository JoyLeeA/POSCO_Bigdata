from bs4 import BeautifulSoup

html = '''
<ul> 
  <li>1교시</li>
  <li>2교시</li>
</ul>

<ol> 
  <li>3교시</li>
  <li>4교시</li>
</ol>
'''

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("ol li")

for tag in tags:
    print(tag.text)
