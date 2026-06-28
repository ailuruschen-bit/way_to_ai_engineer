# Unit 1.6 — Comprehensions & functional tools
# Write your solution here.
from collections import defaultdict
from typing import TypedDict


class Order(TypedDict):
    user: str
    total: int
    paid: bool


def paid_totals(orders: list[Order]) -> list[int]:
    return [order["total"] for order in orders if order["paid"]]


def user_total_map(orders: list[Order]) -> dict[str, int]:
    totals: defaultdict[str, int] = defaultdict(int)
    for order in orders:
        if order["paid"]:
            totals[order["user"]] += order["total"]

    return dict(totals)


def expensive_users(orders: list[Order], minimum: int) -> set[str]:
    user_total = user_total_map(orders)

    return {
        user
        for user, total in user_total.items() if total >= minimum
    }


def format_ranked_users(totals: dict[str, int]) -> list[str]:
    return [
        f"{user}: {total}"
        for user, total in sorted(totals.items(), key=lambda item: item[1], reverse=True)
    ]