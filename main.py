from agents.rewriter_agent import RewriterAgent
from agents.judge_agent import JudgeAgent
from config import MAX_ITERATIONS

def main(input_text):
    agent_a = RewriterAgent(name="Agent A")
    agent_b = RewriterAgent(name="Agent B")
    judge = JudgeAgent()

    for iteration in range(MAX_ITERATIONS):
        output_a = agent_a.rewrite(input_text)
        output_b = agent_b.rewrite(input_text)

        similar, feedback = judge.compare_outputs(output_a, output_b)
        if similar:
            final_result = judge.align_with_input(input_text, output_a, output_b)
            print("✅ Final Output:\n", final_result)
            return

        print(f"⚠️ Iteration {iteration+1}: Outputs too different.")
        agent_a.feedback(feedback)
        agent_b.feedback(feedback)

    print("❌ Reached max iterations without convergence.")

if __name__ == "__main__":
    example_input = "我們最近在處理客訴流程的效率問題，希望優化但不清楚從哪開始。"
    main(example_input)
