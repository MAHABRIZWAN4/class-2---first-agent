
AI AGENT :
Basically AI AGENT hai decision leta hai Hum biryani banate hain aur robot  banata hai Agar biryani jhal jaati hai to insan ke pass kya hota hai brain hota hai ki usko nikal kar saaf use ko sarve kar dena lekin robot ki under programming Nahin Hoti ki woh itna decision nahi Le sakta Lekin AI agent jo hai  yah kam kar sakta hai theek hai jaise insan ke pass brain hota hai wese AI Agent ke pass LLM hota he .LLM hum hum backend per use kerke fornted apni bana ker apna chatgpt bana sakte hein
 


Installation:
Step 1 :  
pip install openai-agents "openai-agents[litellm]"
liteLLM hum gemini ko connect kerne ke liye kerte hein

Step 2: Work Related to Gemini

MODEL_NAME = "gemini/gemini-2.0-flash"
Mujhe gemini use kerne ke liye gemini api key chhaiye hogi
Go the secrets on google colab 
go Gemini Keys > Manage
Click on Create Api keys button 
Then choose the name
copy the secret key 
Again open the secrets on google colab 
Click on ADD NEW SECRET then name and add secret key in it



Step 3 ==> import
from google.colab import userdata
API_KEY = userdata.get("GEMINI_API_KEY")

Step 4 ==> How to make an agent
from agents import Agent,Runner
from agents.extensions.models.litellm_model import LitellmModel
import asyncio

Assistant = Agent( # ye class hai
    name = "Assistant",  # is ko parameter bolte hein
    instructions = "You are a helpful assistant.",
    model = LitellmModel(
        model = MODEL_NAME,
        api_key = API_KEY,
    ),
    # ye mene is is liye kiya taake mera LLM Model Gemini gemini ka use kersake is liye LitellmModel ko import karein ge agar ye bhool gai import kerne  wali itni bari line to hum documentation me se dekh lein ge ## https://openai.github.io/openai-agents-python/models/litellm/
)
# Ye Agent bun gaya he chala nahi he chalane ke liye Runner import karein ge

async def main():
  result = await Runner.run(starting_agent = Assistant,input = "Hello, How are you?") # ye ek function hai is ke under 2 cheezein pass hongi
  print(result.final_output) # agar hamin llm ka agent ka final answer he wo chahyie to wo hamein final_output me mile ga

asyncio.run(main())





ABB COLAB ME NAHI CHUL RAHA LITELLM ME ERROR ARAHA HE TO UV SE VSCODE ME KERTE HEIN : 
STEP 1 ==> UV install
uv init project-name

Step 2 ==> packages and dependencies install
uv add openai-agents
.venv\Scripts\activate

STEP 3 ==> 

MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = "AIzaSyAecsrrwh88cflsLiwae-aBReg_r6LcsUY" is ko .env ke under daalein ge 
ABB ENV SE KEY LANE KE LYE HAMEIN UV KA PACKAGE INSTALL KERNA HE PHIR LOAD KEREIN GE
uv add dotenv
from dotenv import load_dotenv

load_dotenv() ye karein ge load func call 

abb hamari env os me hoti he to  os import
import os
Then env se GEMINI_API_KEY get karein ge aise
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


Step 4  =======> How to make an external client
Abb hum external client banyein ge jis ke liye AsyncAI package ka use karein ge or wo hamein agents SDK provide kerta he
Ye jo hamara Lite LLM wala part hai us ko hum ne AsynopenAI(AsyncopenAI ka jo client hai external client ) se replace kiya  abb us ke through hum pura agent ko banayein ge

from agents import AsyncOpenAI

 exteral_client = AsyncOpenAI(
        # Is ke under 2 Parameters aayein ge api_key And base_url 
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/", # ye url jo hum AsynOpenAI ke through hum jo client bana rahe hein wo use kare ga.. hum ye url is liye use ker rahe ke pata chle ke hum gemini use ker rahe hein 
)



Step 5 ===========> model
from agents import AsyncOpenAI, OpenAIChatCompletionsModel



# OpenAIChatCompletionsModel ka use kiya gaya hai kyunki yeh AI model hai jo human-like text generate kar sakta hai, aur ismein Gemini 2.0 Flash model ka istemal kiya gaya hai jo fast aur efficient hai.

# Short mein: OAI-CCM use AI chat ke liye.


    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
)



Step 6 ===========> How to make an Agent

Assistant = Agent( # ye class hai
    name = "Assistant",  # is ko parameter bolte hein
    instructions = "You job is to assist the user with their queries. You are a helpful assistant.",
    model=model,
    )


Step 7 ================> Abb is agent ko run karein ge With the help of Runner

 result = Runner.run_sync(assistant,"Tell me something interesting about Pakistan")

 print(result.final_output)

LITELLM KE BAGHIR JO HAMEIN AGENT BANANA THA WO BANA LIYA HE 
__________________________THE END__________________________



ABB IS ME EK CHOTA SA ISSUE HOGA ke agar mutgltiple agents ko chalana hoto synchronous work nahi kare ga asynchronous kerna pare ga US KO FIX KERNE KE ASYNCHRONOUS PROCESSING KO IMPLEMENT KERKE 
OR WO KESI HOTI HE 


STEP 1  ============> import asyncio
import asyncio
await Running run
asyncio.run(main()) 

__________________________THE END__________________________


To Remove this error : 
OPENAI_API_KEY is not set, skipping trace export
 config  = RunConfig(
        model = model,
        model_provider=external_client,
        tracing_disabled=True
        )

    result = await Runner.run(assistant,"Tell me something about minar-e-pakistan", run_config=config)













