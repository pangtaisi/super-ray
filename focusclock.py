import time
import winsound

def focus_timer(total_time, focus_interval, break_interval):
    while True:
        print(f"开始专注 {focus_interval} 分钟...")
        time.sleep(focus_interval * 60)  # 将专注时间转换为秒，并等待指定时间

        # 发出提醒铃声
        duration = 1000  # 铃声持续时间（以毫秒为单位）
        freq = 440  # 铃声频率（以赫兹为单位）
        winsound.Beep(freq, duration)

        print(f"休息 {break_interval} 分钟...")
        time.sleep(break_interval * 60)  # 将休息时间转换为秒，并等待指定时间

if __name__ == "__main__":
    total_time = 120  # 总共专注的时间（以分钟为单位）
    focus_interval = 25  # 每次专注的时间间隔（以分钟为单位）
    break_interval = 5  # 休息的时间间隔（以分钟为单位）

    focus_timer(total_time, focus_interval, break_interval)
