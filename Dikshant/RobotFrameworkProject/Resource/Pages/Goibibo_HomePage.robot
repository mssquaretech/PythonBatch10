*** Settings ***
Library                         SeleniumLibrary


*** Variables ***

${HotelsTabXoath}       //a[contains(@href,'hotels')]


*** Keywords ***
Navigate to Hotels Section
    click element       ${HotelsTabXoath}