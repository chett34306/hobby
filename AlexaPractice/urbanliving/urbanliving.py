# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import gettext
import json
import boto3
import datetime
import uuid

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractRequestInterceptor, AbstractExceptionHandler)
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import (SimpleCard, StandardCard)

from ask_sdk_model import Response
from alexa import (data, prompts)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

userinfo = []
yes_list = ['yes','i agree','agree','confirm', 'i confirm']
no_list = ['no','i decline','decline','deny', 'i deny']

def connectoS3getData():
    s3 = boto3.client('s3')
    s3 = boto3.resource('s3', aws_access_key_id='AKIAJY3Q43GYVUH6WOUA',
                        aws_secret_access_key='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')

    file_name = 'urbanliving_info.txt'
    s3_bucket = "urbanliving"
    my_bucket = s3.Bucket(s3_bucket)
    obj = s3.Object(s3_bucket, file_name)
    body = obj.get()['Body'].read().decode('utf-8')
    return body

def writetoS3file(userdata):
    user_data = userdata.encode("utf-8")
    s3 = boto3.resource('s3', aws_access_key_id='AKIAJY3Q43GYVUH6WOUA',
                        aws_secret_access_key='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')
    s3.Bucket('urbanliving').put_object(Key="usersinfo.txt", Body=user_data)

def connecttodynamodbandwrite(userinfo):
    dynamodb = boto3.resource('dynamodb', aws_access_key_id='AKIAJY3Q43GYVUH6WOUA',
                        aws_secret_access_key='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')
    table = dynamodb.Table('urbanliving')
    date = datetime.datetime.now().date().strftime("%m-%d-%Y")
    logger.info(userinfo)
    table.put_item(
        Item={
            "id": str(uuid.uuid1()),
            'email': userinfo[0],
            'created_date':str(date),
            'consent_to_subscribe': userinfo[1]
        }
    )


class WelcomeUrbanLivingIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (ask_utils.is_request_type("LaunchRequest")(handler_input) or
                ask_utils.is_intent_name("WelcomeUrbanLivingIntent")(handler_input))

    def handle(self, handler_input):
        global userinfo
        logger.info("In WelcomeUrbanLivingIntentHandler")
        #data1 = handler_input.attributes_manager.request_attributes["_"]

        _ = handler_input.attributes_manager.request_attributes["_"]
        speech = _(data.WELCOME_MESSAGE)
        prompt = _(data.HELP_MSG)
        speech = speech + " \n" + prompt

        #speech = data1[prompts.WELCOME_MESSAGE] + "\n" + data1[prompts.WHAT_CAN_SKILL_DO]
        #handler_input.response_builder.speak(speech).ask(data1[prompts.WHATS_NEXT]).set_card(
        #    StandardCard(data1[prompts.WELCOME_MESSAGE], data1[prompts.WHAT_CAN_SKILL_DO]))
        handler_input.response_builder.speak(speech).ask(prompt).set_card(
            StandardCard(speech, prompt, {
                "smallImageUrl": "https://urbanliving.s3.amazonaws.com/seattle.png"} ))
        return handler_input.response_builder.response

class UrbanLivingInfoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("UrbanLivingInfoIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In UrbanLivingInfoIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]
        body = connectoS3getData()
        random_fact = body
        speech = body
        handler_input.response_builder.speak(speech).ask(_(data.WHATS_NEXT)).set_card(
            StandardCard(_(data.SKILL_NAME), random_fact, {
                "smallImageUrl": "https://urbanliving.s3.amazonaws.com/team.png"}))
        return handler_input.response_builder.response

class SubscribeToUrbanLivingIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("SubscribeToUrbanLivingIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In SubscribeToUrbanLivingIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]
        speech = _(data.SUBCRIBE_MSG)
        prompt = "say email slowly and distinctly"
        handler_input.response_builder.speak(speech).ask(prompt).set_card(
            StandardCard(speech, prompt, {
                "smallImageUrl": "https://urbanliving.s3.amazonaws.com/seattle.png"}))
        return handler_input.response_builder.response

#todo: add unsubscribe function and intent to ASK if users want to unsubscribe

class UserInfoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("UserInfoIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In UserInfoIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]
        slots = handler_input.request_envelope.request.intent.slots
        logger.info(slots)
        email = slots["email"].value
        #todo: need to added email to userinfo list to be used later to put in dynamodb
        userinfo.append(email)
        logger.info(userinfo[0])
        # see if date_time craeated and consent yes/no can be sent in the same method below writetoS3file.
        #speech = _(data.EMAIL_MSG).format(str(email))
        speech = _(data.EMAIL_CONFIRM_MSG) + "\n" + _(data.CONSENT_MSG)
        logger.info("user info speech: {}".format(speech))
        handler_input.response_builder.speak(speech).ask(_(data.WHATS_NEXT)).set_card(
            StandardCard(speech, speech, {
                "smallImageUrl": "https://urbanliving.s3.amazonaws.com/seattle.png"}))
        return handler_input.response_builder.response

class ConsentMessageInfoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ConsentMessageInfoIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In ConsentMessageInfoIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]
        slots = handler_input.request_envelope.request.intent.slots
        yes_no = slots['consent'].value
        logger.info("conset message yes_no slots:{}".format(yes_no))
        if (str(yes_no).lower() in yes_list):
            #TODO: write the consent info for he email collected. in UserInfoIntentHandler class
            userinfo.append(yes_no)
            logger.info(userinfo[1])
            # writetoS3file(email)
            connecttodynamodbandwrite(userinfo)
            speech = _(data.CONSENT_MSG_CONFIRM)
            handler_input.response_builder.speak(speech).ask(_(data.WHATS_NEXT)).set_card(
                StandardCard(speech, speech, {
                    "smallImageUrl": "https://urbanliving.s3.amazonaws.com/seattle.png"}))
            return handler_input.response_builder.response
        elif (str(yes_no).lower() in no_list):
            """"replace the below to suit for No/Deny message for consent"""
            userinfo.append(yes_no)
            speech = _(data.CONSENT_MSG_DENY)
            handler_input.response_builder.speak(speech).ask(_(data.WHATS_NEXT)).set_card(
                StandardCard(speech, speech, {
                    "smallImageUrl": "https://urbanliving.s3.amazonaws.com/seattle.png"}))
            return handler_input.response_builder.response



class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _(data.HELLO_MSG)

        return (
            handler_input.response_builder
            .speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _(data.HELP_MSG)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _(data.GOODBYE_MSG)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        _ = handler_input.attributes_manager.request_attributes["_"]
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = _(data.REFLECTOR_MSG).format(intent_name)

        return (
            handler_input.response_builder
            .speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)
        _ = handler_input.attributes_manager.request_attributes["_"]
        speak_output = _(data.ERROR)

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class LocalizationInterceptor(AbstractRequestInterceptor):
    """
    Add function to request attributes, that can load locale specific data
    """

    def process(self, handler_input):
        locale = handler_input.request_envelope.request.locale
        i18n = gettext.translation(
            'data', localedir='locales', languages=[locale], fallback=True)
        handler_input.attributes_manager.request_attributes["_"] = i18n.gettext

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(WelcomeUrbanLivingIntentHandler())
sb.add_request_handler(UrbanLivingInfoIntentHandler())
sb.add_request_handler(SubscribeToUrbanLivingIntentHandler())
sb.add_request_handler(UserInfoIntentHandler())
sb.add_request_handler(ConsentMessageInfoIntentHandler())
#sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
# make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
sb.add_request_handler(IntentReflectorHandler())

sb.add_global_request_interceptor(LocalizationInterceptor())

sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()