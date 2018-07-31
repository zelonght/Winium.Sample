# ui_test
Winium: Winium.Desktop is Selenium Remote WebDriver implementation for automated testing of Windows application based on WinFroms and WPF platforms.
Selenium: Selenium is a browser automation library. Most often used for testing web-applications, Selenium may be used for any task that requires automating interaction with the browser.

1. Download: Windows Software Development Kit @ https://dev.windows.com/en-us/downloads/windows-10-sdk to have inspect.exe 
2. Download and install python. Then install some python libraries: selenium, enum34
3. Download Latest https://github.com/2gis/Winium.Desktop/releases
4. Run Winium WebDriver
5. Run a test: 
    - uitest.py --test=suite.Login.Calculator --numberPCs 1
    - uitest.py --test=suite.Login.Login --numberPCs 1 (Single machine)
	- uitest.py --test=suite.Login.Login --numberPCs 2 (Remote machine test start and join video call in 2 differnt machines)
	- uitest.py --test suite.TestBaseTest.TestBaseTest --numberPCs 1 --isLocal True --product 4 (Test cases to test wait for methods)
	
5. Pros/Cons:
	- Pros:
		+ Run via web driver so easily to support remote control: easily to support multi-video calling
		+ Support python unit test(better than Microsoft Unit test framework) and python selenium library(popular test framework)
		+ Python code is fast and small size, without require build/compile before running
		+ Support locate gui element as following ways: From web driver and web element, search other element: By name, class name, AutomationId, Xpath(for simple case work, complex ala: "//classA[@id='A']//classB[@id='C'] not work)
		+ Support to get some attributes of window gui element(Works on: ClassName, Name, AutomationId, ClickablePoint, BoundingRectangle: Return is left top point and x offset, y offset)	
		
	- Cons:
		+ Winium driver not work well when running long time(Need to restart driver to make test work). 
		+ Intermittently, it occurs some unexpected errors.
		+ When running on different screen's resolution, not work
		+ Not destroy app even if call driver.close()/ driver.quit(). Need to do some more things: to clean up and setup before running test.
		+ Hard to get supporting from author(only has 4 contributors in this project) 
		+ Limit on getting gui element properties:
			- Tree relation's element not work(Parent, child, Next item...) Always get None value
			- Offscreen, Enable, Helptext not work: Throw error when get properties which return boolean value(need to modify python selenium source code to work)
			- Scroll properties: None value
			- Other properties not try yet.
		+ Can't operate popup item(Ex: menu signout...), but can do some hacks to solve this(move mouse, click...)
	- Note: 
		+ Tip to validate xpath is correct or not: When finding element by xpath in code needs to add wait for time, then run test if the test skip waiting that means xpath is not correct.
		
Author: TriQuang, LongTruong