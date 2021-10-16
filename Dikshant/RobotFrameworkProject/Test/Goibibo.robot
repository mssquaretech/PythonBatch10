*** Settings ***
Resource            ../Resource/GoibiboSD.robot

*** Test Cases ***
Search Hotels
    Given I navigate to Goibibo.com
    And I Click on Hotels tab
    And I Click on Domestic
    And I Enter City as Goa
    When I Click on Search Hotels
#    Then I see Hotels Result
