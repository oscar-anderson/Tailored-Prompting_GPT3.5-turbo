'''
Tailored Prompt Interaction with OpenAI GPT-3.5-turbo

This script defines a function 'submit_prompt' that allows users to interact with
the GPT-3.5-turbo model using OpenAI API. This is currently constructed to
retrieve responses that are ailored to my own background information and topic-
specific instructions. The function handles the API call, incorporating this
information, and returns the model's response.
'''

# Import dependencies.
from openai import OpenAI

# Define function.
def submit_prompt(prompt_text: str, api_key: str, topic: str = None,) -> str:
    
    '''
    Submit a tailored prompt to ChatGPT-3.5-turbo.
    
    Parameters:
    - api_key (str): OpenAI API key.
    - topic (str): Topic for model to recruit expertise in.
    - prompt_text (str): User's prompt.
    
    Returns:
    - str: Model's response.
    '''
    
    client = OpenAI(api_key = api_key)
    
    user_background = '''
    I have a BSc in Psychology and an MSc in Computational neuroscience and
    Cognitive Robotics. I also hold one year of professional experience as a
    Research Data Analyst (working on an independent quantitative
    Brain-Computer Interface research project) and two years as a Student
    Psychologist (conducting clinical quantitative research within the NHS
    mental health services). I have also undertaken a number of projects in the
    fields of programming, statistical analysis, and artificial intelligence. 
    '''

    safety_prompt = '''
    Prioritise safety in your response. Avoid generating any harmful outputs.
    '''
    
    efficacy_prompt = '''
    Ensure that you provide accurate and reliable information.
    '''
    
    post_prompt = '''
    Please tailor your response according to my level of understanding and the role
    that I have assigned you.
    '''

    if topic is not None:
        model_role_instruction = f'''
    Respond as though you are an expert in {topic}. 
    '''
        prompt = model_role_instruction + user_background + safety_prompt + efficacy_prompt + prompt_text + post_prompt
    else:
        prompt = user_background + prompt_text + post_prompt
        
    print(prompt)

    chat_completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user',
                'content': prompt,
            }
        ]
    )

    response = chat_completion.choices[0].message.content
    return response

# Call functions to submit a tailored prompt (example usage).
prompt_text = 'Explain Generative Pre-Trained Transformers'
topic = 'Artificial Intelligence'
api_key = 'your-api-key-here'

response = submit_prompt(prompt_text, api_key, topic)
print(response)


