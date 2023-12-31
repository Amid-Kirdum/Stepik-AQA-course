# Если значение выражения истинно, то в консоли не должно появиться дополнительных сообщений
assert abs(-42) == 42

# # если условие не выполнено, то в консоли выводится лог ошибки с названием файла и номером строчки,
# # в которой произошла ошибка, а также тип ошибки AssertionError
# assert abs(-42) == -42

# Для добавления дополнительного сообщения можно при вызове assert через запятую написать нужное сообщение,
# которое будет выведено в случае ошибки проверки результата
assert abs(-42) == -42, "Should be absolute value of a number"