*** Settings ***


*** Variables ***

${HOTELSTAB_XPATH}                  //a[contains(@href,'hotels')]


*** Keywords ***

Navigate to Hotels Section
    click element                   ${HOTELSTAB_XPATH}
