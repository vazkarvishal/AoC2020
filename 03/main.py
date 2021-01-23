import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

def required_characters_calculation(steps_to_right):
  lines = open("./input.txt", "r").readlines()
  characters_in_one_line = len(lines[0].strip())
  lines_before_game_over = int(characters_in_one_line/steps_to_right)
  number_of_lines_in_file = len(lines)
  logging.debug(f"CHARACTERS IN A LINE {characters_in_one_line} NUMBER OF LINES {number_of_lines_in_file} CURRENT LIMIT {lines_before_game_over}")

  chars_required_to_complete_game = int((number_of_lines_in_file * characters_in_one_line)/lines_before_game_over)
  logging.debug(f"CHARS REQUIRED TO COMPLETE GAME {chars_required_to_complete_game}")

  # Adding 1 to avoid 0 index calculation errors
  duplicate_string_by = int(chars_required_to_complete_game/characters_in_one_line)+1
  logging.debug(f"Multiply current chars by {int(chars_required_to_complete_game/characters_in_one_line)}")

  logging.debug(f" Characters in each line after manupilation = {len(lines[0].strip() * duplicate_string_by)}")

  # writing_file = open("./output.txt", "w")

  manipulated_list: list = []
  for line in lines:
    manipulated_list.append(line.strip() * duplicate_string_by)
    # writing_file.writelines(line.strip() * duplicate_string_by)

  return manipulated_list
  # writing_file.close()

def move_toboggan(directions_to_airport, steps_to_right, steps_down):

  move_right = 0
  trees = 0
  step_down_counter = steps_down
  for idx, route in enumerate(directions_to_airport):
    if idx != 0 and steps_down == 1:
      logging.debug(f"Moving by {move_right} and found {route[move_right]}")
      if route[move_right] == "#":
        logging.debug("adding tree")
        trees+=1
    elif idx != 0 and steps_down != 1:
      logging.debug(f"step_down is {steps_down}")
      if steps_down <= len(directions_to_airport) and directions_to_airport[steps_down][move_right] == "#":
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
    directions_to_airport = required_characters_calculation(int(step_right))
    trees_found = move_toboggan(directions_to_airport, int(step_right), int(step_down))
    logging.info(f" trees found on our way are {trees_found}")
    trees_found_in_all_slopes = trees_found_in_all_slopes*trees_found
  logging.info(f" total trees found on our way are {trees_found_in_all_slopes}")
if __name__ == "__main__":
  main()

