"""
A simple skill built with the Amazon Alexa Skills Kit.
Copyright @ 2017 - Maksood Mohiuddin
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Mohiuddin Home Alexa Learning Skill. " \
                    "Please start by  saying your name. You can say, " \
                    "my name is Aydin, Maksood, Nav or Guest." \
                    "Or you can say teach me alphabet or teach me numbers or teach me bangla alphabet or bangla numbers."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me your name by saying, " \
                    "my name is Aydin, Maksood, Nav or Guest."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Mohiuddin Home Alexa Learning Skill. " \
                    "Maksood is the best husband ever! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_your_name_attributes(your_name):
    return {"yourName": your_name}


def set_name_in_session(intent, session):
    """ Sets the name in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Name' in intent['slots']:
        yout_name = intent['slots']['Name']['value']
        session_attributes = create_your_name_attributes(yout_name)
        speech_output = "I now know your name is " + \
                        yout_name + \
                        ". You can ask me your name by saying, " \
                        "what's my name?"
        reprompt_text = "You can ask me your name by saying, " \
                        "what's my name?"
    else:
        speech_output = "I'm not sure what your name is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your name is. " \
                        "You can tell me your name by saying, " \
                        "my name is Aydin, Maksood, Nav or Guest."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_name_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "yourName" in session.get('attributes', {}):
        your_name = session['attributes']['yourName']
        speech_output = "Your name is " + your_name + \
                        ". Now you can say teach me alphabet or teach me numbers or teach me bangla alphabet or bangla numbers"
        should_end_session = False
    else:
        speech_output = "I'm not sure what your name is. " \
                        "You can say, my name is Aydin, Maksood, Nav or Guest. Or you can say teach me alphabet or teach me numbers or teach me bangla alphabet or bangla numbers"
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


def get_english_alphabet(intent, session):
    session_attributes = {}
    reprompt_text = "You can say teach me alphabet or teach me english alphabet or english alphabet or alphabet."
    output_as_text = "A. B. C. D. E. F. G. H. I. J. K. L. M. N. O. P. Q. R. S. T. U. V. W. X. Y. Z."

    speech_output = "Here is English Alphabet. " + output_as_text
    should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_numbers(intent, session):
    session_attributes = {}
    reprompt_text = "You can say teach me numbers."
    output_as_text = "Zero. One. Two. Three. Four. Five. Six. Seven. Eight. Nine. Ten."

    speech_output = "Here is numbers. " + output_as_text
    should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_bangla_alphabet(intent, session):
    session_attributes = {}
    reprompt_text = "You can say teach me bangla alphabet or bangla alphabet."
    output_as_text = "Aw. A. Hrashho E. Deergho E. Hrashho O. Deergho REE. E. OY. O. OU." \
                    "KAW. KHAW. GAW. GHAW. OAW. CHAW. CHCHAW. Borgio Jaw. Jhaw. EAW." \
                    "Taw. Thaw. Daw. Dhaw. Mordhonno Naw. Taw. Thaw. Daw. Dhaw. Danto Naw. " \
                    "Paw. Phaw. Baw. Bhaw. Maw. Antostho JAW. Raw. Law. Talobbo SHAW. Mordhonno SHAW." \
                    "Donto SHAW. Haw. Dae Shoono RAW. Dhae Shoono RAW. Antostho AW" \
                    "Khando TAW. Onooshshawr. Bishargo. Chandro Bindoo."
    speech_output = "Here is Bangla Alphabet. " + output_as_text
    should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_bangla_numbers(intent, session):
    session_attributes = {}
    reprompt_text = "You can say teach me bangla numbers."
    output_as_text = "sunya. ek. dhoi. tin. char. punch. chay. saat. aat. nay. dosh."

    speech_output = "Here is Bangla numbers. " + output_as_text
    should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def exit_app(intent, session):
    session_attributes = {}
    reprompt_text = None

    speech_output = "Thank you for trying the Mohiuddin Home Alexa Learning Skill. " \
                    "Maksood is the best husband ever! "
    should_end_session = True

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MyNameIsIntent":
        return set_name_in_session(intent, session)
    elif intent_name == "WhatsMyNameIntent":
        return get_name_from_session(intent, session)
    elif intent_name == "TeachEnglishAlphabet":
        return get_english_alphabet(intent, session)
    elif intent_name == "TeachNumbers":
        return get_numbers(intent, session)
    elif intent_name == "TeachBanglaAlphabet":
        return get_bangla_alphabet(intent, session)
    elif intent_name == "TeachBanglaNumbers":
        return get_bangla_numbers(intent, session)
    elif intent_name == "ExitApp":
        return exit_app(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
