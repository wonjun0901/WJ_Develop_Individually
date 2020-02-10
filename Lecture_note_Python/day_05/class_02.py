# -*- coding: utf-8 -*-

# 학생 클래스의 선언
class Student :
    # 클래스 내부에 선언된 변수는 멤버 필드로서
    # 데이터를 저장하기 위해서 사용됩니다.
    # - None -> 값이 없음을 의미하는 키워드
    name = None
    age = None

    # 클래스의 멤버 메소드 선언
    # - 멤버 메소드는 클래스의 내부에 정의된 함수를 의미함
    # - 멤버 메소드는 클래스의 모든 멤버 필드를
    #   활용할 수 있는 함수입니다.
    
    # 클래스의 멤버 메소드와 일반 함수와의 차이점
    # - 클래스의 멤버 메소드를 선언할 때는
    #   반드시 한개의 매개변수를 선언해야합니다.
    #   (매개변수가 사용되지 않는 경우라도...)
    # - 해당 매개변수의 이름은 일반적으로 self로 작성합니다.
    # - self 매개변수는 실제 클래스의 변수가 선언된
    #   위치를 참조하는 변수입니다.
    def printInfo(self) :
        
        # 클래스의 메소드 내부에서 멤버 필드에 
        # 접근하는 경우 self.멤버필드명 으로 사용합니다.
        
        # self 매개변수가 사용되는 이유
        # - 클래스의 멤버 필드들은 각각의 클래스의 변수가
        #   생성될 때마다 만들어집니다.
        # - 반면, 클래스의 멤버 메소드는 단 하나만 생성되어
        #   모든 클래스의 변수(객체)들이 공유하는 형태를 
        #   취합니다.
        # - 이때, 각각의 클래스의 객체들이 저장하고 있는
        #   값들을 메소드 내부에서 접근하기 위해
        #   self 매개변수가 사용됩니다.
        # - self 매개변수에는 현재 멤버 메소드를 실행하고
        #   있는 객체의 참조값이 전달됩니다.        
        print(f"학생의 이름은 {self.name}, 나이는 {self.age} 입니다.")

s1 = Student()

s1.name = "ABC"
s1.age = 20

# 클래스의 객체를 사용하여 멤버 메소드를 호출할 때
# 자동으로 해당 객체의 값이 전달됩니다.
# 아래의 코드는 실제로 다음과 같이 번역되어 실행됩니다.
# s1.printInfo(s1)
s1.printInfo()

s2 = Student('ABC', 20)





















