*** Setting ***

*** Variable ***

#${CountryRadioButton}          //h4[text()='India']/preceding-sibling::input
${CountryRadioButton}           //h4[text()='International']/preceding-sibling::input
${CityInputValue}               //input[contains(@placeholder,'Hotel')]
${CitySuggestionValue}          //ul[@id='downshift-1-menu']
${SearchButton}                 //button[@data-testid='searchHotelBtn']
*** Keywords ***
Select Domestic Radio Button
    click element               ${CountryRadioButton}

Select Goa as Destination
    Input text                  ${CityInputValue}           Paris
    sleep       1s
    click element               ${CitySuggestionValue}

Click Search Hotels button
    click element               ${SearchButton}