
## add a seperate fillow up question per question as lel 9 asking to eloberate 0 tracking that too!



import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, Form, Response
import logging
from uuid import uuid4

cred = credentials.Certificate('../../firebase.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# FastAPI app initialization
#app = FastAPI()


# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# def initialize_event_collection(event_id, event_name, event_location, event_background, event_date, extraction_settings, bot_topic, bot_aim, bot_principles, bot_personality, bot_additional_prompts, questions, languages):
#     """Initializes the Firestore collection and stores event info, bot settings, and survey questions within the 'info' document."""
#     collection_ref = db.collection(f'AOI_{event_id}')
#     info_doc_ref = collection_ref.document('info')
    
#     # Assign unique IDs to each question and format them into a dictionary
#     formatted_questions = []
#     for idx, question in enumerate(questions):
#         formatted_questions.append({
#             "id": idx,  # Assign a unique ID (index) to each question
#             "text": question,
#             "asked_count": 0
#         })
    
#     # Set the main event info in the 'info' document along with extraction settings, bot configuration, and languages
#     info_doc_ref.set({
#         'event_initialized': True,
#         'event_name': event_name,
#         'event_location': event_location,
#         'event_background': event_background,
#         'event_date': event_date,
#         'welcome_message': f"Welcome to the {event_name} at {event_location}. You can now start sending text and audio messages. To change your name, type 'change name [new name]'. To change your event, type 'change event [event name]'.",
#         'extraction_settings': extraction_settings,
#         'bot_topic': bot_topic,
#         'bot_aim': bot_aim,
#         'bot_principles': bot_principles,
#         'bot_personality': bot_personality,
#         'bot_additional_prompts': bot_additional_prompts,
#         'languages': languages,
#         'questions': formatted_questions  # Each question has "id", "text", and "asked_count"
#     })
    
#     logger.info(f"Event '{event_name}' initialized with {len(questions)} questions.")


def initialize_event_collection(event_id, event_name, event_location, event_background, event_date, extraction_settings, bot_topic, bot_aim, bot_principles, bot_personality, bot_additional_prompts, questions, languages, initial_message, completion_message):
    """Initializes the Firestore collection and stores event info, bot settings, and survey questions within the 'info' document."""
    collection_ref = db.collection(f'AOI_{event_id}')
    info_doc_ref = collection_ref.document('info')
    
    # Assign unique IDs to each question and format them into a dictionary
    formatted_questions = []
    for idx, question in enumerate(questions):
        formatted_questions.append({
            "id": idx,  # Assign a unique ID (index) to each question
            "text": question,
            "asked_count": 0
        })
    
    # Set the main event info in the 'info' document along with extraction settings, bot configuration, and languages
    info_doc_ref.set({
        'event_initialized': True,
        'event_name': event_name,
        'event_location': event_location,
        'event_background': event_background,
        'event_date': event_date,
        'welcome_message': f"Welcome to the {event_name} at {event_location}. You can now start sending text and audio messages. To change your name, type 'change name [new name]'. To change your event, type 'change event [event name]'.",
        'initial_message': initial_message,
        'completion_message': completion_message,
        'extraction_settings': extraction_settings,
        'bot_topic': bot_topic,
        'bot_aim': bot_aim,
        'bot_principles': bot_principles,
        'bot_personality': bot_personality,
        'bot_additional_prompts': bot_additional_prompts,
        'languages': languages,
        'questions': formatted_questions  # Each question has "id", "text", and "asked_count"
    })
    
    logger.info(f"Event '{event_name}' initialized with {len(questions)} questions.")




# Define event details and survey questions
event_id = "CGAI_Studnet165"
event_name = "CGAI Student Ambassadors"
event_location = "United States"
event_background = "A survey exploring the experiences and of student working with AI in college"
event_date = "2024-12-01"
extraction_settings = {
    "name_extraction": True,
    "age_extraction": False,
    "gender_extraction": False,
    "region_extraction": False
}
bot_topic = "Experiences and challenges of working with AI tools in College"
bot_aim = "To gather insights on the unique challenges and o."
bot_principles = [
    "Maintain an open and non-judgmental tone",
    "Respect privacy and confidentiality",
    "Encourage honest and thoughtful responses"
]
bot_personality = "Empathetic, supportive, and respectful"
bot_additional_prompts = [
    #How can your workplace better support LBQ+ individuals?"
]
languages = ["English"]  # Specify the main languages for this event

# Define the list of questions (English versions)
questions = [
    "How has AI changed the way you approach learning, studying, or completing assignments?",
    "What skills do you think students still need to develop on their own—even if AI tools can do the task faster or better?",
    "How do you feel when a classmate uses AI to complete an assignment—does it change how you view collaboration or fairness?",
    "How should professors adapt their teaching or assignments in response to AI tools like ChatGPT?",
    "What rules or values should guide AI use in college?",
    "What do you think future employers will expect from students who grew up using AI tools in college?",
    "What opportunities do you see for AI to improve your college experience—beyond just writing essays or solving problems?",    
]



# Define the initial and completion messages
initial_message = """Thank you for agreeing to participate. We want to assure you that none of the data you provide will be directly linked back to you. Your identity is protected through secure and encrypted links. Please enter your name"""

completion_message = """Congratulations, you’ve completed the survey! Thank you so much for taking the time to share your experiences. If you have any questions, concerns, or feedback, please don’t hesitate to contact us. Your voice matters, and we deeply appreciate your participation."""

# Initialize the event with questions and messages
initialize_event_collection(
    event_id,
    event_name,
    event_location,
    event_background,
    event_date,
    extraction_settings,
    bot_topic,
    bot_aim,
    bot_principles,
    bot_personality,
    bot_additional_prompts,
    questions,
    languages,
    initial_message,      # Add this line
    completion_message    # Add this line
)
