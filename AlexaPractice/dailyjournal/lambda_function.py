# -*- coding: utf-8 -*-
"""Simple fact sample app."""

import random
import logging
import json
import alexa.prompts as prompts
import boto3
import os
from datetime import date, timedelta

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.interfaces.display import (
    ImageInstance, Image, RenderTemplateDirective,
    BackButtonBehavior, BodyTemplate2)
from ask_sdk_model.ui import (SimpleCard, StandardCard)
from ask_sdk_model import Response

sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
aws_access_key_id_dailyjournal = 'AKIAXMB2VF2TNWN3SKRL'
aws_secret_access_key_dailyjournal = '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'
trish_name_list = ["trish's", 'trish', 'trishs']
rhea_name_list = ["rhea's", "rheas", "ria", "rhea"]

s3_bucket = ''


def connectoS3getData(date_uttered):
    s3 = boto3.client('s3')
    s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id_dailyjournal,
                        aws_secret_access_key=aws_secret_access_key_dailyjournal)
    # today = date.today()
    file_name = ''
    my_bucket = s3.Bucket(s3_bucket)

    for file in my_bucket.objects.all():
        # put the file name in this format MM-DD-YY.txt
        if (str(file.key).split(".")[0] == date_uttered):
            # if(str(file.key).split(".")[0] == str(today.strftime("%m-%d-%Y"))):
            file_name = file_name + str(file.key)
            break

    if (file_name == ''):
        random_fact = "No new content is created by {} today, ".format(s3_bucket.split("-")[0]) + date_uttered
        return random_fact
    else:
        obj = s3.Object(s3_bucket, file_name)
        body = obj.get()['Body'].read().decode('utf-8')
        return body


def connectoS3getData(date_uttered, s3bucket):
    s3 = boto3.client('s3')
    s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id_dailyjournal,
                        aws_secret_access_key=aws_secret_access_key_dailyjournal)
    # today = date.today()
    file_name = ''
    my_bucket = s3.Bucket(s3bucket)

    for file in my_bucket.objects.all():
        # put the file name in this format MM-DD-YY.txt
        if (str(file.key).split(".")[0] == date_uttered):
            # if(str(file.key).split(".")[0] == str(today.strftime("%m-%d-%Y"))):
            file_name = file_name + str(file.key)
            break

    if (file_name == ''):
        random_fact = "No new content is created by {} today, ".format(s3bucket.split('-')[0]) + date_uttered
        return random_fact
    else:
        obj = s3.Object(s3bucket, file_name)
        body = obj.get()['Body'].read().decode('utf-8')
        return body


class WelcomeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (is_request_type("LaunchRequest")(handler_input) or
                is_intent_name("WelcomeIntent")(handler_input))

    def handle(self, handler_input):
        data = handler_input.attributes_manager.request_attributes["_"]
        speech = data[prompts.WELCOME_MESSAGE] + data[prompts.WHAT_CAN_SKILL_DO]
        handler_input.response_builder.speak(speech).ask(data[prompts.WHATS_NEXT]).set_card(
            StandardCard(data[prompts.WELCOME_MESSAGE], data[prompts.WHAT_CAN_SKILL_DO],
                         {"smallImageUrl": "https://trish-chettypally.s3.amazonaws.com/trish-rhea.png"}))
        return handler_input.response_builder.response


# Built-in Intent Handlers
class OpenJournalIntentHandler(AbstractRequestHandler):
    """Handler for Skill Launch and OpenJournal Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (  # is_request_type("LaunchRequest")(handler_input) or
            is_intent_name("OpenJournalIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In OpenJournalIntentHandler")

        # get localization data
        data = handler_input.attributes_manager.request_attributes["_"]
        today = date.today()
        today = str(today.strftime("%m-%d-%Y"))
        # send date in MM-DD-YYYY format
        body = connectoS3getData(today)
        random_fact = "Reading article from:" + today
        random_fact = random_fact + "\n" + body
        speech = data[prompts.GET_FACT_MESSAGE].format(random_fact)
        handler_input.response_builder.speak(speech).ask(data[prompts.WHATS_NEXT]).set_card(
            StandardCard(data[prompts.SKILL_NAME], random_fact,
                         {"smallImageUrl": "https://trish-chettypally.s3.amazonaws.com/Trish.png"}))
        return handler_input.response_builder.response


class GetArticleIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("GetArticleIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In GetArticIntentleHandler")
        slots = handler_input.request_envelope.request.intent.slots
        name = slots["kid_name"].value
        # get localization data
        data = handler_input.attributes_manager.request_attributes["_"]
        today = date.today()
        today = str(today.strftime('%m-%d-%Y'))
        today_file = ''
        global s3_bucket
        bucket_set = False
        if (name is not None):
            # if(name[0:5].lower() == "trish" or name[0:7].lower() == "trish's" or name[0:6].lower() == "trishs"):
            if (str(name).lower() in trish_name_list):
                s3_bucket = 'trish-chettypally'
                bucket_set = bucket_set or True
            # elif(name[0:4].lower() == 'rhea' or name[0:6].lower() == "rhea's" or name[0:3].lower() == 'ria' or name[0:5].lower() == "rheas"):
            elif (str(name).lower() in rhea_name_list):
                s3_bucket = 'rhea-chettypally'
                bucket_set = bucket_set or True

            if bucket_set:
                body = connectoS3getData(today, s3_bucket)
                random_fact = body
                speech = data[prompts.GET_FACT_MESSAGE].format(random_fact)
                handler_input.response_builder.speak(speech).ask(data[prompts.WHATS_NEXT]).set_card(
                    StandardCard(data[prompts.SKILL_NAME], random_fact, {
                        "smallImageUrl": "https://trish-chettypally.s3.amazonaws.com/{}.png".format(
                            s3_bucket.split("-")[0])}))
                return handler_input.response_builder.response
            else:
                # ask to say the name right.
                speech = "I don't identify the name. Please say again"
                handler_input.response_builder.speak(speech).ask(data[prompts.WHATS_NEXT]).set_card(
                    StandardCard(data[prompts.SKILL_NAME], speech))
                return handler_input.response_builder.response


        else:
            handler_input.response_builder.speak(data[prompts.WHATS_NEXT]).ask(data[prompts.WHATS_NEXT]).set_card(
                StandardCard(data[prompts.SKILL_NAME],
                             {"smallImageUrl": "https://rhea-chettypally.s3.amazonaws.com/rhea.png"}))
            return handler_input.response_builder.response


class OldArticleIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("OldArticleIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In OldArticleIntentHandler")
        data = handler_input.attributes_manager.request_attributes["_"]
        months = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                  "july": "07", "august": "08", "september": "09", "october": "10", "november": "11", "december": "12"}
        slots = handler_input.request_envelope.request.intent.slots
        month = slots["month"].value
        day = slots["day"].value
        if int(day) < 10:
            day = str("0") + str(day)
        year = slots["year"].value
        if year is None:
            year = date.today().year
        # format MM-DD-YYYY
        date_uttered = months[str(month).lower()] + "-" + str(day) + "-" + str(year)
        body = connectoS3getData(date_uttered,
                                 s3_bucket)  # s3bucket is set when asked for Trish's article or Rhea's article
        random_fact = "Reading article from:" + months[str(month).lower()] + "-" + str(day) + "-" + str(year)
        random_fact = random_fact + "\n" + body
        handler_input.response_builder.speak(random_fact).ask(data[prompts.WHATS_NEXT]).set_card(
            StandardCard(data[prompts.SKILL_NAME], random_fact, {
                "smallImageUrl": "https://trish-chettypally.s3.amazonaws.com/{}.png".format(s3_bucket.split("-")[0])}))
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        # get localization data
        data = handler_input.attributes_manager.request_attributes["_"]

        speech = data[prompts.HELP_MESSAGE]
        reprompt = data[prompts.HELP_REPROMPT]
        handler_input.response_builder.speak(speech).ask(
            reprompt).set_card(StandardCard(
            data[prompts.SKILL_NAME], speech))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        # get localization data
        data = handler_input.attributes_manager.request_attributes["_"]

        speech = data[prompts.STOP_MESSAGE]
        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.

    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")

        # get localization data
        data = handler_input.attributes_manager.request_attributes["_"]

        speech = data[prompts.FALLBACK_MESSAGE]
        reprompt = data[prompts.FALLBACK_REPROMPT]
        handler_input.response_builder.speak(speech).ask(
            reprompt)
        return handler_input.response_builder.response


class LocalizationInterceptor(AbstractRequestInterceptor):
    """
    Add function to request attributes, that can load locale specific data.
    """

    def process(self, handler_input):
        locale = handler_input.request_envelope.request.locale
        logger.info("Locale is {}".format(locale))

        # localized strings stored in language_strings.json
        with open("language_strings.json") as language_prompts:
            language_data = json.load(language_prompts)
        # set default translation data to broader translation
        if locale[:2] in language_data:
            data = language_data[locale[:2]]
            # if a more specialized translation exists, then select it instead
            # example: "fr-CA" will pick "fr" translations first, but if "fr-CA" translation exists,
            # then pick that instead
            if locale in language_data:
                data.update(language_data[locale])
        else:
            data = language_data[locale]
        handler_input.attributes_manager.request_attributes["_"] = data


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info("Session ended reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        handler_input.response_builder.speak(EXCEPTION_MESSAGE).ask(
            HELP_REPROMPT)

        return handler_input.response_builder.response


# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""

    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""

    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers
sb.add_request_handler(WelcomeIntentHandler())
sb.add_request_handler(OpenJournalIntentHandler())
sb.add_request_handler(GetArticleIntentHandler())
sb.add_request_handler(OldArticleIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# Register request and response interceptors
sb.add_global_request_interceptor(LocalizationInterceptor())
sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()
