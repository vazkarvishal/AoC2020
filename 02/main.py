
import re
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

def main():
  
  with open ("./input.txt") as password_collection:
    # part_one(password_collection)
    part_two(password_collection)

def part_one(password_collection):
  all_valid_passwords = 0

  for line in password_collection.readlines():
    min_and_max_occurances, required_letter, password = line.split()
    min_requirement, max_requirement = min_and_max_occurances.split("-")
    required_letter = required_letter.strip(":")
    number_of_occurances = len(re.findall(required_letter, password))
    logging.debug(f"MIN REQ {min_requirement} MAX REQ {max_requirement}")
    logging.debug(f"PASSWORD {password} HAS {number_of_occurances} OF {required_letter}")
    valid_password = number_of_occurances in range(int(min_requirement), int(max_requirement)+1)
    logging.debug(f"PASSWORD {password} is {valid_password}")
    if valid_password:
      all_valid_passwords+=1
      logging.debug(f"increasing count to become {all_valid_passwords}")
    
  logging.info(f"PART 1 ANSWER {all_valid_passwords}")
    
def part_two(password_collection):
  all_valid_passwords = 0

  for line in password_collection.readlines():
    position_of_occurances, required_letter, password = line.split()
    first_position, last_position = position_of_occurances.split("-")
    required_letter = required_letter.strip(":")
    matches = re.finditer(required_letter, password)
    matches_position = [match.start()+1 for match in matches]
    logging.debug(matches_position)
    logging.debug(f"FP {first_position} LP {last_position} MPS {matches_position}")
    if int(first_position) in matches_position:
      if int(last_position) in matches_position:
        pass
      else:
        all_valid_passwords+=1
    elif int(last_position) in matches_position:
      all_valid_passwords+=1
  logging.info(f"PART 2 ANSWER {all_valid_passwords}")



main()