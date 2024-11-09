import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
file_path = "monthly_mean.csv"  # Thay thế bằng đường dẫn tới file CSV của bạn
monthly_mean = pd.read_csv(file_path)
# Vẽ biểu đồ cho dữ liệu lọc được
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_mean["datetime"],
    monthly_mean["T"],
    label="Temperature (T)",
    color="tab:blue",
    marker="o",
)
plt.plot(
    monthly_mean["datetime"],
    monthly_mean["pm2.5"],
    label="PM2.5",
    color="tab:orange",
    marker="x",
)
plt.xlabel("Datetime")
plt.ylabel("Values")
plt.title(f"Temperature (T) and PM2.5")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
