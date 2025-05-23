### 수심을 입력하면 수온을 출력하는 모듛
import nearmodule

depth = int(input("수심 : "))
na = nearmodule.Near(depth)
temp = na.getNearNum()
print(f"수심의 수온은 {temp}도 입니다.")