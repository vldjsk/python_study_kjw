# if문 복습 예제
# : 영화의 평범을 입력받아, 이 평점에따라 다른 메시지를 출력하는 프로그램

# 평점ㅁ이 8 이상이면 '훌륭한 영화입니다'
# 평점이 5 이상 8 미만이면 '괜찮은 영화입니다'
# 그렇지않으면 '기대이하입니다'

rating = float(input('영화의 평점을 입력하세요'))

if rating >= 8:
    print('훌륭한 영화입니다')
elif rating >= 5:
    print('괜찮은 영화입니다')
else:
    print('기대이하입니다')