# from some_llm_wrapper import call_llm
from llm.__init__ import call_llm

def compare_by_llm(problem_a, problem_b, sop_a, sop_b):
    prompt = f"""
                你是負責協調兩位分析師工作的審稿員。以下是他們針對相同輸入產生的兩份輸出：

                ---
                Agent A 的問題描述：
                {problem_a}

                Agent B 的問題描述：
                {problem_b}

                ---
                Agent A 的 SOP：
                {sop_a}

                Agent B 的 SOP：
                {sop_b}

                ---
                請判斷他們的「問題描述」與「SOP」是否邏輯上意思一致，忽略表面文字差異。
                - 如果一致，回覆：SIMILAR
                - 如果有顯著差異，回覆：DIFFERENT，並指出他們可能誤解彼此或漏了什麼觀點
                """

    response = call_llm(prompt)

    if "SIMILAR" in response:
        return True, ""
    else:
        return False, f"LLM 判定輸出有差異：\n{response.strip()}"
