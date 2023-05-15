# olimpiadas-teleco-python
This is a subproject of [olimpiadas-teleco](https://github.com/dangarcar/olimpiadas-teleco)
A Python http server to run the esp32 project's website 

> :warning: You'll have to install python3 to execute this script.

# How to use
1. Download the this repo the way you want (.zip download, git clone, etc.).

2. Connect the olimpiadas-teleco's esp32 SD card to your computer and search for a file called `data.db` in it.

3. Go to the folder where you have downloaded the repo and open up a terminal there.

4. Execute the following command:
```shell
python -m main.py {YOUR_data.db_PATH}
```

5. Now search for localhost:8000 in the browser, the webpage will hopefully be there.