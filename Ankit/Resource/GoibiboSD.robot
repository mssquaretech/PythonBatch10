*** Settings ***
Library     SeleniumLibrary
Resource    Pages/Goibibo_HomePage.robot
Resource    Pages/Goibibo_HotelPage.robot

*** Keywords ***
I navigate to Goibibo.com
    open browser    https://goibibo.com     chrome
    maximize browser window

I Click on Hotels Tab
    Navigate to Hotels Page

I Click on Domestic Hotels
    Select Domestic RadioButton

I enter City as Goa
    Select Goa as Destination

I Click on search hotels
    Click on search button
    capture page screenshot
