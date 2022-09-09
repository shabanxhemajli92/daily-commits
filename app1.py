import sys

fast_mode=False
for i in sys.argv[1:]:
    if i =="--help":
        print("use --help for help or use --fast for fast mode")
    if i =="--fast":
       fast_mode=True


if fast_mode == True:
    print("Fast mode enabled")
else:
    print("slow mode enabled")       