import unittest

def get_mask_account(account_number):
  """
  Маскирует номер счета, оставляя видимыми только последние несколько цифр.

  Args:
    account_number: Строка, представляющая номер счета.

  Returns:
    Строка, представляющая замаскированный номер счета.
    Возвращает пустую строку, если account_number - пустая строка или None.
  """
  if not account_number:
    return ""

  visible_digits = 4  # Количество видимых цифр
  mask = "*" * (len(account_number) - visible_digits)
  return mask + account_number[-visible_digits:]


class TestGetMaskAccount(unittest.TestCase):

  def test_valid_account_number(self):
    self.assertEqual(get_mask_account("1234567890123456"), "************3456")

  def test_short_account_number(self):
    self.assertEqual(get_mask_account("1234"), "****")  # All masked

  def test_account_number_shorter_than_visible_digits(self):
    self.assertEqual(get_mask_account("123"), "***")

  def test_account_number_empty_string(self):
    self.assertEqual(get_mask_account(""), "")

  def test_account_number_none(self):
    self.assertEqual(get_mask_account(None), "") # None is implicitly converted to empty string due to the condition in function

  def test_account_number_with_spaces(self):
    self.assertEqual(get_mask_account("1234 5678 9012 3456"), "***************3456")

  def test_account_number_with_non_numeric_characters(self):
      self.assertEqual(get_mask_account("1234-5678-9012-ABCD"), "***************ABCD")


if __name__ == '__main__':
  unittest.main()
