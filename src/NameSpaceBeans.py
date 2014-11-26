# FunDefBean
from Bean import NameSpaceBean, ClassDefBean , FunDefBean, VarBean
def handMakeNameSpace():
    nameSpace = Bean.NameSpaceBean()
    intClass = Bean.ClassDefBean()
    intClass.FunDefArr['__add__'] = Bean.FunDefBean([('self', 'int'),('value', 'int')], ('returntype' , 'int'), '__add__')
    intClass.FunDefArr['__bool__'] = Bean.FunDefBean([('self' , 'int')] ,('returntype' , 'int'), '__bool__')
    intClass.FunDefArr['__eq__'] = Bean.FunDefBean([('self', 'int'), ('value' , 'int')],('returntype' , 'bool')  , '__eq__')
    intClass.FunDefArr['__float__'] = Bean.FunDefBean([('self', 'int')], ('returntype' ,'float'), '__float__')
    intClass.FunDefArr['__floordiv__'] = Bean.FunDefBean([('self', 'int'), ('value' , 'int')], ('returntype' , 'int'), '__floordiv__')
    intClass.FunDefArr['__ge__'] = Bean.FunDefBean([('self' , 'int'),('value' , 'int' )], ('returntype', 'bool'), '__ge__')
    intClass.FunDefArr['__gt__'] = Bean.FunDefBean([('self' , 'int'),('value' , 'int')], ('returntype' , 'bool'), '__gt__')
    intClass.FunDefArr['__invert__'] = Bean.FunDefBean([('self', 'int')], ('returntype' , 'int'), '__invert__')
    intClass.FunDefArr['__le__'] = Bean.FunDefBean([('self' , 'int') , ('value' , 'int')] , ('returntype' , 'bool') , '__le__')
    intClass.FunDefArr['__lshift__'] = Bean.FunDefBean([('self' , 'int'), ('value' , 'int')] , ('returntype' , 'int') , '__lshift__')
    intClass.FunDefArr['__lt__'] = Bean.FunDefBean([('self' , 'int') , ('value' , 'int')] , ('returntype' , 'bool') , '__lt__')
    intClass.FunDefArr['__mul__'] = Bean.FunDefBean([('self' , 'int') , ('value' , 'int')] , ('returntype' , 'int') , '__mul__')
    intClass.FunDefArr['__rshift__'] = Bean.FunDefBean([('self' , 'int'), ('value' , 'int')] , ('returntype' , 'int') , '__rshift__')
    intClass.FunDefArr['__xor__'] = Bean.FunDefBean([('self' , 'int') , ('value' ,'int')] , ('returntype', 'int') , '__xor__')
    intClass.FunDefArr['__str__'] = Bean.FunDefBean([('self' , 'int')] , ('returntype' , 'str') , '__str__')
    intClass.FunDefArr['__sub__'] = Bean.FunDefBean([('self', 'int') , ('value' , 'int')] , ('returntype' , 'int') , '__sub__')
    nameSpace['int'] = intClass
    
    
    
    strClass = Bean.ClassDefBean()
    strClass.FunDefArr['__add__'] = Bean.FunDefBean([('self' , 'str') , ('value' , 'str') ] , ('returntype' , 'str') , '__add__')
    strClass.FunDefArr['__contains__'] = Bean.FunDefBean([('self' ,'str') , ('key' , 'str')] , ('returntype' , 'bool'), '__contains__')
    strClass.FunDefArr['__eq__'] = Bean.FunDefBean([('self' , 'str') , ('value' , 'str')] , ('returntype' , 'bool') , '__eq__')
    strClass.FunDefArr['__ge__'] = Bean.FunDefBean([('self' , 'str') , ('value' , ' str')] , ('returntype' , 'bool') , '__ge__')
    strClass.FunDefArr['__gt__'] = Bean.FunDefBean([('self' , 'str') , ('value' , 'str')] , ('returntype' , 'bool') , '__gt__')
    strClass.FunDefArr['__le__'] = Bean.FundDefBean([('self' , 'str'), ('value' , 'str')] , ('returntype' , 'bool'), '__le__')
    strClass.FunDefArr['__len__'] = Bean.FunDefBean([('self' , 'str')], ('returntype' , 'int') , '__len__')
    strClass.FunDefArr['__mul__'] = Bean.FunDefBean([('self' , 'str') , ('value' , 'int')] , ('returntype', 'str') , '__mul__')
    strClass.FunDefArr['__ne__'] = Bean.FunDefBean([('self', 'str') ,('value' ,'str')] , ('returntype' , 'bool') , '__ne__')
    strClass.FunDefArr['casefold'] = Bean.FunDefBean([('self', 'str')] , ('returntype', 'str'), 'casefold')
    strClass.FunDefArr['center'] = Bean.FunDefBean([('self' , 'str') , ('width' , 'int')] , ('returntype' , 'str') , 'center')
    strClass.FunDefArr['encode'] = Bean.FunDefBean([('self' , 'str'), ('encoding' , 'str') , ('errors' , 'str')] , ('returntype' , 'bool') , 'encode')
    strClass.FunDefArr['find'] = Bean.FunDefBean([('self' , 'str'), ('sub' , 'str'), ('start', 'int'),('end' ,'int')], ('returntype' , 'int'), 'find')
    strClass.FunDefArr['index'] = Bean.FunDefBean([('self' , 'str') ,('sub' ,'str'),('start' , 'int'), ('end' , 'int')] ,('returntype' , 'int'), 'index')
    strClass.FunDefArr['isdecimal'] = Bean.FunDefBean([('self' , 'str')] , ('returntype' , 'bool') , 'isdecimal')
    strClass.FunDefArr['isdigit'] = Bean.FunDefBean([('self' , 'str')] , ('returntype' , 'bool') , 'idigit')
    strClass.FunDefArr['islower'] = Bean.FunDefBean([('self' , 'str')] , ('returntype' , 'bool') , 'islower')

    strClass.FunDefArr['isnumeric'] = Bean.FunDefBean([('self' , 'str')] , ('returntype' , 'bool') , 'isnumeric')
    strClass.FunDefArr['isprintable'] = Bean.FunDefBean([('self' , 'st')] , ('returntype' , 'bool') , 'isprintable')
    strClass.FunDefArr['isspace'] = Bean.FunDefBean([('self' , 'str')] , ('returntype' , 'bool'), 'isspace')
    strClass.FunDefArr['isupper'] = Bean.FunDefBean([('self' , 'str')] , ('returntype' , 'bool'), 'isupper')
    strClass.FunDefArr['join'] = Bean.FunDefBean([('self' , 'str')] , ('returntype' , 'str'), 'join')
    strClass.FunDefArr['lower'] = Bean.FunDefBean([('self' , 'str')] , ('returntype' , 'str'), 'lower')
    strClass.FunDefArr['replace'] = Bean.FunDefBean([('self' , 'str') , ('old' , 'str'), ('new' , 'str') , ('count' , 'int')] , ('returntype' , 'str') , 'replace')
    strClass.FunDefArr['split'] = Bean.FunDefBean([('self' , 'str'), ('sep' , 'str') , ('maxsplit' , 'int')] , ('returntype' , 'list') , 'split')
    strClass.FunDefArr['splitlines'] = Bean.FunDefBean([('self' , 'str') , ('keepends' , 'boolean')] , ('returntype' , 'list') , 'splitlines')
    strClass.FunDefArr['upper'] = Bean.FunDefBean([('self' , 'str')] , ('returntype' , 'str') , 'upper')
    

                                                
                                                    
    nameSpace['str'] = strclass
    return nameSpace
