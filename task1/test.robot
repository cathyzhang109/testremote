*** Settings ***
Library      pylib.schoolclasslib.Schoolclasslib

*** Test Cases ***
test
#     ${var2}=    listClass
    #返回一个字典格式，取值有两种写法
#    ${fu}=      evaluate    &{var2}[retlist]
#    ${fu}=      evaluate    $var2['retlist']
#    log to console      ${fu}
#    log to console      &{var2}[retlist]
#    ${var}      create list     hello  world

    ${var}  set variable  hello
    should be true  ${var}=='hello'
    log       ${var}