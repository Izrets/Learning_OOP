# Написать функцию, которая принимает список чисел и возвращает True, если в нем есть хотя
# бы два одинаковых числа. Написать тесты с использованием unittest и pytest.
class Dvachisla:

    def inputOfTwo(list1, list2):
        count = 0
        for i in list1:
            if i in list2:
                count += 1
        if count >= 2:
            return True
        else:
            return False




