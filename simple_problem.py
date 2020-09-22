contents = '닭장속에는 암탉이 (꼬꼬댁) 문간 옆에는 거위가 (꽥꽥) 배나무 밑엔 염소가 (음메) 외양간에는 송아지 (음매) 닭장속에는 암탉들이 문간 옆에는 거위들이 배나무 밑엔 염소들이 외양간에는 송아지 오 히 야하 오 오오 오 히 야하 오 오 깊은 산속엔 뻐꾸기 (뻐꾹) 높은 하늘엔 종달새 (호르르) 부뚜막 위엔 고양이 (야옹) 마루 밑에는 강아지 (멍멍) 깊은 산속엔 뻐꾸기가 높은 하늘엔 종달새가 부뚜막 위엔 고양이가 마루 밑에는 강아지 오 히 야하 오 오오 오 히 야하 오 오'
contents=contents.replace(' ','')

findlist = ['암탉','거위','염소','송아지','뻐꾸기','종달새','고양이','강아지']

answer = []
start = 0
end_idx = 0
for find in findlist:
    lst = []
    lst.append(find)
    idx=contents.find("(",start)
    end_idx = contents.find(")",idx)
    lst.append(contents[idx+1:end_idx])
    answer.append(lst)
    start = end_idx
    
print(answer)
