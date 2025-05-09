import MetaTrader5 as mt5
import pandas as pd
import time
import tkinter as tk
from tkinter import messagebox

# Initialize MT5
mt5.initialize()
symbol = "XAUUSD"  # Changed to GOLD (XAUUSD)
timeframe = mt5.TIMEFRAME_M5
lot_size = 0.1
risk_percent = 1  # Risk as a percentage of account balance
rr_ratio = 1.5  # Risk-Reward Ratio (1:1.5)

# GUI Setup
app = tk.Tk()
app.title("GOLD SMC BOT")
app.geometry("400x300")

# Function to fetch recent price data
def get_price_data(symbol, timeframe, n=100):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

# Identify BOS and CHoCH
def identify_structure(df):
    highs = df['high']
    lows = df['low']
    bos = highs[-2] > highs[-3] and lows[-2] < lows[-3]
    choch = lows[-1] > lows[-2]
    return bos, choch

# Set trap (POI and FVG)
def set_trap(df):
    fvg_level = df['high'][-3]
    poi = df['low'][-3]
    return fvg_level, poi

# Calculate SL and TP
def calculate_sl_tp(entry, poi):
    sl = poi
    tp = entry + (entry - sl) * rr_ratio
    return sl, tp

# Execute Buy Order with SL and TP
def place_buy_order():
    try:
        balance = mt5.account_info().balance
        data = get_price_data(symbol, timeframe)
        bos, choch = identify_structure(data)
        fvg, poi = set_trap(data)

        if bos and choch:
            current_price = mt5.symbol_info_tick(symbol).bid
            if current_price <= poi or current_price <= fvg:
                sl, tp = calculate_sl_tp(current_price, poi)
                order = mt5.OrderSend(
                    symbol=symbol,
                    action=mt5.TRADE_ACTION_DEAL,
                    volume=lot_size,
                    type=mt5.ORDER_TYPE_BUY,
                    price=mt5.symbol_info_tick(symbol).ask,
                    sl=sl,
                    tp=tp,
                    deviation=10
                )

                if order.retcode == mt5.TRADE_RETCODE_DONE:
                    messagebox.showinfo("Order Status", "Buy Order Placed with SL and TP")
                else:
                    messagebox.showerror("Order Failed", str(order))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Components
tk.Label(app, text="GOLD SMC BOT").pack(pady=10)
tk.Button(app, text="Start Bot", command=place_buy_order).pack(pady=5)

app.mainloop()
mt5.shutdown()
