from openai import OpenAI

from core.state import STATE_S
from perturbations.basic import (
    role_attack,
    noise_attack,
    contradiction_attack,
)
from metrics.simple import identity_preserved
from metrics.aggregate import aggregate_scores


client = OpenAI()


def model_call(prompt: str) -> str:
    """
    Chamada real à OpenAI.
    Retorna apenas o texto final do modelo.
    """
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )
    return response.output_text


tests = [
    role_attack(STATE_S),
    noise_attack(STATE_S),
    contradiction_attack(STATE_S),
]

# Número de execuções independentes do benchmark
N_RUNS = 10

all_scores = []

for _ in range(N_RUNS):
    scores = []

    for test_prompt in tests:
        response = model_call(test_prompt)
        score = identity_preserved(response)
        scores.append(score)

    stability_score = sum(scores) / len(scores)
    all_scores.append(stability_score)

summary = aggregate_scores(all_scores)

print("Nemosine Stability Benchmark v0.3")
print(f"Runs: {summary['n']}")
print(f"Mean stability: {summary['mean']}")
print(f"Std deviation: {summary['stdev']}")
print(f"Min stability: {summary['min']}")
print(f"Max stability: {summary['max']}")
print(f"Failure rate: {summary['failure_rate']}")

