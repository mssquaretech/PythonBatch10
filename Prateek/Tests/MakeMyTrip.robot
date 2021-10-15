*** Settings ***
Resource                ../Resource/MMT_SD.robot

*** Variables ***
${FROM_CITY1}            Bangalore
${TO_CITY1}              Delhi


*** Test Cases ***
Search Flight
    Given I navigate to MakeMyTrip.com
#    When I Enter Values to Search       ${FROM_CITY1}           ${TO_CITY1}
    When I Enter "${FROM_CITY1}" and "${TO_CITY1}" to search
    And I click Search button
    Then I see flight results

