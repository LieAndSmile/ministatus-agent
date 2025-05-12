Here’s a clean, concise `README.md` for your new `ministatus-agent` repo — written for both home lab users and freelancers who want to monitor remote systems via your MiniStatus project:

---

## 📡 MiniStatus Agent

**MiniStatus Agent** is a lightweight push script that reports basic system health data to a central [MiniStatus](https://github.com/LieAndSmile/MiniStatus-MVP) dashboard.

> 💡 Designed for DevOps freelancers, homelabs, and secure remote monitoring
> 🛰️ Push-based — no need to expose your server to inbound traffic
> 🔐 Works over HTTPS with API key authentication

---

## 🚀 Features

* 🖥️ Reports: hostname, uptime, load average, disk space
* 🔐 Authenticated with API key
* 🌐 Sends data to `/report` endpoint via HTTPS
* 🧩 Configurable via `.env`
* ⚙️ Easy to schedule with `cron` or `systemd`

---

## 🛠️ Usage

### 📦 Requirements

* Python 3.7+
* `pip install requests python-dotenv`

---

### 🧪 Example `.env`

Create a `.env` file in the same folder:

```env
MINISTATUS_URL=https://yourdomain.com/report
MINISTATUS_KEY=your-api-key
MINISTATUS_NAME=client-vps-1
```

> `MINISTATUS_NAME` will be used as the service name on the dashboard

---

### 🧭 Run Manually

```bash
python3 agent.py
```

Expected output:

```
[2025-05-12 18:30:22] Report sent for client-vps-1: Service updated to 'up'
```

---

### ⏰ Run Periodically

#### Add to `crontab`:

```bash
*/5 * * * * /usr/bin/python3 /opt/ministatus-agent/agent.py >> /var/log/ministatus-agent.log 2>&1
```

#### Or use `systemd` (see future releases)

---

## 🧼 Future Improvements

* [ ] Buffered retry if MiniStatus is offline
* [ ] Plugin system for extra checks (e.g. `check_nginx.py`)
* [ ] Auto-installer (`curl | bash`)
* [ ] `.deb` package

---

## 📄 License

MIT © [LieAndSmile](https://github.com/LieAndSmile)

---

Let me know if you'd like a starter `systemd` unit or if you want to convert this to a `setup.sh` installer later!
