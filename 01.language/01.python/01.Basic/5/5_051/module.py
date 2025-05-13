from arithmetic import basic as bs
from arithmetic import dev
from shape import circle as ci
from  shape import trisquare as ts

n1=float(input("숫자 1 입력"))
n2=float(input("숫자 2 입력"))

bs.add(n1,n2)
bs.sub(n1,n2)
bs.mul(n1,n2)
bs.div(n1,n2)

dev.mod(n1, n2)
dev.flo(n1, n2)
dev.pow(n1, n2)

ci.cirarea(n1)
ci.cirarea(n2)

ts.tri(n1,n2)
ts.rect(n1,n2)