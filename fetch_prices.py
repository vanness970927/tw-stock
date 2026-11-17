import json, yfinance as yf
SYMS = {"0050": "0050.TW", "0056": "0056.TW", "00878": "00878.TW",
        "00919": "00919.TW", "5904": "5904.TWO"}  # 5904 為上櫃
out = {}
for k, s in SYMS.items():
    h = yf.Ticker(s).history(period="2y", auto_adjust=False)["Close"].dropna()
    out[k] = "Date,Close\n" + "\n".join(f"{d:%Y-%m-%d},{p:.2f}" for d, p in h.items())
    print(k, len(h), "rows")
json.dump(out, open("data.json", "w"), ensure_ascii=False)
