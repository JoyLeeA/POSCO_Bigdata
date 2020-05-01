import re

news = '''
이에 이 전 총리는 지난 16일 페이스북에서 “저는 1994년부터 살아온 제 아파트를 전세 놓고, 그 돈으로 종로 아파트에 전세로 들어간다”고 
해명한 바 있다. 하지만 잠원동 아파트의 준공 후 입주 시점이 이 전 총리가 밝힌 1994년 이후인 것으로 알려지면서 또 의문이 증폭됐었다.  
한영혜 기자 han.younghye@joongang.co.kr
'''

p = re.compile("[A-Za-z0-9\.]+@[A-Za-z0-9\.]+\.(com|co.kr|net)")
news1 = p.sub("", news)
print(news1)

#p = re.compile(r"[가-힣 \d]+")
#m = p.findall(news)
#print(m)
