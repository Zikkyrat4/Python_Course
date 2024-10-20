# TODO Найдите количество книг, которое можно разместить на дискете

size_of_disk = 1.44     # Мб
count_pages = 100
str_in_page = 50
char_in_str = 25
size_of_char = 4        # Байт

one_book = (size_of_char * char_in_str * str_in_page * count_pages) / 1024**2
count_book = int(size_of_disk // one_book)

print("Количество книг, помещающихся на дискету:", count_book)
