
# %%
import EnvSettings as settings
openai_key = settings.set_key()
###from openai import OpenAI
import Tech16FinalProject_supplychains as deb
import Visualizations as vis
import FileReferences as john
from utils import *  
deb.do_imports()
prompt = "find a car"
table_out = deb.gptrequest(prompt)
print(table_out)
answer = deb.supply_chain_summary()
print(answer)
deb.Environmental_Impacts()
print("\n\nSupply_Chain_Elements_Comparison")
deb.Supply_Chain_Elements_Comparison()

### Visualizationsfrom Beenish
# %%
import EnvSettings as settings
openai_key = settings.set_key()
import Visualizations as vis
from utils import *
vis.visImports()
vis.plotResults()
vis.envireImpactComparison()
vis.efficiencyComparison()
vis.envireImpactElementsComparison
vis.supplyChainComparison
vis.suppyChainElementComparison
### test johns
# %%
import FileReferences as john
import EnvSettings as settings
openai_key = settings.set_key()
john.filesRefs()

# %%
