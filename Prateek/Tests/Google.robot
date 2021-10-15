*** Settings ***
Library                 SeleniumLibrary
Resource                FirstScript.robot

*** Keywords ***
Enter Value in Searchbox
    input text              ${SEARCHBOX_XPATH}          Television
    click button            ${SEARCHBUTTON_ID}

*** Test Cases ***
Amazon Testing
    open browser            ${URL}                      ${BROWSER}
    maximize browser window
    Enter Value in Searchbox

