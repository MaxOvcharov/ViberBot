# -*- coding: utf-8 -*-

import logging
import os
import sched
import threading
import time


from flask import request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

from ViberBot import db, create_app
from ViberBot.config import config

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO, filename=u'{0}/ViberBot.log'.format(os.getcwd()))

app = create_app()

viber = Api(BotConfiguration(
    name=config.APP_NAME,
    avatar=config.APP_AVATAR,
    auth_token=config.AUTH_TOKEN
))


@app.route('/', methods=['POST'])
def incoming():
    logging.info("received request. post data: {0}".format(request.get_data()))
    # Verify the signature of message
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)
    viber_request = viber.parse_request(request.get_data())

    # Simple Echo messenger
    if isinstance(viber_request, ViberMessageRequest):
        message = str(viber_request.message).encode('utf-8')
        logging.info("Received message from user:{0}".
                     format(viber_request.sender.id.encode('utf-8')))
        # if message in content:
        #     msg = content[message][0]
        #     for photo in msg:
        #         viber.send_messages(viber_request.sender.id,
        #                             [PictureMessage(media="{0}".format(photo),
        #                                             text="{0}".format(message))])
        # else:
        #     viber.send_messages(viber_request.user.id,
        #                         [TextMessage(text="Извините, по Вашему запросу: {0} ничего не найдено.\n"
        #                                           "Попробуйте ввести название города еще раз".
        #                                      format(message))])

    # Hello message for StartedRequest, SubscribedRequest, UnsubscribedRequest
    elif isinstance(viber_request, ViberConversationStartedRequest)\
        or isinstance(viber_request, ViberSubscribedRequest)\
            or isinstance(viber_request, ViberUnsubscribedRequest):
        viber.send_messages(viber_request.user.id,
                            [TextMessage(text="Привет, {0}. Какой город тебя интересует?".
                                         format(viber_request.user.name.encode('utf-8')))])

    # Handle FailedRequest
    elif isinstance(viber_request, ViberFailedRequest):
        logging.warning("client failed receiving message. failure: {0}".format(viber_request))
    return Response(status=200)


def set_webhook(viber_bot):
    viber_bot.set_webhook(config.WEBHOOK)
    logging.info("Web hoot was been set")


if __name__ == "__main__":
    scheduler = sched.scheduler(time.time(), time.sleep)
    scheduler.enter(5, 1, set_webhook, (viber, ))
    t = threading.Thread(target=scheduler.run)
    t.start()
    db.run(host='0.0.0.0', port=8443, debug=True, ssl_context=config.ssl_context)

