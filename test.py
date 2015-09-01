a = 5;

def fun():
	a = 10;
	print(a)

def conflict():
	print(a)

print(a)
fun()
conflict()