import random

r = random.randint(1,100)
while True:
	ans = input('請在1~100間猜一個數字:')	
	ans = int(ans)
	if ans == r:
		print('你猜中了！')
		break
	elif ans > r:
		print('你猜的比正確答案大')
	elif ans < r:
		print('你猜的比正確答案小')