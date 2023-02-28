# Date: 2023/2/23 下午5:55
# 京东购物流程
lst = []
for i in range(5):
    goods = input('请输入商品编号和商品名称进行商品入库，每次只能输入一件商品\n')
    lst.append(goods)
for item in lst:
    print(item)

cart = []
while True:
    num = input('请输入要购买的商品的编号：')
    for item in lst:
        if item.find(num) != -1:
            cart.append(item)
            break
    if num == 'q':
        break
print('您购物车里已经选择的商品有：')
'''for m in cart:
    print(m)'''

for m in range(len(cart) - 1, -1, -1):
    print(cart[m])
