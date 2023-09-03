import re
a = "charlie chaplin coa car and the chocolate factory"
b = "akash.vaishnav1908@gmail.com"
c= "hello"
d = "xyz,yz,xyzz,xyyz,xxzzy,zyz,xxy"
# if want to match a . in any string as it is a spacial character which we can not use so we here use / to match it.

match = re.search(r"\.",b)
print(match)

match2 = re.search(r"@",b) 
print(match2)

match3 = re.findall(r"l",c) 
print(match3)

match4 = re.findall(r"a|h",a)
print(match4)

match5 = re.search(r"^akash",b)
print(match5)

match6 = re.search(f"^a",a)
print(match6)

match7 = re.search(r"\.com$",b)
print(match7)

match8 = re.search(r"lo$",a)
print(match8)

match9 = re.findall(r"c.a",a)
print(match9)

match10 = re.findall(r"a|h",a)
print(match10)

match11= re.findall(r"ch?a",a)
print(match11)

match12 = re.findall(r"ch*a",a)
print(match12)

match13 = re.findall(r"ch+a",a)
print(match13)

match14 = re.findall(r"xy+z",d)
print(match14)

match15 = re.findall(r"y{2,4}",d)
print(match15)

match16 = re.findall(r"(x|z)yz",d)
print(match16)

a1 = "harry potter"

num1 = re.search(r'\Ahar',a1)
print(num1)

num2 = re.search(r'\Apott',a1)
print(num2)

num3 = re.search(r'\bhar',a1)
print(num3)

num4 = re.search(r'er\b',a1)
print(num4)

num5 = re.search(r'\Bhar',a1)
print(num5)
num6 = re.search(r'har\B',a1)
print(num6)
num7 = re.search(r'\Ber',a1)
print(num7)

a2 = "harry1 patter3"
num8 = re.search("\d",a2)
print(num8)
num8 = re.findall("\d",a2)
print(num8)

num8 = re.findall("\D",a2)
print(num8)

num9 = re.findall("\s",a2)
print(num9)
num9 = re.findall("\S",a2)
print(num9)

num9 = re.findall("\w",a2)
print(num9)

num9 = re.findall("\W",a2)
print(num9)


num9 = re.findall("3\Z",a2)
print(num9)
num9 = re.findall("3\Z",a2)
print(num9)

c1 = "charli and chocolate factery"
h1 = re.findall("[atx]",c1)
print(len(h1))

h2= re.findall("[a-h]",c1)
print(h2)

p = """Jhon has scored 89 marks 
Lisa has scored 90 marks 
David has scored 70 marks"""
print(re.findall("\d+", p))
print(re.findall(r'[A-Z][a-z]*',p))

p1 = re.compile("[a-d]")
print(re.findall(p1,p))

print(re.split("\d+",p))


print(re.sub("\s+","_",p))
print(re.subn("\s+","_",p))

print(re.escape(p))

string = "Jhon has scored 98 marks"

y1= re.search("\d+",string)
print(y1)
print(y1.re)
print(y1.string)
print(y1.start())
print(y1.end())
print(y1.span())
print(y1.group())