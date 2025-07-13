from agents.base_agent import BaseAgent
# from some_llm_wrapper import call_llm  # 你可以自訂 OpenAI / Claude / Mistral 等 wrapper
from llm.__init__ import call_llm  # 確保這個函式可以調用正確的 LLM 提供者

class RewriterAgent(BaseAgent):
    def __init__(self, name):
        super().__init__(name)
        self.last_feedback = ""

    def rewrite(self, input_text):
        prompt = f"""你是一個分析師，請根據以下輸入內容，產出「詳細問題描述」與「具體SOP」：
                    輸入內容：{input_text}

                    {f"根據以下回饋修正你的輸出：{self.last_feedback}" if self.last_feedback else ""}

                    請輸出格式為：
                    問題描述：
                    ...
                    SOP 步驟：
                    1.
                    2.
                    3.
                    """
        return call_llm(prompt)

    def feedback(self, feedback_text):
        self.last_feedback = feedback_text
