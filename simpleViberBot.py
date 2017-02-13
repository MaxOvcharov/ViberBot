# -*- coding: utf-8 -*-

from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest
import config
import time
import logging
import sched
import threading
import os


logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG,
                    filename=u'{0}/ViberBot.log'.format(os.getcwd()))

app = Flask(__name__)

viber = Api(BotConfiguration(
    name=config.appname,
    avatar=config.appavatar,
    auth_token=config.auth_token
))


@app.route('/', methods=['POST'])
def incoming():
    logging.debug("received request. post data: {0}".format(request.get_data()))

    viber_request = viber.parse_request(request.get_data())
    # Simple Echo messenger
    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.get_message()
        logging.debug("Received message from user:{0}  with content: {1}".
                     format(viber_request.get_sender().get_id(), message))
        viber.send_messages(viber_request.get_sender().get_id(), [message])
    elif isinstance(viber_request, ViberConversationStartedRequest)\
        or isinstance(viber_request, ViberSubscribedRequest)\
            or isinstance(viber_request, ViberUnsubscribedRequest):
        viber.send_messages(viber_request.get_user().get_id(),
                            [TextMessage(None, None, viber_request.get_event_type())])
    elif isinstance(viber_request, ViberFailedRequest):
        logging.warning("client failed receiving message. failure: {0}".format(viber_request))
    return Response(status=200)


def set_webhook(viber_bot):
    viber_bot.set_webhook(config.webhook)
    logging.debug("Web hoot was been set")

if __name__ == "__main__":
    scheduler = sched.scheduler(time.time(), time.sleep)
    scheduler.enter(5, 1, set_webhook, (viber, ))
    t = threading.Thread(target=scheduler.run)
    t.start()
    app.run(host='0.0.0.0', port=8443, debug=True, ssl_context=botconfig.ssl_context)

