# -*- coding: utf-8 -*-

# 파일에 내용을 추가하는 방법
# 파일 경로와 같은 경우 / 를 기준으로 작성합니다.
# (\\ 도 사용 가능)
output_file_name = "data\\file_02.txt"

print(output_file_name)

# open 함수의 결과를 대입받는 변수
# open 함수의 모드 매개변수에 따라서
# 파일의 내용을 읽거나(R), 파일에 내용을
# 추가할 수 있는 변수가 됩니다.
output = open(output_file_name, "w")

# w 모드를 사용하여 파일을 open 하게 되면
# 해당 변수를 사용하여 데이터를 파일에 추가할 수
# 있습니다.(write 메소드를 사용)
output.write("파일 내용 작성 테스트")

# flush 메소드
# - 파일에 대한 출력은 기본적으로 버퍼를 활용
# - 파일에 출력되는 데이터는 실제로 버퍼공간에
#   기록되어 입출력 성능을 향상사킴
# - 버퍼의 저장된 내용을 실제 파일로 출력하기 
#   위해서 flush 메소드가 사용됨
# - flush 메소드는 버퍼에 기록된 내용을
#   실제 파일로 출력하고, 버퍼를 비우는 역할
output.flush()

# 파일과 같이 시스템의 리소스에 접근하는 경우
# 반드시 close 메소드를 호출하여
# 연결을 종료해야만 합니다.
# - close 메소드가 실행될 때, 만약 버퍼에 데이터가
#   존재하는 경우 파일로 출력됩니다.
output.close()

































