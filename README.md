# StreamableChecker

Filter your Streamables and remove invalid/not-working Streamables just in a few clicks!

![](https://img.shields.io/github/v/release/smokedzn/StreamableChecker) ![](https://img.shields.io/github/last-commit/smokedzn/StreamableChecker) 

## Installation
If you don't already use **Python**, you will need it for this Script to work.

#### **Windows:**
1. Using PowerShell (**_winget_**)
```console
  winget install Python.Python.3.9 
```
2. Manual Download

[Python Releases for Windows](https://www.python.org/downloads/windows/)


#### **Linux:**

1. Using Terminal (**_apt-get_**) 
```console
  sudo apt-get install python3
```
2. Using Terminal (**_dnf_**) 
```console
  sudo dnf install python3
```
3. Manual Download

[Python Releases for Linux](https://www.python.org/downloads/source/)

## Usage
1. Create a Folder with your Text-File containing your Streamable URLs (Row-by-Row) **and** the Python-Script `StreamableCheck.py` inside.
2. Open your Terminal at the Folder you just created.
3. Simply run the script using `python StreamableCheck.py [YourTextFile.txt]`.
4. Wait until the Script has finished filtering all the URLs.

**Warning**: Make sure you filter your list 3-4 times by only using the list containing the **invalid** URLs to make sure network errors/timeouts aren't seen as a invalid URL. 

## Troubleshoot

#### Valid URLs are flagged as Invalid.
Rename your File with the Valid URL's and use the List containing all the Invalid URL's as your List to Filter them again (2-3 times). After you ran the Script again, add the valid URL's from the second run to the renamed file. The more you repeat this, the better the result will be.

#### Your Script is too slow.
You can change the number of workers inside the script. However it is not recommended, since the more requests are made, the more false-flags will happen.
