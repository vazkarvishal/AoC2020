

def check_addition_match(number:int, number2:int):
  total = int(number) + int(number2)
  # print (f"numbers checking are {number} ===== {number2} and total is {total}")
  if total == 2020:
    return True
  else:
    return False

def main_function():
  number_list = []
  with open ('./input.txt') as file:
    for line in file:
      line = line.strip()
      number_list.append(line)

  number_list_2 = number_list 

  for number in number_list:
    for number2 in number_list_2:
      result_is_2020 = check_addition_match(number, number2)
      if result_is_2020:
        print(f"Numbers ${number} and ${number2} form a match!!")
        final_result = int(number) * int(number2)
        print(f"Final result is {final_result}")

        


main_function()