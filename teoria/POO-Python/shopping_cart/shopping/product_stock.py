class ProductStock:
  def __init__(self, name, value, quantity):
    self._name = name
    self._value = value
    self._quantity = quantity

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, value: str) -> None:
    self._name = value

  @property
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str) -> None:
    self._value = value

  @property
  def quantity(self) -> str:
    return self._quantity

  @quantity.setter
  def quantity(self, value: str) -> None:
    self._quantity = value

  def __str__(self):
    return f"\nname:\t\t{self._name}\nvalue:\t{self._value}\nquantity:\t{self._quantity}\n"


