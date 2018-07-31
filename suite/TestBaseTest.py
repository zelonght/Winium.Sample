from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import params
import uitest

class TestBaseTest(uitest.TestBase):
    # Require to launch Calculator app to test these functions

    def test_get_all_attribute_from_gui_element(self):
        driver = self.testconfig.drivers[str(0)]
        print "Driver is {0}".format(driver)
        print '+++++ test_get_all_attribute_from_gui_element is called.'
        elem = driver.find_element_by_id("num2Button")
        ## Find element by name takes longer time than id(if the path has more than 3 sub levels it always fail)
##        elem = driver.find_element_by_name("Two")
        temp = elem.get_attribute('Name')
        self.assertEqual('Two', temp)
        temp = elem.get_attribute('ClassName')
        self.assertEqual('Button', temp)
        ## Bug of winium here, #Fail to value of Next is always None
        temp = elem.get_attribute('Next') 
        self.assertIsNone(temp)
        ## Bug of winium here, #Fail to value of Next is always None
        temp = elem.get_attribute('Ancestors') 
        self.assertIsNone(temp)
        ## Error to get, due to selenium web driver source code(webelement.py", line 113, in get_attribute), so this will fail attributes has boolean
        temp = elem.get_attribute('IsOffscreen')
        ## Get top left point and width, heigh of rectangle 
        temp = elem.get_attribute('BoundingRectangle')
        self.assertIsNotNone(temp)
        ## Failed to get
        ## Bug of winium here, #Fail to value of Next is always None
        temp = elem.get_attribute('HelpText')
        self.assertIsNotNone(temp)
        print '+++++ test_get_all_attribute_from_gui_element is ended.'
        
    def test_wait_for_elem_enable(self):
        driver = self.testconfig.drivers[str(0)]
        print '+++++ test_wait_for_elem_enable is called.'
        # Valid case: Visible and enable
        ## By AutomationId
        result = self.is_wait_for_elem_enable(0, By.ID, 'TitleBar', params.DEFAULT_IMPLIWAIT)
        self.assertTrue(result)

        ## By Name
        result = self.is_wait_for_elem_enable(0, By.NAME, 'System', params.DEFAULT_IMPLIWAIT)
        self.assertTrue(result)

        ## By ClassName
        result = self.is_wait_for_elem_enable(0, By.CLASS_NAME, 'ApplicationFrameWindow', params.DEFAULT_IMPLIWAIT)
        self.assertTrue(result)

        ## By Simple Xpath
        result = self.is_wait_for_elem_enable(0, By.XPATH, u'//*[@Name="System"]', params.DEFAULT_IMPLIWAIT)
        ## Not found base on invalid xpath
##      ##  result = self.is_wait_for_elem_enable(0, By.XPATH, u'//window[@Name="Calculator"]', 60)
        self.assertTrue(result)

        ## By Complex Xpath
        result = self.is_wait_for_elem_enable(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[@Name="Calculator" and @ClassName="Windows.UI.Core.CoreWindow"]', 20)
##      ##  result = self.is_wait_for_elem_enable(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[contains(@Name, "Calculator") and @ClassName="Windows.UI.Core.CoreWindow"]', 20)
##      ##  result = self.is_wait_for_elem_enable(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[@Name="Calculator" and @ClassName="Windows.UI.Core.CoreWindow"]/*[@AutomationId="divideButton"]', 20)
        ## Not found even if 5 minutes timeout
##        result = self.is_wait_for_elem_enable(0, By.XPATH, u'//*[@AutomationId="TitleBar"]//*[@AutomationId="divideButton"]', 300) 
        self.assertTrue(result)

        # Invalid case: element is not existed
        result = self.is_wait_for_elem_enable(0, By.ID, 'XXXXXXXXXXXXXXXXXXXXXXXXX', params.DEFAULT_IMPLIWAIT)
        self.assertFalse(result)

        # Invalid case: element is visible not enable
        result = self.is_wait_for_elem_enable(0, By.ID, 'MemRecall', params.DEFAULT_IMPLIWAIT)
        self.assertFalse(result)

        # Invalid case: element is existed, clickable but not visible(Bug of driver, per Selenium, must be return False)
        result = self.is_wait_for_elem_enable(0, By.XPATH, '//*[@AutomationId="TitleBar"]/*[@AutomationId="TitleBar" and @LocalizedControlType="title bar"]', 20)
        self.assertFalse(result)
        print '+++++ test_wait_for_elem_enable is end.'

    def test_wait_for_elem_visible(self):
        driver = self.testconfig.drivers[str(0)]
        print '+++++ test_wait_for_elem_visible is called.'
        # Valid case: Visible and enable
        ## By AutomationId
        result = self.is_wait_for_elem_visible(0, By.ID, 'TitleBar', params.DEFAULT_IMPLIWAIT)
        self.assertTrue(result)

        ## By Name
        result = self.is_wait_for_elem_visible(0, By.NAME, 'System', params.DEFAULT_IMPLIWAIT)
        self.assertTrue(result)

        ## By ClassName
        result = self.is_wait_for_elem_visible(0, By.CLASS_NAME, 'ApplicationFrameWindow', params.DEFAULT_IMPLIWAIT)
        self.assertTrue(result)

        ## By Simple Xpath
        result = self.is_wait_for_elem_visible(0, By.XPATH, u'//*[@Name="System"]', params.DEFAULT_IMPLIWAIT)
        self.assertTrue(result)

        ## By Complex Xpath
        result = self.is_wait_for_elem_visible(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[@Name="Calculator" and @ClassName="Windows.UI.Core.CoreWindow"]', 20)
##        result = self.is_wait_for_elem_visible(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[contains(@Name, "Calculator") and @ClassName="Windows.UI.Core.CoreWindow"]', 20)
        self.assertTrue(result)

        # Valid case: element is visible not enable
        result = self.is_wait_for_elem_visible(0, By.ID, 'MemRecall', params.DEFAULT_IMPLIWAIT)
        self.assertTrue(result)

        # Invalid case: element is not existed
        result = self.is_wait_for_elem_visible(0, By.ID, 'XXXXXXXXXXXXXXXXXXXXXXXXX', params.DEFAULT_IMPLIWAIT)
        self.assertFalse(result)        

        # Invalid case: element is existed, clickable but not visible(Bug of driver, per Selenium, must be return False)
        result = self.is_wait_for_elem_visible(0, By.XPATH, '//*[@AutomationId="TitleBar"]/*[@AutomationId="TitleBar" and @LocalizedControlType="title bar"]', 10)
        self.assertFalse(result)
        print '+++++ test_wait_for_elem_visible is ended.'

    def test_wait_for_elem_appear(self):
        driver = self.testconfig.drivers[str(0)]

        print '+++++ test_wait_for_elem_appear is called.'
        # Valid case: Visible and enable
        ## By AutomationId
##        result = self.is_wait_for_elem_appear(0, By.ID, 'TitleBar', params.DEFAULT_IMPLIWAIT)
##        self.assertTrue(result)
##
##        ## By Name
##        result = self.is_wait_for_elem_appear(0, By.NAME, 'System', params.DEFAULT_IMPLIWAIT)
##        self.assertTrue(result)
##
##        ## By ClassName
##        result = self.is_wait_for_elem_appear(0, By.CLASS_NAME, 'ApplicationFrameWindow', params.DEFAULT_IMPLIWAIT)
##        self.assertTrue(result)
##
##        ## By Simple Xpath
##        result = self.is_wait_for_elem_appear(0, By.XPATH, u'//*[@Name="System"]', params.DEFAULT_IMPLIWAIT)
####          Not found
####        result = self.is_wait_for_elem_appear(0, By.XPATH, u'//window[@Name="Calculator"]', 60)
##        self.assertTrue(result)
##
##        ## By Complex Xpath
####        result = self.is_wait_for_elem_appear(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[@Name="Calculator" and @ClassName="Windows.UI.Core.CoreWindow"]', 20)
##        result = self.is_wait_for_elem_appear(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[contains(@Name, "Calculator") and @ClassName="Windows.UI.Core.CoreWindow"]', 20)
####        result = self.is_wait_for_elem_appear(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[@Name="Calculator" and @ClassName="Windows.UI.Core.CoreWindow"]/*[@AutomationId="divideButton"]', 20)
##        ## Not found even if 5 minutes timeout
####        result = self.is_wait_for_elem_appear(0, By.XPATH, u'//*[@AutomationId="TitleBar"]//*[@AutomationId="divideButton"]', 300)
##        self.assertTrue(result)
##        ##        # Valid case: element is visible not enable
##        result = self.is_wait_for_elem_appear(0, By.ID, 'MemRecall', params.DEFAULT_IMPLIWAIT)
##        self.assertTrue(result)
##
##        # Invalid case: element is not existed
##        result = self.is_wait_for_elem_appear(0, By.ID, 'XXXXXXXXXXXXXXXXXXXXXXXXX', params.DEFAULT_IMPLIWAIT)
##        self.assertFalse(result)

##        # Invalid case: element is existed, clickable but not visible(Bug of driver, per Selenium, must be return False)
        result = self.is_wait_for_elem_appear(0, By.XPATH, '/*[@AutomationId="TitleBar"]/*[@AutomationId="TitleBar" and @LocalizedControlType="title bar"]/*[@AutomationId="Maximize-Restore"]', params.DEFAULT_IMPLIWAIT)
        self.assertFalse(result)
        print '+++++ wait_for_elem_appear is end.'

    def test_wait_for_elem_disappear(self):
        driver = self.testconfig.drivers[str(0)]
        print '+++++ test_wait_for_elem_disappear is called.'
        # Invalid case: Visible and enable
        ## By AutomationId
        result = self.is_wait_for_elem_disappear(0, By.ID, 'TitleBar', params.DEFAULT_IMPLIWAIT)
        self.assertFalse(result)
        ## By Name
        result = self.is_wait_for_elem_disappear(0, By.NAME, 'System', params.DEFAULT_IMPLIWAIT)
        self.assertFalse(result)
        ## By ClassName
        result = self.is_wait_for_elem_disappear(0, By.CLASS_NAME, 'ApplicationFrameWindow', params.DEFAULT_IMPLIWAIT)
        self.assertFalse(result)
        ## By Simple Xpath
        result = self.is_wait_for_elem_disappear(0, By.XPATH, u'//*[@Name="System"]', params.DEFAULT_IMPLIWAIT)
        ## Not found
##        result = self.is_wait_for_elem_disappear(0, By.XPATH, u'//window[@Name="Calculator"]', 60)
        self.assertFalse(result)
        ## By Complex Xpath
        result = self.is_wait_for_elem_disappear(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[@Name="Calculator" and @ClassName="Windows.UI.Core.CoreWindow"]', 20)
##        result = self.is_wait_for_elem_disappear(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[contains(@Name, "Calculator") and @ClassName="Windows.UI.Core.CoreWindow"]', 20)
##        result = self.is_wait_for_elem_disappear(0, By.XPATH, u'//*[@AutomationId="TitleBar"]/*[@Name="Calculator" and @ClassName="Windows.UI.Core.CoreWindow"]/*[@AutomationId="divideButton"]', 20)
        ## Not found even if 5 minutes timeout
##        result = self.is_wait_for_elem_disappear(0, By.XPATH, u'//*[@AutomationId="TitleBar"]//*[@AutomationId="divideButton"]', 300) 
        self.assertFalse(result)

        # Valid case: element is not existed
        result = self.is_wait_for_elem_disappear(0, By.ID, 'XXXXXXXXXXXXXXXXXXXXXXXXX', 20)
        self.assertTrue(result)
        # Invalid case: element is visible not enable
        result = self.is_wait_for_elem_disappear(0, By.ID, 'MemRecall', params.DEFAULT_IMPLIWAIT)
        self.assertFalse(result)
        # Valid case: element is existed but not visible
        result = self.is_wait_for_elem_disappear(0, By.XPATH, '//*[@AutomationId="TitleBar"]/*[@AutomationId="TitleBar" and @LocalizedControlType="title bar"]', params.DEFAULT_IMPLIWAIT)
        self.assertFalse(result)
        # Valid case: element not existed, existed(when click on button) then disappear(when re-click)        
        button = driver.find_element_by_id('NavButton')
        button.click()
        self.is_wait_for_elem_enable(0, By.ID, 'PaneRoot', 10)
        button.click()
        result = self.is_wait_for_elem_disappear(0, By.ID, 'PaneRoot', 10)
        self.assertTrue(result)
        print '+++++ test_wait_for_elem_disappear is end.'

        
