## What does this scraper do?
This simple Selenium-based scraper extracts the price of any product from the Wildberries online marketplace using its product code (articul). It is intended for future use in other projects, most likely a Telegram bot.

## How does it work?
The script automatically launches a browser in the background (headless mode) and navigates to the specific product page on Wildberries using its unique item number. It waits for the page to load completely, locates the price element, and extracts the numerical value from it. Finally, the script closes the browser and returns the found price as a clean numerical string, or reports an error if something goes wrong during the process.

## Requirements
- Selenium (pip install selenium)
- Chrome browser
- ChromeDriver

### ChromeDriver Setup (if you don't have)
Check your Chrome version:
- Open Chrome → Settings → About Chrome
- Note the version number (e.g., 128.0.6613.120)
- Download matching ChromeDriver: Go to https://chromedriver.chromium.org/

Download the same version as your Chrome browser:
- Install ChromeDriver:
- Extract the downloaded file
- Add the folder to your system PATH
