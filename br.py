import pexpect
import sys
import time


WEBSITE = 'browser.goto "' + sys.argv[1] + '"'
WAIT_TIME = int(sys.argv[2])

def setupBrowserController():
	controller = pexpect.spawn('/usr/bin/irb')
	controller.expect('>>')
	controller.sendline('require "watir-webdriver"')
	controller.expect('>>')
	controller.sendline('browser = Watir::Browser.new :ff')
	controller.expect('>>')
	return controller

def main():
	print WEBSITE 
	browserController = setupBrowserController()
	while (True):
		browserController.sendline(WEBSITE)
		browserController.expect('>>')
		time.sleep(WAIT_TIME)
if __name__ == '__main__':
	main()
