from __future__ import division
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import unittest
import os, sys, re
import argparse
import singleinstanceparams
import multipleinstanceparams
import params
from enum import Enum

Product = Enum('Product', 'None P4C P4C_Remote MergeMe MergeMe_Remote Calculator Calculator_Remote AppInvisibleElement Notepad IExplore Firefox Chrome')
P4CScreen = Enum('P4CScreen', 'Unavailable Login Home')
FunctionResult = Enum('FunctionResult', 'Error Success SuccessWithoutProcess')

##class SetTestConfig:
##    def __init__(self, listParamsDict):
##        """
##            List of params dictionary contains sample datas: [{'RunningProduct' : '', 'IPHub' : '', 'Username' : '', 'Password' : '', 'WiniumDriverPath' : '', 'Id' : ''}]
##        """
##        print '+++++++ Test Config initialize is called.'
##        if listParamsDict is not None:
##            self.listParamsDict = listParamsDict        
##            print '++ listParamsDict is {0} in TestConfig class'.format(self.listParamsDict[0]['RunningProduct']['apps_path'])
##            self.NumberPCs = len(self.listParamsDict)
##            self.drivers = {}
##            for i in range(0, self.NumberPCs):
##                driver = webdriver.Remote(command_executor = self.listParamsDict[i]['IPHub'], desired_capabilities = {'app': self.listParamsDict[i]['RunningProduct']['apps_path']})
##                self.drivers[str(i)] = driver
##        else:
##            raise IOError('Can not intialize test config to run test suites')
##        print '+++++++ Test Config initialize is ended.'
            
class ReadTestConfigFile:
    def __init__(self, product = Product.Calculator, numberPCs = 1, isLocal = True):
        """
            List of params dictionary contains sample datas: [{'RunningProduct' : '', 'IPHub' : '', 'Username' : '', 'Password' : '', 'WiniumDriverPath' : '', 'Id' : ''}]
        """
        print '+++++++ Read Test Config File initialize is called.'
        print 'numberPcs is {0}'.format(numberPCs)
        print 'Product is {0}'.format(product.value)
        run_product_local = None
        run_product_remote = None
        
        if product == Product.P4C:
            run_product_local = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_P4C]
            run_product_remote = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_P4C_REMOTE]
        elif product == Product.Calculator:
            run_product_local = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_WINCALC]
            run_product_remote = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_WINCALC_REMOTE]
        elif product == Product.MergeMe:
            run_product_local = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_MERGEME]
            run_product_remote = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_MERGEME_REMOTE]
        elif product == Product.AppInvisibleElement:
            run_product_local = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_TEST_INVISIBLE_ELEMENTS]
            run_product_remote = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_TEST_INVISIBLE_ELEMENTS]
        elif product == Product.Notepad:
            run_product_local = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_NOTEPAD]
        elif product == Product.Chrome:
            run_product_local = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_CHROME]
        elif product == Product.IExplore:
            run_product_local = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_IEXPLORE]
        elif product == Product.Firefox:
            run_product_local = multipleinstanceparams.PRODUCTS[multipleinstanceparams.PRODUCT_FIREFOX]
        


            
##        print 'run_product_local is {0}'.format(run_product_local)
        
        if int(numberPCs) == 1:
            if isLocal == True:
                print "run_product_local is {0}".format(run_product_local)
##                self.listParamsDict = [{'RunningProduct' : run_product_local['apps_path'], 'IPHub' : singleinstanceparams.HUB_LOCAL, 'Username' : singleinstanceparams.P4C_USERNAME,
##                self.listParamsDict = [{'RunningProduct' : run_product_local['apps_path'], 'ProcessName' : run_product_local['apps_process_name'], 'IPHub' : singleinstanceparams.HUB_LOCAL, 'Username' : singleinstanceparams.P4C_USERNAME,
##                                    'Password': singleinstanceparams.P4C_PASSWORD, 'WiniumDriverPath' : singleinstanceparams.WINIUM_LOCAL_PATH, 'Id' : '0'}]
                self.listParamsDict = [{'RunningProduct' : run_product_local['apps_path'], 'IPHub' : singleinstanceparams.HUB_LOCAL, 'Username' : singleinstanceparams.P4C_USERNAME,
                                    'Password': singleinstanceparams.P4C_PASSWORD, 'WiniumDriverPath' : singleinstanceparams.WINIUM_LOCAL_PATH, 'Id' : '0'}]
                
            else:
                print "run_product_local is {0}".format(run_product_remote)
                self.listParamsDict = [{'RunningProduct' : run_product_remote['apps_path'], 'ProcessName' : run_product_local['apps_process_name'], 'IPHub' : singleinstanceparams.HUB_REMOTE, 'Username' : singleinstanceparams.P4C_USERNAME,
                                    'Password': singleinstanceparams.P4C_PASSWORD, 'WiniumDriverPath' : singleinstanceparams.WINIUM_REMOTE_PATH, 'Id' : '0'}]

        else:
            print "numberPCs is not 1"
            self.listParamsDict = None
##            self.listParamsDict = [{'RunningProduct' : run_product_local['apps_path'], 'ProcessName' : run_product_local['apps_process_name'], 'IPHub' : multipleinstanceparams.HUB_LOCAL, 'Username' : multipleinstanceparams.LOCAL_P4C_USERNAME,
##                                    'Password': multipleinstanceparams.LOCAL_P4C_PASSWORD, 'WiniumDriverPath' : multipleinstanceparams.WINIUM_LOCAL_PATH, 'Id' : '0'},
##                                   {'RunningProduct' : run_product_remote['apps_path'], 'ProcessName' : run_product_local['apps_process_name'], 'IPHub' : multipleinstanceparams.HUB_REMOTE, 'Username' : multipleinstanceparams.REMOTE_P4C_USERNAME,
##                                    'Password': multipleinstanceparams.REMOTE_P4C_PASSWORD, 'WiniumDriverPath' : multipleinstanceparams.WINIUM_REMOTE_PATH, 'Id' : '1'}]
        
        self.NumberPCs = int(numberPCs)
        self.drivers = {}
        print 'self.listParamsDict is {0}'.format(self.listParamsDict)
        for i in range(0, self.NumberPCs):
            #print 'self.listParamsDict[i]["RunningProduct"] is {0} and self.listParamsDict[i]["ProcessName"] is {1}'.format(self.listParamsDict[i]['RunningProduct'], self.listParamsDict[i]["ProcessName"])
            #driver = webdriver.Remote(command_executor = self.listParamsDict[i]['IPHub'], desired_capabilities = {'app': self.listParamsDict[i]['RunningProduct'],
                                                                                                                  #'realProcessName' : self.listParamsDict[i]['ProcessName']})
            driver = webdriver.Remote(command_executor = self.listParamsDict[i]['IPHub'], desired_capabilities = {'app': self.listParamsDict[i]['RunningProduct'], 'launchdelay':3000})
            self.drivers[str(i)] = driver
        print '+++++++ Read Test Config File initialize is ended.'

class TestBase(unittest.TestCase):
    testconfig = None
    
    @classmethod
    def setUpClass(self):
        print '+++++++ Base Test Set Up Class is called.'
        print '----Params args are: {0}'.format(params.args)
        product_type = int(params.args.product)        
        self.testconfig = ReadTestConfigFile(Product(product_type), params.args.numberPCs, params.args.isLocal)
        print '+++++++ Base Test Set Up Class is ended.'
##        self.readtestconfigfile = ReadTestConfigFile()
##        self.testconfig = SetTestConfig(self.readtestconfigfile.listParamsDict)

    @classmethod
    def tearDownClass(self):
        print '+++++++ Base Test Tear Down Class is called.'
        for i in range(0, self.testconfig.NumberPCs):
##            self.testconfig.drivers[str(i)].quit()
            self.testconfig.drivers[str(i)].close()
            if self.testconfig.drivers[str(i)] is not None:
                self.testconfig.drivers[str(i)] = None
        self.testconfig.listParamsDict = None
        self.testconfig.NumberPCs = None
        
        print '+++++++ Base Test Tear Down Class is ended.'
    
    def setUp(self):
        print '+++++++ Base Test setUp function is called.'
        self.print_test_config()
        print '+++++++ Base Test setUp function end.'
        print 'Self base class is: {0}'.format(self)


    def tearDown(self):
        print '+++++++ Base Test Tear Down is called.'
        print '+++++++ Base Test Tear Down is ended.'

    def print_test_config(self):
        print 'Number of PCs is {0}'.format(self.testconfig.NumberPCs)
        for i in range(0, self.testconfig.NumberPCs):
            print 'List param of PC{0} is {1}'.format(i, self.testconfig.listParamsDict[i])
            print 'Driver of PC{0} is {1}'.format(i, self.testconfig.drivers[str(i)])

    def load(self,computed,truth):
        pass

    def debug(self,label,image):
        pass
    
    def defaultTestResult(self):
        print 'DefaultTestResult'
        return FancyResult()

    def send_keys_to_active_element_object(self, index, text):
        driver = self.testconfig.drivers[str(index)]
        actions = webdriver.ActionChains(driver)
        actions.send_keys(text)
        actions.perform()

##    def move_mouse_to_element_object_with_offsets(self, index, element, offsetx, offsety):
##        driver = self.testconfig.drivers[str(index)]
##        actions = webdriver.ActionChains(driver)
##        actions.move_to_element_with_offset(element, offsetx, offsety)
##        actions.click()
##        actions.perform()
##
##    def click_on(self, index):
##        driver = self.testconfig.drivers[str(index)]
##        actions = webdriver.ActionChains(driver)
##        actions.click()
##        actions.perform()    
    def is_wait_for_elem_enable(self, index, how, what, timeout=15):
        result = self.wait_for_elem_enable(index, how, what, timeout)
        print 'Result is {0}'.format(result)
        if result is not None:
            return True
        return False
        
    def wait_for_elem_enable(self, index, how, what, timeout=15):
        """ Wait for element is displayed and enable(clickable)
        """
        driver = self.testconfig.drivers[str(index)]
        print 'Params are {0} , {1}, {2}'.format(how, what, timeout)
        elem = None
        try:
            print 'In Try command in wait_for_elem_enable with params: {0}, {1}, {2}'.format(how, what, timeout)
            elem = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((how,what)))
        except TimeoutException,e:
            print 'In TimeoutException command in wait_for_elem_enable with params: {0}, {1}, {2}'.format(how, what, timeout)
        finally:
            return elem    

    def is_wait_for_elem_visible(self, index, how, what, timeout=15):
        result = self.wait_for_elem_visible(index, how, what, timeout)
        if result is not None:
            return True
        return False

    def wait_for_elem_visible(self, index, how, what, timeout=15):
        """ Wait for element is existed in DOM and also displayed(height+width >0)
        """
        driver = self.testconfig.drivers[str(index)]
        print 'Params are {0} , {1}, {2}'.format(how, what, timeout)
        elem = None
        try:
            print 'In Try command in wait_for_elem_visible with params: {0}, {1}, {2}'.format(how, what, timeout)
            elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((how,what)))
        except TimeoutException,e:
            print 'In TimeoutException command in wait_for_elem_visible with params: {0}, {1}, {2}'.format(how, what, timeout)
        finally:
            return elem
        
    def is_wait_for_elem_appear(self, index, how, what, timeout=15):
        result = self.wait_for_elem_appear(index, how, what, timeout)
        if result is not None:
            return True
        return False
        
    def wait_for_elem_appear(self, index, how, what, timeout=15):
        """ Wait for element is existed in DOM.
        Support: By.NAME, By.CLASS_NAME, By.TAG_NAME, By.LINK_TEXT, By.PARTIAL_LINK_TEXT, By.CSS_SELECTOR, By.XPATH
        """
        driver = self.testconfig.drivers[str(index)]
        print 'Params are {0} , {1}, {2}'.format(how, what, timeout)
        elem = None
        try:
            print 'In Try command in wait_for_elem_appear with params: {0}, {1}, {2}'.format(how, what, timeout)
            elem = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((how,what)))
        except TimeoutException,e:
            print 'In TimeoutException command in wait_for_elem_appear with params: {0}, {1}, {2}'.format(how, what, timeout)
        finally:
            return elem

    def is_wait_for_elem_disappear(self, index, how, what, timeout=15):
        result = self.wait_for_elem_disappear(index, how, what, timeout)
        print 'Result is {0}'.format(result)
        if result:
            print '.....In if statement'
            return True
        elif result is not None:
            print '.....In elif statement'
            return False
        return True
    
    def wait_for_elem_disappear(self, index, how, what, timeout=15):
        """ Wait for element is not existed in DOM or existed but not visible
        """
        driver = self.testconfig.drivers[str(index)]
        print 'Params are {0} , {1}, {2}'.format(how, what, timeout)
        try:
            print 'In Try command in wait_for_elem_disappear with params: {0}, {1}, {2}'.format(how, what, timeout)
            elem = WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located((how,what)))
            return elem
        except TimeoutException,e:
            print 'In TimeoutException command in wait_for_elem_disappear with params: {0}, {1}, {2}'.format(how, what, timeout)
            return False
            
class Runner(unittest.TextTestRunner):
    def _makeResult(self):
        return FancyResult(self.stream, self.descriptions, self.verbosity)


class Suite(unittest.TestSuite):
    def run(self,result,debug=False):
        super(Suite,self).run(result)


class FancyResult(unittest.TextTestResult):
    def addError(self,test,err):
        super(FancyResult,self).addError(test,err)

    def addFailure(self,test,err):
        super(FancyResult,self).addFailure(test,err)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run UI tests')
    parser.add_argument('--test', help='test(s) name',default="")
    parser.add_argument('--numberPCs', help='Number of PCs to run test',default="1")
    parser.add_argument('--isLocal', help='When number of PCs is 1: there are 2 modes to run: local(True), remote(False)',default="True")
    parser.add_argument('--product', help='Product to launch. Currently, there are 3 products: P4C(1), merge.me(3), Calculator(5)',default="2")    
    args, remaining_argv = parser.parse_known_args()
    loader = unittest.TestLoader()
    loader.suiteClass = Suite
    if args.numberPCs is None:
        args.numberPCs = 1
    if args.isLocal is None:
        args.isLocal = True
    if args.product is None:
        args.product = 2    
    value = 0
    try:
        value = int(args.numberPCs)
    except ValueError:
        args.numberPCs = 1
    if value > 2:
        args.numberPCs = 2
    if args.isLocal.find('True') != -1:
        args.isLocal = True
    elif args.isLocal.find('False') != -1:
        args.isLocal = False
    else:
        args.isLocal = True
    if (int(args.product) < Product.P4C.value) or (int(args.product) > Product.Chrome.value):
        args.product = Product.MergeMe.value
    params.args = args
    params.remaining_argv = remaining_argv
    print '--isLocal is {0}'.format(args.isLocal)

    if args.test is not "":
        sys.path.insert(0, os.path.abspath( os.path.dirname(__file__)))
        suite = loader.loadTestsFromName(args.test)
    else:
        suite = loader.discover(start_dir = os.getcwd(),pattern='*.py')
    
    # if args.xml:
    #     result = xmlrunner.XMLTestRunner(output='test-reports',verbose=True).run(suite)
    # else:
    result = Runner(verbosity=2, stream=sys.stderr).run(suite)
    
    # Exit with error status if all tests don't pass. necessary for Jenkins to notice failure.
    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)
