import time
import RPi.GPIO as GPIO
from adafruit_htu21d import HTU21D
import busio

def init(cs, mosi, miso, clk):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(cs, GPIO.OUT)
        GPIO.setup(mosi, GPIO.OUT)
        GPIO.setup(miso, GPIO.IN)
        GPIO.setup(clk,GPIO.OUT)

def sendCmd(cs, mosi, clk, command):
        GPIO.output(cs, GPIO.HIGH)
        GPIO.output(cs, GPIO.LOW)
        GPIO.output(clk, GPIO.LOW)
        for i in range (4):
                if(command & 0x80):
                        GPIO.output(mosi, GPIO.HIGH)
                else:
                        GPIO.output(mosi, GPIO.LOW)
                command = command << 1
                GPIO.output(clk, GPIO.HIGH)
                GPIO.output(clk, GPIO.LOW)

def readData(miso, clk):
        value = 0
        for i in range(13):
                GPIO.output(clk, GPIO.HIGH)
                GPIO.output(clk, GPIO.LOW)
                value = value << 1
                if GPIO.input(miso):
                        value = value | 0x1
                else:
                        value = value | 0x0
        # discard the first bit
        value = value >> 1
        return value

def getIlluminance():
        cs = 8 # board.SPI_CE0_N
        mosi = 10 # board.MOSI
        miso = 9 # board.MISO
        clk = 11 # board.CLK
        init(cs, mosi, miso, clk)
        sendCmd(cs, mosi, clk, ((0<<1)|0x0d)<<4)
        return int(readData(miso, clk))

# 초음파 센서를 대한 전역 변수 선언 및 초기화
trig = 20
echo = 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)


def measureDistance():
        global trig, echo
        GPIO.output(trig, True) # 신호 1 발생
        time.sleep(0.00001) # 짧은시간후 0으로 떨어뜨려 falling edge를 만들기 위함             
        GPIO.output(trig, False) # 신호 0 발생(falling 에지)

        while(GPIO.input(echo) == 0):
                pass
        pulse_start = time.time() # 신호 1. 초음파 발생이 시작되었음을 알림
        while(GPIO.input(echo) == 1):
                pass
        pulse_end = time.time() # 신호 0. 초음파 수신 완료를 알림

        pulse_duration = pulse_end - pulse_start
        return 340*100/2*pulse_duration

#온습도 센서에 대한 전역 변수 선언 및 초기화
sda = 2 # GPIO 핀 번호, sda라고 이름이 보이는 핀
scl = 3 # GPIO 핀 번호, scl이라고 이름이 보이는 핀
i2c = busio.I2C(scl, sda)
sensor = HTU21D(i2c) # HTU21D 장치를 제어하는 객체 리턴

def getTemperature() :
        return float(sensor.temperature) # HTU21D 장치로부터 온도 값 읽기
def getHumidity() :
        return float(sensor.relative_humidity) # HTU21D 장치로부터 습도 값 읽기

# LED 점등을 위한 전역 변수 선언 및 초기화
red_led = 6 # 핀 번호 GPIO6 의미
green_led = 13 # 핀 번호 GPIO13 의미
yellow_led = 5 # 핀 번호 GPIO5 의미
white_led = 19 # 핀 번호 GPIO19 의미
green_button = 21 # 핀 번호 GPIO21 의미
yellow_button = 12 # 핀 번호 GPIO12 의미
white_button = 25 # 핀 번호 GPIO25 의미
GPIO.setup(red_led, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정.
GPIO.setup(green_led, GPIO.OUT) # GPIO 13번 핀을 출력 선으로 지정.
GPIO.setup(yellow_led, GPIO.OUT) # GPIO 5번 핀을 출력 선으로 지정.
GPIO.setup(white_led, GPIO.OUT) # GPIO 19번 핀을 출력 선으로 지정.
GPIO.setup(green_button, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(yellow_button, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(white_button, GPIO.IN, GPIO.PUD_DOWN)
g_btnStatus = 0
y_btnStatus = 0
w_btnStatus = 0

def controlLED(onOff): # led 번호의 핀에 onOff(0/1) 값 출력하는 함수
        GPIO.output(red_led, onOff)

def ledOnOff(led, onOff): # led 번호의 핀에 onOff(0/1) 값 출력하는 함수
        GPIO.output(led, onOff)

def g_buttonPressed(pin):
        global g_btnStatus
        g_btnStatus = 0 if g_btnStatus ==1 else 1
        ledOnOff(green_led, g_btnStatus)

def y_buttonPressed(pin):
        global y_btnStatus
        y_btnStatus = 0 if y_btnStatus ==1 else 1
        ledOnOff(yellow_led, y_btnStatus)

def w_buttonPressed(pin):
        global w_btnStatus
        w_btnStatus = 0 if w_btnStatus ==1 else 1
        ledOnOff(white_led, w_btnStatus)

GPIO.add_event_detect(green_button, GPIO.RISING, g_buttonPressed, 200)
# 핀 21에 올라가는 에지가 발견되면 buttonPressed 를 호출하도록 지정
# 200ms 사에 발생한 에지는 무시

GPIO.add_event_detect(yellow_button, GPIO.RISING, y_buttonPressed, 200)

GPIO.add_event_detect(white_button, GPIO.RISING, w_buttonPressed, 200)

while True :
        pass



