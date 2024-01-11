#!/bin/bash
## Copyright (c) Microsoft Corporation. All rights reserved.

import sys

if __name__ == '__main__':

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 get_core.py <entity_id> <thread_id>")
        sys.exit(1)  # Exit with an error code

    # Access command-line arguments
    entity_id = sys.argv[1]
    thread_id = sys.argv[2]

    # Display the values of arguments
    # print(f"entity_id:{entity_id} thread_id:{thread_id}")

    entity_match = False
    # Open a file in read mode ('r')
    file_path = 'thread_list.txt'
    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            sline = line.split(':')
            len_sline = len(sline)

            if len_sline == 4:
                entity = sline[0].strip()
                core = sline[1].strip()
                thread = sline[2].split('/')[0].strip()
                entity_match = True if (entity_id in sline[0]) else False
            elif len_sline == 3:
                if entity_match:
                    core = sline[0].strip()
                    thread = sline[1].split('/')[0].strip()
            elif len_sline == 2:
                if entity_match:
                    thread = sline[0].split('/')[0].strip()

            if entity_match:
                if thread == thread_id:
                    print(core)
                    sys.exit(1)
    sys.exit(0)
