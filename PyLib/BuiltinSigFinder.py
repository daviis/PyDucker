"""
A programmatic way to find which methods builtin classes have  

commented out part of info method taken from : http://www.diveintopython.net/power_of_introspection/index.html

@author: Isaac
@created: 2014-11-02
"""
import inspect
import datetime
import sys

def info(object, spacing=10, collapse=1): 
    """
    Print methods and doc strings. Takes module, class, list, dictionary, or string.
    """
    aFile = open("./BuiltIn/" + type(object).__name__ + ".py", "x")   #open a file with the name of the class.py
    
    aFile.write('"""\nA python implementation of built in classes for looking at method signatures.\n\nModified on ' + str(datetime.date.today()) + '\n"""\n\n')
    aFile.write("class " + type(object).__name__ + "():\n")
    stuffList =  inspect.getmembers(object)
    for member in stuffList:
        aFile.write("\tdef " + str(member[0]) + "(self, ???):\n")
        
        aFile.write('\t\t"""\n')
        for aLine in str(getattr(object, member[0]).__doc__).split('\n'):
            aFile.write("\t\t" + aLine + "\n")
        aFile.write('\t\t"""\n\n')
    aFile.close()
        
#     #     methodList = [method for method in dir(object) if callable(getattr(object, method))]
#     processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
#     print ("\n".join(["%s %s" %
#                       (method.ljust(spacing),
#                        processFunc(str(getattr(object, method).__doc__)))
#                      for method in methodList]))

def info_help_class(object):
    aFile = open("./Builtin/" + type(object).__name__ + ".py", "w")   #open a file with the name of the class.py
    sys.stdout = aFile
    help(object)
    aFile.close()
    sys.stdout = sys.__stdout__

def main_class():
#     objs = [1, 'a', [], (), {}, 1.0]
    objs = [True]
    for obj in objs:
        print(type(obj))
        info(obj)
        #print('\n')

def main_fun():
    aFile = open("./HelpTest/fun.py", "w")   #open a file with the name of the class.py
    sys.stdout = aFile
    funs = [__import__, abs, all, any, ascii, bin, bool, bytearray, bytes, callable, chr, classmethod, compile, complex, delattr, dict, dir, divmod, enumerate, eval, exec, filter, float, format, frozenset, getattr, globals, hasattr, hash, help, hex, id, input, int, isinstance, issubclass, iter, len, list, locals, map, max, memoryview, min, next, object, oct, open, ord, pow, print, property, range, repr, reversed, round, set, setattr, slice, sorted, staticmethod, str, sum, super, tuple, type, vars, zip]
    for fun in funs:
        print(fun)
        help(fun)
    aFile.close()
    sys.stdout = sys.__stdout__    
        
def main():
    main_class()
    
if __name__ == '__main__':
    main()