
from config.env import load_env
from config.models import OpenAIModel
from services.llm_service import LLMService

def main():
    load_env()
    llm = LLMService(model=OpenAIModel.GPT_41)
    result = llm.run("Explain modular design in one line")

    print(result)


if __name__ == "__main__":
    main()
