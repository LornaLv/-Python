# Date: 2023/2/21 下午7:53

src_file = open('logo.png', 'rb')  # a表示追加内容

target_file = open('copylogo.png', 'wb')

target_file.write(src_file.read())

target_file.close()
src_file.close()
