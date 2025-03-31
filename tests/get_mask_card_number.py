import unittest

def get_mask_card_number(card_number): # Замените на вашу реальную функцию
  """
  Маскирует номер карты, заменяя цифры между первыми 6 и последними 4 символами на звездочки (*).
  """
  if not isinstance(card_number, str):
    return "Invalid input"
  if len(card_number) < 10:
      return card_number # Или можно возвращать "Invalid card number" или "" - зависит от требований
  return card_number[:6] + '*' * (len(card_number) - 10) + card_number[-4:]

class TestGetMaskCardNumber(unittest.TestCase):

    def test_valid_card_number(self):
        """Тест на стандартный номер карты"""
        self.assertEqual(get_mask_card_number("1234567890123456"), "123456******3456")

    def test_card_number_with_spaces(self):
        """Тест на номер карты с пробелами"""
        self.assertEqual(get_mask_card_number("1234 5678 9012 3456"), "1234 56******3456")

    def test_card_number_with_dashes(self):
        """Тест на номер карты с дефисами"""
        self.assertEqual(get_mask_card_number("1234-5678-9012-3456"), "1234-56******3456")

    def test_short_card_number(self):
        """Тест на номер карты менее 10 символов"""
        self.assertEqual(get_mask_card_number("123456789"), "123456789") # Или измените ожидаемый результат, если ваша функция должна обрабатывать такие случаи по-другому.

    def test_long_card_number(self):
        """Тест на номер карты больше стандартной длины (16 символов)"""
        self.assertEqual(get_mask_card_number("12345678901234567890"), "123456**********7890")

    def test_empty_card_number(self):
        """Тест на пустую строку"""
        self.assertEqual(get_mask_card_number(""), "") # или какой результат ожидаете в этом случае

    def test_invalid_input_type(self):
        """Тест на не строковый ввод"""
        self.assertEqual(get_mask_card_number(1234567890123456), "Invalid input")
        self.assertEqual(get_mask_card_number(None), "Invalid input")
        self.assertEqual(get_mask_card_number([1,2,3]), "Invalid input")

    def test_card_number_with_letters(self):
        """Тест на номер карты с буквами (может быть неверным номером)"""
        self.assertEqual(get_mask_card_number("123456ABCDEF3456"), "123456******3456")

    def test_card_number_with_special_characters(self):
        """Тест на номер карты со специальными символами (может быть неверным номером)"""
        self.assertEqual(get_mask_card_number("123456!@#$%^3456"), "123456******3456")

if __name__ == '__main__':
    unittest.main()
