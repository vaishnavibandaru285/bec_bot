from langchain import OpenAI
import sys
import os
from llama_index import SimpleDirectoryReader, GPTListIndex, GPTVectorStoreIndex, LLMPredictor, PromptHelper, \
    ServiceContext
from llama_index import StorageContext, load_index_from_storage


def create_index(path):
    max_input = 4096
    tokens = 200
    chunk_size = 600  # for LLM, we need to define chunk size
    max_chunk_overlap = 20

    prompt_helper = PromptHelper(max_input, tokens, max_chunk_overlap, chunk_size_limit=chunk_size)  # define prompt

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001", max_tokens=tokens))  # define LLM
    docs = SimpleDirectoryReader(path).load_data()  # load data

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    vectorIndex = GPTVectorStoreIndex.from_documents(
        docs, service_context=service_context
    )

    vectorIndex.storage_context.persist(persist_dir="storage")

    return vectorIndex


def answerMe():
    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    q = "What is the best plan?"
    print(q)
    print('------------')
    response = query_engine.query(q)
    print(response)


# create_index('data')
answerMe()