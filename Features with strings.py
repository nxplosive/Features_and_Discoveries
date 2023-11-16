# print("----------")
# x = 0.1 + 0.2
# print(x)
# print(round(x,1))
# print(round(1.333333, 2))
# print("----------")
# print("Hello, world!")
# print("\"Hello, world!\"")
# print("""Hello''"", ""''world!""")

'''
a = "Hello, \nworld!"
b = "Hello, " \
     "world!"
c = ("Hello, "
     "world!")
d = """Hello, 
       world!"""
e = r"Hello, \\nworld!"
f = "Hello" "world!"
print(a, b, c, d , e, f, sep="\n")

"""
a = "Hello"
b = "World"
print(a + ", " + b + "!")
print("%s, %s!" % (a, b))
print("{a}, {b}!".format(a=a, b=b))
print(f"{a}, {b}!")
print(f"{a=}, {b=}!")
print(f"{a = }, {b = }!")
print(f"{a.lower()}, {b.upper()}!")
"""
'''

'''
email = "username@domain.com"
print(email[8:12])
print(email[8:-4])
print(email[-4])
print(email[:-4])
print(email[4:-4:3])
print(email[::-1])
#email.split("@")
assert email.endswith(".com")
'''

#url_template = "https://yourservice.com/v1/api/{}"
#users_url = url_template.format("users")
#groups_url = url_template.format("groups")

#s = "1234" #строка
#n = 1234   #число
#assert s == str(n)
#assert int(s) == n