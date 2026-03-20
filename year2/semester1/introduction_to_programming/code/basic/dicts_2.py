d = {
  "name": "Помесячное количество выступлений и гонораров на 2021 год",
  "artists": [
    {
      "name": "Паста",
      "musical_style": "rap",
      "monthly_calendar": [20, 14, 13, 19, 27, 22, 14, 7, 23, 6, 5, 6],
      "fee": [2, 21, 26, 0, 11, 0, 14, 12, 9, 25, 17, 18]
    },
    {
      "name": "Клавец",
      "musical_style": "rap",
      "monthly_calendar": [6, 2, 0, 2, 6, 0, 2, 7, 3, 9, 1, 1],
      "fee": [3, 6, 0, 1, 4, 6, 2, 7, 3, 0, 7, 4]
    },
    {
      "name": "Злой Мух",
      "musical_style": "rap",
      "monthly_calendar": [23, 18, 21, 20, 4, 6, 22, 13, 19, 9, 9, 25],
      "fee": [13, 16, 10, 27, 1, 6, 1, 4, 10, 19, 7, 23]
    },
    {
      "name": "Мультик",
      "musical_style": "rap",
      "monthly_calendar": [6, 23, 8, 10, 18, 7, 11, 11, 25, 10, 5, 9],
      "fee": [16, 21, 16, 26, 3, 28, 28, 19, 3, 25, 17, 0]
    },
    {
      "name": "Опера",
      "musical_style": "rap",
      "monthly_calendar": [25, 5, 17, 16, 12, 29, 24, 15, 2, 24, 6, 1],
      "fee": [24, 29, 0, 26, 12, 0, 17, 8, 25, 17, 17, 9]
    },
    {
      "name": "Натулис Пампулис",
      "musical_style": "rap",
      "monthly_calendar": [7, 20, 18, 12, 5, 28, 20, 11, 21, 2, 18, 4],
      "fee": [6, 28, 27, 11, 1, 20, 8, 23, 2, 23, 6, 15]
    },
    {
      "name": "Паста",
      "musical_style": "rock",
      "monthly_calendar": [14, 22, 15, 15, 22, 19, 4, 13, 23, 21, 2, 3],
      "fee": [4, 7, 15, 28, 27, 4, 13, 13, 5, 7, 20, 17]
    },
    {
      "name": "Мультик",
      "musical_style": "rock",
      "monthly_calendar": [6, 6, 15, 10, 2, 17, 25, 29, 18, 26, 7, 28],
      "fee": [12, 12, 15, 4, 23, 5, 26, 17, 9, 17, 0, 4]
    },
    {
      "name": "Злой Мух",
      "musical_style": "rock",
      "monthly_calendar": [0, 8, 4, 21, 1, 23, 24, 14, 6, 27, 28, 11],
      "fee": [11, 4, 8, 26, 0, 28, 24, 20, 8, 8, 24, 11]
    },
    {
      "name": "Мультик",
      "musical_style": "djs",
      "monthly_calendar": [25, 20, 14, 18, 17, 3, 18, 18, 2, 24, 9, 6],
      "fee": [19, 9, 11, 23, 13, 27, 16, 12, 1, 29, 21, 24]
    },
    {
      "name": "Опера",
      "musical_style": "djs",
      "monthly_calendar": [7, 21, 1, 25, 16, 0, 14, 9, 18, 18, 9, 3],
      "fee": [25, 12, 2, 9, 6, 29, 21, 16, 18, 23, 6, 14]
    },
    {
      "name": "Натулис Памулис",
      "musical_style": "djs",
      "monthly_calendar": [19, 21, 4, 4, 4, 4, 25, 22, 22, 11, 16, 3],
      "fee": [7, 13, 25, 17, 6, 5, 25, 22, 19, 22, 3, 9]
    }
  ]
}

styles_income = {}  # словарь для хранения сумм доходов по стилям музыки

for artist in d["artists"]:
    style = artist["musical_style"]
    income = sum(artist["fee"])
    if style not in styles_income:
        styles_income[style] = income
    else:
        styles_income[style] += income

max_income_style = max(styles_income, key=styles_income.get)

# Нахождение месяца с максимальным доходом для музыкального стиля
max_month_income = [0] * 12
for artist in d["artists"]:
    if artist["musical_style"] == max_income_style:
        for i in range(12):
            max_month_income[i] += artist["fee"][i]
max_month = max_month_income.index(max(max_month_income)) + 1

min_income = float('inf')
lowest_earning_artist = ""

for artist in d["artists"]:
    if artist["fee"][max_month - 1] < min_income:
        min_income = artist["fee"][max_month - 1]
        lowest_earning_artist = artist["name"]

print(f"Музыкальный стиль, который приносит музыкантам больше всего денег: {max_income_style}")
print(f"Номер месяца в году, в котором на этом стиле можно заработать больше всего: {max_month}")
print(f"Название музыкальной группы, которая меньше всего зарабатывает в этом месяце: {lowest_earning_artist}")
