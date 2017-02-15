import logging
import os

from ViberBot.simpleViberBot.simpleViberBot import app


logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG,
                    filename=u'{0}/ViberBot.log'.format(os.getcwd()))


def main():
    try:
        logging.debug("Wsgi app is running")
        app.run(host='0.0.0.0', port=8000,  debug=False)
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    main()

