"""
Created Nov-25-2014

@author: Emily
@editor: Isaac

A module that hand makes a namespace which will be used in early testing of PyDucker walking. It generates ClassDefBeans for ints and strs and some of the
FunDefBeans that are inside them.
"""
from Bean import NameSpaceBean, ClassDefBean , FunDefBean

def handMakeNameSpace():
    nameSpace = NameSpaceBean()
    intClass = ClassDefBean('int', None)
    #intClass = ClassDefBean()
    intClass.FunDefArr['__add__'] = FunDefBean(['self', 'int'],  'int', '__add__')
    intClass.FunDefArr['__bool__'] = FunDefBean(['self'] , 'int', '__bool__')
    intClass.FunDefArr['__eq__'] = FunDefBean(['self' , 'int'], 'bool' , '__eq__')
    intClass.FunDefArr['__float__'] = FunDefBean(['self'], 'float', '__float__')
    intClass.FunDefArr['__floordiv__'] = FunDefBean(['self' , 'int'],  'int', '__floordiv__')
    intClass.FunDefArr['__ge__'] = FunDefBean(['self' , 'int' ],  'bool', '__ge__')
    intClass.FunDefArr['__gt__'] = FunDefBean(['self' , 'int'],  'bool', '__gt__')
    intClass.FunDefArr['__invert__'] = FunDefBean(['self'], 'int', '__invert__')
    intClass.FunDefArr['__le__'] = FunDefBean(['self' , 'int'], 'bool', '__le__')
    intClass.FunDefArr['__lshift__'] = FunDefBean(['self' , 'int'] ,  'int', '__lshift__')
    intClass.FunDefArr['__lt__'] = FunDefBean(['self' , 'int'] ,  'bool', '__lt__')
    intClass.FunDefArr['__mul__'] = FunDefBean(['self' , 'int'] ,  'int', '__mul__')
    intClass.FunDefArr['__rshift__'] = FunDefBean(['self' , 'int'] ,  'int', '__rshift__')
    intClass.FunDefArr['__xor__'] = FunDefBean(['self' , 'int'] , 'int', '__xor__')
    intClass.FunDefArr['__str__'] = FunDefBean(['self'] ,  'str', '__str__')
    intClass.FunDefArr['__sub__'] = FunDefBean(['self' , 'int'] ,  'int', '__sub__')
    nameSpace.put(intClass.name, intClass)
    
    
    
    strClass = ClassDefBean('str', None)
    strClass.FunDefArr['__add__'] = FunDefBean(['self' , 'str' ] , 'str', '__add__')
    strClass.FunDefArr['__contains__'] = FunDefBean(['self' , 'str'] , 'bool', '__contains__')
    strClass.FunDefArr['__eq__'] = FunDefBean(['self' , 'str'] , 'bool', '__eq__')
    strClass.FunDefArr['__ge__'] = FunDefBean(['self' , ' str'] , 'bool', '__ge__')
    strClass.FunDefArr['__gt__'] = FunDefBean(['self' , 'str'] , 'bool', '__gt__')
    strClass.FunDefArr['__le__'] = FunDefBean(['self' , 'str'] , 'bool', '__le__')
    strClass.FunDefArr['__len__'] = FunDefBean(['self'], 'int', '__len__')
    strClass.FunDefArr['__mul__'] = FunDefBean(['self' , 'int'] , 'str', '__mul__')
    strClass.FunDefArr['__ne__'] = FunDefBean(['self' , 'str'] , 'bool' , '__ne__')
    strClass.FunDefArr['casefold'] = FunDefBean(['self'] , 'str', 'casefold')
    strClass.FunDefArr['center'] = FunDefBean(['self' , 'int'] , 'str', 'center')
    strClass.FunDefArr['encode'] = FunDefBean(['self' , 'str' , 'str'] , 'bool' , 'encode')
    strClass.FunDefArr['find'] = FunDefBean(['self' , 'str' , 'int' , 'int'], 'int', 'find')
    strClass.FunDefArr['index'] = FunDefBean(['self' , 'str' , 'int' , 'int'] , 'int', 'index')
    strClass.FunDefArr['isdecimal'] = FunDefBean(['self'] ,  'bool', 'isdecimal')
    strClass.FunDefArr['isdigit'] = FunDefBean(['self'] ,  'bool', 'idigit')
    strClass.FunDefArr['islower'] = FunDefBean(['self'] ,  'bool', 'islower')
    strClass.FunDefArr['isnumeric'] = FunDefBean(['self'] ,  'bool', 'isnumeric')
    strClass.FunDefArr['isprintable'] = FunDefBean(['self'] ,  'bool', 'isprintable')
    strClass.FunDefArr['isspace'] = FunDefBean(['self'] ,  'bool', 'isspace')
    strClass.FunDefArr['isupper'] = FunDefBean(['self'] ,  'bool', 'isupper')
    strClass.FunDefArr['join'] = FunDefBean(['self'] ,  'str', 'join')
    strClass.FunDefArr['lower'] = FunDefBean(['self'] ,  'str', 'lower')
    strClass.FunDefArr['replace'] = FunDefBean(['self' , 'str' , 'str' , 'int'] ,  'str', 'replace')
    strClass.FunDefArr['split'] = FunDefBean(['self' , 'str' , 'int'] ,  'list', 'split')
    strClass.FunDefArr['splitlines'] = FunDefBean(['self' , 'boolean'] ,  'list', 'splitlines')
    strClass.FunDefArr['upper'] = FunDefBean(['self'] ,  'str', 'upper')
                                                
                                                    
    nameSpace.put(strClass.name, strClass)
    return nameSpace
