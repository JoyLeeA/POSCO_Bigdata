from bs4 import BeautifulSoup

html = '''
<div>
  <div class="snack">
    <div id="first"> 양파링 </div>
    <div id="second"> 새우깡 </div>
  </div>
  <div class="icecream">
    <div> 빵빠레 </div>
    <div> 죠스바 </div>
  </div>
</div>
'''

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#second")
print(tags[0].text)