from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

class BaseExpert(object):

    def __init__(self, name, description, model):
        self.name = name
        self.description = description
        self.model = model

        # self.llm = ChatOpenAI(
        #     model_name=model,
        #     temperature=0
        # )


        self.llm = ChatOllama(
            model="qwen2.5",
            temperature=0,
            # other params...
        )



        self.forward_prompt_template = self.ROLE_DESCRIPTION + '\n' + self.FORWARD_TASK
        self.forward_prompt_template = PromptTemplate.from_template(self.forward_prompt_template)
        self.forward_chain = self.forward_prompt_template | self.llm
        # self.forward_chain = LLMChain(
        #     llm=self.llm,
        #     prompt=PromptTemplate.from_template(self.forward_prompt_template)
        # )
        if hasattr(self, 'BACKWARD_TASK'):
            self.backward_prompt_template = self.ROLE_DESCRIPTION + '\n' + self.BACKWARD_TASK
            self.backward_prompt_template = PromptTemplate.from_template(self.backward_prompt_template)
            self.backward_chain = self.backward_prompt_template | self.llm
            # self.backward_chain = LLMChain(
            #     llm=self.llm,
            #     prompt=PromptTemplate.from_template(self.backward_prompt_template)
            # )

    def forward(self):
        pass

    def backward(self):
        pass

    def __str__(self):
        return f'{self.name}: {self.description}'
