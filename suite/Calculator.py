from __future__ import division
import os, time
import uitest

class Calculator(uitest.TestBase):    
    def process_sum(self, index):
        """
            A test for calculator product
        """
        driver = self.testconfig.drivers[str(index)]
        print 'Driver is {0}'.format(driver)
        time.sleep(5)
##        titlebar = driver.find_element_by_xpath("/*[@AutomationId='TitleBar']/*[@AutomationId='TitleBar' and @LocalizedControlType='title bar']")
##        child = titlebar.find_element_by_id("SystemMenuBar")
##        child = titlebar.find_element_by_id("Maximize-Restore")
##        properties = ["Name", "ControlType", "LocalizedControlType", "BoundingRectangle",
##                      "IsEnabled", "IsOffscreen", "IsKeyboardFocusable", "HasKeyboardFocus",
##                      "ProcessId",
##        properties = [
##                      "BoundingRectangle", "RuntimeId", "AutomationId", "FrameworkId", "ClassName",
##                      "IsControlElement", "IsContentElement",
                      ##"ProviderDescription", "LiveSettingProperty", Not support
##                      "IsPassword",
                      #"IsRequiredForForm", "ClickablePoint",
##                      "Orientation", "LegacyIAccessible.ChildId",
##                      "LegacyIAccessible.DefaultAction", "LegacyIAccessible.Description", "LegacyIAccessible.Help",
##                      "LegacyIAccessible.KeyboardShortcut", "LegacyIAccessible.Name", "LegacyIAccessible.Role",
##                      "LegacyIAccessible.State", "LegacyIAccessible.Value", "IsAnnotationPatternAvailable",
##                      "IsDragPatternAvailable",
##                      "IsDockPatternAvailable",
##                      "IsDropTargetPatternAvailable",
##                      "IsExpandCollapsePatternAvailable", "IsGridItemPatternAvailable", "IsGridPatternAvailable",
##                      "IsInvokePatternAvailable", "IsItemContainerPatternAvailable",  "IsLegacyIAccessiblePatternAvailable",
##                      "IsMultipleViewPatternAvailable", "IsMultipleViewPatternAvailable", "IsRangeValuePatternAvailable",
##                      "IsScrollItemPatternAvailable", "IsScrollPatternAvailable", "IsSelectionItemPatternAvailable",
##                      "IsSelectionPatternAvailable", "IsSpreadsheetItemPatternAvailable", "IsSpreadsheetPatternAvailable",
##                      "IsStylesPatternAvailable", "IsSynchronizedInputPatternAvailable", "IsTableItemPatternAvailable",
##                      "IsTablePatternAvailable", "IsTextChildPatternAvailable", "IsTextEditPatternAvailable",
##                      "IsTextPatternAvailable", "IsTextPattern2Available", "IsTogglePatternAvailable",
##                      "IsTransformPatternAvailable", "IsTransform2PatternAvailable", "IsValuePatternAvailable",
##                      "IsVirtualizedItemPatternAvailable", "IsWindowPatternAvailable", "FirstChild", "LastChild", "Next",
##                      "Previous", "Other Props", "Children",
##                      "Ancestors"
##                      ]
##        num2btn = driver.find_element_by_id("num2Button")
##        for s in properties:
##            temp = num2btn.get_attribute(s)
##            print "+++Atribute {0} is {1}".format(s, temp)
##        self.assertEqual('Two', temp)
##        temp = elem.get_attribute('ClassName')
##        self.assertEqual('Button', temp)
##        ## Bug of winium here, #Fail to value of Next is always None
##        temp = elem.get_attribute('Next') 
##        self.assertIsNone(temp)
##        ## Bug of winium here, #Fail to value of Next is always None
##        temp = elem.get_attribute('Ancestors') 
##        self.assertIsNone(temp)
##        ## Error to get, due to selenium web driver source code(webelement.py", line 113, in get_attribute), so this will fail attributes has boolean
##        temp = elem.get_attribute('IsOffscreen')
##        ## Get top left point and width, heigh of rectangle 
##        temp = elem.get_attribute('BoundingRectangle')
##        self.assertIsNotNone(temp)
##        ## Failed to get
##        ## Bug of winium here, #Fail to value of Next is always None
##        temp = elem.get_attribute('HelpText')
##        self.assertIsNotNone(temp)
        driver.find_element_by_id("num2Button").click()
##        print 'child offscreen property is {0}'.format(titlebar.get_attribute("IsOffscreen"))
##        print 'child is_display() is {0}'.format(titlebar.is_displayed())
##        print 'Num2Button offscreen property is {0}'.format(num2btn.get_attribute("IsOffscreen"))
##        print 'Num2Button is_display() is {0}'.format(num2btn.is_displayed())
        driver.find_element_by_id("plusButton").click()
        driver.find_element_by_id("num5Button").click()
        driver.find_element_by_id("equalButton").click()
        time.sleep(5)
        driver.find_element_by_id("num2Button").click()
        driver.find_element_by_id("plusButton").click()
        driver.find_element_by_id("num5Button").click()
        driver.find_element_by_id("equalButton").click()
        resultDisplay = driver.find_element_by_id("CalculatorResults").get_attribute("Name")
        self.assertEquals(resultDisplay, u'Display is  7 ')

        

    def test_calculator(self):
        result = True
        for i in range(0, self.testconfig.NumberPCs):
            print 'Index is {0}'.format(i)
            temp = self.process_sum(str(i))
            if temp == False:
                result = False
        self.assertTrue(result)

