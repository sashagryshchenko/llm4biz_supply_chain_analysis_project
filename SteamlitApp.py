# %%

import streamlit as st
import EnvSettings as settings
openai_key = settings.set_key()
from openai import OpenAI
import Tech16FinalProject_supplychains as deb
from utils import *
deb.do_imports()
# %%
st.set_page_config(layout = "wide" , page_title = "Request")
st.write("Hello world")
output_path = '/home/nbahrami/Downloads/LLM/results/'
###deb.do_installs()
label = r"$\textsf{\tiny Type of Request}$"  # https://stackoverflow.com/questions/77377439/how-to-change-font-size-in-streamlit
st.title(label)

# subject = st.selectbox(label = "Subject" , options = ['Fuel Cell Cars' , 'Electric Cars' , 
#                                             'Environmental Resources' , 'Autonomous Fuel'],
#                                                 index=None,
#                                                 placeholder="Select contact method...",)
subject = st.multiselect(label = "Subject" , options = ['Fuel Cell Cars' , 'Electric Cars' , 
                                            ])
st.write('You selected:', subject)
# print(subject)

label = r"$\textsf{\tiny Sub Type}$"
st.title(label)
impacts = st.multiselect(label = "Chose one of the subtypes below" , options = ['Supply Chain Resources' , 'Supply Chain' , 'Environmental Resources' , 'Environmental Impacts' , 'Manufacturing Process'])
st.write('You selected:', impacts)
# print(impacts)


st.write('');st.write('');st.write('**Actions**')
option_1 = st.checkbox('Search for Documents') # if it is checked it will be 'True'
option_2 = st.checkbox('Parse Document(s) for Answers')
option_3 = st.checkbox('Project Costs')
option_4 = st.checkbox('Comparison Summary')
options_lst = [option_1 , option_2, option_3, option_4]

st.write('');st.write('');st.write('**Export Format**')
option_csv_format = st.checkbox('.csv') 
option_json_format = st.checkbox('.json')

if option_csv_format:
    option_csv_format = '.csv'
if option_json_format:
    option_json_format = '.json'



col1, col2, col3 , col4, col5 = st.columns(5)
with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Submit') # https://docs.streamlit.io/library/api-reference/widgets/st.button

if center_button:
    print(subject)
    print(impacts)
    print(options_lst)




############################################ Comparison Summary #############################

if center_button & option_4:
    for i in range(len(subject)):
        for j in range(len(impacts)):

            prompt = ""
            prompt = f"Summarize {impacts[j]} impacts of {subject[i]}"
            ###table_out =get_summary(prompt)
            table_out = deb.gptrequest(prompt)
            save_file(table_out ,output_path , impacts[j] , subject[i], option_csv_format)

            if len(subject) > 1:
                prompt = f"create a table of a comparison between {impacts[j]} impacts of {subject[0]} vs {subject[1]}"
                table_out = get_comparison(prompt)
                save_file(table_out ,output_path , impacts[j] , 'comparison-EC-FCC', option_csv_format)


# %%
