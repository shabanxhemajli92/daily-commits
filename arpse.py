import argparse
parser=argparse.ArgumentParser()#this is where you open the parser/initstantiating the parser
parser.add_argument("Hotels",help="There is only3 hotels(Delfin,Bellvie,Titanic)and after you type the Hotel name it is going to tell you the location")#this is where you add the arguments
args=parser.parse_args()#this is where the parsing happens and this is where you close the functions
if args.Hotels=="Delfin":
    print("This is located in Antalya")
elif args.Hotels=="Bellvie":
        print("This is hotel is located in Bodrum ")
elif args.Hotels=="Titanic":
    print("This hotel is located in Cesme")
else:
    print("This is not a turistic destination")            

#in order to add arguments to the parser, for each new argument you would have to write a new argument
 