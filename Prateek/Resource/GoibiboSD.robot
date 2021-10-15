*** Settings ***
Library         SeleniumLibrary
Resource        Pages/Goibibo_HomePage.robot
Resource        Pages/Goibibo_HotelsPage.robot

*** Keywords ***
I navigate to Goibibo.com
    open browser        https://goibibo.com         chrome
    maximize browser window
    capture page screenshot

I Click on Hotels Tab
    Navigate to Hotels Section


I Click on Domestic Hotels
    Select Domestic RadioButton

I Enter City as
    [Arguments]         ${CITY}
    Select "${CITY}" as Destination

I click on Search Hotels
    Click search hotels button