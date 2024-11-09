import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv("air_quality.csv")

# Chuyển đổi cột 'datetime' thành kiểu dữ liệu datetime
data["datetime"] = pd.to_datetime(data["datetime"], format="%d/%m/%Y")
# Chuyển kiểu dữ liệu từ string sang float
data.replace("-", "0", inplace=True)
data["T"] = pd.to_numeric(data["T"])
data["TM"] = pd.to_numeric(data["TM"])
data["Tm"] = pd.to_numeric(data["Tm"])
data["H"] = pd.to_numeric(data["H"])
data["PP"] = pd.to_numeric(data["PP"])
data["VV"] = pd.to_numeric(data["VV"])
data["V"] = pd.to_numeric(data["V"])
data["VM"] = pd.to_numeric(data["VM"])
data["pm2.5"] = pd.to_numeric(data["pm2.5"])
# Thiết lập cột 'datetime' làm chỉ số của DataFrame
data.set_index("datetime", inplace=True)

# Tính giá trị trung bình theo tháng
monthly_mean = data.resample("Q").mean()
# Làm tròn các giá trị của monthly_mean đến chữ số thập phân thứ nhất
monthly_mean = monthly_mean.round(1)

# Chuyển đổi định dạng chỉ số datetime thành 'YYYY-MM'
monthly_mean.index = monthly_mean.index.strftime("%Y-%m")
print(monthly_mean)
# Lưu các giá trị của monthly_mean vào một file CSV
monthly_mean.to_csv("quarterly_avg.csv")
print('Monthly mean values have been saved to "monthly_mean.csv".')
# # Vẽ biểu đồ cho dữ liệu lọc được
# plt.figure(figsize=(12, 6))
# plt.plot(
#     monthly_mean.index,
#     monthly_mean["T"],
#     label="Temperature (T)",
#     color="tab:blue",
#     marker="o",
# )
# plt.plot(
#     monthly_mean.index,
#     monthly_mean["pm2.5"],
#     label="PM2.5",
#     color="tab:orange",
#     marker="x",
# )
# plt.xlabel("Datetime")
# plt.ylabel("Values")
# plt.title(f"Temperature (T) and PM2.5")
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
