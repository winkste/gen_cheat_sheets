TEST = 2

if TEST == 0:
    import argparse
    parser = argparse.ArgumentParser()
    parser.parse_args()

#this results in the following:
#$ python3 prog.py --help
#usage: prog.py [-h]

#options:
#  -h, --help  show this help message and exit
#---------------------------------------------------------------

if TEST == 1:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")
    args = parser.parse_args()
    print(args.echo)

#this results in the following:
#$ python3 prog.py
#usage: prog.py [-h] echo
#prog.py: error: the following arguments are required: echo
#$ python3 prog.py --help
#usage: prog.py [-h] echo

#positional arguments:
#  echo     echo the string you use here

#options:
#  -h, --help  show this help message and exit
#$ python3 prog.py foo
#foo
#---------------------------------------------------------------
if TEST == 2:
    import argparse
    parser = argparse.ArgumentParser(description = "this is the description of the program")
    parser.add_argument("-e", "--emul", help="emulation mode active", action="store_true")
    parser.add_argument("-i", "--input", type=str, help="input file")
    parser.add_argument("-o", "--output", type=str, help="output file")
    parser.add_argument("-t", "--target", type=str, help="target selection")
    args = parser.parse_args()
    
    if args.emul:
        print("emulation mode on")
    
    if args.input:
        print(args.input)
    
    if args.output:
        print(args.output)

    if args.target:
        print(args.target)

#this results in the following output:
#stephan_wink@winkste-mbp scripts % python3 cc_argparse.py -e -i "c:\input" -o "c:\output" -t "x86"    
#emulation mode on
#c:\input
#c:\output
#x86