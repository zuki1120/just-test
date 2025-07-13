import re

def extract_problem_sop(text):
    problem_match = re.search(r"問題描述：(.+?)SOP 步驟：", text, re.DOTALL)
    sop_match = re.search(r"SOP 步驟：(.*)", text, re.DOTALL)

    problem = problem_match.group(1).strip() if problem_match else ""
    sop = sop_match.group(1).strip() if sop_match else ""

    return problem, sop
