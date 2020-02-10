# -*- coding: utf-8 -*-
"""
class Car:
    honk = '빵빵'
    
    def info(self, color, year):
        print("color : %s , year : %d" format(color, year))
        
위와 같이 클래스 메소드의 첫 번째 인수로 self를 써 줘야하만 해당 메소드(여기선 info)를 
인스턴스의 메소드로 사용할 수 있게 됩니다.

self는 간단히 말하면 이 메소드를 부르는 객체(my_car)가 해당 클래스(Car)의 인스턴스인지 
확인해주기 위한 장치입니다.

하지만 단순히 확인하는 것에서 나아가 self를 이용하여 객체 내의 정보를 저장하거나 불러올 수 있습니다.

class Car:
    honk = '빵빵'
    
    def set_info(self, color, year):
        self.color = color
        self.year = year
        
    def get_info(self)
        print("color : %s , year : %d" format(self.color, self.year))

my_car = Car()
my_car.set_info("Red", 2017)

위에서 my_car라는 Car의 인스턴스를 이용하여 my_car.set_info("Red", 2017)를
수행하면 self.color에는 "Red" 값이, self.year에는 2017값이 저장되게 됩니다.
이 때 self는 my_car라는 객체입니다.

get_info()라는 메소드는 self를 통해서 my_car에 해당하는 color와 year를 리턴하게 됩니다.

==============================================================================

실습
 
1. Member 라는 클래스를 만들어 봅시다.
2. setId 라는 클래스 메소드(멤버 메소드)를 만들고 id와 비밀번호를 인자로 받습니다.
3. setId 클래스 메소드 내에 self를 이용하여 해당 인스턴스의 아이디와 비밀번호를 
   각각 변수에 저장합니다.
4. getId 라는 클래스 메소드를 만든 뒤 호출하면 아이디와 비밀번호를 출력하도록 합니다.
5. Member 클래스의 인스턴스를 두 개 만든 후 setId와 getId 메소드를 자유롭게 실행해봅시다.

"""

class Member:
    
    def setId(self, id1, password):
        
        self.id1 = id1
        self.password = password
        
    def getId(self):
        
        print(f'이 멤버의 id는 {self.id1} 이며, 비밀번호는 {self.password} 입니다.')
        
a = Member()
a.setId('wonjun0901', 'quadmed')
a.getId()

print(a.id1)
