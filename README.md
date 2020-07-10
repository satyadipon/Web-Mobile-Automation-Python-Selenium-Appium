# Setup

1. Install Python 
2. Install Selenium
   ```sh
   pip3 install selenium
   ```
3. Install pytest
    ```sh
   pip3 install pytest
   ```
4. Install Webdriver-client
    ```sh
   pip3 install webdriver_manager
   ```
5. Install Appium-Python-Client
   ```sh
   pip3 install Appium-Python-Client
   ```
6. Install Android Studio and configure an emulator
7. Install Appium Desktop
8. Clone this repository and open a shell in the folder of this repo

   Your setup is ready to run the tests
   
### For Web Test, run:

   ```sh
   py.test -v -s tests/web_test.py  
   ```

### For mobile-android Test, run:

   ```sh
    py.test -v -s tests/mobile_test.py  

   ```