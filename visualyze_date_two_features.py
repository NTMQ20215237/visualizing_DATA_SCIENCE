import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
file_path = "air_quality.csv"  # Thay thế bằng đường dẫn tới file CSV của bạn
data = pd.read_csv(file_path)
# Pre-process invalid data
data.replace("-", "0", inplace=True)
# Chuyển đổi cột 'datetime' sang kiểu datetime
data["datetime"] = pd.to_datetime(data["datetime"], dayfirst=True)
# Sửa kiểu giá trị từ string sang float
data["T"] = pd.to_numeric(data["T"])
data["pm2.5"] = pd.to_numeric(data["pm2.5"])
# Xác định khoảng ngày cho dữ liệu
start_date = "2022-12-01"
end_date = "2022-12-31"
data["T"] = pd.to_numeric(data["T"])
data["pm2.5"] = pd.to_numeric(data["pm2.5"])

# Lọc dữ liệu trong khoảng ngày xác định
filtered_data = data[(data["datetime"] >= start_date) & (data["datetime"] <= end_date)]

# Vẽ biểu đồ cho dữ liệu lọc được
plt.figure(figsize=(12, 6))
plt.plot(
    filtered_data["datetime"],
    filtered_data["T"],
    label="Temperature (T)",
    color="tab:blue",
    marker="o",
)
plt.plot(
    filtered_data["datetime"],
    filtered_data["pm2.5"],
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
