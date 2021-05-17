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

class ActionShowTypeOfLoan(Action):
	def name(self):
		return 'action_show_type_of_loan'
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
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
		attachment = {
			"query_response": reply,
			"data":[{"buttons":buttons}],
			"type":"message_with_buttons",
			"data_fetch_status": "success"
		}
		# dispatcher.utter_message(attachment=attachment, quick_replies=buttons)
		dispatcher.utter_message(attachment=attachment)
		return []


class FetchTypeOfLoan(Action):
	def name(self):
		return 'action_fetch_type_of_loan'

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		try:
			loan_type = tracker.get_slot('type_of_loan')
		except:
			messages = ["Sorry, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it. Would you repeat it please?",
				"I find it quite ambiguous. Can you tell me again a bit clearly?"]
			reply = random.choice(messages)
			attachment = {
				"query_response": reply,
				"data":[],
				"type":"normal_message",
				"data_fetch_status": "success"
			}
			dispatcher.utter_message(attachment=attachment)
			return [UserUtteranceReverted()]
		
		loan_link = "<a href = 'http://vyccu.org.np/services/loans'>loan</a>"
		reply = f"VYCCU Savings and Credit Cooperative Ltd provides attractive {loan_type} . You can get more info on {loan_type} from {loan_link}"
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
		attachment = {
			"query_response": reply,
			"data":[{"buttons":buttons}],
			"type":"message_with_buttons",
			"data_fetch_status": "success"
		}
		# dispatcher.utter_message(attachment=attachment, quick_replies=buttons)
		dispatcher.utter_message(attachment=attachment)
		return []

class FetchTypeOfServices(Action):
	def name(self):
		return 'action_fetch_type_of_services'

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		service_type = tracker.get_slot('type_of_services')
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
		try:
			service_link = type_list[service_type]
		except:
			messages = ["Sorry, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it. Would you repeat it please?",
				"I find it quite ambiguous. Can you tell me again a bit clearly?"]
			reply = random.choice(messages)
			attachment = {
				"query_response": reply,
				"data":[],
				"type":"normal_message",
				"data_fetch_status": "success"
			}
			dispatcher.utter_message(attachment=attachment)
			return [UserUtteranceReverted()]

		reply = "Oh you want to get {}. We are happy to serve you. Learn more about {} from {} ".format(service_type,service_type,service_link)
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
		reply = "Interest rate varies for following services"
		buttons = [{'title': 'Loan',
				   'payload': '{}'.format('rate loan')},
				  {'title': 'Deposit',
				   'payload': '{}'.format('rate deposit')}   
				   ]
		attachment = {
			"query_response": reply,
			"data":[{"buttons":buttons}],
			"type":"message_with_buttons",
			"data_fetch_status": "success"
		}
		# dispatcher.utter_message(attachment=attachment, quick_replies=buttons)
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
			messages = ["Sorry, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it. Would you repeat it please?",
				"I find it quite ambiguous. Can you tell me again a bit clearly?"]
			reply = random.choice(messages)
			attachment = {
				"query_response": reply,
				"data":[],
				"type":"normal_message",
				"data_fetch_status": "success"
			}
			dispatcher.utter_message(attachment=attachment)
			return [UserUtteranceReverted()]
		
		reply = "Oh, you want to check interest rate for {}. Get detailed information about our interest rates at <a href='http://vyccu.org.np/interest-rates/'>Interest Rate</a>".format(interest_type)
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
		messages = ['VYCCU Savings and Credit Cooperative Limited is a primary-level single-purpose cooperative organization . You can get more info on <a href = "http://vyccu.org.np/category/our-profile-2">vyccu.org.np/our-profile</a>']
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
		messages = ['Sorry I didn’t catch that word? Could you tell me more clearly?',
					'I am sorry I did not understand? Can you tell again?']
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
		messages = ['We are sorry for not being able to understand you. Could you provide us with one of your contact number so that we could help you properly?',
					"Sorry, I don't think I can help you. Can you give us one of your contant detail so that we could help you properly?"]
		buttons = [
			{"title":"Email Address", "payload":"/form_email"},
			{"title":"Contact Number", "payload":"/form_contact"}
		]
		reply = random.choice(messages)
		attachment = {
			"query_response": reply,
			"data":[{"buttons":buttons}],
			"type":"message_with_buttons",
			"data_fetch_status": "success"
		}
		# dispatcher.utter_message(attachment=attachment,quick_replies=buttons)
		dispatcher.utter_message(attachment=attachment)
		return []

class AskFirstName(Action):
	def name(self):
		return "action_ask_first_name"

	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ['Please give your First name',
					'Provide us your First name']
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
		messages = ['Please give your Last name',
					'Provide us your Last name']
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
		messages = ['Please give your contact number',
					'Provide us your contact number']
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
		messages = ['Please give your email',
					'Provide us your email']
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
			messages = [f'Thank you {f_name} {l_name}. Your form has been submitted successfully. We will contact you very soon.',
						f'Thank you {f_name} {l_name} for your information. We will contact you as soon as possible.']
		else:
			messages = ['Thank you. Your form has been submitted successfully. We will contact you very soon.',
						'Thank you for your information. We will contact you as soon as possible.']
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
		messages = ["Hi there. It's such a pleasure to have you here. Welcome to VYCCU saving and credit co-operative Ltd. How can we help you.",
					"Hello, welcome to VYCCU saving and credit co-operative Ltd. How can we assist you."]
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
		messages = ["I am fine. How can we help you.",
					"I am doing very well. How can we assist you."]
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
		messages = ['Thank you, I am happy to help you. For more details about us please visit our website <a href="http://vyccu.org.np">vyccu.org.np</a>',
					'I hope I was helpful for you. To know more about us you can visit our website <a href="http://vyccu.org.np">vyccu.org.np</a>']
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
		messages = ['VYCCU Savings and Credit Cooperative Limited is located in Bijaynagar, Gaindakot-05, Nawalpur. Folllow us at google maps <a href="https://www.google.com/maps/dir//27.7015019,84.3871719/@27.701502,84.387172,17z?hl=en-US">maps</a>',
					'You can visit us at Bijaynagar, Gaindakot-05, Nawalpur. Follow us at google maps <a href="https://www.google.com/maps/dir//27.7015019,84.3871719/@27.701502,84.387172,17z?hl=en-US">maps</a>']
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
		messages = ['To know more about us and our services, follow us at <a href="http://vyccu.org.np/contact-us/">vyccu.org.np/contact</a> \nEmail:vyccu@vyccu.org.np \nHead Office Bijaynagar, Gaindakot-05, Nawalpur \nPhone: 078-502601, 078-501364, 078-503162, 078-503104 \nPlease provide us with your following details so that we can contact you further.']
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
		messages = ['We have 11 service centers. You can get more info on service centers from <a href = "http://vyccu.org.np/service-center">vyccu.org.np/service-centers</a>',
					'The information about our service centers can be found in this link: <a href = "http://vyccu.org.np/service-center">vyccu.org.np/service-centers</a>']
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
		messages = ["Do you have a saving account with VYCCU saving and credit co-operative Ltd.?"]
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
		messages = ["Dear customer, as you are already an existing customer of VYCCU saving and credit co-operative Ltd. You cannot open a new account with us as per local regulations. We will keep you posted here as we are adding many new exciting services soon.",
					"Sir, since an account on your name already exist in VYCCU saving and credit co-operative Ltd. we cannot create a new account for you."]
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
		messages = ["Ok, now lets create an account for you."]
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
		reply = "Do you want to take Loan?"
		buttons = [{'title': 'Yes',
				   'payload': '{}'.format('yes')},
				  {'title': 'No',
				   'payload': '{}'.format('no')},   
				   ]
		attachment = {
			"query_response": reply,
			"data":[{"buttons":buttons}],
			"type":"message_with_buttons",
			"data_fetch_status": "success"
		}
		# dispatcher.utter_message(attachment=attachment,quick_replies=buttons)
		dispatcher.utter_message(attachment=attachment)
		return []

class AfterNo(Action):
	def name(self):
		return "action_no"
	
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		messages = ["Ok sir. Are there any ways in which we can help you?","Ok sir. Is there anything more you want to know?"]
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
		messages = ['Please contact to your nearest Service center to get your ATM card. The information on our service center can be found in this link: <a href = "http://vyccu.org.np/service-center">vyccu.org.np/service-centers</a>']
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
		type_list = {
			"atm": "Dear Member, you can't register ATM services through online, we are adding many new exciting services soon. For ATM register please contact to your nearest <a href='http://vyccu.org.np/service-center'>Service Center</a>",
			"sms banking": "Dear Member, you can register SMS Banking service through our VYCCU Smart Banking Application. It is available on Play store and Apple store.",
			"deposit": "Dear Member, you can know about the deposit from this link <a href = 'http://vyccu.org.np/services/deposit'>Deposit Service</a>",
			"loan": "Dear Member, you can know about the loan from this link <a href = 'http://vyccu.org.np/services/loans'>Loan Service</a>",
			"remittance": "Dear Member, you can know about the remittance from this link <a href = 'http://vyccu.org.np/services/remittance'>Remittance Service</a>",
			"health insurance": "Dear Member, you can know about the health insurance from this link <a href = 'http://vyccu.org.np/services/health-insurance'>Health Insurance Service </a>",
			"mobile banking": "Dear Member, you can know about the mobile banking from this link <a href = 'http://vyccu.org.np/services/other-services'>Mobile Banking Service</a>",
		}
		try:
			reply = type_list[service_type]
		except:
			messages = ["Sorry, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it. Would you repeat it please?",
				"I find it quite ambiguous. Can you tell me again a bit clearly?"]
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
		type_list = {
			"deposit": "The types of deposit can be found from this link <a href = 'http://vyccu.org.np/services/deposit'>Deposit Service</a>",
			"loan": "The various types of loan provided by us are: - \n1. Agriculture Loan \n2. Business Loan \n3. Career Loan \n4. Education Loan \n5. Hire Purchase Loan \n6. Home Loan \n7. Industry Loan",
		}
		try:
			reply = type_list[service_type]
		except:
			messages = ["Sorry, I cannot understand you. Could you repeat it again?", "I am having confusion in understanding it. Would you repeat it please?",
				"I find it quite ambiguous. Can you tell me again a bit clearly?"]
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