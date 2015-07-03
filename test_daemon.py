import random
import logging
import sys, time
from daemon import Daemon

class MyDaemon(Daemon):
	def run(self):
		while True:
			time.sleep(3)
			logging.info("->")


def init_log():
	logging.basicConfig(filename='/var/log/amir.log',level=logging.INFO,
	 format="[%(asctime)s][%(levelname)s] %(message)s",
	 datefmt="%Y-%m-%d %H:%M:%S")


def test(s):
	ch = 2
	assert s > ch
	logging.info("%s is greater than %s" %(s,ch))


init_log()

if __name__ == "__main__":
	daemon = MyDaemon('/tmp/amir.pid')

	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			logging.info("starting service")
			daemon.start()
		elif 'stop' == sys.argv[1]:
			logging.info("stopping service")
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			logging.info("restarting service")
			daemon.restart()
		elif 'status' == sys.argv[1]:
			pid = daemon.status()
			if pid:
				print "Service is running [pid:%s]" %pid
			else:
				print "Service is stopped!"


		else:
			print "Unknown command!"
			sys.exit(2)

		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)



a = random.randint(1,5)

"""
try:
	test(a)
except AssertionError:
	logging.error("Assert! for %s" %a)
except Exception:
	print "Exception!"

"""