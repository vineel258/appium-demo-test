*** Settings ***
Library           admin_page.AdminPage  WITH NAME  AdminPage

*** Variables ***
${REMOTE_URL}     http://localhost:4723/wd/hub
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}    6.0
${DEVICE_NAME}    Android Emulator
${APP}            ${CURDIR}/apps/app-sample.apk

*** Keywords ***
add new contact
    Open Application  http://localhost:4723/wd/hub  platformName=Android  platformVersion=6.0  deviceName=192.168.56.101:5555  app=${CURDIR}/apps/app-sample.apk  automationName=appium  appPackage=com.ustwo.sample  appActivity=CommitListActivity
    Capture Page Screenshot
    Sleep  10
    Get Available Commits
    Click Refresh

*** Test Cases ***
Test Case One
    add new contact