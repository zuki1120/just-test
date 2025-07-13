from config import COMPARISON_METHOD
from utils.formatter import extract_problem_sop

if COMPARISON_METHOD == "llm":
    from utils.llm_judge import compare_by_llm
else:
    from utils.similarity import is_similar

class JudgeAgent:
    def compare_outputs(self, output_a, output_b):
        pa, sa = extract_problem_sop(output_a)
        pb, sb = extract_problem_sop(output_b)

        if COMPARISON_METHOD == "llm":
            return compare_by_llm(pa, pb, sa, sb)
        else:
            prob_sim = is_similar(pa, pb)
            sop_sim = is_similar(sa, sb)
            if prob_sim and sop_sim:
                return True, ""
            feedback = f"問題描述相似度：{prob_sim:.2f}，SOP 相似度：{sop_sim:.2f}，請檢查差異。"
            return False, feedback

    def align_with_input(self, input_text, output_a, output_b):
        # LLM 自動整合 or 選擇其中一個合理結果
        return output_a
