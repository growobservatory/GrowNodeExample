# GrowNodeExample
This code reads from the Thingful node, gets  list of all Sensors

The code then reads through the list of sensors and counts the number with a location of
zero 

Then displays percentage that are zero locations

## Dependencies 
- python2 or python3
- [pip](https://pip.pypa.io/en/stable/installing/) - the recommended tool for installing Python packages.
- [requests](http://docs.python-requests.org/en/master/) - http requests library

## Run the script
This script requires python.
To verify that python is already installed on your machine run 
```
python --version
```
If the command above returns something like `Python 2.7.10` then python is already installed. If not you can download it [here](https://www.python.org/downloads/).
Further instructions can be found on the [official documentation](http://docs.python-guide.org/en/latest/starting/installation/)

The next step is to install the required dependencies. We recommend using `pip`.
Verify that pip is installed by running 
```
pip --version
```
If pip is not installed follow the step described on the [official documentation](https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) 

You can install dependencies with :
```
pip install -r requirements.txt
```
Alternatively you can install individual packages running:
```
pip install <package-name>
```

Finally run the script with
```
python Get.py <your-api-key>
```

## Obtaining API Keys
Users must be authenticated using their [API key](https://en.wikipedia.org/wiki/Application_programming_interface_key) when interacting with the GROW Node.
In order to obtain a key please contact
- dev@thingful.net 

## Documentation for GROW node
https://growobservatory.github.io/ThingfulNode/#tag/Locations



