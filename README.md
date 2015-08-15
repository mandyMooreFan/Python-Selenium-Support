<h1>Python-Selenium-Support</h1>

<p>
	This is a support library for Selenium using Python. It is meant to just streamline some of the basic functionality into something you can quickly script
</p>

<h2>Setup Required</h2>

1. You will need to have Python 2.7. installed (https://www.python.org/)  Right now Python 3.0 + won't work with Selenium.

2. Download and install Selenium for Python (https://selenium-python.readthedocs.org/installation.html#downloading-python-bindings-for-selenium).

3. You will need to download any other webdrivers you would like to use.  

>>Chrome: https://sites.google.com/a/chromium.org/chromedriver/

>>IE: https://code.google.com/p/selenium/wiki/InternetExplorerDriver

>>Firefox: Comes with Selenium

>>Once you have gather these place them in the folder:  "\webDriverSupport\drivers"

Add your code to __main__.py"

<h2> Example </h2>
```python
google = wd('http://www.google.com',"NONE")
google.open()

searchbar = support(google,'//*[@id="lst-ib"]').xpath_element()
searchbar.send_keys("idkmybffmark.com")
searchbar.submit()

google.driver.quit()
```

For more information and examples visit: http://idkmybffmark.com/2015/08/using-selenium-with-python/