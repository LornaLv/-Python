# Date: 2023/2/19 下午8:35
# 字符串的编码与解码
s = '天涯共此时'
#编码过程
print(s.encode(encoding='GBK'))  # GBK编码格式中一个中文占两个字节
print(s.encode(encoding='utf-8'))  # utf-8编码格式中，一个字符占三个字节
#解码过程
# bytes代表的是一个二进制数据（字节类型的数据）
byte=s.encode(encoding='GBK')  #编码
print(byte.decode(encoding='GBK'))#解码

byte1=s.encode(encoding='utf-8')  #编码
print(byte1.decode(encoding='utf-8'))#解码
