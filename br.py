import pexpect
import sys
import time


website = 'browser.goto "' + sys.argv[1] + '"'

def setupBrowserController():
	controller = pexpect.spawn('/usr/bin/irb')
	controller.expect('>>')
	controller.sendline('require "watir-webdriver"')
	controller.expect('>>')
	controller.sendline('browser = Watir::Browser.new :ff')
	controller.expect('>>')
	return controller

def main():
	print website
	browserController = setupBrowserController()
	while (True):
		browserController.sendline(website)
		browserController.expect('>>')
		time.sleep(2)
if __name__ == '__main__':
	main()
