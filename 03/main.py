import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

def move_toboggan(steps_to_right, steps_down):

  lines = open("./input.txt", "r").readlines()
  characters_in_one_line = len(lines[0].strip())
  move_right = 0
  trees = 0
  step_down_counter = steps_down
  for idx, route in enumerate(lines):
    if idx != 0 and steps_down == 1:
      logging.debug(f"Moving by {move_right} and found {route[move_right % characters_in_one_line]}")
      if route[move_right % characters_in_one_line] == "#":
        logging.debug("adding tree")
        trees+=1
    elif idx != 0 and steps_down != 1:
      logging.debug(f"step_down is {steps_down}")
      if steps_down <= len(lines) and lines[steps_down][move_right % characters_in_one_line] == "#":
        logging.debug(f"adding tree at index {steps_down}")
        trees+=1
      steps_down = steps_down + step_down_counter
    move_right+=steps_to_right
    logging.debug(f"move right is now {move_right}")
  return trees

def main():

  list_of_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  trees_found_in_all_slopes = 1
  for slope in list_of_slopes:
    trees_found = 0
    step_right, step_down = slope
    logging.debug(f"right is {step_right} down is {step_down}")
    # directions_to_airport = required_characters_calculation(int(step_right))
    trees_found = move_toboggan(int(step_right), int(step_down))
    logging.info(f" trees found on our way are {trees_found}")
    trees_found_in_all_slopes = trees_found_in_all_slopes*trees_found
  logging.info(f" total trees found on our way are {trees_found_in_all_slopes}")
  
if __name__ == "__main__":
  main()

