## Greet Story
* greeting
    - action_greeting

## Goodbye Story
* goodbye
    - action_goodbye


## story2
* out_of_scope
    - action_out_of_scope

## interactive_story_1
* type_of_specific_service{"type_of_services": "loan"}
    - slot{"type_of_services": "loan"}
    - action_type_of_specific_service
    - slot{"type_of_services": null}
    - action_ask_want_loan
* affirm
    - action_show_type_of_loan
* about_specific_service{"type_of_loan": "education loan"}
    - slot{"type_of_loan": "education loan"}
    - action_fetch_type_of_loan
    - slot{"type_of_loan": null}

## interactive_story_1
* get_atm_card
    - action_get_atm_card
    - slot{"type_of_services": null}

## interactive_story_2
* location
    - action_location

## interactive_story_5
* open_account
    - action_ask_account_already_open
* affirm
    - action_account_already_exist

## interactive_story_6
* open_account
    - action_ask_account_already_open
* deny
    - action_create_account

## interactive_story_7
* contact
    - action_contact

## interactive_story_7
* about_service_center
    - action_about_service_center

## interactive_story_1
* about
    - action_about

## interactive_story_2
* services
    - action_show_type_of_services
* services{"type_of_services": "mobile banking"}
    - slot{"type_of_services": "mobile banking"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}

## interactive_story_1
* services
    - action_show_type_of_services
* about_specific_service{"type_of_services": "loan"}
    - slot{"type_of_services": "loan"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}
    - action_ask_want_loan
* affirm
    - action_show_type_of_loan
* about_specific_service{"type_of_loan": "business loan"}
    - slot{"type_of_loan": "business loan"}
    - action_fetch_type_of_loan
    - slot{"type_of_loan": null}

## interactive_story_1
* services
    - action_show_type_of_services
* services{"type_of_services": "atm"}
    - slot{"type_of_services": "atm"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}

## interactive_story_2
* about_specific_service{"type_of_services": "loan"}
    - slot{"type_of_services": "loan"}
    - action_show_type_of_loan
* about_specific_service{"type_of_loan": "education loan"}
    - slot{"type_of_loan": "education loan"}
    - action_fetch_type_of_loan
    - slot{"type_of_loan": null}

## interactive_story_1
* about_specific_service{"type_of_services": "mobile banking"}
    - slot{"type_of_services": "mobile banking"}
    - action_about_specific_service
    - slot{"type_of_services": null}
* about_specific_service{"type_of_services": "sms banking"}
    - slot{"type_of_services": "sms banking"}
    - action_about_specific_service
    - slot{"type_of_services": null}

## interactive_story_2
* type_of_specific_service{"type_of_services": "loan"}
    - slot{"type_of_services": "loan"}
    - action_type_of_specific_service
    - slot{"type_of_services": null}
    - action_ask_want_loan
* affirm
    - action_show_type_of_loan
* about_specific_service{"type_of_loan": "career loan"}
    - slot{"type_of_loan": "career loan"}
    - action_fetch_type_of_loan
    - slot{"type_of_loan": null}

## interactive_story_1
* type_of_specific_service{"type_of_services": "deposit"}
    - slot{"type_of_services": "deposit"}
    - action_type_of_specific_service
    - slot{"type_of_services": null}

## interactive_story_1
* services
    - action_show_type_of_services
* about_specific_service{"type_of_services": "loan"}
    - slot{"type_of_services": "loan"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}
    - action_ask_want_loan
* deny
    - action_no

## interactive_story_2
* services
    - action_show_type_of_services
* about_specific_service{"type_of_services": "loan"}
    - slot{"type_of_services": "loan"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}
    - action_ask_want_loan
* affirm
    - action_show_type_of_loan
* about_specific_service{"type_of_loan": "education loan"}
    - slot{"type_of_loan": "education loan"}
    - action_fetch_type_of_loan
    - slot{"type_of_loan": null}

## interactive_story_3
* type_of_specific_service{"type_of_services": "loan"}
    - slot{"type_of_services": "loan"}
    - action_type_of_specific_service
    - slot{"type_of_services": null}
    - action_ask_want_loan
* deny
    - action_no

## interactive_story_4
* type_of_specific_service{"type_of_services": "loan"}
    - slot{"type_of_services": "loan"}
    - action_type_of_specific_service
    - slot{"type_of_services": null}
    - action_ask_want_loan
* affirm
    - action_show_type_of_loan
* about_specific_service{"type_of_loan": "industry loan"}
    - slot{"type_of_loan": "industry loan"}
    - action_fetch_type_of_loan
    - slot{"type_of_loan": null}

## interactive_story_5
* interest_rate
    - action_show_type_of_interest
* interest_rate{"type_of_services": "rate loan"}
    - slot{"type_of_services": "rate loan"}
    - action_fetch_type_of_interest
    - slot{"type_of_services": null}

## interactive_story_6
* interest_rate
    - action_show_type_of_interest
* interest_rate{"type_of_services": "deposit"}
    - slot{"type_of_services": "deposit"}
    - action_fetch_type_of_interest
    - slot{"type_of_services": null}

## interactive_story_7
* interest_rate{"type_of_services": "deposit"}
    - slot{"type_of_services": "deposit"}
    - action_fetch_type_of_interest
    - slot{"type_of_services": null}

## interactive_story_8
* interest_rate{"type_of_services": "loan"}
    - slot{"type_of_services": "loan"}
    - action_fetch_type_of_interest
    - slot{"type_of_services": null}

## interactive_story_1
* services
    - action_show_type_of_services
* services{"type_of_services": "atm"}
    - slot{"type_of_services": "atm"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}

## interactive_story_2
* services
    - action_show_type_of_services
* services{"type_of_services": "sms banking"}
    - slot{"type_of_services": "sms banking"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}

## interactive_story_3
* services
    - action_show_type_of_services
* services{"type_of_services": "mobile banking"}
    - slot{"type_of_services": "mobile banking"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}

## interactive_story_4
* services
    - action_show_type_of_services
* about_specific_service{"type_of_services": "remittance"}
    - slot{"type_of_services": "remittance"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}

## interactive_story_5
* services
    - action_show_type_of_services
* services{"type_of_services": "health insurance"}
    - slot{"type_of_services": "health insurance"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}

## interactive_story_6
* services
    - action_show_type_of_services
* about_specific_service{"type_of_services": "loan"}
    - slot{"type_of_services": "loan"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}
    - action_ask_want_loan
* deny
    - action_no

## interactive_story_7
* services
    - action_show_type_of_services
* services{"type_of_services": "deposit"}
    - slot{"type_of_services": "deposit"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}


## interactive_story_1
* services
    - action_show_type_of_services
* services{"type_of_services": "deposit"}
    - slot{"type_of_services": "deposit"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}

## interactive_story_2
* services
    - action_show_type_of_services
* services{"type_of_services": "other services"}
    - slot{"type_of_services": "other services"}
    - action_fetch_type_of_services
    - slot{"type_of_services": null}
