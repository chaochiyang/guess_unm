import random

r = random.randint(1,100)
count = 0
while True:
	count += 1 # count = count + 1
	ans = input('請在1~100間猜一個數字:')	
	ans = int(ans)
	if ans == r:
		print('你猜中了！')
		print('這是你猜的', count, '次')
		break
	elif ans > r:
		print('比答案大')
	elif ans < r:
		print('比答案小')
	print('這是你猜的', count, '次')