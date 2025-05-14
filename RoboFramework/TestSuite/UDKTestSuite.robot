*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections
Resource        E:/RoboFramework/Keyword.robot

*** Test Cases ***
FirstTestCase
        [Tags]      login
        Log To Console      This is my first robot testcase
        Login
