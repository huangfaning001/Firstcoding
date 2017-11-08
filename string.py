#__author__:'Faning Huang'
#__time__:'2017/11/8 0008 下午 9:57'

#字符串（string）

# a = "Let's go!"
# print(a)

# * 重复输出字符串
# print('Hello,world!'*10)

# []通过索引获取字符串中字符，这里和列表的切片操作是相同的
# print('helloworld'[2:])

#关键字 in
# print(123 in [12,56,123])
# print('hh' in 'hello')


# % 格式字符串
# print('FN is a good man')
# print('%s is a good man'%'FN')

#字符拼接
# a = '123'
# b = 'abc'
# d = '000'
# c = a + b
# print(c)

# c='***'.join([a,b,d])
# print(c)


#String的内置方法

st = 'Hello Kitty'
# print(st.count('l')) #统计元素个数
# print(st.capitalize()) #首字母大写
# print(st.center(50,'-')) #居中
# print(st.endswith('y')) #以判断是否以某个内容结尾
# print(st.startswith('He')) #判断是否以某个内容开头
# st = 'He\tllo Kitty
# print(st.expandtabs(tabsize=10))
# print(st.find('t')) #查找到第一个元素,并将索引值返回
# st = 'Hello Kitty {name} is {age}'
# print(st.format(name='FN',age='25')) #格式化输出的另一种方式
# print(st.format_map({'name':'FN','age':'26'}) )
# print(st.index('t'))
# print('abc456'.isalnum())
# print('0100'.isdecimal())
# print('888'.isdigit())
# print('99656'.isnumeric())
# print('a98798656'.isidentifier())
# print('aBc'.islower())
# print('BSS'.isupper())
#print(' 2 '.isspace())
# print('My Title'.istitle())
# print('BoY Girl'.lower())
# print('BoY GirL'.upper())
# print('BoY GirL'.swapcase())
# print('BoY GirL'.ljust(20,'*'))
# print('BoY GirL'.rjust(20,'*'))
# print('    \tBOy girl\n'.strip())
# print('    \tBOy girl\n'.lstrip())
# print('    \tBOy girl\n'.rstrip())
# print('Boy Girl')
# print('Boy Boy  GIRL'.replace('Boy','Girl',1))
# print('Boy Girl'.rfind('l'))
# print('Boy Girl Girl'.split('i'))
# print('BOY girl girl'.rsplit('g',1))
# print('bOY giRl'.title())

#摘一些重要的字符串方法
print(st.count('l'))
print(st.center(50,'-'))
print(st.startswith('He'))
print(st.find('t'))
print(st.format(name='FN',age='25'))
print('BoY Girl'.lower())
print('BoY GirL'.upper())
print('Boy Boy  GIRL'.replace('Boy','Girl',1))
print('Boy Girl Girl'.split('i'))
print('    \tBOy girl\n'.strip())


