""" TestSuite that holds test cases as different report type """
from __future__ import division
import os, time
import uitest
from selenium.webdriver.common.by import By
import params

class Login(uitest.TestBase):
    def setUp(self):        
        print '+++++++Login Test setUp function is called.'
        self.print_test_config()
        print '+++++++Login Test setUp function end.'
        
    def tearDown(self):
        print '+++++++Login Test tearDown function is called.'
        print '+++++++Login Test tearDown function end.'
        
    def check_current_screen_is_p4c_login_or_home(self, index, timeout=10):
        driver = self.testconfig.drivers[str(index)]
        current = self.wait_for_elem_enable(index, By.XPATH, u'/*[@Name="Personify"]', timeout/2)
        if current is None:
            print ('++ Not found login screen')
            current = self.wait_for_elem_enable(index, By.XPATH, u'/*[@Name="Home"]', timeout/2)
            if current is None:
                print ('++ Also not found home screen')
                return uitest.P4CScreen.Unavailable
            else:
                return uitest.P4CScreen.Home
        else:
            return uitest.P4CScreen.Login

    def process_psy_login(self, index, username, password, timeout=60):
        """ Return FunctionResult.Success: if success to login and access Home screen
            Return FunctionResult.Error: if there's login error
            Return FunctionResult.SuccessWithoutProcess: if there's already logged in(at Home screen)
        """
        ## Login logic
        driver = self.testconfig.drivers[str(index)]
        current = self.check_current_screen_is_p4c_login_or_home(index, timeout/2)
        print 'current value is {0}'.format(current)
        if current == uitest.P4CScreen.Login:
            print 'Find username edit by id'
            tbx_username = driver.find_element_by_id('Username')
            tbx_username.click()
            tbx_username.send_keys(username)
            tbx_password = driver.find_element_by_id('Password')            
            tbx_password.click()
            tbx_password.send_keys(password)
            tbx_password.submit()
            button = self.wait_for_elem_enable(index, By.ID, 'start_newcall_btn', timeout/2)
            if button is None:
                return uitest.FunctionResult.Error
            else:
                return uitest.FunctionResult.Success
        return uitest.FunctionResult.SuccessWithoutProcess

    def start_call_then_invite_on_silhouette(self, index, username, timeout=60):
        ## Start call then invite from user B's silhouette in video call screen
        driver = self.testconfig.drivers[str(index)]
        button = self.wait_for_elem_enable(index, By.ID, 'start_newcall_btn', timeout/3)
        button.click()
        button = self.wait_for_elem_enable(index, By.ID, 'PART_ToggleButton', timeout/3)
        button.click()
        invite = self.wait_for_elem_enable(index, By.ID,'mAutoCompleteBox', timeout/3)
        self.send_keys_to_active_element_object(index, username)
        invite.submit()
        driver.implicitly_wait(params.DEFAULT_IMPLIWAIT)
        driver.find_element_by_id('mWidnow').click()
        temp = self.wait_for_elem_disappear(index, By.ID,'mAutoCompleteBox', params.DEFAULT_IMPLIWAIT)
        if temp is not None:
            return True
        return False

##    def start_call_from_home_recent_contact_list(self, index, timeout = 10):
##        ## This need to be done more, currently require have 1 recent contact in recent list, and click on 1st item
##        driver = self.testconfig.drivers[str(index)]
##        recent_contact = self.wait_for_elem_enable(index, By.CLASS_NAME,'AutoCompleteBox', timeout)
##        offset = 100
##        self.move_mouse_to_element_object_with_offsets(index, recent_contact, offset, offset)
##        self.click_on()
##        driver.implicitly_wait(timeout)
##        panel = self.wait_for_elem_enable(index, By.ID, 'PART_ScrollViewer', timeout*6)
##        persona = panel.find_element_by_id('mPersonaFrame')
##        if persona is None:
##            return False
##        return True

    def receive_invited_call(self, index, fromUser, timeout=120):
        driver = self.testconfig.drivers[str(index)]
        incoming = self.wait_for_elem_enable(index, By.NAME, 'Incoming Call', timeout/4)
        if incoming is None:
            return False
        # TBD: Need to add Id for invitor name/email in StagePresence source code
##        result = incoming.find_element_by_name(fromUser)
##        print 'Result is {0}'.format(result)        
##        self.wait_for_elem_enable(index, By.NAME, fromUser, timeout*3)
##        button = incoming.find_element_by_xpath(u'(//button)[3]')
##        xpath = u'//*[@LegacyIAccessible.Name="' + fromUser + '"' + ' and @LocalizedControlType="text"' + ']'
##        print 'Xpath to find from contact is {0}'.format(xpath)
##        from_contact = incoming.find_element_by_xpath(xpath)
##        print 'Find from contact text is {0}'.format(from_contact)
        button = incoming.find_element_by_xpath(u'(//*[@LocalizedControlType="button"])[3]')
        button.click()
        return self.is_wait_for_elem_appear(index, By.ID, 'mWidnow', timeout/4)
        xpath = u'/*[@Name="Control Panel"]/*[@AutomationId="PART_ScrollViewer"]/*[@Name="me"]'
        temp = self.is_wait_for_elem_appear(0, By.XPATH, xpath, timeout/4)
        if temp == False:
            return False
        xpath = u'/*[@Name="Control Panel"]/*[@AutomationId="PART_ScrollViewer"]/*[@Name="' + self.testconfig.listParamsDict[0]['Username'] + '"]'
        return self.is_wait_for_elem_enable(0, By.XPATH, xpath, timeout/4)
##        subpanel = videocall.find_element_by_id('PART_ScrollViewer')
##        image = subpanel.find_element_by_id('mPersonaFrame')
####        image = self.wait_for_elem_enable(index, By.XPATH, u'//*[@AutomationId="mWidnow"]/*[@AutomationId="PART_ScrollViewer"]/*[@AutomationId="mPersonaFrame"]', timeout*3)
##        image.click()
####        xpath = u'//*[@AutomationId="mWidnow"]/*[@AutomationId="PART_ScrollViewer"]/*[@AutomationId="mDisplayNameOnly" and @Name="' + fromUser + '"]'
##        xpath = u'//*[@AutomationId="mWidnow"]/*[@AutomationId="PART_ScrollViewer"]/*[@Name="' + fromUser + '"]'
##        print "---Xpath is {0}".format(xpath)
##        return self.is_wait_for_elem_appear(index, By.XPATH, xpath, timeout*3)
       
        
    def test_p4c(self):
        """
            Testing https://github.com/2gis/Winium.Desktop/ for UI Automation
        """
        result = True
        ## Make sure all devices successfully login and in Home screen
        for i in range(0, self.testconfig.NumberPCs):
            print 'Index is {0}'.format(i)
            temp = self.process_psy_login(str(i), self.testconfig.listParamsDict[i]['Username'], self.testconfig.listParamsDict[i]['Password'])
            if temp == uitest.FunctionResult.Error:
                result = False
        self.assertTrue(result)
        ## Start call in local
        result = self.start_call_then_invite_on_silhouette(0, self.testconfig.listParamsDict[1]['Username'])
        self.assertTrue(result)
        # Receive invitation from remote side
        if self.testconfig.NumberPCs == 2:
            print '+++++++++++Call receive invitation function start'            
            result = self.receive_invited_call(1, self.testconfig.listParamsDict[0]['Username'])
            print '+++++++++++Call receive invitation function end'
            self.assertTrue(result)        
            #xpath = u'//*[@AutomationId="mWidnow"]/*[@AutomationId="PART_ScrollViewer"]/*[@AutomationId="mDisplayNameOnly" and @Name="' + self.testconfig.listParamsDict[1]['Username'] + '"]'
            xpath = u'/*[@Name="Control Panel"]/*[@AutomationId="PART_ScrollViewer"]/*[@Name="me"]'
            result = self.is_wait_for_elem_appear(0, By.XPATH, xpath, 30)
            self.assertTrue(result)
            xpath = u'/*[@Name="Control Panel"]/*[@AutomationId="PART_ScrollViewer"]/*[@Name="' + self.testconfig.listParamsDict[1]['Username'] + '"]'
            result = self.is_wait_for_elem_enable(0, By.XPATH, xpath, 30)
            self.assertTrue(result)
        
