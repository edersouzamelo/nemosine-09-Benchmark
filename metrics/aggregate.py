from typing import List, Dict
import statistics


def aggregate_scores(scores: List[float]) -> Dict[str, float]:
    """
    Agrega múltiplos scores de estabilidade em métricas estatísticas básicas.

    Retorna:
        - mean: média dos scores
        - stdev: desvio padrão (0.0 se N < 2)
        - min: menor score observado
        - max: maior score observado
        - failure_rate: proporção de execuções com score < 1.0
    """
    if not scores:
        raise ValueError("Lista de scores vazia.")

    mean = statistics.mean(scores)
    stdev = statistics.stdev(scores) if len(scores) > 1 else 0.0
    min_v = min(scores)
    max_v = max(scores)
    failure_rate = sum(1 for s in scores if s < 1.0) / len(scores)

    return {
        "mean": round(mean, 4),
        "stdev": round(stdev, 4),
        "min": round(min_v, 4),
        "max": round(max_v, 4),
        "failure_rate": round(failure_rate, 4),
        "n": len(scores),
    }
