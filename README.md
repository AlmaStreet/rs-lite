# rs-lite

### Getting started

1. Create a virtual environment
```
python3 -m venv venv
```
2. Activate the virtual environment
```
source venv/bin/activate
```
3. Install the required packages 
```
pip install -r requirements.txt
```
4. Run rs-lite
```
python3 rs_afk_menu.py
```
<br>

### Uninstalling

Remove all dependencies
```
pip freeze | xargs pip uninstall -y
```

### Troubleshooting - TKinter
TKinter labels appears to be invisible for Python 3.9
Updating to Python 3.10 or newer will no longer include TKinter, so we need to seperately install a suitable TKinter.

Example for Python 3.11, install and verify TKinter
```
brew install python-tk@3.11
python3 -m tkinter -c "print('Tkinter is working')"
```