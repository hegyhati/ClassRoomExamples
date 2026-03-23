# Example Programming Test


## General instructions

 - In this directory you can find the example for the "1. Teilprüfung". 
 - The test will consists of 1 exercise, that will be built step-by-step.
 - Some subtasks depend on each other, it is suggested to progress by the order given by the first two digits of the filename.
 - In each file, there is:
   - A list of previous task on which this depends, and a place to copy former code from previous file, if needed.
   - Description of the new function/class/method to be written.
   - Tests for the new function/class/method.
 - In grading, we will look at the contents of these files, but feel free to create additional files for sandboxing if it helps you.
 - Regarding the unit tests:
   - They are there to help you. If they pass, your code is probably ok. 
   - You do **not** need to understand how these tests work, feel free to collapse the code of these classes. If your code fails somehow, they should provide understandable feedback to you (without looking into their code).
   - While preparing the solution, they can be annoying. While it is not ready, feel free to 
     - sandbox the solution first in another file (e.g. `tmp.py`) 
     - or comment out `unittest.main()`.

## Rules

You may use:
 - code from previous classes
 - your written notes
 - online python references/tutorials

You may **not** use:
 - Generative AI
 - Chats/forums/etc. with other people

## General topic

The goal is to develop a system, that allows the user to:
 1. Register POIs
 2. Maintain a "database" (JSON) of how many times these POIs were visited. 
 3. Parse `.gpx` files, and increase POI-visit statistics in the DB

