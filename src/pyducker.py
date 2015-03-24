'''
Created on Sep 18, 2014

@author: daviis01
'''
import sys
import argparse
from TestAST import testFiles

def main():
    parser = argparse.ArgumentParser(description="A static analysis tool for Python 3.x")
    parser.add_argument('files', metavar='F', type=open, nargs='+',
                   help='an file to statically check')
    parser.add_argument('-n', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='check the variable names in the file only')
    parser.add_argument('-w', action='store_const', const = 'false', help = 'turns of PyDucker warnings')
    args = parser.parse_args()
    
    if args.files:
        testFiles(args.files, args.w) #args.w well tell if PyDuckerWarning should be on or off
    



if __name__ == '__main__':
    main()