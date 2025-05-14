*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections


*** Test Cases ***
FirstTestCase
        Log To Console      This is my first robot testcase
        Login

*** Keywords ***
Login
        Log     Enter the Username
        Log     Enter the Password
        Log     Press Login Button
        Log     Select the Product
        Log     Complete the payment....