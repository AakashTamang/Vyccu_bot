# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUtteranceReverted
from rasa_sdk.forms import FormAction

from langdetect import detect

class ActionShowTypeOfLoan(Action):
    def name(self):
        return 'action_show_type_of_loan'
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            reply = "VYCCU Savings and Credit Cooperative Limited provides following type of loans to it's customers."
            buttons = [{'title': 'Agriculture Loan',
                        'payload': '{}'.format('agriculture loan')},
                        {'title': 'Career Loan',
                        'payload': '{}'.format('career loan')},
                        {'title': 'Education Loan',
                        'payload': '{}'.format('education loan')},
                        {'title': 'Hire Purchase Loan',
                        'payload': '{}'.format('hire purchase loan')},
                        {'title': 'Home Loan',
                        'payload': '{}'.format('home loan')},
                        {'title': 'Business Loan',
                        'payload': '{}'.format('business loan')},
                        {'title': 'Industry Loan',
                        'payload': '{}'.format('industry loan')}   
                        ]
        else:
            reply = "विकु बचत तथा ॠण सहकारी लिमिटेडले आफ्ना ग्राहकहरु लाई निम्न प्रकारको ऋण (loan) प्रदान गर्दछ।"
            buttons = [{'title': 'कृषि ऋण',
                        'payload': 'मलाई कृषि ऋण बारे भन'},
                        {'title': 'क्यारियर ऋण',
                        'payload': 'मलाई क्यारियर ऋण बारे भन'},
                        {'title': 'शौक्षिक ऋण',
                        'payload': 'मलाई शौक्षिक ऋण बारे भन'},
                        {'title': 'भाडा खरीद ऋण',
                        'payload': 'मलाई भाडा खरीद ऋण बारे भन'},
                        {'title': 'घर सम्पती ऋण',
                        'payload': 'मलाई घर सम्पती ऋण बारे भन'},
                        {'title': 'व्यवसायिक ऋण',
                        'payload': 'मलाई व्यवसायिक ऋण बारे भन'},
                        {'title': 'उद्योग ऋण',
                        'payload': 'मलाई उद्योग ऋण बारे भन'}   
                        ]
        attachment = {
            "query_response": reply,
            "data":[{"buttons":buttons}],
            "type":"message_with_buttons",
            "data_fetch_status": "success"
        }
        # dispatcher.utter_message(attachment=attachment, buttons=buttons)
        dispatcher.utter_message(attachment=attachment)
        return []


class FetchTypeOfLoan(Action):
    def name(self):
        return 'action_fetch_type_of_loan'

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            loan_type = tracker.get_slot('type_of_loan')
        except:
            messages = [" 😕 Sorry, I cannot understand you. Could you repeat it again? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।", " 😕 I am having confusion in understanding it. Would you repeat it please? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।",
                "😕 I find it quite ambiguous. Can you tell me again a bit clearly? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।"]
            reply = random.choice(messages)
            attachment = {
                "query_response": reply,
                "data":[],
                "type":"normal_message",
                "data_fetch_status": "success"
            }
            dispatcher.utter_message(attachment=attachment)
            return [UserUtteranceReverted()]
        language_list = ["hi","ne","mr"]
        question = tracker.latest_message['text']
        if detect(question) not in language_list:
            loan_link = "<a href = 'http://vyccu.org.np/services/loans'>loan</a>"
            reply = f"VYCCU Savings and Credit Cooperative Ltd provides attractive {loan_type} . You can get more info on {loan_type} from {loan_link}"
        else:
            loan_link = "<a href = 'http://vyccu.org.np/services/loans'>ऋण (Loan)</a>"
            reply = f"विकु बचत तथा ॠण सहकारी लिमिटेडले आकर्षक {loan_type} प्रदान गर्दछ। तपाइँ थप जानकारीका लागि यो लिन्क म जान सक्नुहुन्छ: {loan_link}"
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return [SlotSet('type_of_loan', None)]

class ActionShowTypeOfServices(Action):
    def name(self):
        return 'action_show_type_of_services'
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            reply = "We facilitate following type of services."
            buttons = [{'title': 'ATM',
                    'payload': '{}'.format('atm')},
                    {'title': 'SMS Banking',
                    'payload': '{}'.format('sms banking')},
                    {'title': 'Mobile Banking',
                    'payload': '{}'.format('mobile banking')},
                    {'title': 'Remittance',
                    'payload': '{}'.format('remittance')},
                    {'title': 'Health Insurance',
                    'payload': '{}'.format('health insurance')},
                    {'title': 'Loan',
                    'payload': '{}'.format('loan')},
                    {'title': 'Deposit',
                    'payload': '{}'.format('deposit')},
                    {'title': 'Other Services',
                    'payload': '{}'.format('other services')}   
                    ]
        else:
            reply = "हामी निम्न प्रकारका सेवाहरूको सुविधा दिन्छौं।"
            buttons = [{'title': 'एटीएम सेवा',
                    'payload': 'मलाई एटीएम सेवा बारे भन'},
                    {'title': 'एसएमएस बैंकिंग सेवा',
                    'payload': 'मलाई एसएमएस बैंकिंग सेवा बारे भन'},
                    {'title': 'मोबाइल बैंकिंग सेवा',
                    'payload': 'मलाई मोबाइल बैंकिंग सेवा बारे भन'},
                    {'title': 'रेमिट्यान्स सेवा',
                    'payload': 'मलाई रेमिट्यान्स सेवा बारे भन'},
                    {'title': 'स्वास्थ्य बीमा सेवा',
                    'payload': 'मलाई स्वास्थ्य बीमा सेवा बारे भन'},
                    {'title': 'ऋण सेवा',
                    'payload': 'मलाई ऋण सेवा बारे भन'},
                    {'title': 'डिपोजिट सेवा',
                    'payload': 'मलाई डिपोजिट सेवा बारे भन'},
                    {'title': 'अन्य बैंकिंग सेवा',
                    'payload': 'मलाई अन्य बैंकिंग सेवा बारे भन'}   
                    ]
        attachment = {
            "query_response": reply,
            "data":[{"buttons":buttons}],
            "type":"message_with_buttons",
            "data_fetch_status": "success"
        }
        # dispatcher.utter_message(attachment=attachment, buttons=buttons)
        dispatcher.utter_message(attachment=attachment)
        return []

class FetchTypeOfServices(Action):
    def name(self):
        return 'action_fetch_type_of_services'

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        service_type = tracker.get_slot('type_of_services')
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            type_list = {
                "deposit": "<a href = 'http://vyccu.org.np/services/deposit'>Deposit Service</a>",
                "loan": "<a href = 'http://vyccu.org.np/services/loans'>Loan Service</a>",
                "remittance": "<a href = 'http://vyccu.org.np/services/remittance'>Remittance Service</a>",
                "health insurance": "<a href = 'http://vyccu.org.np/services/health-insurance'>Health Insurance Service </a>",
                "atm": "<a href= 'http://vyccu.org.np/services/atm-service'>ATM Service</a>",
                "sms banking": "<a href = 'http://vyccu.org.np/services/other-services'>SMS Banking Service</a>",
                "mobile banking": "<a href = 'http://vyccu.org.np/services/other-services'>Mobile Banking Service</a>",
                "other services": "<a href = 'http://vyccu.org.np/services/other-services'>Other Banking Service</a>"
            }
        else:
            type_list = {
                "deposit": "<a href = 'http://vyccu.org.np/services/deposit'>डिपोजिट सेवा (Deposit Service)</a>",
                "loan": "<a href = 'http://vyccu.org.np/services/loans'>ऋण सेवा (Loan Service)</a>",
                "remittance": "<a href = 'http://vyccu.org.np/services/remittance'>रेमिट्यान्स सेवा (Remittance Service)</a>",
                "health insurance": "<a href = 'http://vyccu.org.np/services/health-insurance'>स्वास्थ्य बीमा सेवा (Health Insurance Service)</a>",
                "atm": "<a href= 'http://vyccu.org.np/services/atm-service'>एटीएम सेवा (ATM Service)</a>",
                "sms banking": "<a href = 'http://vyccu.org.np/services/other-services'>एसएमएस सेवा (SMS Banking Service)</a>",
                "mobile banking": "<a href = 'http://vyccu.org.np/services/other-services'>मोबाइल बैंकिंग सेवा (Mobile Banking Service)</a>",
                "other services": "<a href = 'http://vyccu.org.np/services/other-services'>अन्य बैंकिंग सेवा (Other Banking Service)</a>"
            }
        try:
            service_link = type_list[service_type]
        except:
            messages = ["😕 Sorry, I cannot understand you. Could you repeat it again? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।", "😕 I am having confusion in understanding it. Would you repeat it please? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।",
                "😕 I find it quite ambiguous. Can you tell me again a bit clearly? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।"]
            reply = random.choice(messages)
            attachment = {
                "query_response": reply,
                "data":[],
                "type":"normal_message",
                "data_fetch_status": "success"
            }
            dispatcher.utter_message(attachment=attachment)
            return [UserUtteranceReverted()]
        if detect(question) not in language_list:
            reply = f"Oh you want to get {service_type}. We are happy to serve you. Learn more about {service_type} from {service_link}"
        else:
            reply = f"ओह तपाईं {service_type} प्राप्त गर्न चाहानुहुन्छ। हामी तपाईंको सेवा गर्न पाउँदा खुसी छौं। {service_type} को बारेमा बढि जन्न यो लिन्क म थिच्नुहोस: {service_link}"
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return [SlotSet('type_of_services', None)]


class ActionShowTypeOfInterest(Action):
    def name(self):
        return 'action_show_type_of_interest'
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            reply = "Interest rate varies for following services:"
            buttons = [{'title': 'Loan',
                    'payload': '{}'.format('rate loan')},
                    {'title': 'Deposit',
                    'payload': '{}'.format('rate deposit')}   
                    ]
        else:
            reply = "ब्याज दर निम्न सेवाहरूको लागि भिन्न हुन्छ:"
            buttons = [{'title': 'ऋण',
                    'payload': 'ऋण ब्याज दर'},
                    {'title': 'डिपोजिट',
                    'payload': 'डिपोजिट ब्याज दर'}   
                    ]
        attachment = {
            "query_response": reply,
            "data":[{"buttons":buttons}],
            "type":"message_with_buttons",
            "data_fetch_status": "success"
        }
        # dispatcher.utter_message(attachment=attachment, buttons=buttons)
        dispatcher.utter_message(attachment=attachment)
        return []

class FetchTypeOfInterest(Action):
    def name(self):
        return 'action_fetch_type_of_interest'

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            interest_type = tracker.get_slot('type_of_services')
            if interest_type == "rate loan":
                interest_type = "loan"
            elif interest_type == "rate deposit":
                interest_type = "deposit"
        except:
            messages = ["😕 Sorry, I cannot understand you. Could you repeat it again? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।", "😕 I am having confusion in understanding it. Would you repeat it please? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।",
                "😕 I find it quite ambiguous. Can you tell me again a bit clearly? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।"]
            reply = random.choice(messages)
            attachment = {
                "query_response": reply,
                "data":[],
                "type":"normal_message",
                "data_fetch_status": "success"
            }
            dispatcher.utter_message(attachment=attachment)
            return [UserUtteranceReverted()]
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            reply = f"Oh, you want to check interest rate for {interest_type}. Get detailed information about our interest rates at <a href='http://vyccu.org.np/interest-rates/'>Interest Rate</a>"
        else:
            reply = f"ओह, तपाइँ {interest_type}का लागि ब्याज दर जन्न चाहानुहुन्छ। हाम्रो ब्याज दर को बारेमा विस्तृत जानकारी यो लिन्कमा प्राप्त गर्न सक्नुहुन्छ:  <a href='http://vyccu.org.np/interest-rates/'>Interest Rate</a>"
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return [SlotSet('type_of_services', None)]

class About(Action):
    def name(self):
        return "action_about"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ['👋😃 I am your virtual assistant for VYCCU. VYCCU Savings and Credit Cooperative Limited is a primary-level single-purpose cooperative organization . You can get more info on <a href = "http://vyccu.org.np/category/our-profile-2">vyccu.org.np/our-profile</a>']
        else:
            messages = ['👋😃 म तपाइँको विकुबारे प्रश्नहरुको मद्दत गर्ने तपाइँको सहायक हुँ। विकु बचत तथा ॠण सहकारी लिमिटेड एक प्राथमिक-स्तर एकल-उद्देश्य सहकारी संस्था हो। तपाईं मा अधिक जानकारी प्राप्त गर्न सक्नुहुन्छ  <a href = "http://vyccu.org.np/category/our-profile-2">vyccu.org.np/our-profile</a>',
                        '😁 म यहाँ तपाइँको विकुबारे रहेका जिज्ञासाहरु बारे मद्दत गर्ने साथी हुँ। विकु बचत तथा ॠण सहकारी लिमिटेड एक प्राथमिक-स्तर एकल-उद्देश्य सहकारी संस्था हो। तपाईं मा अधिक जानकारी प्राप्त गर्न सक्नुहुन्छ  <a href = "http://vyccu.org.np/category/our-profile-2">vyccu.org.np/our-profile</a>']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class OutOfScope(Action):
    def name(self):
        return "action_out_of_scope"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = ['😕 Sorry I didn’t catch that word? Could you tell me more clearly? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।',
                    '😕 I am sorry I did not understand? Can you tell again? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return [UserUtteranceReverted()]

class AfterOutOfScope(Action):
    def name(self):
        return "action_after_out_of_scope"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = ['😕 We are sorry for not being able to understand you. Could you provide us your contact details so that we could help you properly? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। के तपाई हामीलाई आफ्नो सम्पर्क विवरण दिन सक्नुहुन्छ ताकि हामी तपाईलाई अगाडि सम्पर्क गर्न सकौ?',
                    "😕 Sorry, I don't think I can help you. Can you give us your contant detail so that we could help you properly? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। के तपाई हामीलाई आफ्नो सम्पर्क विवरण दिन सक्नुहुन्छ ताकि हामी तपाईलाई अगाडि सम्पर्क गर्न सकौ?"]
        # buttons = [
        # 	{"title":"Email Address", "payload":"/form_email"},
        # 	{"title":"Contact Number", "payload":"/form_contact"}
        # ]
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"message_with_form",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class AskFirstName(Action):
    def name(self):
        return "action_ask_first_name"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = ['Please give your First name <br>तपाईंको पहिलो नाम भर्नुहोस्',
                    'Provide us your First name <br>तपाईंको पहिलो नाम भर्नुहोस्']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class AskLastName(Action):
    def name(self):
        return "action_ask_last_name"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = ['Please give your Last name <br>तपाईंको अन्तिम नाम भर्नुहोस्',
                    'Provide us your Last name <br>तपाईंको अन्तिम नाम भर्नुहोस्']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class AskContactNumner(Action):
    def name(self):
        return "action_ask_contact_number"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = ['Please give your contact number <br>तपाईंको सम्पर्क नम्बर भर्नुहोस्',
                    'Provide us your contact number <br>तपाईंको सम्पर्क नम्बर भर्नुहोस्']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class AskEmailAddress(Action):
    def name(self):
        return "action_ask_email"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = ['Please give your email address <br>तपाईंको ईमेल भर्नुहोस्',
                    'Provide us your email address <br>तपाईंको ईमेल भर्नुहोस्']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class FormSubmitted(Action):
    def name(self):
        return "action_form_submitted"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        f_name = tracker.get_slot('first_name')
        l_name = tracker.get_slot('last_name')
        if f_name != None or l_name != None:
            messages = [f'Thank you {f_name} {l_name}. 😃 Your form has been submitted successfully. We will contact you very soon. <br>धन्यवाद {f_name} {l_name}! 🙏 हामी तपाईंलाई चाँडै सम्पर्क गर्नेछौं।',
                        f'Thank you {f_name} {l_name} for your information. 😃 We will contact you as soon as possible. <br>धन्यवाद {f_name} {l_name}! 🙏 हामी तपाईंलाई चाँडै सम्पर्क गर्नेछौं।']
        else:
            messages = ['Thank you. 😃 Your form has been submitted successfully. We will contact you very soon. <br>धन्यवाद! 🙏 हामी तपाईंलाई चाँडै सम्पर्क गर्नेछौं।',
                        'Thank you for your information. 😃 We will contact you as soon as possible. <br>धन्यवाद! 🙏 हामी तपाईंलाई चाँडै सम्पर्क गर्नेछौं।']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class Greeting(Action):
    def name(self):
        return "action_greeting"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ["Hi there. 👋😃 It's such a pleasure to have you here. Welcome to VYCCU saving and credit co-operative Ltd. How can we help you.",
                        "Hello, 🤗 welcome to VYCCU saving and credit co-operative Ltd. How can we assist you."]
        else:
            messages = ["नमस्कार! 🙏 तपाईलाई यहाँ पाउँदा खुसी लाग्यो। विकु बचत तथा ॠण सहकारी लिमिटेडमा स्वागत छ हामी कसरी तपाईंलाई मद्दत गर्न सक्दछौं?",
                        "नमस्कार, 🙏 विकु बचत तथा ॠण सहकारी लिमिटेडमा स्वागत छ। हामी कसरी तपाईंलाई सहयोग गर्न सक्दछौं?"]
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class AfterGreeting(Action):
    def name(self):
        return "action_after_greet"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ["I am fine. How can we help you.",
                        "I am doing very well. How can we assist you."]
        else:
            messages = ["म ठिक छु। 😃 तपाईलाई कसरी सहयोग गर्न सक्छौ?",
                        "म धेरै राम्रो गर्दै छु। 😃 हामी तपाईंलाई कसरी मद्दत गर्न सक्छौं?"]
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class Goodbye(Action):
    def name(self):
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ['Thank you, 🙏 I am happy to help you. For more details about us please visit our website <a href="http://vyccu.org.np">vyccu.org.np</a>',
                        'I hope I was helpful for you. 😁 To know more about us you can visit our website <a href="http://vyccu.org.np">vyccu.org.np</a>']
        else:
            messages = ['धन्यबाद, 🙏 म तपाईंलाई सहयोग गर्न पाएकोमा खुसी छु। 😁 हामी बारे बढि जानकारीका लागि कृपया हाम्रो वेबसाइटमा जानुहोस् <a href="http://vyccu.org.np">vyccu.org.np</a>',
                        'धन्यबाद, 😁 आशा गर्दछु कि म तपाईको लागि सहयोगी थियो। 🙏 यदि तपाईं हाम्रो बारेमा बढि जान्न चाहानुहुन्छ भने तपाईं हाम्रो वेबसाइट भ्रमण गर्न सक्नुहुन्छ <a href="http://vyccu.org.np">vyccu.org.np</a>']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class Location(Action):
    def name(self):
        return "action_location"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ['VYCCU Savings and Credit Cooperative Limited is located in Bijaynagar, Gaindakot-05, Nawalpur. Folllow us at google maps <a href="https://www.google.com/maps/dir//27.7015019,84.3871719/@27.701502,84.387172,17z?hl=en-US">maps</a>',
                        'You can visit us at Bijaynagar, Gaindakot-05, Nawalpur. Follow us at google maps <a href="https://www.google.com/maps/dir//27.7015019,84.3871719/@27.701502,84.387172,17z?hl=en-US">maps</a>']
        else:
            messages = ['विकु बचत तथा ॠण सहकारी लिमिटेड विजयनगर, गैंडाकोट-०५, नवलपुरमा स्थित छ। हाम्रो ठेगाना गूगलमा पनि हेर्न सक्नुहुन्छ <a href="https://www.google.com/maps/dir//27.7015019,84.3871719/@27.701502,84.387172,17z?hl=en-US">स्थान</a>',
                        'तपाईं हामीलाई यहाँ विजयनगर, गैंडाकोट-०५, नवलपुरमा भेट्न सक्नुहुन्छ। हाम्रो ठेगाना गूगलमा पनि हेर्न सक्नुहुन्छ <a href="https://www.google.com/maps/dir//27.7015019,84.3871719/@27.701502,84.387172,17z?hl=en-US">स्थान</a>']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class Contact(Action):
    def name(self):
        return "action_contact"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ['To know more about us and our services you can use these details: <br>Website: <a href="http://vyccu.org.np/contact-us/">vyccu.org.np/contact</a> <br>Email: vyccu@vyccu.org.np <br>Head Office Bijaynagar, Gaindakot-05, Nawalpur <br>Phone: 078-502601, 078-501364, 078-503162, 078-503104 <br>Please provide us with your following details so that we can contact you further.']
        else:
            messages = ['हामी र हाम्रो सेवाहरूको बारेमा बढि जान्नको लागि तपाईं यी विवरणहरू प्रयोग गर्न सक्नुहुनेछ, <br>हाम्रो वेबसाइटमा <a href="http://vyccu.org.np/contact-us/">vyccu.org.np/contact</a> <br>ईमेल: vyccu@vyccu.org.np <br>ठेगाना: विजयनगर, गैंडाकोट-०५, नवलपुर <br>फोन नम्बर: ०७८-५०२६०१, ०७८-५०१३६४, ०७८-५०३१६२, ०७८-५०३१०४ <br>कृपया हामीलाई तपाईंको निम्न विवरणहरू प्रदान गर्नुहोस्, ताकि हामी तपाईंलाई सम्पर्क गर्न सकौ।']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class AboutServiceCenter(Action):
    def name(self):
        return "action_about_service_center"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ['We have 11 service centers. You can get more info on service centers from <a href = "http://vyccu.org.np/service-center">vyccu.org.np/service-centers</a>',
                        'The information about our service centers can be found in this link: <a href = "http://vyccu.org.np/service-center">vyccu.org.np/service-centers</a>']
        else:
            messages = ['हामीसँग ११ सेवा केन्द्रहरू छन्। हाम्रो सेवा केन्द्रहरूबारे थप जानकारी प्राप्त गर्न यो लिंकमा थिच्नुहोस् <a href = "http://vyccu.org.np/service-center">vyccu.org.np/service-centers</a>',
                        'हाम्रो ११ सेवा केन्द्रहरूको बारेमा जानकारी यस लिंकमा फेला पार्न सकिन्छ <a href = "http://vyccu.org.np/service-center">vyccu.org.np/service-centers</a>']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class AskAccountAlreadyOpen(Action):
    def name(self):
        return "action_ask_account_already_open"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ["Do you have a saving account with VYCCU saving and credit co-operative Ltd.?"]
        else:
            messages = ["के तपाइँ विकु बचत तथा ॠण सहकारी लिमिटेडमा पहिलेनै खाता भएको मान्छे हो?"]
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class AccountAlreadyExist(Action):
    def name(self):
        return "action_account_already_exist"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ["Dear customer, as you are already an existing customer of VYCCU saving and credit co-operative Ltd. You cannot open a new account with us as per local regulations. We will keep you posted here as we are adding many new exciting services soon.",
                        "Sir, since an account on your name already exist in VYCCU saving and credit co-operative Ltd. we cannot create a new account for you."]
        else:
            messages = ["प्रिय ग्राहक, तपाईं पहिले नै विकु बचत तथा ॠण सहकारी लिमिटेडको एक ग्राहक हुनुहुन्छ। तपाईं नियमहरू अनुसार हामीसँग नयाँ खाता खोल्न सक्नुहुन्न। हामी चाँडै नै थुप्रै नयाँ उत्साहजनक सेवाहरू थप्दै छौं र तपाईंलाई सूचना दिनेछौं।",
                        "तपाईको नाममा खाता पहिले नै विकु बचत तथा ॠण सहकारी लिमिटेडमा अवस्थित छ। त्यसकारण हामी तपाईको लागि नयाँ खाता बनाउन सक्दैनौं।"]
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class CreateAccount(Action):
    def name(self):
        return "action_create_account"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ["Ok, now lets create an account for you."]
        else:
            messages = ["ठीक छ, अब तपाईंको लागि खाता बनाउँदछौं।"]
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class TypesofDeposit(Action):
    def name(self):
        return "action_ask_want_loan"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            reply = "Do you want to take Loan?"
            buttons = [{'title': 'Yes',
                    'payload': 'yes'},
                    {'title': 'No',
                    'payload': 'no'},   
                    ]
        else:
            reply = "के तपाई ऋण लिन चाहानुहुन्छ?"
            buttons = [{'title': 'हो',
                    'payload': 'हो'.format('')},
                    {'title': 'नाइ',
                    'payload': 'नाइ'},   
                    ]
        attachment = {
            "query_response": reply,
            "data":[{"buttons":buttons}],
            "type":"message_with_buttons",
            "data_fetch_status": "success"
        }
        # dispatcher.utter_message(attachment=attachment,buttons=buttons)
        dispatcher.utter_message(attachment=attachment)
        return []

class AfterNo(Action):
    def name(self):
        return "action_no"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ["Ok sir. Are there any ways in which we can help you?","Ok sir. Is there anything more you want to know?"]
        else:
            messages = ["हुन्छ सर। के तपाईंसँग अरु केहि प्रश्न हरुछन जस्को म उत्तर दिएर सहयोग गर्न सक्छु?"]
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return []

class GetATMCard(Action):
    def name(self):
        return "action_get_atm_card"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            messages = ['Please contact to your nearest Service center to get your ATM card. The information on our service center can be found in this link: <a href = "http://vyccu.org.np/service-center">vyccu.org.np/service-centers</a>']
        else:
            messages = ['तपाईंको एटीएम कार्ड प्राप्त गर्नका लागि कृपया तपाईंको नजिकको सेवा केन्द्रमा सम्पर्क गर्नुहोस्। हाम्रो सेवा केन्द्रमा जानकारी यस लिंकमा फेला पार्न सकिन्छ: <a href = "http://vyccu.org.np/service-center">vyccu.org.np/service-centers</a>']
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return [SlotSet('type_of_services', None)]

class AboutSpecificService(Action):
    def name(self):
        return "action_about_specific_service"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        service_type = tracker.get_slot('type_of_services')
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            type_list = {
                "atm": "Dear Member, you can't register ATM services through online, we are adding many new exciting services soon. For ATM register please contact to your nearest <a href='http://vyccu.org.np/service-center'>Service Center</a>",
                "sms banking": "Dear Member, you can register SMS Banking service through our VYCCU Smart Banking Application. It is available on Play store and Apple store.",
                "deposit": "Dear Member, you can know about the deposit from this link <a href = 'http://vyccu.org.np/services/deposit'>Deposit Service</a>",
                "loan": "Dear Member, you can know about the loan from this link <a href = 'http://vyccu.org.np/services/loans'>Loan Service</a>",
                "remittance": "Dear Member, you can know about the remittance from this link <a href = 'http://vyccu.org.np/services/remittance'>Remittance Service</a>",
                "health insurance": "Dear Member, you can know about the health insurance from this link <a href = 'http://vyccu.org.np/services/health-insurance'>Health Insurance Service </a>",
                "mobile banking": "Dear Member, you can know about the mobile banking from this link <a href = 'http://vyccu.org.np/services/other-services'>Mobile Banking Service</a>",
            }
        else:
            type_list = {
                "atm": "तपाईं अनलाइन मार्फत एटीएम (ATM) सेवा दर्ता गर्न सक्नुहुन्न। एटीएम रेजिस्टरका लागि कृपया तपाईंको नजिकको सेवा केन्द्रमा (service center) सम्पर्क गर्नुहोस्। लिंक: <a href='http://vyccu.org.np/service-center'>Service Center</a>",
                "sms banking": " तपाईं हाम्रो विकु स्मार्ट बैंकिंग मार्फत SMS बैंकिंग सेवा दर्ता गर्न सक्नुहुन्छ। यो प्ले स्टोर र एप्पल स्टोरमा उपलब्ध छ।",
                "deposit": "तपाईं यो लिंक बाट डिपोजिट (Deposit) को बारेमा जान्न सक्नुहुन्छ: <a href = 'http://vyccu.org.np/services/deposit'>Deposit Service</a>",
                "loan": "तपाईं यो लिंक बाट ऋण (Loan) को बारेमा जान्न सक्नुहुन्छ: <a href = 'http://vyccu.org.np/services/loans'>Loan Service</a>",
                "remittance": "तपाईं यो लिंक बाट रेमिट्यान्स (Remittance) को बारेमा जान्न सक्नुहुन्छ: <a href = 'http://vyccu.org.np/services/remittance'>Remittance Service</a>",
                "health insurance": "तपाईं यो लिंक बाट स्वास्थ्य बीमा (Health Insurance) को बारेमा जान्न सक्नुहुन्छ: <a href = 'http://vyccu.org.np/services/health-insurance'>Health Insurance Service </a>",
                "mobile banking": "तपाईं यो लिंक बाट मोबाइल बैंकिंग (Mobile Banking) को बारेमा जान्न सक्नुहुन्छ: <a href = 'http://vyccu.org.np/services/other-services'>Mobile Banking Service</a>",
            }
        try:
            reply = type_list[service_type]
        except:
            messages = ["😕 Sorry, I cannot understand you. Could you repeat it again? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।", "😕 I am having confusion in understanding it. Would you repeat it please? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।",
                "😕 I find it quite ambiguous. Can you tell me again a bit clearly? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।"]
            reply = random.choice(messages)
            attachment = {
                "query_response": reply,
                "data":[],
                "type":"normal_message",
                "data_fetch_status": "success"
            }
            dispatcher.utter_message(attachment=attachment)
            return [UserUtteranceReverted()]
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return [SlotSet('type_of_services', None)]

class TypeOfSpecificService(Action):
    def name(self):
        return "action_type_of_specific_service"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        service_type = tracker.get_slot('type_of_services')
        question = tracker.latest_message['text']
        language_list = ["hi","ne","mr"]
        if detect(question) not in language_list:
            type_list = {
                "deposit": "The types of deposit can be found from this link <a href = 'http://vyccu.org.np/services/deposit'>Deposit Service</a>",
                "loan": "The various types of loan provided by us are: - <br>1. Agriculture Loan <br>2. Business Loan <br>3. Career Loan <br>4. Education Loan <br>5. Hire Purchase Loan <br>6. Home Loan <br>7. Industry Loan",
            }
        else:
            type_list = {
                "deposit": "यस लिन्कबाट डिपोजिट (Deposit) का प्रकारहरू बारे जन्न सकिन्छ। लिन्क: <a href = 'http://vyccu.org.np/services/deposit'>Deposit Service</a>",
                "loan": "हामीद्वारा प्रदान गरिएको ऋणका विभिन्न प्रकारहरू यस्ताछन: - <br>1. कृषि ऋण (Agriculture Loan) <br>2. व्यवसायिक ऋण (Business Loan) <br>3. क्यारियर ऋण (Career Loan) <br>4. शौक्षिक ऋण (Education Loan) <br>5. भाडा खरीद ऋण (Hire Purchase Loan) <br>6. घर सम्पती ऋण (Home Loan) <br>7. उद्योग ऋण (Industry Loan)",
            }
        try:
            reply = type_list[service_type]
        except:
            messages = ["😕 Sorry, I cannot understand you. We only have types of services for 'Deposit' and 'Loan'. Could you repeat it again? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला। हामीसँग 'डिपोजिट' र 'ऋण' को लागि मात्र सेवाहरू प्रकारहरू छन्।", "😕 I am having confusion in understanding it. We only have types of services for 'Deposit' and 'Loan'. Would you repeat it please? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला। हामीसँग 'डिपोजिट' र 'ऋण' को लागि मात्र सेवाहरू प्रकारहरू छन्।",
                "😕 I find it quite ambiguous. We only have types of services for 'Deposit' and 'Loan'. Can you tell me again a bit clearly? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला। हामीसँग 'डिपोजिट' र 'ऋण' को लागि मात्र सेवाहरू प्रकारहरू छन्।"]
            reply = random.choice(messages)
            attachment = {
                "query_response": reply,
                "data":[],
                "type":"normal_message",
                "data_fetch_status": "success"
            }
            dispatcher.utter_message(attachment=attachment)
            return [UserUtteranceReverted()]
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return [SlotSet('type_of_services', None)]

class EmailAddress(Action):
    def name(self):
        return "action_email_id"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            email_id = tracker.get_slot('email')
        except:
            messages = ["😕 Sorry, I cannot understand you. Could you repeat it again? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।", "😕 I am having confusion in understanding it. Would you repeat it please? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।",
                "😕 I find it quite ambiguous. Can you tell me again a bit clearly? <br>माफ गर्नुहोला। तपाईंले भनेको बुजिना। किर्पया फेरी एक पल्ट भन्नुहोला।"]
            reply = random.choice(messages)
            attachment = {
                "query_response": reply,
                "data":[],
                "type":"normal_message",
                "data_fetch_status": "success"
            }
            dispatcher.utter_message(attachment=attachment)
            return [UserUtteranceReverted()]
        messages = ["🙏 Thank you. We will contact you very soon. <br>धन्यवाद। हामी तपाईंलाई चाँडै सम्पर्क गर्नेछौं।","🙏 Thank you for giving us information. We will contact you soon. <br>धन्यवाद। हामी तपाईंलाई चाँडै सम्पर्क गर्नेछौं।"]      
        reply = random.choice(messages)
        attachment = {
            "query_response": reply,
            "data":[],
            "type":"normal_message",
            "data_fetch_status": "success"
        }
        dispatcher.utter_message(attachment=attachment)
        return [SlotSet('email', None)]