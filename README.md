# 🚗 Tesla Proximity Alert System

A Python-based automation tool to **alert your phone when your Tesla is within a set minutes driving distance** of your chosen location (like your home), using the Tesla API, OpenRouteService, and SMS via Email-to-SMS gateway.

---

## ✨ **Features**

- Fetches your Tesla’s live GPS location using Tesla’s unofficial API.
- Calculates driving ETA from your car to your chosen destination using OpenRouteService.
- Sends you an SMS alert if your car is within x minutes of arrival.
- Fully automated—run on a schedule with a loop or via `cron`.

---

## 🧰 **Tech Stack**

- Python 3
- FastAPI (optional, for future web API)
- TeslaPy (`teslapy`) for Tesla API integration
- Requests for HTTP calls
- OpenRouteService API for directions/ETA
- Email-to-SMS (using Python’s `smtplib`) for notifications

---

## ⚡ **Project Structure**

```
tesla-proximity-alert/
├── app/
│   ├── __init__.py
│   ├── main.py              # Orchestrates everything
│   ├── tesla_api.py         # Fetches Tesla location
│   ├── eta_calculator.py    # Calculates ETA via OpenRouteService
│   ├── notifications.py     # Sends SMS via Email-to-SMS
├── requirements.txt
├── .env                     # Secrets and credentials (not tracked by git)
├── .gitignore
├── README.md
```

---

## 🚀 **Setup Instructions**

### 1. **Clone the Repo**

```bash
git clone https://github.com/XLYN529/tesla-proximity-alert.git
cd tesla-proximity-alert
```

### 2. **Create & Activate a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Set Up the `.env` File**

Create a `.env` file in your project root with the following contents:

```ini
SENDER_EMAIL=yourgmail@gmail.com # Your Gmail to send SMS from
SENDER_PASSWORD=your_gmail_app_password # create an app password using your Gmail or click on the link below
RECIPIENT=1234567890@vtext.com  # Your phone's carrier email gateway address, refer to the list below for U.S. Carriers
TESLA_EMAIL=your_tesla_email
ORS_API_KEY=your_openrouteservice_api_key  # create an account at https://api.openrouteservice.org/, and paste the API key here. (Its free for upto 2000 requests per day)
```
- **Tip:** Use a Gmail [App Password](https://support.google.com/accounts/answer/185833?hl=en) for `SENDER_PASSWORD`.
- For U.S. carriers:  
  - Verizon: `number@vtext.com`  
  - AT&T: `number@txt.att.net`  
  - T-Mobile: `number@tmomail.net`  

### 5. **Test Each Module**

- **SMS test:**  
  ```bash
  python app/notifications.py
  ```
- **Tesla location:**  
  ```bash
  python app/tesla_api.py
  ```
- **ETA calculation:**  
  ```bash
  python app/eta_calculator.py
  ```
- **Automated alert:**  
  ```bash
  python app/main.py
  ```

---

## ⏲️ **Automate With Cron (Optional)**

To run every minute, add this to your crontab (`crontab -e`):

```
* * * * * cd /path/to/tesla-proximity-alert && /path/to/venv/bin/python app/main.py >> /path/to/tesla-proximity-alert/cronlog.txt 2>&1
```

---

## 📝 **Customization**

- **Set your destination coordinates** in `app/main.py`:
  ```python
  DEST_LAT = 40.5000  # Replace with your latitude
  DEST_LON = -74.4500 # Replace with your longitude
  ```
- **Set your desired time radius** in `app/main.py`:
 ```python
  if eta <= x: # Replace x with your desired minutes
  ```

- **Change check interval:**  
  - Edit the `time.sleep()` value or your cron schedule as desired.

---

## ❗ **Notes and Limitations**

- Only works if your Tesla is online (not asleep). The script will attempt to wake it if needed.
- Email-to-SMS gateways depend on your carrier and may have limits/delays.
- All secrets should be in `.env` and **never committed to git**.

---

## 🙌 **Credits**

- [TeslaPy](https://github.com/tdorssers/TeslaPy)
- [OpenRouteService](https://openrouteservice.org/)
- Python

