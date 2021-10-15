*** Settings ***
Library                     SeleniumLibrary

*** Variables ***
${URL}                      https://amazon.in
${BROWSER}                  chrome
${SEARCHBOX_XPATH}          //input[@id='twotabsearchtextbox']
${SEARCHBUTTON_ID}          twotabsearchtextbox
${SEARCHVALUE}              Toys

*** Keywords ***
Enter Value in Searchbox
    input text              ${SEARCHBOX_XPATH}          ${SEARCHVALUE}
    click button            ${SEARCHBUTTON_ID}

