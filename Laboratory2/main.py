import random
from typing import *

quick_sort = lambda list: sorted(list)

def find_el(list: List, element: Any):
  try:
    el_index = list.index(element)
    print(f"Element \"{list[el_index]}\" at index [{el_index}]")
    return el_index
  except ValueError:
    return False

def find_few_els(list: List, elements_list: List):
  result = []
  for el in elements_list:
    found_index = find_el(list, el)
    if found_index != False:
      result.append(tuple([found_index, el]))
  return result.sort(key = lambda item: item[0])