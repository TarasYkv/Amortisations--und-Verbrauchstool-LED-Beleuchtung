import logging
import threading
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


class meinThread(object):
    zahl1 = 2
    zahl2 = 5
    def __init__(self):
        super().__init__()
        self.alleThreads()

    def alleThreads(self):
        thread1 = threading.Thread(target=self.fun1, args=(1,))
        thread6 = threading.Thread(target=self.fun1, args=(6,))
        thread6.start()
        logger.info('zwischen den Threads')
        thread1.start()
        for t in threading.enumerate():
            logging.info('joining %s', t.getName())

        #thread1.join()
        #thread6.join()


    def fun1(self, a):
        logger.info('Gestartet Funktion mit der Zahl  %s', a)
        time.sleep(a) # complex calculation takes 1 seconds
        logger.info('Beendet Funktion mit der Zahl  %s', a)



def main():
    window11 = meinThread()


if __name__ == "__main__":
    main()