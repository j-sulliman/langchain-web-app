

import os


from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.globals import set_debug

from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow, task

from opentelemetry.sdk.trace.export import ConsoleSpanExporter


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TRACELOOP_API_KEY = os.getenv("TRACELOOP_API_KEY")
#Traceloop.init(exporter=ConsoleSpanExporter())
#Traceloop.init(app_name="[JS]-langchain-openai", api_key=TRACELOOP_API_KEY, disable_batch=True)
Traceloop.init(app_name="[JS]-langchain-openai", disable_batch=True)


@task(name="prep_invoke_prompt_chain")
def prompt_invoke():

    llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)  
    st.title("Ask me Anything")
    prompt=st.text_input("Enter the  question: ")
    if prompt:
        response = llm.invoke(prompt)
    else:
        st.write("Please enter valid questions")
        response = llm.invoke(prompt)
    return response.content
         

@workflow(name="display_response")
def display_response(response):
        st.write(response)


if __name__ == "__main__":

    data = prompt_invoke()
    display_response(data)

    st.link_button("Dynatrace full-stack observability platform combined with Traceloop's OpenLLMetry OpenTelemetry SDK", "https://docs.dynatrace.com/docs/observe-and-explore/dynatrace-for-ai-observability/traceloop-openllmetry")