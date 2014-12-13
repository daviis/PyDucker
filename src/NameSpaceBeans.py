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
    intClass.funs['__add__'] = FunDefBean(['self', 'int'],  'int', '__add__')
    intClass.funs['__bool__'] = FunDefBean(['self'] , 'int', '__bool__')
    intClass.funs['__eq__'] = FunDefBean(['self' , 'int'], 'bool' , '__eq__')
    intClass.funs['__float__'] = FunDefBean(['self'], 'float', '__float__')
    intClass.funs['__floordiv__'] = FunDefBean(['self' , 'int'],  'int', '__floordiv__')
    intClass.funs['__ge__'] = FunDefBean(['self' , 'int' ],  'bool', '__ge__')
    intClass.funs['__gt__'] = FunDefBean(['self' , 'int'],  'bool', '__gt__')
    intClass.funs['__invert__'] = FunDefBean(['self'], 'int', '__invert__')
    intClass.funs['__le__'] = FunDefBean(['self' , 'int'], 'bool', '__le__')
    intClass.funs['__lshift__'] = FunDefBean(['self' , 'int'] ,  'int', '__lshift__')
    intClass.funs['__lt__'] = FunDefBean(['self' , 'int'] ,  'bool', '__lt__')
    intClass.funs['__mul__'] = FunDefBean(['self' , 'int'] ,  'int', '__mul__')
    intClass.funs['__rshift__'] = FunDefBean(['self' , 'int'] ,  'int', '__rshift__')
    intClass.funs['__xor__'] = FunDefBean(['self' , 'int'] , 'int', '__xor__')
    intClass.funs['__str__'] = FunDefBean(['self'] ,  'str', '__str__')
    intClass.funs['__sub__'] = FunDefBean(['self' , 'int'] ,  'int', '__sub__')
    intClass.funs['__pos__'] = FunDefBean(['self' , 'int'] ,  'int', '__pos__')
    intClass.funs['__neg__'] = FunDefBean(['self' , 'int'] ,  'int', '__neg__')
    nameSpace.put(intClass.name, intClass)
    
    
    
    strClass = ClassDefBean('str', None)
    strClass.funs['__add__'] = FunDefBean(['self' , 'str' ] , 'str', '__add__')
    strClass.funs['__contains__'] = FunDefBean(['self' , 'str'] , 'bool', '__contains__')
    strClass.funs['__eq__'] = FunDefBean(['self' , 'str'] , 'bool', '__eq__')
    strClass.funs['__ge__'] = FunDefBean(['self' , ' str'] , 'bool', '__ge__')
    strClass.funs['__gt__'] = FunDefBean(['self' , 'str'] , 'bool', '__gt__')
    strClass.funs['__le__'] = FunDefBean(['self' , 'str'] , 'bool', '__le__')
    strClass.funs['__len__'] = FunDefBean(['self'], 'int', '__len__')
    strClass.funs['__mul__'] = FunDefBean(['self' , 'int'] , 'str', '__mul__')
    strClass.funs['__ne__'] = FunDefBean(['self' , 'str'] , 'bool' , '__ne__')
    strClass.funs['casefold'] = FunDefBean(['self'] , 'str', 'casefold')
    strClass.funs['center'] = FunDefBean(['self' , 'int'] , 'str', 'center')
    strClass.funs['encode'] = FunDefBean(['self' , 'str' , 'str'] , 'bool' , 'encode')
    strClass.funs['find'] = FunDefBean(['self' , 'str' , 'int' , 'int'], 'int', 'find')
    strClass.funs['index'] = FunDefBean(['self' , 'str' , 'int' , 'int'] , 'int', 'index')
    strClass.funs['isdecimal'] = FunDefBean(['self'] ,  'bool', 'isdecimal')
    strClass.funs['isdigit'] = FunDefBean(['self'] ,  'bool', 'idigit')
    strClass.funs['islower'] = FunDefBean(['self'] ,  'bool', 'islower')
    strClass.funs['isnumeric'] = FunDefBean(['self'] ,  'bool', 'isnumeric')
    strClass.funs['isprintable'] = FunDefBean(['self'] ,  'bool', 'isprintable')
    strClass.funs['isspace'] = FunDefBean(['self'] ,  'bool', 'isspace')
    strClass.funs['isupper'] = FunDefBean(['self'] ,  'bool', 'isupper')
    strClass.funs['join'] = FunDefBean(['self'] ,  'str', 'join')
    strClass.funs['lower'] = FunDefBean(['self'] ,  'str', 'lower')
    strClass.funs['replace'] = FunDefBean(['self' , 'str' , 'str' , 'int'] ,  'str', 'replace')
    strClass.funs['split'] = FunDefBean(['self' , 'str' , 'int'] ,  'list', 'split')
    strClass.funs['splitlines'] = FunDefBean(['self' , 'boolean'] ,  'list', 'splitlines')
    strClass.funs['upper'] = FunDefBean(['self'] ,  'str', 'upper')
    nameSpace.put(strClass.name, strClass)
    
    boolClass = ClassDefBean('bool', None)
    boolClass.funs['__eq__'] = FunDefBean(['self', 'bool'], 'bool', '__eq__')
    nameSpace.put(boolClass.name, boolClass)

    listClass = ClassDefBean('list' , None)
    listClass.funs['__contains__'] = FunDefBean(['self' , 'obj'], 'bool', '__contains__')
    nameSpace.put(listClass.name , listClass)

    dictClass = ClassDefBean('dict' , None)
    dictClass.funs['__contains__'] = FunDefBean(['self' , 'obj'], 'bool', '__contains__')
    nameSpace.put(dictClass.name, dictClass) 
    return nameSpace
