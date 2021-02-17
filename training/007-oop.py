# 간단 연습 1
# width, height, color 속성을 가진 사각형 클래스를 만들고 다음 2개의 객체 만들기
# 직사각형 1개 객체 속성: width = 10, height = 5, color = 'red'
# 정사각형 1개 객체 속성: width = 7, height = 7, color = 'blue'
"""
class Rectangle():
    width = 0
    height = 0
    color = ''


square1 = Rectangle()
square2 = Rectangle()

square1.width = 10
square1.height = 5
square1.color = 'red'

square2.width = 7
square2.height = 7
square2.color = 'blue'

print(square1.width, square1.height, square1.color)
print(square2.width, square2.height, square2.color)
"""


# 간단 연습 2
# 아래에 작성한 Quadrangle 클래스를 기반으로 직사각형 1개 객체와 정사각형 1개 객체를 만들고,
# 각 사각형 넓이 출력하기
# 직사각형 속성: width = 10, height = 5, color = 'red'
# 정사각형 설정: width = 7, height = 7, color = 'blue'
"""
class Quadrangle():
    width = 0
    height = 0
    color = ''

    def get_area(self):
        return self.width * self.height

    def set_area(self, width_data, height_data, color_data):
        self.width = width_data
        self.height = height_data
        self.color = color_data


square1 = Quadrangle()
square2 = Quadrangle()

square1.set_area(10, 5, 'red')
square2.set_area(7, 7, 'blue')

print(square1.get_area())
print(square2.get_area())
"""


# 심화 문제
# 위에서 작성한(간단 2) Quadrangle 클래스를 기반으로 직사각형 1개, 정사각형 1개 객체를 만들되,
# width, height, color를 한번에 설정할 수 있는 메소드를 만들고,
# 다음 값으로 각 객체의 속성값을 변경한 후, 사각형 너비와 색상도 함께 출력하기
# 직사각형 속성: width = 10, height = 5, color = 'red'
# 정사각형 속성: width = 7, height = 7, color = 'blue'
class Quadrangle():
    width = 0
    height = 0
    color = ''

    def get_area_and_color(self):
        return self.width * self.height, self.color

    def set_area(self, width_data, height_data, color_data):
        self.width = width_data
        self.height = height_data
        self.color = color_data


square1 = Quadrangle()
square2 = Quadrangle()

square1.set_area(10, 5, 'red')
square2.set_area(7, 7, 'blue')

print(square1.get_area_and_color())
print(square2.get_area_and_color())
