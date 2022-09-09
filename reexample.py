import re  # import the regular expression library
text_to_be_searched = "some text mail@web.de some text"  # target text
pattern = r"^s.+t$"  # the actual regular expression (r stands for raw string)
x = re.match(pattern, text_to_be_searched)  # using the pattern to search the target text
print(x)  # printing out the match