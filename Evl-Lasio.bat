@echo off
setlocal enabledelayedexpansion

if not exist "Input" (
    mkdir "Input"
    echo Created "Input" folder.
) else (
    echo "Input" folder already exists.
)

if not exist "Output" (
    mkdir "Output"
    echo Created "Output" folder.
) else (
    echo "Output" folder already exists.
)

:begin
cls
echo Listing all .evl files in the "Input" folder:
echo:
set /a i=1
for %%f in (Input\*.evl) do (
    echo !i!. %%f
    set "file!i!=%%f"
    set /a i+=1
)

if %i%==1 (
    echo No .evl files found in the "Input" folder.
    echo:
    pause
    exit /b
)

echo:
set /p choice=Enter the number of the .evl file you want to translate:
set selected_file=!file%choice%!

if not defined selected_file (
    echo Invalid selection. Exiting.
    exit /b
)

echo Translating !selected_file! to C...
python EvlTranslator.py "!selected_file!" "Output"

set filename=!selected_file:Input\=!
set c_file=Output\!filename:.evl=.c!

if not exist "!c_file!" (
    echo Translation failed. No .c file found in the "Output" folder.
    exit /b
)

echo Compiling !c_file!...
gcc "!c_file!" -o Output\Output.exe

if errorlevel 1 (
    echo Compilation failed. Exiting.
    exit /b
)

cls

echo Running the program...
echo:
Output\Output.exe

:ask_again
echo.
echo:
set /p userchoice=Do you want to translate another file? (y/n): 

if /i "%userchoice%"=="y" (
    goto begin
) else if /i "%userchoice%"=="n" (
    echo:
    echo Exiting the program.
    exit /b
) else (
    echo:
    echo Invalid choice. Please enter y or n.
    goto ask_again
)

endlocal
