from core.state import STATE_S
from perturbations.basic import (
    role_attack,
    noise_attack,
    contradiction_attack,
)
from metrics.simple import identity_preserved


def fake_model(prompt: str) -> str:
    """
    Mock de resposta do modelo.
    Substituir por chamada real posteriormente.
    """
    return "This analysis explains the concept clearly."


tests = [
    role_attack(STATE_S),
    noise_attack(STATE_S),
    contradiction_attack(STATE_S),
]

scores = []

for test_prompt in tests:
    response = fake_model(test_prompt)
    score = identity_preserved(response)
    scores.append(score)

final_score = sum(scores) / (len(scores) * 2)

print("Nemosine Stability Score:", final_score)
