# Написать функцию, которая принимает список чисел и возвращает True, если в нем есть хотя
# бы два одинаковых числа. Написать тесты с использованием unittest и pytest.


class Dvachisla:

    def inputOfTwo(self, l1, l2):
        self.list1 = l1
        self.list2 = l2
        count = 0
        for i in l1:
            if i in l2:
                count += 1
        if count >= 2:
            return True
        else:
            return False




