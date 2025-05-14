*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections


*** Test Cases ***
FirstTestCase
        [Tags]      login
        Log To Console      This is my first robot testcase