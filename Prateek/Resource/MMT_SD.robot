*** Settings ***
Library             SeleniumLibrary
Resource            ../Config/Env1.robot

*** Keywords ***
I navigate to MakeMyTrip.com
    open browser            ${URL}          ${BROWSER}
    maximize browser window


#I Enter Values to Search
#    [Arguments]        ${FROM_CITY}        ${TO_CITY}

I Enter "${FROM_CITY}" and "${TO_CITY}" to search
    click element       //li[@data-cy='account']
    click element       fromCity
    sleep       1s
    input text          //input[@placeholder='From']        ${FROM_CITY}
    sleep       1s
    click element       //ul[@role='listbox']/li
    click element       toCity
    sleep       1s
    input text          //input[@placeholder='To']        ${TO_CITY}
    sleep       1s
    click element       //ul[@role='listbox']/li
    click element       //div[@class='dateInnerCell']/p[text()='10']

I click Search button
    click element       //a[text()='Search']


I see flight results
    ${FlightResult}         get text        //div[@class='listingRhs']/p
    log to console          ${FlightResult}
