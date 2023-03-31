# JTMS-14
# a5 p9.py
# Abdullah Rafique
# arafique@jacobs-university.de

text = input("long string:")
s = input("string to be replace:")
r = input("string replacing:")
print(text)

res = [text.replace(s, r) for sub in text]
print(res)
