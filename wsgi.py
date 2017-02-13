from simpleViberBot import app, set_webhook, viber
import time
import sched
import threading
import logging
import os

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG,
                    filename=u'{0}/ViberBot_error.log'.format(os.getcwd()))


def main():
    try:
        scheduler = sched.scheduler(time.time(), time.sleep)
        scheduler.enter(5, 1, set_webhook, (viber,))
        t = threading.Thread(target=scheduler.run)
        t.start()
        logging.debug("Wsgi app is running")
        app.run(host='0.0.0.0', port=8000,  debug=False)
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    main()

