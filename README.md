# autoscan-tg-qr
This is a script to automatically scan and accept new login for telegram desktop client.
Made with telethon and you need telethon StringSession.

## How to install

Simply clone the repo and install requirements

### Clone

```bash
git clone https://github.com/viraj-bookanna/autoscan-tg-qr.git
```

### Installing requirements

```bash
cd autoscan-tg-qr
```

```bash
pip install -r requirements.txt
```

## Usage

You have to set environment variables with .env file or in yor system

Example .env file

```
API_ID=00000000
API_HASH=00000000000000000000000000000000
```

Start the scanner in background and switch to telegram desktop:

```bash
python scanner.py
```

Have Fun !