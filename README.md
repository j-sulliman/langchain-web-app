# Introduction

This lab explores instrumenting a langchain and openai application with Opentelemtry traces and sending those traces to Dynatrace


## Lab overview

### LangChain

[Langchain](https://www.langchain.com/langchain) is framework that simplifies and abstracts working with Large Lange Models (LLMs) from various providers. 

For this lab we use LangChain's OpenAI integration to interact with the GPT4 model.

### OpenAI
You'll need to create an [OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) which will be used to autheniticate requests from Langchain

For this lab we use OpenAI's gpt-4o model

###  Traceloop
[Traceloop](https://www.traceloop.com/docs/introduction) integrates with OpenLLMetry SDK and simplifies getting performance, code level traces from LLM applications to observability platforms.

### Streamlit

We use [streamlit](https://streamlit.io/) to simplify the creation of our front end LLM web app.  No Java, CSS exprience needed. 

### Dynatrace

We use the article [Traceloop OpenLLMetry](https://docs.dynatrace.com/docs/shortlink/dynatrace-traceloop-openllmetry) to send OTEL traces to Dynatrace


### Lab Components
![Lab Components](https://github.com/j-sulliman/langchain-web-app/blob/main/architecture_diagram.png?raw=true")


## Running the lab

### Open with Codespaces
* Create a fork of this repo
* Under the **< > Code**, click **+ Create a codespace on main** 


###  Set environment variables

From the codespaces terminal(note - the %20 formatting is not a typo!):

```
export OPENAI_API_KEY=<your-open-api-key>
export TRACELOOP_BASE_URL=https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp
export TRACELOOP_HEADERS=Authorization=Api-Token%20<your-token>
```

### Install dependencies and run the application

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt 
```
Launch streamlit:

```
streamlit run streamlit_openai_app.py
```

**Note** Using a virtualenv shouldn't ordinarily be required here.  Further research needed to run streamlit in the defaul codespaces python environment.  Above is a simple workaround.

```
streamlit run streamlit_openai_app.py
```

###  View Application Service Metrics and OTEL Traces in Dynatrace


#### Service Metrics
Open Services(the service name will appear in Dynatrace as the **app-name** defined in line20, **(Traceloop.init(app_name="[your-app-name]-langchain-openai", disable_batch=True)**:

![Lab Components](https://github.com/j-sulliman/langchain-web-app/blob/main/services.png?raw=true")


#### Traces

![Lab Components](https://github.com/j-sulliman/langchain-web-app/blob/main/traces.png?raw=true")
