from bs4 import BeautifulSoup

html = '''
<table>
  <tr>
    <th> 재무정보 </th>
    <th> 2018     </th>
    <th> 2019     </th>
  </tr>
  <tr>
    <td> 매출액 </td>
    <td> 100    </td>
    <td> 200    </td>
  </tr>  
</table>
'''

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("table tr td:nth-of-type(2)")
print(tags[0].text)
