proudcts = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input ('請輸入商品價格:')
	price = int(price)
	proudcts.append([name,price])
print(proudcts)

for p in products:
	print(P[0],'的價格是',P[1])

with open ('products.cvs','w',encoding='utf-8') as f:
	f.write('商品,價格')
	for p in products:
		f.write(p[0] + ','+ p[1] + '\n')