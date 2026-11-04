
import truststore
truststore.inject_into_ssl()
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

def main() -> None:
    information= """Elon Reeve Musk is an industrialist, technologist, and former public official who is the chief executive officer and largest shareholder of Tesla and SpaceX."""
    summary_template="""
    given the information {information} about a person I want you to create:
    1. short summary
    2. two intresting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables=["infomation"], template=summary_template);

    llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__== "__main__":
    main()