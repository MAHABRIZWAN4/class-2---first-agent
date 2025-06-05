from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
import asyncio
load_dotenv()
async def main():

    MODEL_NAME = "gemini-2.0-flash"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


    external_client = AsyncOpenAI(
        # Is ke under 2 Parameters aayein ge api_key And base_url 
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/", # ye url jo hum AsynOpenAI ke through hum jo client bana rahe hein wo use kare ga.. hum ye url is liye use ker rahe ke pata chale ke hum gemini use ker rahe hein 
        )
    

# OpenAIChatCompletionsModel ka use kiya gaya hai kyunki yeh AI model hai jo human-like text generate kar sakta hai, aur ismein Gemini 2.0 Flash model ka istemal kiya gaya hai jo fast aur efficient hai.
# Short mein: OAI-CCM use AI chat ke liye.
    model = OpenAIChatCompletionsModel(
        model=MODEL_NAME,
        openai_client=external_client
        )
    
#     To Remove this error : 
# OPENAI_API_KEY is not set, skipping trace export
    
    config  = RunConfig(
        model = model,
        model_provider=external_client,
        tracing_disabled=True
        )
    
    assistant = Agent(
        name = "Assistant",  # is ko parameter bolte hein
        instructions = "You job is to assist the user with their queries. You are a helpful assistant.",
        model=model,
        )
    

    user_input = input("Enter your query: ")  
    result = await Runner.run(assistant,user_input, run_config=config)


    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())  # Ye line main function ko asynchronous tarike se run karne ke liye hai, taki hum async functions ka istemal kar sakein. Ye Python mein concurrency aur parallelism ko handle karne ka ek tareeqa hai.













