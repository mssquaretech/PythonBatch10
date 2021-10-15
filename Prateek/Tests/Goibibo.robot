*** Settings ***
Resource            ../Resource/GoibiboSD.robot

*** Test Cases ***
Search Hotels
    Given I navigate to Goibibo.com
    And I Click on Hotels Tab
    And I Click on Domestic Hotels
    And I Enter City as         Mysore
    When I click on Search Hotels
#    Then I see Hotel Results