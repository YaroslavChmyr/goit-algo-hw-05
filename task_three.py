import timeit
from algorithms import kmp_search, boyer_moore_search, rabin_karp_search

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

text1 = read_file('стаття 1.txt')
text2 = read_file('стаття 2.txt')


# Підрядки: один, який дійсно існує в тексті, та інший, вигаданий
existing_substring1 = "Пошук – поширена дія, яка виконується в бізнес-додатках. Розглянемо деякі реалізації відомих алгоритмів пошуку [2] на Java."
existing_substring2 = "Перевага розгорнутого списку над іншими розглянутими структурами даних у використанні пам’яті значною мірою за рахунок того, що зберігається лише факт вподобання"
non_existing_substring = "Цей рядок не існує в тексті!"

search_algorithms = {'Кнута-Морріса-Прата': kmp_search,
                     'Боєра-Мура': boyer_moore_search,
                     'Рабіна-Карпа': rabin_karp_search}

texts = {text1: existing_substring1,
         text2: existing_substring2}

# Порівнюємо швидкість алгоритмів
for algorithm, func in search_algorithms.items():
    article_number = 1
    for text, substring in texts.items():
        measure_existing = timeit.timeit(lambda: func(text, substring), number=50)
        print(f"Час виконання алгоритму {algorithm} для існуючого рядка в статті {article_number}: {measure_existing}")
        measure_nonexisting = timeit.timeit(lambda: func(text, non_existing_substring), number=50)
        print(f"Час виконання алгоритму {algorithm} для неіснуючого рядка в статті {article_number}: {measure_nonexisting}\n")
        article_number += 1

