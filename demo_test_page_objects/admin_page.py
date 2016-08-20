from AppiumLibrary import AppiumLibrary


class AdminPage(AppiumLibrary):

    def click_refresh(self):
        """
        This function clicks on refresh icon available on the app
        :return: current page object
        """
        self.wait_until_page_contains_element("id=com.ustwo.sample:id/commit_list_button_refresh", 10,
                                              "Could not find refresh element")
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

    def get_commit_at_index(self, index):
        """
        This function returns available commits
        :param index: index of the commit
        :return: List
        """
        self.wait_until_page_contains_element("id=com.ustwo.sample:id/commit_list_row_textview_message", 10,
                                              "Could not find commit message")
        elements = self.get_elements("id=com.ustwo.sample:id/commit_list_row_textview_message")
        for element_index, element in enumerate(elements):
            if str(index) == str(element_index+1):
                return element.text
        raise ValueError('Could not find element at index %s' % index)

    def get_available_projects(self):
        """
        This function returns available projects
        :return: List
        """
        try:
            self.wait_until_page_contains_element("id=com.ustwo.sample:id/commit_list_textview_title", 10,
                                                  "Could not find commit message")
            elements = self.get_elements("id=com.ustwo.sample:id/commit_list_textview_title")
            available_commits = []
            for element in elements:
                available_commits.append(element.text)
            return available_commits
        except AssertionError as known_exception:
            print known_exception
            return []

    def get_timestamp_for_commit(self, commit_name):
        """
        This function returns timestamp for given commit name
        :param commit_name: Commit name for which the timestamp is requested
        :return: String
        """
        available_commits = self.get_available_commits()
        for index, commit in enumerate(available_commits):
            if commit.lower() == commit_name.lower():
                return self.get_elements(
                    "xpath=(//android.widget.LinearLayout[%s]/android.widget.TextView[2])" % (index+1))[0].text
        raise ValueError('Unable to find commit %s' % commit_name)

    def click_on_commit(self, commit_name):
        """
        This function clicks on requested commit
        :param commit_name: Commit name for which the timestamp is requested
        :return: self
        """
        available_commits = self.get_available_commits()
        for index, commit in enumerate(available_commits):
            if commit.lower() == commit_name.lower():
                self.click_element("xpath=(//android.widget.LinearLayout[%s])" % (index+1))
                return self
        raise ValueError('Unable to find commit %s' % commit_name)

    def get_project_name(self):
        """
        This function returns the project title displayed in app
        :return: string
        """
        self.wait_until_page_contains_element("id=com.ustwo.sample:id/action_bar", 10, "Could not find action bar")
        elements = self.get_elements("xpath=(//android.widget.TextView[1])")
        for sub_element in elements:
            return sub_element.text

    def get_author_name(self):
        """
        This function returns the author name for the commit selected
        :return: string
        """
        self.wait_until_page_contains_element("id=com.ustwo.sample:id/action_bar", 10, "Could not find action bar")
        return self.get_element_attribute("id=com.ustwo.sample:id/commit_detail_textview_name", "text")

    def get_author_email(self):
        """
        This function returns the author email for the commit selected
        :return: string
        """
        self.wait_until_page_contains_element("id=com.ustwo.sample:id/action_bar", 10, "Could not find action bar")
        return self.get_element_attribute("id=com.ustwo.sample:id/commit_detail_textview_email", "text")

    def get_commit_date(self):
        """
        This function returns the author email for the commit selected
        :return: string
        """
        self.wait_until_page_contains_element("id=com.ustwo.sample:id/action_bar", 10, "Could not find action bar")
        return self.get_element_attribute("id=com.ustwo.sample:id/commit_detail_textview_date", "text")

    def get_commit_message(self):
        """
        This function returns the author email for the commit selected
        :return: string
        """
        self.wait_until_page_contains_element("id=com.ustwo.sample:id/action_bar", 10, "Could not find action bar")
        return self.get_element_attribute("id=com.ustwo.sample:id/commit_detail_textview_message", "text")

    def is_private_project(self):
        """
        This function returns the author email for the commit selected
        :return: string
        """
        self.wait_until_page_contains_element("id=com.ustwo.sample:id/commit_list_row_textview_message", 10,
                                              "Could not find commit message")
        if self._is_element_present("id=com.ustwo.sample:id/commit_list_imageview_privacy_state"):
            return False
        return True

    def is_public_project(self):
        """
        This function returns the author email for the commit selected
        :return: string
        """
        self.wait_until_page_contains_element("id=com.ustwo.sample:id/commit_list_row_textview_message", 10,
                                              "Could not find commit message")
        if self._is_element_present("id=com.ustwo.sample:id/commit_list_imageview_privacy_state"):
            return True
        return False
