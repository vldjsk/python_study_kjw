### 파이썬 파일 입출력 ###

# 파일 복사
# 원본파일의 복사본 파일(copy)을 만드는것

# 2. 파일 복사의 절차
# 2-1. 원본 파일 열기
# 2-2. 복사본 파일 생성
# 2-3. 원본파일의 내용읽기 & 복사본 쓰기
# : 원본파일에서한번에 읽어 들이는 테이터의 크기를 1KB(1024Byte)로 설절해 복사프로그램을 구현
# 2-4. 파일 닫기(with문 사용시 생략 가능)

video_size = 1024 # 1024Byte로 1KB를 의미

with open('pexels-rachel-claire-8856785 (2160p).mp4', 'rb') as source:
    with open('copy_video.mp4', 'wb') as copy:
        while True:
            # read(파일의 용량지정)
            buffer = source.read(video_size)
            if not buffer:
                break
            copy.write(buffer)
print('copy_ video.mp4 파일이 복사 되었습니다')