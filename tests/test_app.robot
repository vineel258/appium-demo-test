*** Settings ***
Library           admin_page.AdminPage  WITH NAME  AdminPage
Test Teardown     Close All Applications

*** Variables ***
${REMOTE_URL}     http://localhost:4723/wd/hub
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}    6.0
${DEVICE_NAME}    Android Emulator
${APP}            ${CURDIR}/apps/app-sample.apk

*** Keywords ***
Open Application On Mobile
    Open Application  http://localhost:4723/wd/hub  platformName=Android  platformVersion=6.0  deviceName=192.168.56.101:5555  app=${CURDIR}/apps/app-sample.apk  automationName=appium  appPackage=com.ustwo.sample  appActivity=CommitListActivity

Open Application And Verify Project Information
    Open Application On Mobile
    ${available_projects} =  Get Available Projects
    ${available_commits} =  Get Available Commits
    ${project_status} =  Is Public Project
    Should Be True  ${project_status}

Open Application And Verify Latest Project Activity
    [Documentation]  This keyword is intentionally made a negative test case, assuming no latest activity, otherwise it will pass
    Open Application On Mobile
    ${ref_commit} =  Get Commit At Index  1
    Click Refresh
    ${latest_commit} =  Get Commit At Index  1
    Should Not Be Equal  ${ref_commit}  ${latest_commit}

Open Application And Verify Commit Information
    Open Application On Mobile
    ${ref_commit} =  Get Commit At Index  3
    ${ref_timestamp} =  Get Timestamp For Commit  ${ref_commit}
    Click On Commit  ${ref_commit}
    ${proj_name} =  Get Project Name
    Should Be Equal  ${proj_name}  Full Cycle App Testing Sample
    ${author_name} =  Get Author Name
    Should Be Equal  ${author_name}  Martin Stolz
    ${author_email} =  Get Author Email
    Should Be Equal  ${author_email}  martin@ustwo.co.uk
    ${commit_date} =  Get Commit Date
    Should Be Equal  ${commit_date}  2013-11-27T13:11:12Z
    ${commit_message} =  Get Commit Message
    Should Be Equal  ${commit_message}  Modified email recipients

*** Test Cases ***
User Should Be Able To Access Project Information
    [Tags]  Demo Test  Acceptance Criteria  TestCase01
    [Documentation]  AC: Display project information (title, public / private, etc)
    Open Application And Verify Project Information

User Should Be Able To View the Latest Project Activity
    [Tags]  Demo Test  Acceptance Criteria  TestCase02
    [Documentation]  AC: Display latest project activity
    Open Application And Verify Latest Project Activity

User Should Be Able To View Additional Information For Any Desired Commit
    [Tags]  Demo Test  Acceptance Criteria  TestCase03
    [Documentation]  AC: Display commit information
    Open Application And Verify Commit Information