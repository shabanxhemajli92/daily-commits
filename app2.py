import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--f",type=str,help="This is the first name")#this is where you add the arguments
parser.add_argument("--l",type=str,help="this is the last name")
parser.add_argument("--a",type=int,help="This is the age")
parser.add_argument("--F",action="store_true",help="This is fast mode enabled")
args=parser.parse_args()

if args.a==None:
    args.a=100
if args.l==None:
    args.l="Hanson"    
if args.f==None:
    args.f="Lary"
if args.F:
    print("\n","Hello",args.f,args.l,"\n","I see that you have had",str(args.a+1),"birthdays")
    print("fast mode enabled","\n")
else:
    print("\n","Hello",args.f,args.l,"\n","I see you have had",str(args.a+1),"birthdays")       