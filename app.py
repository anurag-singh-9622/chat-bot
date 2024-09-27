from openai import OpenAI
# import openai
import streamlit as st
import os
# import getpass
import pandas as pd
# import snowflake.connector
# import re
from langchain_openai import ChatOpenAI
# import json
# from pyngrok import ngrok 
# import subprocess



database='CPH_DB_TEST'

# @st.cache_resource(show_spinner=False)
# def connect_to_snowflake():
#     # Connect to Snowflake
#     conn = snowflake.connector.connect(
#         # user=user,
#         # password=password,
#         # account=account,
#         # database=database,
#         user='DQDCRCA1',
#         password='Rcaiscompleted@1511',
#         account='bf30978.ap-southeast-1',
#         database='CPH_DB_TEST'
#     )
#     # Return the connection object
#     return conn

# conn =connect_to_snowflake()



# def fetch_business_data():
#     data={}
#     data['table-name'] = 'bv_cvent_contact'
#     data['layer'] ='Enrich'
#     data['database'] ='CPH_DB_TEST'
#     data['table_names_from_information_schema'] 
    
   
# @st.cache_data
# @st.cache_resource(show_spinner=False)
# def get_all_table_names():
#     # conn = connect_to_snowflake()
#     query = """
#         SELECT table_catalog, table_schema, table_name
#         FROM cph_db_test.information_schema.tables
#         WHERE table_type = 'BASE TABLE';
#     """
    
#     cursor = conn.cursor()
#     cursor.execute(query)
#     tables = cursor.fetchall()
#     # cursor.close()
#     # conn.close()
    
#     # Format the tables as 'schema.table_name'
#     formatted_table_names = [f"{table[1]}.{table[2]}" for table in tables]
#     return formatted_table_names

# table_names_from_information_schema = get_all_table_names()

# @st.cache_data
# @st.cache_resource(show_spinner=False)
# def prompt_selector(user_question):
    

#     json_file= open("prompt.json") 
#     all_prompts = json.load(json_file)
#     json_file.close()
#     all_prompts = json.dumps(all_prompts, indent=2)
    


        

#     prompt1 =f"""
# You are an intelligent assistant that selects the most appropriate SQL prompt based on user questions. Given the following user question, choose the most relevant SQL prompt from the list provided and return its value not key. 

# User Question: "{user_question}"

# Available Prompts:{all_prompts}


# Please return the selected prompt in the format: "Prompt: [Your selected prompt]"

# """

    
#     response = llm.invoke(prompt1)
#     selected_prompt = response.content
    

#     selected_prompt=selected_prompt.format(table_names_from_information_schema,schema_str,user_question,table_name)
    



#     return selected_prompt




if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] == st.secrets["openaiapi"]
    

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=500)


# @st.cache_resource(show_spinner=False)
# def get_table_description(table_name):
#     cur = conn.cursor()
    
#     cur.execute(f"DESC TABLE {table_name}")
#     # description =pd.read_sql(f"DESC TABLE {table_name}",conn)
#     description = cur.fetchall()
#     return description



# table_name = "CPH_DB_TEST.Enrich.bv_cvent_contact"
# data_base ='CPH_DB_TEST'

# table_schema = get_table_description(table_name)

# schema_str = "\n".join([f"{col[0]}: {col[1]}" for col in table_schema])
# # print(schema_str)


# def find_mapping_table(table_name):
#     prompt =f""" If user table name is of model then return the respective enrich table name from table_names_from_information_schema and if user table name is of enrich then return the respective model table name from table_names_from_information_schema.
#     \n\n **User's Table Name:**{table_name}.
#     \n\n **table_names_from_information_schema** :{table_names_from_information_schema}
#     \n\n  **format to return table name is**\n  Table_name ='--Identified table name here':
# """
#     response = llm.invoke(prompt)
#     resp_contant = response.content

#     if match := re.search(r"Table_name\s*=\s*'(.*?)'", resp_contant, re.DOTALL):
#         identified_table = match.group(1)

#         cur = conn.cursor()
#         if  'MODEL' in table_name.upper():
#             cur.execute(f"desc table {table_name}")
#             Model_table_columns = cur.fetchall()

#             cur.execute(f"desc table {identified_table}")
#             Enrich_table_columns = cur.fetchall()
#         else:
#             cur.execute(f"desc table {table_name}")
#             Enrich_table_columns = cur.fetchall()

#             cur.execute(f"desc table {identified_table}")
#             Model_table_columns = cur.fetchall()

#         Model_table_columns_with_datatype = "\n".join([f"{col[0]}: {col[1]}" for col in Model_table_columns])
#         Enrich_table_columns_with_datatype = "\n".join([f"{col[0]}: {col[1]}" for col in Enrich_table_columns])

#         return Model_table_columns_with_datatype,Enrich_table_columns_with_datatype
#     else:
#         return None,None

        





# @st.cache_resource(show_spinner=False)
# def get_table_description(prompt):
#     cur = conn.cursor()


#     prompt2="""
  
#       "task": "Table Identification",

#       "description": "When a user provides a  sql query or asks a question related to sql, identify the most appropriate table based on the information in the `information_schema`:{0} \n\n `User's Question :{1}  \n\n If table is  identified Return the  table name in the following format  Table_name ='--Identified table name here' else if table is not identified the retun the user's question . "
#     """.format(table_names_from_information_schema,prompt)
  
#     llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=500)

#     response = llm.invoke(prompt2)

#     response_content = response.content

#     # print("prompt:",prompt)
#     # print("response_content:",response_content)

#     # match = re.search(r"Table_name ='(.*?)'", response)
    
#     if match := re.search(r"Table_name\s*=\s*'(.*?)'", response_content, re.DOTALL):
#     # if match := re.search(r"```sql\n(.*)\n```", response_content, re.DOTALL):
        
#         identified_table = match.group(1) 
#         print("identified_table:",identified_table)
    
#         try:
#             cur.execute(f"DESC TABLE {identified_table};")
#             description = cur.fetchall()
#             return description,identified_table
#         except:
#             # msg = llm.invoke(f"prompt:{identified_table} table is not correct sugggest the user to re enter the query with correct table name")
#             # st.write_stream(msg)
#             # st.session_state.messages.append({"role": "assistant", "content": msg,"templete":msg})   
#             return None ,identified_table
#     else:
#         # msg = llm.invoke(f"prompt:{response_content} table is not correct sugggest the user to re-enter the query with correct table name")
#         # st.write_stream(msg)
#         # st.session_state.messages.append({"role": "assistant", "content": msg,"templete":msg})
#         return None ,None

   


st.title("AI Based Chatbot  ")

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"
    # st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []



# llm = ChatOpenAI(model=st.session_state["openai_model"])
# @st.cache_data(show_spinner=False)
# @st.cache_resource(show_spinner=False)
def message_backup():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


message_backup()

if prompt := st.chat_input("What is up?"):
    templete = 'You are a assistant who provides good anwer to the user query.'
    # table_schema,table_name = get_table_description(prompt)
    # if table_schema and table_name:
    #     try:

    #         model_table_columns,enrich_table_columns=find_mapping_table(table_name)
    #         schema_str = "\n".join([f"{col[0]}: {col[1]}" for col in table_schema])
        


    #         # templete= prompt_selector(prompt)
    #         json_file= open("prompt.json") 
    #         all_prompts = json.load(json_file)
    #         json_file.close()
    #         all_prompts = json.dumps(all_prompts, indent=2)
    #         templete= all_prompts
    #         # selected_prompt=selected_prompt.format(table_names_from_information_schema,schema_str,user_question,table_name)

    #         templete += f""" **Data** \n\nmodel_table_columns:{str(model_table_columns)}  \n\n enrich_table_columns:{enrich_table_columns}  \n\ntable_names_from_information_schema:{table_names_from_information_schema} \n\n table_name:{table_name}
    #         \n\n Database:{database}
    #         \n\n User's Question:{prompt}

    #         """
    #     except:
    #         templete =f"""  You are a Snowflake Sql expert, but You can also handle any types of question user ask other than sql query like greeting(hi,hello) or any types of information user's need. \n\nuse the below user's question to answer. \n\n User's Table: {prompt}"""

    # else:
    #     templete =f"""  You are a Snowflake Sql expert, but You can also handle any types of question user ask other than sql query like greeting(hi,hello) or any types of information user's need. \n\nuse the below user's question to answer. \n\n User's Table: {prompt}"""




    st.session_state.messages.append({"role": "user", "content": prompt,"templete":templete})
    with st.chat_message("user"):
        st.markdown(prompt)
        # st.markdown(templete)

    with st.chat_message("assistant"):

        # response = llm.invoke(templete)
        # generated_query = response.content
        # sql_pattern = re.compile(r'```sql\n(.*?)\n```', re.DOTALL)

        # match = sql_pattern.search(generated_query)
        # try:
        #     query =match.group(1)
        #     # df = pd.read_sql(query, conn)
        # except:
        #     pass

        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["templete"]}
                for m in st.session_state.messages
            ],
            max_tokens=4000,
            temperature=0,

            stream=True,
        )
        response = st.write_stream(stream)
        # print(response)
    st.session_state.messages.append({"role": "assistant", "content": response,"templete":response})
