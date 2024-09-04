# Rhino Module Placement and Rotation Pattern Management
## Overview
This project provides a Python script for Rhino to assist with module placement and rotation pattern management. It focuses on efficiently managing module placement and rotation while avoiding duplicate configurations.

## Features
- Module duplication and placement
- Generation and management of unique rotation patterns
- Debugging to ensure non-duplicate module placements from all perspectives

## Usage
- Open Rhino.
- Type EditPythonScript into the command line and press Enter.
- Copy and paste the code into the Python script editor that opens.

## Files Description
### rotate_listup_all.py
- Generates all possible rotation patterns based on specified angles and arranges them in a grid.
- After executing the code, click on the module to start the process.
- Due to code structure, the process is divided into two stages. Click the module again after the first stage completes.
### rotate_listup_nodup_WIP.py
- Generates all possible rotation patterns based on specified angles and removes duplicates before arranging them in a grid (planned).
- Currently in the debugging phase and may not function perfectly.
- After executing the code, click on the module to start the process.
- Due to code structure, the process is divided into two stages. Click the module again after the first stage completes.
### random_rotator_line.py
- Randomly generates a specified number of rotation patterns based on angles and places each module in a line, avoiding duplicates.
- After executing the code, click on the module to start the process.
- For example, rotating X, Y, and Z axes by multiples of 45° results in 512 possible patterns. From these, 30 patterns can be randomly selected and output.
### random_rotator_grid.py
- Randomly generates a specified number of rotation patterns based on angles and places each module in a grid, avoiding duplicates.
- For example, generating 25 patterns results in a 5x5 grid. When generating 24 patterns, the layout is adjusted to be close to a 5x5 square.
- After executing the code, click on the module to start the process.
- For example, rotating X, Y, and Z axes by multiples of 45° results in 512 possible patterns. From these, 30 patterns can be randomly selected and output.
