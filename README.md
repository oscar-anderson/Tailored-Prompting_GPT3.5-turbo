# Tailored Prompt Interaction with OpenAI GPT-3.5-turbo

This Python script provides a convenient way to interact with the OpenAI GPT-3.5-turbo model using the OpenAI API. The `submit_prompt` function allows users to submit prompts tailored to their background information and specific topic instructions, receiving responses from the model accordingly. Speciically, this script is currently constructed to allow me to interact with OpenAI's GPT-3.5 turbo and receive responses that prioritise relevance, safety and account for my own specific level of understanding/area of expertise.

## Prerequisites

Before using this script, make sure that you have the following:

- OpenAI API key: You can obtain your API key by signing up on the [OpenAI website](https://beta.openai.com/signup/).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Install the required dependencies:

    ```bash
    pip install openai
    ```

## Usage

1. Open the script file (`prompt_gpt3.5.py`) and replace `'your-api-key'` with your actual OpenAI API key.

2. You can customise the `api_key`, `prompt_text` and `topic` variables within the script, to fit your requirements.

3. Run the script:

    ```bash
    python prompt_gpt3.5.py.py
    ```

4. The model's response will be printed to the console.

## Function Parameters

- `api_key` (str): Your OpenAI API key.
- `prompt_text` (str): The user's prompt for the model.
- `topic` (str, optional): The topic for the model to recruit expertise in.

## Additional Information

The `submit_prompt` function incorporates specific information about your background and safety/efficacy prompts to guide the model's responses. You can customise these prompts within the function based on your preferences.

Note: Ensure that you follow OpenAI's usage policies and guidelines when interacting with the GPT-3.5-turbo model.

## Example

Here's an example usage of the script:

```python
api_key = 'your-api-key'
prompt_text = 'Explain Generative Pre-Trained Transformers'
topic = 'Artificial Intelligence'

response = submit_prompt(api_key, prompt_text, topic)
print(response)
