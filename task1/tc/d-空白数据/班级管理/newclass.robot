*** Settings ***
Library      pylib.schoolclasslib.Schoolclasslib
Resource    rflib/rc.robot
*** Test Cases ***
添加班级 1--tc000001
    ${var}    addClass      1   1班  80
   should be true   ${var}[retcode]==0
   #调用list接口
   ${listclass}     listClass   1
   ${fu}        evaluate    $listclass['retlist'][0]
   should be equal      ${fu}[invitecode]   ${var}[invitecode]
   should be equal      ${fu}[id]   ${var}[id]
添加班级 2--tc000002
#添加7年级2班
    ${var}      addClass    1   2班      80
    should be true      ${var}[retcode]==0
    #调用list接口
    ${listclass}     listClass
    ${fu}       evaluate    $listclass['retlist']
    ${listvar}      classlist_should_contain   七年级      ${var}[id]      ${var}[invitecode]      2班      80

添加班级 3--tc000003
#添加7年级2班（同年级同班--报错）
#先列出所有的课程
    ${listclass}     listClass
    ${fu}       evaluate    $listclass['retlist']
    ${lenfu}    get length      ${fu}

    ${var}      addClass    1   2班      80
    should be true      ${var}[retcode]==1
    should be true      ${var}[reason]==duplicated class name

    ${listclass}     listClass
    ${fu2}       evaluate    $listclass['retlist']
    ${lenfu2}    get length      ${fu2}
    should be true      ${lenfu}    ${lenfu2}