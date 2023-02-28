# Date: 2023/2/21 下午8:54
with open('logo.png', 'rb') as src_file:
    with open('copy2logo.png', 'wb') as target_file:
        target_file.write(src_file.read())
