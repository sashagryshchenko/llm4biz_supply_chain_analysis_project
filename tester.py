

# %%
import EnvSettings as settings
openai_key = settings.set_key()
###from openai import OpenAI
import Tech16FinalProject_supplychains as deb
from utils import *
deb.do_imports()
prompt = "find a car"
table_out = deb.gptrequest(prompt)
print(table_out)
answer = deb.supply_chain_summary()
print(answer)
deb.Environmental_Impacts()
deb.Supply_Chain_Elements_Comparison()

#result = refs.use_rag()
#print(result)

# %%
