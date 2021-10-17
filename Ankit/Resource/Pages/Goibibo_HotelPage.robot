
*** Settings ***
Library     SeleniumLibrary

*** Variables ***

${CountryRadioButton}    //h4[text()='India']/preceding-sibling::input
${CityValue}    //input[contains(@placeholder,'Hotel')]
${CitySuggestion}    //ul[@id = 'downshift-1-menu']/li
${SearchButton}    //button


*** Keywords ***
Select Domestic RadioButton
    click element   ${CountryRadioButton}

Select Goa as Destination
    input text     ${CityValue}     Goa
    Sleep   1s
    click element   ${CitySuggestion}

Click on search button
    click button    ${SearchButton}
