# 간단 연습 1
# width, height, color 속성을 가진 사각형 클래스를 만들고 다음 2개의 객체 만들기
# 직사각형 1개 객체 속성: width = 10, height = 5, color = 'red'
# 정사각형 1개 객체 속성: width = 7, height = 7, color = 'blue'
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
