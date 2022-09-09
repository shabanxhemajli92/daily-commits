import re


text = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com

Kind regards,
Tanisha"""

email_match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+',text)#prints the emails
print(email_match)
somthelse_match=re.findall(r'\d+\w+\w',text)#prints the first part of the 2pac emails till the @ char
print(somthelse_match)
somthelse_match2=re.search(r'\w+[^abc]+.I',text)#prints Okay I and boy how I
print(somthelse_match2)
