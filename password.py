password = 'a123456'
cnt = 3
while cnt > 0:
	pw = input('請輸入密碼：')
	if pw != password:
		cnt-=1
		if cnt > 0:
			print('密碼錯誤! 還有', cnt, '次機會')
		else:
			print('沒機會嘗試了!要鎖帳號了啦!')
	else:
		print('登入成功')
		break