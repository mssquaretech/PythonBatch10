*** Settings ***
Library     SeleniumLibrary

*** Variables ***

${HotelsTabXpath}    //a[contains(@href,'hotels')]

*** Keywords ***
Navigate to Hotels Page
    click element   ${HotelsTabXpath}