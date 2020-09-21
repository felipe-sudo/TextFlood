# TextFlood

This is a small program that can be used to spam with a lot of text. Basically this  program is made to run in a n infinite loop that will keep on typing random sentences. You can use it to spam your whatsapp contacts or anywhere you like.

## Installation

You need to install pyautogui

```bash
pip install pyautogui
```

## Usage

```python
import random
import pyautogui
import time

def text_flood():
    store = ("This is a hacking code","This was intended to irritate and disturb others","This was intended to annoy people who we are angry with")

    data = random.choice(store)


    pyautogui.typewrite(data)
    pyautogui.press('enter')

def pause():
    print("Starting the engine...")
    time.sleep(2)
    print("Please be patient...")
    time.sleep(2)
    print("Almost ready...")
    time.sleep(2)
    print("Starting text flooding...")
    
pause()
while True:
    text_flood()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License & Copyright
MIT License

Copyright (c) [2020] [Swastik Sarkar]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
