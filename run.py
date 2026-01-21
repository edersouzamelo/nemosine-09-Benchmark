from openai import OpenAI

from core.state import STATE_S
from core.state_alt import STATE_JUNIOR

from perturbations.basic import (
    role_attack,
    noise_attack,
    contradiction_attack,
)

from metrics.simple import identity_preserved
from metrics.aggregate import aggregate_scores
from metrics.logger import log_run


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


# Estados canônicos a serem comparados
STATES = {
    "senior": STATE_S,
    "junior": STATE_JUNIOR,
}

# Número de execuções independentes
N_RUNS = 10

for state_name, STATE in STATES.items():
    tests = [
        role_attack(STATE),
        noise_attack(STATE),
        contradiction_attack(STATE),
    ]

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

    print(f"\nNemosine Stability Benchmark v0.4 — state={state_name}")
    print(f"Runs: {summary['n']}")
    print(f"Mean stability: {summary['mean']}")
    print(f"Std deviation: {summary['stdev']}")
    print(f"Min stability: {summary['min']}")
    print(f"Max stability: {summary['max']}")
    print(f"Failure rate: {summary['failure_rate']}")

    log_run({**summary, "state": state_name})


