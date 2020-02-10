# -*- coding: utf-8 -*-

# 파일 처리
# open 함수
# open(파일명, 모드 [encoding, newline .. ] )

# open 함수를 사용한 파일 생성 예제
# open 함수의 두번째 매개변수(모드)의 값을 w 로
# 지정하게 되면 쓰기 모드로 동작하여 
# 파일이 생성됩니다.
# 주의사항( W 모드로 파일에 접근하는 경우 
# 기존의 파일이 존재한다면, 내용이 삭제됩니다. )
open("data/file_01.txt", "w")