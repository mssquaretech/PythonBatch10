*** Settings ***
Library                         SeleniumLibrary

*** Variables ***
${CountryRadioButton}           //h4[text()='India']/preceding-sibling::input
${CityValueTextBox}             //input[contains(@placeholder,'Hotel')]
${CitySuggestion}               //ul[@id='downshift-1-menu']/li
${SearchButton}                 //button

*** Keywords ***
Select Domestic RadioButton
    click element               ${CountryRadioButton}

Select "${CITY}" as Destination
    input text                  ${CityValueTextBox}         ${CITY}
    sleep       1s
    click element               ${CitySuggestion}

Click search hotels button
    click button                ${SearchButton}