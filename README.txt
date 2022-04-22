We use python3 version 3.9.6. This project requires pysat library and pygame for GUI, so we have to install it.

Here is some installation guide of setting up pysat package:

1. Run terminal on window.

2. Upgrade pip first, run command: "python -m pip install --upgrade pip".

3. To install pysat package, run command: "python -m pip install python-sat[pblib,aiger]".

4. To install pygame library, run command: "python -m pip install pygame".

WARNING: If you have error while downloading pysat package, please CLEAR ALL python in your computer then install new python version 3.9.6. After downloading python successfully, please turn back to step 1.

-----------------------------------------------------
Here is introduction to running tasks' python files:

1. When running Task_c.py, it will create 2 txt files, which are Level1_CNF.txt and Level2_CNF.txt. This two files contains CNF clauses of Level 1 and Level 2.

2. When running Task_d.py, it will print out the result of chessboard.

3. When running Task_e.py, please enter the input file name on console screen, it will print out the initate board with some first coordinate(s) from the input file and the result chessboard after running A* algorithm.

4. When running Task_f.py, please type the input file name to the black-border box (WARNING: If you enter the unexist file, the program will automatically quit!). Then, press ENTER on your keyboard, the some first queen(s) will appear on the chessboard. In the next step, press on the button SEARCH, the rest of queens will appear one after another.