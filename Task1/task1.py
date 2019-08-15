

def func(str):
	a = str.split(',')
	ans = ""

	for cur in a:
		num = int(cur)
		res = 0
		count = 0
		while num > 0:
			digit = num % 10
			num //= 10
			res += (digit * pow(2, count))
			count += 1
		if res % 5 == 0:
			ans += (cur + ",")
			

	if ans[-1] == ',':
		ans = ans[:-1]

	return ans




#str = "010,1111,1010,10010,100000,10100,110,11001,1000101011"
str = "010,1111,1010,10010,100000,10100,110,11"
	
print(func(str))




