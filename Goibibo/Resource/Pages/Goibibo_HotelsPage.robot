*** Settings ***
Library                         SeleniumLibrary

*** Variables ***
${DOMESTIC_XPATH}               //h4[ text()='India' ]/preceding-sibling::input
${INTERNATIONAL_XPATH}          //h4[ text()='International' ]/preceding-sibling::input
${CITYINPUT_XPATH}              //input[ contains(@placeholder,'Hotel') or contains(@placeholder,'Area') ]
${CITYSUGGESTION_XPATH}         //ul[ @role = 'listbox' and @id = 'downshift-1-menu' ]/li
${SEARCHBUTTON_XPATH}           //button[ text() = 'Search Hotels' ]

*** Keywords ***
Select Domestic RadioButton
    click element       ${DOMESTIC_XPATH}

#Select Goa as Destination
#    input text          ${CITYINPUT_XPATH}          Goa
#    sleep               1s
#    click element       ${CITYSUGGESTION_XPATH}

Select "${CITY}" as Destination
    input text          ${CITYINPUT_XPATH}          ${CITY}
    sleep               1s
    click element       ${CITYSUGGESTION_XPATH}

Click Search Hotels Button
    click element       ${SEARCHBUTTON_XPATH}