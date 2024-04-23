from rx.subject import Subject
from collections import defaultdict

# Создаем реактивную переменную для подсчета голосов
votes = Subject()

# Создаем словарь для подсчета голосов по кандидатам
votes_count = defaultdict(int)


# Функция для подсчета голосов
def count_votes(vote, votes_count):
    votes_count[vote] += 1
    return votes_count[vote]  # Возвращаем только значение, а не весь словарь


# Подписываемся на голоса и выводим результат
votes.subscribe(
    lambda vote: print(f"Получен голос за вариант {vote}. Общее количество голосов: {count_votes(vote, votes_count)}."))

print("Для окончания голосования введите 'exit'")
while True:
    vote = input("Введите свой голос: ")
    if vote == 'exit':
        break
    else:
        votes.on_next(vote)

# Преобразуем votes_count в обычный словарь для вывода
result_dict = dict(votes_count)
print("Голосование завершено. Итоговый подсчет голосов:", result_dict)
