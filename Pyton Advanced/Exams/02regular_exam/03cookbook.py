def cookbook(*args):
    receptions = {}
    result = ""

    for food, cuisine, ingredients in args:
        if cuisine not in receptions:
            receptions[cuisine] = []
        receptions[cuisine].append((food, ingredients))

    sorted_info = sorted(receptions.items(), key=lambda x: (-len(x[1]), x[0]))

    for cuisine, recipes in sorted_info:
        result += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        sorted_recipes = sorted(recipes, key=lambda x: x[0])
        for recipe, ingredients in sorted_recipes:
            result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))

