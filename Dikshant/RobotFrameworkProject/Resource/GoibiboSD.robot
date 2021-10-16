*** Setting ***
Library     SeleniumLibrary
Resource    Pages/Goibibo_HomePage.robot
Resource    Pages/Goibibo_HotelsPage.robot

*** Keywords ***
I navigate to Goibibo.com

    open browser    https://Goibibo.com  chrome
    maximize browser window

I Click on Hotels tab
    Navigate to Hotels Section

I Click on Domestic
    Select Domestic Radio Button

I Enter City as Goa
    Select Goa as Destination

I Click on Search Hotels
    Click Search Hotels button


