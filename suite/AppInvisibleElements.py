from __future__ import division
import os, time
import uitest

class AppInvisibleElements(uitest.TestBase):    
    def process(self, index):
        """
            A test for calculator product
        """
        driver = self.testconfig.drivers[str(index)]
        print 'Driver is {0}'.format(driver)
        time.sleep(1)
        visiblebtn = driver.find_element_by_id("VisibleBtn")
        print 'visiblebtn offscreen property is {0}'.format(visiblebtn.get_attribute("IsOffscreen"))
        hiddenbtn = driver.find_element_by_id("InvisibleHidden")
        print 'hiddenbtn offscreen property is {0}'.format(hiddenbtn.get_attribute("IsOffscreen"))
        collapsebtn = driver.find_element_by_id("InvisibleCollapse")
        print 'collapsebtn offscreen property is {0}'.format(collapsebtn.get_attribute("IsOffscreen"))        

    def test_new_app(self):
        result = True
        for i in range(0, self.testconfig.NumberPCs):
            print 'Index is {0}'.format(i)
            temp = self.process(str(i))
            if temp == False:
                result = False
        self.assertTrue(result)

