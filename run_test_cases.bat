 @echo off
(
    @echo.
    @echo --------------------------------------
    @echo Simple Valid Test Case
    @echo python diamond_challenge.py E
    @echo.
    python diamond_challenge.py E
    @echo.

    @echo --------------------------------------
    @echo Test case for A
    @echo python diamond_challenge.py A
    @echo.
    python diamond_challenge.py A
    @echo.

    @echo --------------------------------------
    @echo Invalid Test case
    @echo.
    @echo python diamond_challenge.py Invaild_input
    @echo.
    python diamond_challenge.py Invaild_input
    @echo.
    
    @echo --------------------------------------
    @echo Invalid Test case Asterisk
    @echo.
    @echo python diamond_challenge.py *
    @echo.
    python diamond_challenge.py *
    @echo.

    @echo --------------------------------------
    @echo Keyboard Entry of Z
    @echo.
    @echo Note: Z does not appear after the prompt
    @echo due to limitations in Bash.
    @echo.
    @echo python diamond_challenge.py
    @echo.
    python diamond_challenge.py < automated_test_inputs\test_input_Z.txt

    @echo --------------------------------------
    @echo Too Many Command Line Arguments
    @echo Followed by input of B 
    @echo.
    @echo Note: B does not appear after the prompt 
    @echo due to limitations in Bash.
    @echo.
    @echo python diamond_challenge.py One Two!
    @echo.
    python diamond_challenge.py One Two! < automated_test_inputs\test_input_B.txt
)> test_output.txt & type test_output.txt
