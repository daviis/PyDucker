"""
Created Nov-25-2014

@author: Emily
@editor: Isaac

A module that hand makes a namespace which will be used in early testing of PyDucker walking. It generates ClassDefBeans for ints and strs and some of the
FunDefBeans that are inside them.
"""
from Bean import NameSpaceBean, ScopeLevelBean, ClassDefBean , FunDefBean, VarBean

def handMakeNameSpace():
    nameSpace = NameSpaceBean()
    intClass = ClassDefBean('int', None)
    intClass.funs['__add__'] = FunDefBean([VarBean('int')],  VarBean('int'), '__add__')
    intClass.funs['__div__'] = FunDefBean([VarBean('int')],  VarBean('int'), '__div__')
    intClass.funs['__mod__'] = FunDefBean([VarBean('int')],  VarBean('int'), '__mod__')
    intClass.funs['__or__'] = FunDefBean([VarBean('int')],  VarBean('int'), '__or__')
    intClass.funs['__and__'] = FunDefBean([VarBean('int')],  VarBean('int'), '__and__')
    intClass.funs['__ne__'] = FunDefBean([VarBean('int')],  VarBean('int'), '__ne__')
    intClass.funs['__pow__'] = FunDefBean([VarBean('int')],  VarBean('int'), '__pow__')
    intClass.funs['__flooriv__'] = FunDefBean([VarBean('int')],  VarBean('int'), '__floordiv__')
    intClass.funs['__bool__'] = FunDefBean([] , VarBean('int'), '__bool__')
    intClass.funs['__eq__'] = FunDefBean([VarBean('int')], VarBean('bool') , '__eq__')
    intClass.funs['__float__'] = FunDefBean([], VarBean('float'), '__float__')
    intClass.funs['__floordiv__'] = FunDefBean([VarBean('int')],  VarBean('int'), '__floordiv__')
    intClass.funs['__ge__'] = FunDefBean([VarBean('int') ],  VarBean('bool'), '__ge__')
    intClass.funs['__gt__'] = FunDefBean([VarBean('int')],  VarBean('bool'), '__gt__')
    intClass.funs['__invert__'] = FunDefBean([], VarBean('int'), '__invert__')
    intClass.funs['__le__'] = FunDefBean([VarBean('int')], VarBean('bool'), '__le__')
    intClass.funs['__lshift__'] = FunDefBean([VarBean('int')] ,  VarBean('int'), '__lshift__')
    intClass.funs['__lt__'] = FunDefBean([VarBean('int')] ,  VarBean('bool'), '__lt__')
    intClass.funs['__mul__'] = FunDefBean([VarBean('int')] ,  VarBean('int'), '__mul__')
    intClass.funs['__rshift__'] = FunDefBean([VarBean('int')] ,  VarBean('int'), '__rshift__')
    intClass.funs['__xor__'] = FunDefBean([VarBean('int')] , VarBean('int'), '__xor__')
    intClass.funs['__str__'] = FunDefBean([] ,  VarBean('str'), '__str__')
    intClass.funs['__sub__'] = FunDefBean([VarBean('int')] ,  VarBean('int'), '__sub__')
    intClass.funs['__pos__'] = FunDefBean([VarBean('int')] ,  VarBean('int'), '__pos__')
    intClass.funs['__neg__'] = FunDefBean([VarBean('int')] ,  VarBean('int'), '__neg__')
    nameSpace.put(intClass.name, intClass)
    
    
    
    strClass = ClassDefBean('str', None)
    strClass.funs['__add__'] = FunDefBean([VarBean('str')] , VarBean('str'), '__add__')
    strClass.funs['__contains__'] = FunDefBean([VarBean('str')] , VarBean('bool'), '__contains__')
    strClass.funs['__eq__'] = FunDefBean([VarBean('str')] , VarBean('bool'), '__eq__')
    strClass.funs['__ge__'] = FunDefBean([VarBean('str')] , VarBean('bool'), '__ge__')
    strClass.funs['__gt__'] = FunDefBean([VarBean('str')] , VarBean('bool'), '__gt__')
    strClass.funs['__le__'] = FunDefBean([VarBean('str')] , VarBean('bool'), '__le__')
    strClass.funs['__len__'] = FunDefBean([], VarBean('int'), '__len__')
    strClass.funs['__mul__'] = FunDefBean([VarBean('int')] , VarBean('str'), '__mul__')
    strClass.funs['__ne__'] = FunDefBean([VarBean('str')] , VarBean('bool') , '__ne__')
    strClass.funs['casefold'] = FunDefBean([] , VarBean('str'), 'casefold')
    strClass.funs['center'] = FunDefBean([VarBean('int')] , VarBean('str'), 'center')
    strClass.funs['encode'] = FunDefBean([VarBean('str'), VarBean('str')] , VarBean('bool') , 'encode')
    strClass.funs['find'] = FunDefBean([VarBean('str') , VarBean('int') , VarBean('int')], VarBean('int'), 'find')
    strClass.funs['index'] = FunDefBean([ VarBean('str') , VarBean('int') , VarBean('int')] , VarBean('int'), 'index')
    strClass.funs['isdecimal'] = FunDefBean([] ,  VarBean('bool'), 'isdecimal')
    strClass.funs['isdigit'] = FunDefBean([] ,  VarBean('bool'), 'idigit')
    strClass.funs['islower'] = FunDefBean([] ,  VarBean('bool'), 'islower')
    strClass.funs['isnumeric'] = FunDefBean([] ,  VarBean('bool'), 'isnumeric')
    strClass.funs['isprintable'] = FunDefBean([] ,  VarBean('bool'), 'isprintable')
    strClass.funs['isspace'] = FunDefBean([] ,  VarBean('bool'), 'isspace')
    strClass.funs['isupper'] = FunDefBean([] ,  VarBean('bool'), 'isupper')
    strClass.funs['join'] = FunDefBean([] ,  VarBean('str'), 'join')
    strClass.funs['lower'] = FunDefBean([] ,  VarBean('str'), 'lower')
    strClass.funs['replace'] = FunDefBean([ VarBean('str') , VarBean('str') , VarBean('int')] ,  VarBean('str'), 'replace')
    strClass.funs['split'] = FunDefBean([ VarBean('str') , VarBean('int')] ,  VarBean('list'), 'split')
    strClass.funs['splitlines'] = FunDefBean([ VarBean('boolean')] ,  VarBean('list'), 'splitlines')
    strClass.funs['upper'] = FunDefBean([] ,  VarBean('str'), 'upper')
    #strClass.funs['range'] = FunDefBean([VarBean(int),VarBean(int),VarBean(int)], VarBean('range'), 'range' )
    nameSpace.put(strClass.name, strClass)
    
    boolClass = ClassDefBean('bool', None)
    boolClass.funs['__eq__'] = FunDefBean([VarBean('bool')], VarBean('bool'), '__eq__')
    boolClass.funs['__bool__'] = FunDefBean([VarBean('bool')], VarBean('bool'), '__bool__')
    nameSpace.put(boolClass.name, boolClass)

    listClass = ClassDefBean('list' , None)
    listClass.funs['__contains__'] = FunDefBean([VarBean('obj')], VarBean('bool'), '__contains__')
    listClass.funs['__iter__'] = FunDefBean(['self'], 'obj', '__iter__')
    nameSpace.put(listClass.name , listClass)

    setClass = ClassDefBean('set' , None)
    setClass.funs['__contains__'] = FunDefBean([VarBean('obj')], VarBean('bool'), '__contains__')
    setClass.funs['__iter__'] = FunDefBean(['self'], 'obj', '__iter__')
    nameSpace.put(setClass.name , setClass)

    tupleClass = ClassDefBean('tuple' , None)
    tupleClass.funs['__contains__'] = FunDefBean([VarBean('obj')], VarBean('bool'), '__contains__')
    tupleClass.funs['__iter__'] = FunDefBean(['self'], 'obj', '__iter__')
    nameSpace.put(tupleClass.name , tupleClass)

    dictClass = ClassDefBean('dict' , None)
    dictClass.funs['__contains__'] = FunDefBean([VarBean('obj')], VarBean('bool'), '__contains__')
    nameSpace.put(dictClass.name, dictClass) 
    
    bytesClass = ClassDefBean('bytes' , None)
    nameSpace.put(bytesClass.name, bytesClass) 
    
    exceptionClass = ClassDefBean("Exception", None)
    nameSpace.put(exceptionClass.name, exceptionClass)
    

    floatClass = ClassDefBean('float', None)
    floatClass.funs['__add__'] = FunDefBean([VarBean('float')], VarBean('float'), '__add__')
    floatClass.funs['__sub__'] = FunDefBean([VarBean('float')], VarBean('float'), '__sub__' )
    nameSpace.put(floatClass.name, floatClass)

    generatorClass = ClassDefBean("generator", None)
    nameSpace.put(generatorClass.name, generatorClass)

    
    rangeClass = ClassDefBean("range", None)
    rangeClass.funs['range'] = FunDefBean([VarBean(int),VarBean(int),VarBean(int)], VarBean('range'), 'range' )
    nameSpace.put(rangeClass.name, rangeClass)
    
    return nameSpace

def handMakeScope():
    scope = ScopeLevelBean()
    
    scope.append(VarBean("Exception", "ValueError"))
    #scope.append(VarBean("rangeClass", 'range'))
    #scope.append(VarBean('str', 'range' ))
    
    return scope
