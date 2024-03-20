# %%
def asynchApply():
    
    #chatbots apparently need it https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/chatbots/building_a_chatbot.html
    import nest_asyncio
    nest_asyncio.apply()

# %% [markdown]

def ragBatterHydrogen():
    # # Retrieval Augmented Generation - Battery vs. Hydrogen Fuel Cell Comparison Documents
    #https://pypi.org/project/pypdf/
    # Vector Storage
    print("ragBatteryHydrogen")

# %%
def getIndex():
    #Class 5 and
    #https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/examples/agent/openai_agent_with_query_engine.ipynb
    #see below
    try:
        storage_context = StorageContext.from_defaults(
            persist_dir="./storage/ev_vec_idx"
        )
        index = load_index_from_storage(storage_context)

        index_loaded = True
    except:
        index_loaded = False
    return index_loaded

# %% [markdown]
def listArticles():
    import os
    print("listArticles")
    # #Articles to get (I get and save these together in one folder. I didn't see a reason to separate out like in the lyft vs. uber example)

    # 1.	Brian D. James, Jennie M. Huya-Kouadio, Cassidy Houchins, Daniel A. DeSantis, Mass Production Cost Estimation of Direct H2 PEM Fuel Cell Systems for Transportation Applications: 2018 Update, December 2018 (DOE grant) https://www.energy.gov/sites/prod/files/2019/12/f70/fcto-sa-2018-transportation-fuel-cell-cost-analysis.pdf
    # 
    # 2.	Wong, E.Y.C.; Ho, D.C.K.; So, S.; Tsang, C.-W.; Chan, E.M.H. Life Cycle Assessment of Electric Vehicles and Hydrogen Fuel Cell Vehicles Using the GREET Model—A Comparative Study. Sustainability 2021, 13, 4872 - April 26, 2021. https://doi.org/10.3390/su13094872; http://transportproblems.polsl.pl/pl/Archiwum/2020/zeszyt3/2020t15z3_13.pdf
    # 
    # 3.	Ivan Evtimov, Rosen Ivanov, Hristo Stanchev, Georgi Kadikyanov, Gergana Staneva, Life Cycle Assessment of Fuel Cells Electric Vehicles, Transport Problems, 15(3): 153-166 DOI: 10.21307/tp-2020-041 https://www.mdpi.com/2071-1050/13/9/4872/pdf?version=1620813581
    # 
    # 4.	Aristeidis Tsakiris, Analysis of hydrogen fuel cell and battery efficiency, Copenhagen Centre on Energy Efficiency (C2E2) March 2019 https://c2e2.unepccc.org/wp-content/uploads/sites/3/2019/09/analysis-of-hydrogen-fuel-cell-and-battery.pdf
    # 
    # 5.	Oliver Gröger et al., Review—Electromobility: Batteries or Fuel Cells? 2015 J. Electrochem. Soc. 162 A2605 https://iopscience.iop.org/article/10.1149/2.0211514jes/pdf
    # 
    # 6.	C. E. (Sandy) Thomas, Fuel Cell and Battery Electric Vehicles Compared, DOE (Mar. 27, 2009) https://www.energy.gov/eere/fuelcells/articles/fuel-cell-and-battery-electric-vehicles-compared
    # 
    # 7.	Jennie Huya-Kouadio, Brian D. James, Fuel Cell Cost and Performance Analysis Presentation for the DOE Hydrogen Program, 2023 Annual Merit Review and Peer Evaluation Meeting, Strategic Analysis Inc. (Jun.6, 2023) https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/review23/fc353_james_2023_o-pdf.pdf
    # 
    # 8.	Andrew Burke, Marshall Miller, Anish Sinha, Lew Fulton, Evaluation of the Economics of Battery-Electric and Fuel Cell Trucks and Buses: Methods, Issues, and Results, UC Davis (Aug. 4, 2022) https://escholarship.org/content/qt1g89p8dn/qt1g89p8dn_noSplash_e15c9e67dd1aab914d70e37a56cb70da.pdf?t=rg5613
    # 
    # 9.	Fuquan Zhao, Zhexuan Mu, Han Hao, Zongwei Liu,* Xin He, Steven Victor Przesmitzki, and Amer Ahmad Amery, Hydrogen Fuel Cell Vehicle Development in China: An Industry Chain Perspective, Energy Technol. 2020, 8, 2000179 https://www.researchgate.net/journal/Energy-Technology-2194-4296/publication/341918035_Hydrogen_Fuel_Cell_Vehicle_Development_in_China_An_Industry_Chain_Perspective/links/619d50f2d7d1af224b1fdd50/Hydrogen-Fuel-Cell-Vehicle-Development-in-China-An-Industry-Chain-Perspective.pdf
    # 
    # 10.	De Wolf, D.; Smeers, Y., Comparison of Battery Electric Vehicles and Fuel Cell Vehicles. World,  Electr. Veh. J. 2023, 14, 262. https:// doi.org/10.3390/wevj14090262 https://www.mdpi.com/2032-6653/14/9/262/pdf?version=1695025567
    # 
    # 11.	Achim Kampker, Heiner Heimes, Mario Kehrer, Sebastian Hagedorn, Philipp Reims, Oliver Kaul, Fuel cell system production cost modeling and analysis, Energy Reports, Vol. 9, Supp. 1, March 2023, Pages 248-255 https://www.researchgate.net/profile/Philipp-Reims/publication/365267244_ScienceDirect_Fuel_cell_system_production_cost_modeling_and_analysis/links/636cbd1c431b1f53008755b5/ScienceDirect-Fuel-cell-system-production-cost-modeling-and-analysis.pdf
    # 
    # 12.	Ahmad Mayyas, Assia Chadly, Saed Talib Amer, Elie Azar, Economics of the Li-ion batteries and reversible fuel cells as energy storage systems when coupled with dynamic electricity pricing schemes, Energy, Volume 239, Part A, 15 January 2022, 121941 https://www.researchgate.net/profile/Assia-Chadly/publication/354393953_Economics_of_the_Li-ion_Batteries_and_Reversible_Fuel_Cells_as_Energy_Storage_Systems_when_Coupled_with_Dynamic_Electricity_Pricing_Schemes/links/648ad96c7fcc811dcdce5f89/Economics-of-the-Li-ion-Batteries-and-Reversible-Fuel-Cells-as-Energy-Storage-Systems-when-Coupled-with-Dynamic-Electricity-Pricing-Schemes.pdf
    # 
    # 13.	Ahmed I. Osman, Neha Mehta, Ahmed M. Elgarahy, Mahmoud Hefny, Amer Al-Hinai, Ala’a H. Al-Muhtaseb & David W. Rooney, Hydrogen production, storage, utilisation and environmental impacts: a review, Environmental Chemistry Letters, Vol. 20:153–188 (Oct. 6, 2021) https://link.springer.com/content/pdf/10.1007/s10311-021-01322-8.pdf
    # 
    # 14.	Hydrogen Council, Path to hydrogen competitiveness: A cost perspective (Jan. 20, 2020) https://hydrogencouncil.com/wp-content/uploads/2020/01/Path-to-Hydrogen-Competitiveness_Full-Study-1.pdf
    # 
    # 15.	Laurent Vandepaera, Julie Cloutierb, Ben Amor, Environmental impacts of Lithium Metal Polymer and Lithium-ion stationary batteries, Renewable and Sustainable Energy Reviews, Vol. 78:46-60, 2017, https://www.ourenergypolicy.org/wp-content/uploads/2017/05/1-s2.0-S1364032117305580-main.pdf
    # 
    # 16.	 Miotti, Marco, Johannes Hofer, and Christian Bauer. “Integrated Environmental and Economic Assessment of Current and Future Fuel Cell Vehicles.” The International Journal of Life Cycle Assessment (2015) https://dspace.mit.edu/bitstream/handle/1721.1/104912/11367_2015_Article_986.pdf?sequence=1&isAllowed=y; https://web.archive.org/web/20220203102434/https://dspace.mit.edu/bitstream/handle/1721.1/104912/11367_2015_Article_986.pdf
    # 
    # 17.	Datu Buyung Agusdinata, Wenjuan Liu, Hallie Eakin and Hugo Romer, Socio-environmental impacts of lithium mineral extraction: towards a research agenda, https://doi.org/10.1088/1748-9326/aae9b1 https://iopscience.iop.org/article/10.1088/1748-9326/aae9b1/pdf
    # 
    # 18.	Bonnie J. Glaister, Gavin M. Mudd, The environmental costs of platinum–PGM mining and sustainability: Is the glass half-full or half-empty? Minerals Engineering 23 (2010) 438–450 https://wikirate.s3.amazonaws.com/files/784785/12677380.pdf
    # 
    # 19.	Yogesh Manoharan, Seyed Ehsan Hosseini, Brayden Butler, Hisham Alzhahrani, Bhi Thi Fou Senior, Turaj Ashuri, and John Krohn, Hydrogen Fuel Cell Vehicles; Current Status and Future Prospect, Applied Sciences. 2019, 9(11), 2296 https://www.mdpi.com/2076-3417/9/11/2296/pdf?version=1559636127
    # 
    # 20.	University of Cambridge, Dissemination of IT for the Promotion of Materials Science (DoITPoMS) Fuel Cells https://www.doitpoms.ac.uk/tlplib/fuel-cells/printall.php
    # 
    ###%mkdir -p 'data/ev_energy_source/'
    path = 'data/ev_energy_source/'
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

# %%
def getFileReq(file):
    import requests
    from urllib.parse import urlparse
    import os
    ###%mkdir -p '/data/ev_energy_source/'
    path = './data/ev_energy_source/'
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    os.chdir(path)
    url = file
    a = urlparse(url)
    print(a.path)                    
    print(os.path.basename(a.path))  
    ##fileOut =  os.path.basenme("a.path") 
    fileOut = os.path.basename(url)
    ###req = requests.get(url, allow_redirects=True)
    req = requests.get(url, allow_redirects=False)
    print("URL:  ",req.url)
    print("content",req.content)
    print("read using requests")
    
    open(fileOut, 'wb').write(req.content)
    fileResult = 0
    
    #fileResult = open(fileOut,'r').read(req.content)
    print("downloaded file:  ",fileOut)
    print("read result =: ",fileResult)
    return(fileOut)
# %%
def getArticles():
    r = getFileReq('https://www.energy.gov/sites/prod/files/2019/12/f70/fcto-sa-2018-transportation-fuel-cell-cost-analysis.pdf -O data/ev_energy_source/fcto-sa-2018-transportation-fuel-cell-cost-analysis.pdf')
    print("getArticles return:  ", r)
    r =getFileReq('http://transportproblems.polsl.pl/pl/Archiwum/2020/zeszyt3/2020t15z3_13.pdf -O data/ev_energy_source/2020t15z3_13.pdf')  
    r =getFileReq('https://www.mdpi.com/2071-1050/13/9/4872/pdf?version=1620813581 -O data/ev_energy_source/pdf?version=1620813581')
    r =getFileReq('https://c2e2.unepccc.org/wp-content/uploads/sites/3/2019/09/analysis-of-hydrogen-fuel-cell-and-battery.pdf -O data/ev_energy_source/analysis-of-hydrogen-fuel-cell-and-battery.pdf')
    r =getFileReq('https://iopscience.iop.org/article/10.1149/2.0211514jes/pdf -O data/ev_energy_source/pdf')
    r =getFileReq('https://www.energy.gov/eere/fuelcells/articles/fuel-cell-and-battery-electric-vehicles-compared -O data/ev_energy_source/fuel-cell-and-battery-electric-vehicles-compared')
    r =getFileReq('https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/review23/fc353_james_2023_o-pdf.pdf  -O data/ev_energy_source/fc353_james_2023_o-pdf.pdf')
    r =getFileReq('https://escholarship.org/content/qt1g89p8dn/qt1g89p8dn_noSplash_e15c9e67dd1aab914d70e37a56cb70da.pdf?t=rg5613 -O data/ev_energy_source/qt1g89p8dn_noSplash_e15c9e67dd1aab914d70e37a56cb70da.pdf?t=rg5613')
    r =getFileReq('https://www.researchgate.net/journal/Energy-Technology-2194-4296/publication/341918035_Hydrogen_Fuel_Cell_Vehicle_Development_in_China_An_Industry_Chain_Perspective/links/619d50f2d7d1af224b1fdd50/Hydrogen-Fuel-Cell-Vehicle-Development-in-China-An-Industry-Chain-Perspective.pdf -O data/ev_energy_source/Hydrogen-Fuel-Cell-Vehicle-Development-in-China-An-Industry-Chain-Perspective.pdf')   
    r =getFileReq('https://www.mdpi.com/2032-6653/14/9/262/pdf?version=1695025567 -O data/ev_energy_source/pdf?version=1695025567')
    r =getFileReq('https://www.researchgate.net/profile/Philipp-Reims/publication/365267244_ScienceDirect_Fuel_cell_system_production_cost_modeling_and_analysis/links/636cbd1c431b1f53008755b5/ScienceDirect-Fuel-cell-system-production-cost-modeling-and-analysis.pdf -O data/ev_energy_source/pdfft?md5=178a0ab35b1a29a2992ded6bbfd32c6b&pid=1-s2.0-S2352484722022995-main.pdf')
    r =getFileReq('https://www.researchgate.net/profile/Assia-Chadly/publication/354393953_Economics_of_the_Li-ion_Batteries_and_Reversible_Fuel_Cells_as_Energy_Storage_Systems_when_Coupled_with_Dynamic_Electricity_Pricing_Schemes/links/648ad96c7fcc811dcdce5f89/Economics-of-the-Li-ion-Batteries-and-Reversible-Fuel-Cells-as-Energy-Storage-Systems-when-Coupled-with-Dynamic-Electricity-Pricing-Schemes.pdf -O data/ev_energy_source/pdfft?md5=a6ae75e573ed603fe2be61b809aadfeb&pid=1-s2.0-S0360544221021897-main.pdf')
    r =getFileReq('https://link.springer.com/content/pdf/10.1007/s10311-021-01322-8.pdf -O data/ev_energy_source/s10311-021-01322-8.pdf')
    r =getFileReq('https://hydrogencouncil.com/wp-content/uploads/2020/01/Path-to-Hydrogen-Competitiveness_Full-Study-1.pdf -O data/ev_energy_source/Path-to-Hydrogen-Competitiveness_Full-Study-1.pdf')
    r =getFileReq('https://www.ourenergypolicy.org/wp-content/uploads/2017/05/1-s2.0-S1364032117305580-main.pdf -O data/ev_energy_source/1-s2.0-S1364032117305580-main.pdf')
    r =getFileReq('https://dspace.mit.edu/bitstream/handle/1721.1/104912/11367_2015_Article_986.pdf -O data/ev_energy_source/11367_2015_Article_986.pdf')
    r =getFileReq('https://iopscience.iop.org/article/10.1088/1748-9326/aae9b1/pdf -O data/ev_energy_source/pdf')
    r =getFileReq('https://wikirate.s3.amazonaws.com/files/784785/12677380.pdf -O data/ev_energy_source/12677380.pdf')
    r =getFileReq('https://www.mdpi.com/2076-3417/9/11/2296/pdf?version=1559636127 -O data/ev_energy_source/pdf?version=1559636127')
    r =getFileReq('https://www.doitpoms.ac.uk/tlplib/fuel-cells/printall.php -O data/ev_energy_source/printall.php')
# %%
def getKeys():
    import os
    import EnvSettings as envSettings
    openai_key = envSettings.set_key()
    #non-Colab line
    os.environ.get('OPENAI_API_KEY')
    
    #Colab (2 lines)
    #from google.colab import userdata
    #os.environ["OPENAI_API_KEY"] = userdata.get('open_ai_key')
    return openai_key
# %%
def importClases():
    # Import necessary classes from the llama_index package
    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


# %%
def getDirectory(index_loaded):    
    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
    #Class 5 and
    #https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/examples/agent/openai_agent_with_query_engine.ipynb
    #see above
    if not index_loaded:
        # load data
        path = './data/ev_energy_source/'
        reader = SimpleDirectoryReader(path)
        documents = reader.load_data()
        #https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader.html
        #https://github.com/run-llama/llama_index/blob/main/docs/examples/data_connectors/simple_directory_reader_remote_fs.ipynb

        # build index
        index = VectorStoreIndex.from_documents(documents)

        # persist index
        index.storage_context.persist(persist_dir='./storage/ev_vec_idx')
    print(f"Loaded {len(documents)} documents")
    #It is unclear to me why there are so many documents
    #Currently three documents are not indexed. I think there's a Captcha check box
    return index
# %%
# ##Formatting Function    
def format_output(text, max_line_length=80):
    lines = []
    current_line = ""

    for word in text.split():
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())

    return '\n'.join(lines)


# %% [markdown]
def chatFunctions():
    # # Chat functionality
    #from llama_index.llms.openai import OpenAI
    #llm = OpenAI(model="gpt-3.5-turbo")
    #llm = OpenAI(model="gpt-4")
    #It seemsto give betteranswers when a model is not specified--doesn't make a lot of sense
    chat_engine = index.as_chat_engine(chat_mode="openai",
                                    tool_choice="query_engine_tool",
                                    verbose=False,
                                    system_prompt=(
                                    "You are a chatbot who is an expert in the"
                                    " engineering, economics, and environmental"
                                    " impacts of battery and hydrogen fuel cell"
                                    " technology for use in vehicles, as well as"
                                    " lithium and platinum group metals mining"
                                    " and are able to have normal interactions,"
                                    " as well as talk."),
                                    #llm = llm
                                    )
    #this made a huge difference in the quality and quantity of responses
    #https://docs.llamaindex.ai/en/latest/examples/chat_engine/chat_engine_context.html
    #there is a setting for chat_mode="context" as opposed to openai, but the webpage
    #says "context retrieved can take up a large amount of the available LLM context,
    #let’s ensure we configure a smaller limit to the chat history!"
    #https://docs.llamaindex.ai/en/latest/examples/chat_engine/chat_engine_openai.html - set which llm model

# %%
def chatEngine():    
    response = chat_engine.chat("Hi")
    #print(response) using the above user-defined function instead - see below

    # Convert the response object to a string
    response_text = str(response)

    # Format the output with line returns
    formatted_text = format_output(response_text)

    # Print or use the formatted text as needed
    print(formatted_text)
    response = chat_engine.chat(
        "What is the comparative cost for battery technology vs. hydrogen fuel cell technology?"
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)

    
    response = chat_engine.chat(
        "On a dollars per kwh basis, are batteries more expensive or are hydrogen fuel cells more expensive?"
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)


    response = chat_engine.chat(
        "How much more expensive?"
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)

    response = chat_engine.chat(
        "Yes, and please tell me what your source of information is."
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)

    response = chat_engine.chat(
        "Please provide a citation for the document you referred to."
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)

    response = chat_engine.chat(
        "What are the prospects for hydrogen fuel cell technology?"
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)


    response = chat_engine.chat(
        "Compare the environmental impacts of battery technology vs. hydrogen fuel cell technology."
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)

    
    response = chat_engine.chat(
        "What about the environmental impacts of mining lithium vs. mining platinum group metals?"
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)

    response = chat_engine.chat(
        "What are the differences in the amount of lithium vs. platinum group metals available in the earth?"
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)

# %%
def platinumAlternatives():
    response = chat_engine.chat(
        "What promising technological alternatives are there to using platinum group metals in hydrogen fuel cells?"
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)

# %%
def envireAlkaline():
    response = chat_engine.chat(
        "What are the environmental impacts of using alkaline anion exchange membrane electrolysis in hydrogen fuel cells?"
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)
    return response

# %%
def hydrogenEffective():
    response = chat_engine.chat(
        "Are hydrogen fuel cells cost-effective at this point in time?"
    )
    response_text = str(response)
    formatted_text = format_output(response_text)
    print(formatted_text)
    return response

