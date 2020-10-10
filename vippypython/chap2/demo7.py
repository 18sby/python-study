# 三引号可以折行输出字符串，保留换行符

str1 = '人生苦短，我用Python'
str2 = "人生苦短，我用Python"
str3 = """人生苦短，
我用
Python"""
str4 = '''人生苦短，
我用
Python'''
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))