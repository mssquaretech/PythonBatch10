*** Settings ***
Library             SeleniumLibrary
Resource            ../Resource/Pages/Goibibo_HomePage.robot
Resource            ../Resource/Pages/Goibibo_HotelsPage.robot


*** Keywords ***
I navigate to Goibibo.com
    open browser            https://goibibo.com         chrome
    maximize browser window

I Click on Hotels Tab
    Navigate to Hotels Section

I Click on Domestic Hotels
    Select Domestic RadioButton

#I Enter City as Goa
#    Select Goa as Destination

I Enter City as
    [Arguments]     ${CITY}
    Select "${CITY}" as Destination

I Click on Search Hotels
    Click Search Hotels Button