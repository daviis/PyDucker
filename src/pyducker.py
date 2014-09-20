'''
Created on Sep 18, 2014

@author: daviis01
'''
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="A static analysis tool for Python 3.x")
    parser.add_argument('files', metavar='F', type=str, nargs='+',
                   help='an file to statically check')
    parser.add_argument('-n', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='check the variable names in the file only')
    args = parser.parse_args()
    

if __name__ == '__main__':
    main()