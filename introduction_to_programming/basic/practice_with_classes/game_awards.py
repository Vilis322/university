from game_awards import TheGameAwards


winners_dict = {"God of War": "2018",
                "Sekiro: Shadows Die Twice": "2019",
                "The last of us: part two": "2020",
                "It Takes Two": "2021",
                "Elden Ring": "2022"}

for game, year in winners_dict.items():
    winner = TheGameAwards(game, year)
    print(f"Победитель премии игра года: {winner.game}, год победы - {winner.year}.")

