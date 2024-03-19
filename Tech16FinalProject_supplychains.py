
# %% [markdown]
# Final Project-David Brown version

# %%
def gptrequest(prompt):
  import EnvSettings as settings
  openai_key = settings.set_key()
  from openai import OpenAI
  client = OpenAI(api_key=openai_key)
  response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": "You are an AI that takes instructions from a human and produces an answer. Be concise in your output."},
        {"role": "user", "content": prompt},
    ]
  )
  print("\n\n prompt:  " + prompt)
  return response

# %%
def do_imports():  # imports and keys
  from openai import OpenAI
  import os
  import matplotlib.pyplot as plt
  ###import exploring_materials_needed as materials
  import EnvSettings as envsettings
  ###import final_project_tech16_llm_john_part as refs
  ###for k, v in os.environ.items():
          ###print(f'{k}={v}')
  import textwrap
  import pandas as pd
  from pandasai import SmartDatalake
  from pandasai.llm import OpenAI
  df = pd
# %%
def supply_chain_summary():
  prompt = ""
  print("\n\nSupply Chain Summary Fuel Cells =================================================\n")
  prompt = "Summarize Supply Chain impacts of Fuel Cell Cars"

  response = gptrequest(prompt)
  table_out = response.choices[0].message.content
  print(table_out)
  df = table_out
  print("Count:=========================  " )
  print(df.count)
  print(df)
  return(table_out)


# %%
def Supply_Chain_Summary_Electric():
  print("\n\nSupply Chain Summary Electric Cars=================================================\n")
  prompt = "Summarize Supply Chain impacts of Electric cars"
  print("\n\n prompt:  " + prompt)
  response = gptrequest(prompt)
  table_out = response.choices[0].message.content
  print(table_out)
  print("\n\nFirst Question Supply Chain Comparison =================================================\n")
  prompt = "create a table of a comparison between supply chain impacts of fuel cell cars vs electric vehicles"
  print("\n\n prompt:  " + prompt)
  response = gptrequest(prompt)
  table_out = response.choices[0].message.content
  print(table_out)

# %%
def Environmental_Impacts():
  print("\n\nSecond Question Environmental Impact Comparison =================================================\n")
  prompt = "create a table of a comparison between environmental impacts of fuel cell cars vs electric vehicles"
  ###prompt = "create a table in JSON format of a comparison between environmental impacts of fuel cell cars vs electric vehicles"
  print("\n\n prompt:  " + prompt)
  response = gptrequest(prompt)
  table_out = response.choices[0].message.content
  print(table_out)
  from pandasai import SmartDataframe
  from pandasai.llm import OpenAI
  sdf = SmartDataframe
  df = pd.DataFrame(response)
  ###df.plot(x='fuelCellCars', y='electricVehicles', kind='scatter')
  ###df.sort_values(by=['aspect'], inplace=True)
  ###plt.show()
  ###print("\n\nDataframe print=========================  \n\n" )
  ###print(df)

# %%
def Supply_Chain_Elements_Comparison():  
  print("\n\nThird Question Supply chain element Comparison =================================================\n")
  prompt = "create a table of a comparison between Manufacturing Process of fuel cell cars vs electric vehicles"
  print("\n\n prompt:  " + prompt)
  response = gptrequest(prompt)

  table_out = response.choices[0].message.content
  ###print(table_out)
  from pandasai import SmartDataframe
  from pandasai.llm import OpenAI

  df = pd.DataFrame(response)
  from pandasai import SmartDataframe
  from pandasai.llm import OpenAI
  sdf = SmartDataframe
  df = pd.DataFrame(response)
  print(table_out)