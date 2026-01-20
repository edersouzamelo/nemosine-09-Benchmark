from openai import OpenAI

from core.state import STATE_S
from perturbations.basic import (
    role_attack,
    noise_attack,
    contradiction_attack,
)
from metrics.simple import identity_preserved


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

scores = []

for test_prompt in tests:
    response = model_call(test_prompt)
    score = identity_preserved(response)
    scores.append(score)

final_score = sum(scores) / (len(scores) * 2)

print("Nemosine Stability Score:", final_score)

