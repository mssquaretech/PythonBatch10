*** Settings ***
Library         SeleniumLibrary

*** Variable ***

${SearchBox}
*** Keywords ***
Enter Value in Serachbox
    input text             twotabsearchtextbox      Mobile
    click button            nav-search-submit-button

Menu selection
    select from list by label

*** Test Cases ***
Amazon Testing
    open browser    https://amazon.in   chrome
    maximize browser window
    Enter Value in Serachbox
