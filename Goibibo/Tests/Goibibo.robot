*** Settings ***
Resource            ../Resource/Goibibo_SD.robot

*** Test Cases ***
Search Hotels
    Given I navigate to Goibibo.com
    And I Click on Hotels Tab
    And I Click on Domestic Hotels
#    And I Enter City as Goa
    And I Enter City as                 Delhi
    When I Click on Search Hotels
#    Then I see Hotel Results

