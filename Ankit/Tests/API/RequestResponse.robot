*** Settings ***
Library     RequestsLibrary

*** Variables ***
${UserID}       1

*** Keyword ***
Details Print
    FOR   ${UserID}   IN    RANGE    1   5
        \ ${UserDetailsResponse}     get on session  TEST    https://reqres.in/api/users/${UserID}
        \ log to console   ${UserDetailsResponse.status_code}
        \ log to console   ${UserDetailsResponse.text}
    END

*** Test Cases ***
Get List of Users
    create session  TEST                    https://reqres.in
    ${Response}     get on session  TEST    url=api/users?page=2
    log to console   ${Response.status_code}
    log to console   ${Response.text}

Get Users Details
    create session  TEST                    https://reqres.in
    Details Print
