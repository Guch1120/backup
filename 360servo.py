import RPi.GPIO as GPIO
import time

# サーボモーターをGPIOの18に接続します
servo_pin = 18

# GPIOのモードをBCMに設定します
GPIO.setmode(GPIO.BCM)

# サーボモーターのピンを出力に設定します
GPIO.setup(servo_pin, GPIO.OUT)

# PWMを50Hzに設定します
pwm = GPIO.PWM(servo_pin, 50)

# 初期位置（停止状態）にセット
pwm.start(7.5)  # 1.5msパルス幅で停止

try:
    # 2秒間正転 (FS90Rは1msのパルスで正転)
    pwm.ChangeDutyCycle(5)  # 1msパルス幅で正転
    time.sleep(2)

    # 2秒間逆転 (FS90Rは2msのパルスで逆転)
    pwm.ChangeDutyCycle(10)  # 2msパルス幅で逆転
    time.sleep(2)

    # 停止 (FS90Rは1.5msのパルスで停止)
    pwm.ChangeDutyCycle(7.5)  # 1.5msパルス幅で停止
    time.sleep(2)

finally:
    # プログラムが終了したらクリーンアップ
    pwm.stop()
    GPIO.cleanup()
