# QuitNow — Home Assistant Integration

A custom Home Assistant integration that pulls your [QuitNow](https://quitnowapp.com) stats into Home Assistant as sensors.

## Sensors

| Sensor | Unit | Description |
|---|---|---|
| Days Smoke Free | days | Total days since you quit |
| Cigarettes Avoided | — | Total cigarettes not smoked |
| Money Saved | currency | Money saved since quitting |
| Days Won Back | days | Life days regained |

## Installation

### Manual

1. Copy the `custom_components/quitnow` folder into your Home Assistant `custom_components` directory.
2. Restart Home Assistant.

### HACS

Coming soon.

## Setup & Configuration

### 1. Find Your QuitNow Nickname

1. Open the QuitNow app on your phone
2. Go to **Profile** (usually bottom right or in the menu)
3. Your **nickname** is displayed at the top of your profile
4. Write it down or copy it

### 2. Find Your Access Token

1. Open [QuitNow](https://quitnow.app) in a web browser (Chrome recommended)
2. Make sure you're **logged in**
3. Open **Chrome DevTools** by pressing **Ctrl+Shift+I** (or **F12**)
4. Go to the **Network** tab
5. **Refresh the page** (Ctrl+R or F5)
6. Look for a request that starts with `loginV2?nick=...&access=...`
7. Click on that request to open its details
8. In the **Headers** section, look at the **Request URL**
9. Find the `access=` parameter in the URL
10. Copy the long string that comes after `access=` — **that's your access token**

**Example URL:**
```
https://api.quitnow.app/quitnow-server/users/loginV2?nick=YourNickname&os=w&app=14005000&t=f&access=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```
The part starting with `eyJ...` is your token.

### 3. Add Integration to Home Assistant

1. Go to **Settings → Devices & Services → Create Automation** and search for **QuitNow**
2. Enter your **nickname** and **access token**
3. Click **Submit**
4. Your QuitNow sensors will appear under a new device

## Usage

Once added, you'll have 4 sensors:
- **Days Smoke Free** — How many days since you quit
- **Cigarettes Avoided** — Total cigarettes you didn't smoke
- **Money Saved** — Total money you've saved
- **Days Won Back** — Days of life you've regained (based on health improvements)

You can use these in automations, templates, and dashboards.

## Troubleshooting

### "Could not connect" error

- Double-check your **nickname** — make sure it's spelled correctly (case-sensitive)
- Make sure your **access token** is complete — it's a long string starting with `eyJ`
- Make sure you copied the token from the `access=` parameter in the URL, not from elsewhere

### Token not found

- Make sure you're logged into QuitNow before opening DevTools
- Make sure you refreshed the page **after** opening the Network tab
- Try opening the QuitNow app in a different browser (Firefox, Safari) to see if the token appears differently

## Disclaimer

This integration uses QuitNow's **unofficial mobile API**. It is not affiliated with or endorsed by QuitNow. The API may change at any time, which could break the integration. Use at your own risk.

## License

MIT
