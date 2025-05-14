*** Variables ***
${name}     lokesh
${age}      22

@{list}     apple banana orange

&{DictVariable}     username=Lokesh     password=1234

*** Test Cases ***
Variable TestCases
        Log To Console      ${name}
        Log To Console      ${age}
        Log To Console      @{list}
        Log TO Console      &{DictVariable}{username}