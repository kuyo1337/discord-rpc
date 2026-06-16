# Discord RPC

A lightweight Python-based Discord Rich Presence client built on WebSocket RPC.

This project was created as a simple alternative to the more common Node.js implementations. Parts of the WebSocket logic were inspired by Cheddlatron Selfbot and adapted for this project.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the client:

```bash
python main.py
```

## Configuration

Edit `config.py` and configure:

* Your Discord token
* Rich Presence details
* Image assets
* Activity text
* Additional RPC settings

## Notes

* This project uses Discord's RPC WebSocket connection for custom Rich Presence.
* Make sure Discord is running before starting the client.
* Custom image assets must be uploaded in the Discord Developer Portal.
