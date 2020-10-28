# 字符串的编码转换

s = '春风不动柳如纱'

# 编码
# 在 GBK 编码中，一个中文占两个字节
print(s.encode('GBK')) # b'\xb4\xba\xb7\xe7\xb2\xbb\xb6\xaf\xc1\xf8\xc8\xe7\xc9\xb4'

# UTF-8 中，一个中文占三个字节
print(s.encode(encoding='UTF-8')) 

# 解码
# byte 代表的就是一个二进制数据
print(s.encode('GBK').decode(encoding="GBK"))
print(s.encode('UTF-8').decode(encoding="utf-8"))
# print(s.encode('GBK').decode(encoding="UTF-8")) # 解不了，编码格式和解码格式要相同
