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
    intClass = ClassDefBean()
    intClass.FunDefArr['__add__'] = FunDefBean([('self', 'int'),('value', 'int')],  'int', '__add__')
    intClass.FunDefArr['__bool__'] = FunDefBean([('self' , 'int')] , 'int', '__bool__')
    intClass.FunDefArr['__eq__'] = FunDefBean([('self', 'int'), ('value' , 'int')], 'bool' , '__eq__')
    intClass.FunDefArr['__float__'] = FunDefBean([('self', 'int')], 'float', '__float__')
    intClass.FunDefArr['__floordiv__'] = FunDefBean([('self', 'int'), ('value' , 'int')],  'int', '__floordiv__')
    intClass.FunDefArr['__ge__'] = FunDefBean([('self' , 'int'),('value' , 'int' )], ('returntype', 'bool'), '__ge__')
    intClass.FunDefArr['__gt__'] = FunDefBean([('self' , 'int'),('value' , 'int')],  'bool', '__gt__')
    intClass.FunDefArr['__invert__'] = FunDefBean([('self', 'int')], 'int', '__invert__')
    intClass.FunDefArr['__le__'] = FunDefBean([('self' , 'int') , ('value' , 'int')], 'bool', '__le__')
    intClass.FunDefArr['__lshift__'] = FunDefBean([('self' , 'int'), ('value' , 'int')] ,  'int', '__lshift__')
    intClass.FunDefArr['__lt__'] = FunDefBean([('self' , 'int') , ('value' , 'int')] ,  'bool', '__lt__')
    intClass.FunDefArr['__mul__'] = FunDefBean([('self' , 'int') , ('value' , 'int')] ,  'int', '__mul__')
    intClass.FunDefArr['__rshift__'] = FunDefBean([('self' , 'int'), ('value' , 'int')] ,  'int', '__rshift__')
    intClass.FunDefArr['__xor__'] = FunDefBean([('self' , 'int') , ('value' ,'int')] , 'int', '__xor__')
    intClass.FunDefArr['__str__'] = FunDefBean([('self' , 'int')] ,  'str', '__str__')
    intClass.FunDefArr['__sub__'] = FunDefBean([('self', 'int') , ('value' , 'int')] ,  'int', '__sub__')
    nameSpace['int'] = intClass
    
    
    
    strClass = ClassDefBean()
    strClass.FunDefArr['__add__'] = FunDefBean([('self' , 'str') , ('value' , 'str') ] , 'str', '__add__')
    strClass.FunDefArr['__contains__'] = FunDefBean([('self' ,'str') , ('key' , 'str')] , 'bool', '__contains__')
    strClass.FunDefArr['__eq__'] = FunDefBean([('self' , 'str') , ('value' , 'str')] , 'bool', '__eq__')
    strClass.FunDefArr['__ge__'] = FunDefBean([('self' , 'str') , ('value' , ' str')] , 'bool', '__ge__')
    strClass.FunDefArr['__gt__'] = FunDefBean([('self' , 'str') , ('value' , 'str')] , 'bool', '__gt__')
    strClass.FunDefArr['__le__'] = FunDefBean([('self' , 'str'), ('value' , 'str')] , 'bool', '__le__')
    strClass.FunDefArr['__len__'] = FunDefBean([('self' , 'str')], 'int', '__len__')
    strClass.FunDefArr['__mul__'] = FunDefBean([('self' , 'str') , ('value' , 'int')] , 'str', '__mul__')
    strClass.FunDefArr['__ne__'] = FunDefBean([('self', 'str') ,('value' ,'str')] , 'bool' , '__ne__')
    strClass.FunDefArr['casefold'] = FunDefBean([('self', 'str')] , 'str', 'casefold')
    strClass.FunDefArr['center'] = FunDefBean([('self' , 'str') , ('width' , 'int')] , 'str', 'center')
    strClass.FunDefArr['encode'] = FunDefBean([('self' , 'str'), ('encoding' , 'str') , ('errors' , 'str')] , 'bool' , 'encode')
    strClass.FunDefArr['find'] = FunDefBean([('self' , 'str'), ('sub' , 'str'), ('start', 'int'),('end' ,'int')], 'int', 'find')
    strClass.FunDefArr['index'] = FunDefBean([('self' , 'str') ,('sub' ,'str'),('start' , 'int'), ('end' , 'int')] , 'int', 'index')
    strClass.FunDefArr['isdecimal'] = FunDefBean([('self' , 'str')] ,  'bool', 'isdecimal')
    strClass.FunDefArr['isdigit'] = FunDefBean([('self' , 'str')] ,  'bool', 'idigit')
    strClass.FunDefArr['islower'] = FunDefBean([('self' , 'str')] ,  'bool', 'islower')
    strClass.FunDefArr['isnumeric'] = FunDefBean([('self' , 'str')] ,  'bool', 'isnumeric')
    strClass.FunDefArr['isprintable'] = FunDefBean([('self' , 'st')] ,  'bool', 'isprintable')
    strClass.FunDefArr['isspace'] = FunDefBean([('self' , 'str')] ,  'bool', 'isspace')
    strClass.FunDefArr['isupper'] = FunDefBean([('self' , 'str')] ,  'bool', 'isupper')
    strClass.FunDefArr['join'] = FunDefBean([('self' , 'str')] ,  'str', 'join')
    strClass.FunDefArr['lower'] = FunDefBean([('self' , 'str')] ,  'str', 'lower')
    strClass.FunDefArr['replace'] = FunDefBean([('self' , 'str') , ('old' , 'str'), ('new' , 'str') , ('count' , 'int')] ,  'str', 'replace')
    strClass.FunDefArr['split'] = FunDefBean([('self' , 'str'), ('sep' , 'str') , ('maxsplit' , 'int')] ,  'list', 'split')
    strClass.FunDefArr['splitlines'] = FunDefBean([('self' , 'str') , ('keepends' , 'boolean')] ,  'list', 'splitlines')
    strClass.FunDefArr['upper'] = FunDefBean([('self' , 'str')] ,  'str', 'upper')
                                                
                                                    
    nameSpace['str'] = strClass
    return nameSpace
