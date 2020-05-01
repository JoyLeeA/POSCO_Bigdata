words = ["설", "연휴", "민족", "대이동", "시작", "늘어", "교통량",
         "교통사고", "특히", "자동차", "고장", "상당수", "차지",
         "나타", "것", "기자"]

stopwords = ["가다", "늘어", "나타", "것", "기자"]

words2 = [w for w in words if w not in stopwords]
print(words2)
