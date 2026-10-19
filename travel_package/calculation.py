"""Simple calculations (NumPy is used for the statistics)."""

import numpy as np


def cost_per_day(total, days):
    if days > 0:
        return total / days
    return 0.0


def cost_per_person(total, travellers):
    if travellers > 0:
        return total / travellers
    return 0.0


def summarize(totals):
    # count, average, minimum and maximum of a list of trip totals
    numbers = np.array(totals)
    return {
        "count": len(numbers),
        "average": float(np.mean(numbers)),
        "minimum": float(np.min(numbers)),
        "maximum": float(np.max(numbers)),
    }
