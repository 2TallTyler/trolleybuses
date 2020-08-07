@ECHO OFF

ECHO Batch: Running Python file merger
python %~dp0\nmlc\merge_nml.py

ECHO Batch: Copying merged file to src/merged directory
copy /y /v %~dp0\nmlc\2cc_trolleybuses.nml %~dp0\src\merged\2cc_trolleybuses.nml

ECHO Batch: Running NMLC compiler
%~dp0\nmlc\nmlc -c -t src\custom_tags.txt -l src\lang --grf 2cc_trolleybuses.grf nmlc\2cc_trolleybuses.nml

ECHO Batch: Cleaning up
DEL %~dp0\nmlc\2cc_trolleybuses.nml

set /P c=Complete!
if /I "%c%" EQU "TT" (goto :copy
) else (exit)

:copy
ECHO Copying to NewGRF directory
copy /y /v %~dp0\2cc_trolleybuses.grf C:\Users\train\Documents\OpenTTD\newgrf\
pause
exit
