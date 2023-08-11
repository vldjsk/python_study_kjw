### 파일 출력 ###

# 1. (텍스트 파일) 생성
file = open('file_output.txt', 'wt')
file.write('hello, this is a sample text file!')
file.close()
# 2. (텍스트 파일) 내용 추가하기
file = open('file_output.txt', 'a')
file.write('\n') # \n 줄바꿈
file.write('This is additional text!')
file.close()