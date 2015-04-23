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
    intClass = ClassDefBean('int', None, ScopeLevelBean())
    intClass.dataMembers.append(FunDefBean([VarBean('int')],  VarBean('int'), '__add__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')],  VarBean('int'), '__div__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')],  VarBean('int'), '__mod__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')],  VarBean('int'), '__or__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')],  VarBean('int'), '__and__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')],  VarBean('int'), '__ne__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')],  VarBean('int'), '__pow__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')],  VarBean('int'), '__floordiv__'))
    intClass.dataMembers.append(FunDefBean([] , VarBean('int'), '__bool__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')], VarBean('bool') , '__eq__'))
    intClass.dataMembers.append(FunDefBean([], VarBean('float'), '__float__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int') ],  VarBean('bool'), '__ge__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')],  VarBean('bool'), '__gt__'))
    intClass.dataMembers.append(FunDefBean([], VarBean('int'), '__invert__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')], VarBean('bool'), '__le__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')] ,  VarBean('int'), '__lshift__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')] ,  VarBean('bool'), '__lt__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')] ,  VarBean('int'), '__mul__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')] ,  VarBean('int'), '__rshift__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')] , VarBean('int'), '__xor__'))
    intClass.dataMembers.append(FunDefBean([] ,  VarBean('str'), '__str__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')] ,  VarBean('int'), '__sub__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')] ,  VarBean('int'), '__pos__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')] ,  VarBean('int'), '__neg__'))
    intClass.dataMembers.append(FunDefBean([VarBean('int')] ,  VarBean('int'), '__index__'))
    nameSpace.put(intClass.name, intClass)
    
    
    
    strClass = ClassDefBean('str', None, ScopeLevelBean())
    strClass.dataMembers.append(FunDefBean([VarBean('str')] , VarBean('str'), '__add__'))
    strClass.dataMembers.append(FunDefBean([VarBean('str')] , VarBean('bool'), '__contains__'))
    strClass.dataMembers.append(FunDefBean([VarBean('str')] , VarBean('bool'), '__eq__'))
    strClass.dataMembers.append(FunDefBean([VarBean('str')] , VarBean('bool'), '__ge__'))
    strClass.dataMembers.append(FunDefBean([VarBean('str')] , VarBean('bool'), '__gt__'))
    strClass.dataMembers.append(FunDefBean([VarBean('str')] , VarBean('bool'), '__le__'))
    strClass.dataMembers.append(FunDefBean([], VarBean('int'), '__len__'))
    strClass.dataMembers.append(FunDefBean([VarBean('int')] , VarBean('str'), '__mul__'))
    strClass.dataMembers.append(FunDefBean([VarBean('str')] , VarBean('bool') , '__ne__'))
    strClass.dataMembers.append(FunDefBean([] , VarBean('str'), 'casefold'))
    strClass.dataMembers.append(FunDefBean([VarBean('int')] , VarBean('str'), 'center'))
    strClass.dataMembers.append(FunDefBean([VarBean('str'), VarBean('str')] , VarBean('bool') , 'encode'))
    strClass.dataMembers.append(FunDefBean([VarBean('str') , VarBean('int') , VarBean('int')], VarBean('int'), 'find'))
    strClass.dataMembers.append(FunDefBean([ VarBean('str') , VarBean('int') , VarBean('int')] , VarBean('int'), 'index'))
    strClass.dataMembers.append(FunDefBean([] ,  VarBean('bool'), 'isdecimal'))
    strClass.dataMembers.append(FunDefBean([] ,  VarBean('bool'), 'idigit'))
    strClass.dataMembers.append(FunDefBean([] ,  VarBean('bool'), 'islower'))
    strClass.dataMembers.append(FunDefBean([] ,  VarBean('bool'), 'isnumeric'))
    strClass.dataMembers.append(FunDefBean([] ,  VarBean('bool'), 'isprintable'))
    strClass.dataMembers.append(FunDefBean([] ,  VarBean('bool'), 'isspace'))
    strClass.dataMembers.append(FunDefBean([] ,  VarBean('bool'), 'isupper'))
    strClass.dataMembers.append(FunDefBean([] ,  VarBean('str'), 'join'))
    strClass.dataMembers.append(FunDefBean([] ,  VarBean('str'), 'lower'))
    strClass.dataMembers.append(FunDefBean([ VarBean('str') , VarBean('str') , VarBean('int')] ,  VarBean('str'), 'replace'))
    strClass.dataMembers.append(FunDefBean([ VarBean('str') , VarBean('int')] ,  VarBean('list'), 'split'))
    strClass.dataMembers.append(FunDefBean([ VarBean('boolean')] ,  VarBean('list'), 'splitlines'))
    strClass.dataMembers.append(FunDefBean([] ,  VarBean('str'), 'upper'))
    nameSpace.put(strClass.name, strClass)
    
    boolClass = ClassDefBean('bool', None, ScopeLevelBean())
    boolClass.dataMembers.append(FunDefBean([VarBean('bool')], VarBean('bool'), '__eq__'))
    boolClass.dataMembers.append(FunDefBean([VarBean('bool')], VarBean('bool'), '__bool__'))
    nameSpace.put(boolClass.name, boolClass)

    listClass = ClassDefBean('list' , None, ScopeLevelBean())
    listClass.dataMembers.append(FunDefBean([VarBean('object')], VarBean('bool'), '__contains__'))
    listClass.dataMembers.append(FunDefBean(['self'], 'object', '__iter__'))
    nameSpace.put(listClass.name , listClass)

    setClass = ClassDefBean('set' , None, ScopeLevelBean())
    setClass.dataMembers.append(FunDefBean([VarBean('object')], VarBean('bool'), '__contains__'))
    setClass.dataMembers.append(FunDefBean(['self'], 'object', '__iter__'))
    nameSpace.put(setClass.name , setClass)

    tupleClass = ClassDefBean('tuple' , None, ScopeLevelBean())
    tupleClass.dataMembers.append(FunDefBean([VarBean('object')], VarBean('bool'), '__contains__'))
    tupleClass.dataMembers.append(FunDefBean(['self'], 'object', '__iter__'))
    nameSpace.put(tupleClass.name , tupleClass)

    dictClass = ClassDefBean('dict' , None, ScopeLevelBean())
    dictClass.dataMembers.append(FunDefBean([VarBean('object')], VarBean('bool'), '__contains__'))
    nameSpace.put(dictClass.name, dictClass) 
    
    bytesClass = ClassDefBean('bytes' , None, ScopeLevelBean())
    nameSpace.put(bytesClass.name, bytesClass) 
    
    exceptionClass = ClassDefBean("Exception", None, ScopeLevelBean())
    nameSpace.put(exceptionClass.name, exceptionClass)
    
    floatClass = ClassDefBean('float', None, ScopeLevelBean())
    floatClass.dataMembers.append(FunDefBean([VarBean('float')], VarBean('float'), '__add__'))
    floatClass.dataMembers.append(FunDefBean([VarBean('float')], VarBean('float'), '__sub__'))
    nameSpace.put(floatClass.name, floatClass)

    generatorClass = ClassDefBean("generator", None, ScopeLevelBean())
    generatorClass.dataMembers.append(FunDefBean([], VarBean('object'), '__iter__'))
    nameSpace.put(generatorClass.name, generatorClass)

    fileClass = ClassDefBean("file", None, ScopeLevelBean())
    fileClass.dataMembers.append(FunDefBean([], VarBean("list"), "read"))
    fileClass.dataMembers.append(FunDefBean([VarBean('str')], VarBean('None'), 'write'))
    nameSpace.put(fileClass.name, fileClass)

    
    rangeClass = ClassDefBean("range", None, ScopeLevelBean())
    rangeClass.dataMembers.append(FunDefBean([], VarBean('int'), "__iter__"))
    nameSpace.put(rangeClass.name, rangeClass)
    
    return nameSpace

def handMakeScope():
    scope = ScopeLevelBean()
    
    scope.append(FunDefBean([VarBean('str'), VarBean("$rept")], VarBean('None'), "print", someKwargs={"end": VarBean("str"), "sep": VarBean("str"), "file": VarBean("file"), "flush" : VarBean("bool")}))
    rangeType = VarBean('range')
    rangeType.homo = True
    rangeType.compType = [VarBean("int")]
    scope.append(FunDefBean([VarBean('int')], rangeType, "range"))
    scope.append(FunDefBean([VarBean('str'), VarBean('str')], VarBean("file"), "open"))
    scope.append(FunDefBean([VarBean('str')], VarBean('None'), "write"))
    
    scope.append(VarBean("Exception", "ValueError"))
    
    scope.append(FunDefBean([], VarBean("byte"), "byte"))
        
    return scope
