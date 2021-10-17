*** Settings ***
Resource    ../Resource/GoibiboSD.robot

*** Test Cases ***
Search Hotels
    Given I navigate to Goibibo.com
    And I Click on Hotels Tab
    And I Click on Domestic Hotels
    And I enter City as Goa
    When I Click on search hotels
#   Then I see Hotel Results


