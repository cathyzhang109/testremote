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
