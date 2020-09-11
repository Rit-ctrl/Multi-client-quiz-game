import sys, select
from timeit import default_timer as timer

print("You have ten seconds to answer!")

start = timer()
i, o, e = select.select( [sys.stdin], [], [], 3 )


if (i):
  x=sys.stdin.readline().strip()
  print("You said", x)
else:
  print("You said nothing!")
end = timer()

print(i)
print(o)
print(e)




print(end - start) 