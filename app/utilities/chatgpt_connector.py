import openai

class ChatGPTConnector:
    def __init__(self):
        # Initialize OpenAI API client with your API key
        self.api_key = "YOUR_API_KEY"  # Replace with your actual API key
        openai.api_key = self.api_key

    def generate_response(self, input_text, max_tokens=50):
        """
        Generate a response from the ChatGPT model.

        Args:
            input_text (str): The user's input text.
            max_tokens (int): The maximum number of tokens in the response.

        Returns:
            str: The generated response.
        """
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt=input_text,
                max_tokens=max_tokens,
                temperature=0.7,  # Adjust the temperature for different levels of randomness
                stop=None,  # You can specify a list of strings to stop generation
            )
            return response.choices[0].text.strip()
        except Exception as e:
            # Handle any exceptions that may occur during API request
            return str(e)