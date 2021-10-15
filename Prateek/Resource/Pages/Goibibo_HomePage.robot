*** Settings ***

*** Variables ***
${HotelsTabXpath}           //a[contains(@href,'hotels')]

*** Keywords ***
Navigate to Hotels Section
    click element           ${HotelsTabXpath}

