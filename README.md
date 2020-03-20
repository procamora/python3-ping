# python3-ping


This library provides an easy way to manage a sqlite database. To do this, use the _sqlite3_ library to connect to the database and the _logging_ library to display information about errors and debugging.



# Installation

Installation can be done through the _pip3_ command:



```bash
pip3 install procamora-sqlite3 --user
```


You can also update the library with:



```bash
python3 -m pip install --user --upgrade procamora-sqlite3
```



# Basic Usage


To use this class the first thing to do is import the library:


```python
from procamora_sqlite3.logger import get_logger, logging
from procamora_sqlite3.interface_sqlite import *
```

The _interface_sqlite_ file when doing an _import *_ we are importing three functions, these are:


```python
__all__ = ['conection_sqlite', 'execute_script_sqlite', 'dump_database']
```

## conection_sqlite

This function is responsible for carrying out the main SQL operations, such as: _SELECT_, _INSERT_, _UPDATE_ or _DELETE_.


An example of some of these functions would be:


```python
def select_all_hosts() -> List[Dict[Text, Any]]:
    query: Text = "SELECT * FROM Hosts"
    response_query: List[Dict[Text, Any]] = conection_sqlite(self.db, query, is_dict=True)
    return response_query

def update_host_offline(date: Text):
    query: Text = f"UPDATE Hosts SET active=0 WHERE date <> '{date}';"
    conection_sqlite(self.db, query)
```


## execute_script_sqlite


This function allows you to run a script or dump that you receive in string format. With this function, databases could be created.


```python

execute_script_sqlite(self.db, self.dump.read_text())
```

## dump_database


This function allows you to perform a complete dump of the database.




```python
response = dump_database(self.db)
```



