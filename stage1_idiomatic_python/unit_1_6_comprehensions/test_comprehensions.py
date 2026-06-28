from comprehensions import (
    Order,
    expensive_users,
    format_ranked_users,
    paid_totals,
    user_total_map,
)


def test_paid_only_filtering() -> None:
    orders: list[Order] = [
        {"user": "Alice", "total": 100, "paid": True},
        {"user": "Bob", "total": 50, "paid": True},
    ]

    assert paid_totals(orders) == [100, 50]


def test_unpaid_orders_ignored() -> None:
    orders: list[Order] = [
        {"user": "Alice", "total": 100, "paid": True},
        {"user": "Bob", "total": 999, "paid": False},
    ]

    assert paid_totals(orders) == [100]
    assert user_total_map(orders) == {"Alice": 100}
    assert expensive_users(orders, 500) == set()


def test_repeated_users_are_summed() -> None:
    orders: list[Order] = [
        {"user": "Alice", "total": 100, "paid": True},
        {"user": "Alice", "total": 50, "paid": True},
        {"user": "Bob", "total": 30, "paid": True},
    ]

    assert user_total_map(orders) == {
        "Alice": 150,
        "Bob": 30,
    }
    assert expensive_users(orders, 120) == {"Alice"}


def test_ranking_order_is_descending() -> None:
    totals = {
        "Alice": 150,
        "Bob": 30,
        "Charlie": 200,
    }

    assert format_ranked_users(totals) == [
        "Charlie: 200",
        "Alice: 150",
        "Bob: 30",
    ]


def test_empty_input() -> None:
    assert paid_totals([]) == []
    assert user_total_map([]) == {}
    assert expensive_users([], 100) == set()
    assert format_ranked_users({}) == []