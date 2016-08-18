from AppiumLibrary import AppiumLibrary


class AdminPage(AppiumLibrary):

    def click_refresh(self):
        """
        This function clicks on refresh icon available on the app
        :return: current page object
        """
        self.click_element("id=com.ustwo.sample:id/commit_list_button_refresh")
        return self

    def get_available_commits(self):
        """
        This function returns available commits
        :return: List
        """
        try:

            self.wait_until_page_contains_element("id=com.ustwo.sample:id/commit_list_row_textview_message", 10,
                                                  "Could not find commit message")
            elements = self.get_elements("id=com.ustwo.sample:id/commit_list_row_textview_message")
            available_commits = []
            for element in elements:
                available_commits.append(element.text)
            return available_commits
        except AssertionError as known_exception:
            print known_exception
            return []

