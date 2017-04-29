# adidas-waiting-room-festivus
Python script that opens multiple sessions of Adidas Splash screen to increase chances of getting limited pairs of shoes
## Requirements:
1. Python 3.6.1 - [https://www.python.org/downloads/](https://www.python.org/downloads/)

   Required modules: selenium, beautifulsoup, virtualenv (optional - but is used in the instructions)

   If you don't have virtualenv and want to be able to follow the directions completely then install it with:

   ```
   pip3 install virtualenv
   ```

   If you don't have pip3 already installed then install it with (assuming you have Python 3.5.x installed):

   ```
   easy_install-3.5 pip
   ```


2. chromedriver

   Neededed to drive Chrome.

   **Mac/Linux** users: Run the bash script get_chrome_driver.sh in the adidas-waiting-room-festivus directory

   ```
   cd adidas-waiting-room-festivus
   chmod 755 get_chrome_driver.sh
   ./get_chrome_driver.sh
   ```

## Installing:

1. Either use git to clone this repository or click on "Download Zip"
2. Navigate to the `adidas-waiting-room-festivus` or `adidas-waiting-room-festivus-master` folder depending on what you did in step 1.

   I will assume that if you are using `git clone` then you already know how to navigate to the appropriate folder. For everyone else, unzip `d3stryr-3stripes-master.zip`.  Then move the folder into your home directory. Then open up a terminal window and type the following to navigate to the `d3stryr-3stripes-master` folder:
   ```
   cd adidas-waiting-room-festivus
   ```

3. Create a virtual environment (only needs to be done once per install):

   ```
   virtualenv -p python3 --no-site-packages env
   ```

4. Activate the virtual environment (needs to be done for once for an active session in your terminal):

   Mac/Linux:
   ```
   source env/bin/activate
   ```

5. Install the requirements (needs to be done once per install):

   ```
   pip3 install -r requirements.txt
   ```

That is all that is needed to install.

## Configuring:

The only file that needs to be modified is `config.ini`.

## Running
If you are starting from a new terminal and the `adidas-waiting-room-festivus-master` folder is in your home directory then navigate (change into) the `adidas-waiting-room-festivus-master` folder:

```
cd adidas-waiting-room-festivus-master
```

Make sure you have activated the virtual environment:

Mac/Linux:
```
source env/bin/activate
```

Then you are ready to run:

Mac/Linux:
```
./run.py
```