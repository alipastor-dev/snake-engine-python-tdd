from logic.food import Food


def test_food_position():
    initial_food_position = (5, 5)
    food = Food(initial_food_position)

    assert food.position == initial_food_position
