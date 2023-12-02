#!/usr/bin/env python3

# Answer 90882
# Attempts
# Final 32398920008

# Need to figure out the worry algorithm

"""
Advent of Code 2022 Day 1 Puzzle 1

Usage:
  aoc_d1_p1 <input_file>
        [-r <number_of_rounds> | --rounds <number_of_rounds> ]
        [-w <worry> | --worry <worry> ]
        [-h | --help]
        [--version]

Options:
  input_file   Puzzle Input File
  -r <number_of_rounds> --rounds <number_of_rounds>  Number of Rounds [default: 1]
  -w <worry> --worry <worry>  Devisor [default: 3]
  --version    Show version.
  -h --help    Show this screen.
"""

import pprint
import math
from docopt import docopt
import yaml
import operator
ops = { "+": operator.add, "*": operator.mul }


import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.WARNING)
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(levelname)s - %(message)s')
#formatter = logging.Formatter('')
handler.setFormatter(formatter)
root.addHandler(handler)

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')


class cmd_arguments():
    pass

def pritty_print(stuff):
    return
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stuff)

def docopt_handler():
    args = cmd_arguments()
    arguments = docopt(__doc__)
    args.input_file = arguments['<input_file>']
    args.rounds = int(arguments['--rounds'])
    args.worry = int(arguments['--worry'])
    return args

def process_data(args):
    with open(args.input_file, "r") as stream:
        try:
            #yaml_dict = yaml.safe_load(stream)
            yaml_dict = yaml.load(stream, Loader=yaml.BaseLoader)
        except yaml.YAMLError as exc:
            logging.debug(exc)
    logging.debug(yaml_dict)
    monkeys ={}
    for monkey in yaml_dict:
        # Data Handling
        logging.debug(f"yaml_dict: {monkey}")
        l = monkey.split(" ")
        monkey_id = int(l[1])

        logging.debug(f"Operation: { yaml_dict[monkey]['Operation']}")
        l = yaml_dict[monkey]['Operation'].split(" ")
        operation, value = l[3], l[4]
        value = value.strip()
        if value == "old":
            pass
        else:
            value = int(value)
        yaml_dict[monkey]['Operation'] = operation
        yaml_dict[monkey]['Operation Value'] = value

        logging.debug(f"Test: {yaml_dict[monkey]['Test']}")
        l = yaml_dict[monkey]['Test'].split(" ")
        test = int(l[2])
        yaml_dict[monkey]['Test'] = test

        logging.debug(f"If True: {yaml_dict[monkey]['If true']}")
        l = yaml_dict[monkey]['If true'].split(" ")
        monkey_true = int(l[3])
        yaml_dict[monkey]['If true'] = monkey_true

        logging.debug(f"If False: {yaml_dict[monkey]['If false']}")
        l = yaml_dict[monkey]['If false'].split(" ")
        monkey_false = int(l[3])
        yaml_dict[monkey]['If false'] = monkey_false

        logging.debug(f"Starting items: {yaml_dict[monkey]['Starting items']}")

        items = yaml_dict[monkey]["Starting items"].split(",")
        items = [int(item.strip()) for item in items]
        logging.debug(f"items: {items}")
        yaml_dict[monkey]["Starting items"] = items
        for item in items:
            logging.debug(f"{item}")
        yaml_dict[monkey]["Inspected items"] = 0

        monkeys[monkey_id] = yaml_dict[monkey].copy()

    return monkeys


def monkey_in_the_middle(monkeys, args):
    worry = 0
    
    logging.info(f"Rounds: {args.rounds}")
    for r in range(1, args.rounds + 1):
        for monkey in monkeys:
            logging.info(f"moneky: {monkey}")
            for item in list(monkeys[monkey]['Starting items']):
                ########### Worry Calculation ###########################
                #logging.info(f"item: {item}")
                operation = monkeys[monkey]['Operation']
                operation_value = monkeys[monkey]['Operation Value']
                if operation_value == "old":
                    worry = ops[operation](item,item)
                else:
                    worry = ops[operation](item,operation_value)
                # Part One
                worry = math.floor(worry / args.worry)
                # Part Two
                #worry = worry / 10
                # logging.info(f"worry: {worry}")
                ###########  Push Pop Logic ###########################
                monkeys[monkey]['Starting items'].pop(0)
                monkeys[monkey]["Inspected items"] += 1
                logging.info(f"monkeys[monkey]['Test']: {monkeys[monkey]['Test']}")
                logging.info(f"Test: {monkeys[monkey]['Test']}")
                logging.info(f"Worry: {worry}")
                if worry % monkeys[monkey]['Test'] == 0:
                    monkeys[monkeys[monkey]['If true']]['Starting items'].append(worry)
                    logging.info("True")
                    logging.info(f"Pass To: {monkeys[monkey]['If true']}")
                else:
                    monkeys[monkeys[monkey]['If false']]['Starting items'].append(worry)
                    logging.info("False")
                    logging.info(f"Pass To: {monkeys[monkey]['If false']}")
                #logging.info(f"end moneky loop: {monkeys}")
                pritty_print(monkeys)

        logging.info(f"End of Round {r} =================")
        pritty_print(monkeys)

        logging.warning(f"End of Round {r} =================")
    logging.info(f"Final ============================")
    pritty_print(monkeys)
    for monkey in monkeys:
        print(f"{monkeys[monkey]['Inspected items']}")
    monkey_inspections = [monkeys[monkey]['Inspected items'] for monkey in monkeys]
    print(f"monkey_inspections {monkey_inspections}")
    monkey_max_1 = monkey_inspections.pop(monkey_inspections.index(max(monkey_inspections)))
    monkey_max_2 = monkey_inspections.pop(monkey_inspections.index(max(monkey_inspections)))
    print(f"Final {monkey_max_1 * monkey_max_2}")
    
                

def main():
    """Main Function
    - Handle docopt parameters
    - Read input File
    - Compute Result
    - Print Output
    """
    args = docopt_handler()
    monkeys = process_data(args)
    monkey_in_the_middle(monkeys, args)


if __name__ == "__main__":
    main()
