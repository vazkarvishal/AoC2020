

def check_addition_match(number:int, number2:int, number3:int = 0):
  
  total=0
  if number3!=0:
    total = number + number2 + number3
  else:
    total = number + number2 + number3
  
  # print (f"numbers checking are {number} ===== {number2} and total is {total}")
  if total == 2020:
    return True
  else:
    return False

def part_one(number_list):
  for number in number_list:
    for number2 in number_list:
      result_is_2020 = check_addition_match(number, number2)
      if result_is_2020:
        # print(f"Numbers ${number} and ${number2} form a match!!")
        final_result = number * number2
        print(f"Part one final result is {final_result}")

def part_two(number_list):
  for number in number_list:
    for number2 in number_list:
      for number3 in number_list:
        result_is_2020 = check_addition_match(number, number2, number3)
        if result_is_2020:
          # print(f"Numbers ${number} and ${number2} form a match!!")
          final_result = number * number2 * number3
          print(f"Part two final result is {final_result}")


def main_function():
  number_list = []
  with open ('./input.txt') as file:
    for line in file:
      line = line.strip()
      number_list.append(int(line))
  part_one(number_list)
  part_two(number_list)

main_function()