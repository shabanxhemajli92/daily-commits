import argparse
parser=argparse.ArgumentParser()
parser.add_argument("John",help="This is the first name")#this is where you add the arguments
parser.add_argument("Hanson",help="this is the last name")
parser.add_argument("30",help="This is the age")
parser.add_argument("--F",help="This is fast mode enabled")
args=parser.parse_args()
if args=="John":
    print("This is the first name")
if args=="Hanson":
    print("This is the last name")    
if args=="30":
    print("this is the age")
if args=="--F":
    print("Fast mode enabled")    