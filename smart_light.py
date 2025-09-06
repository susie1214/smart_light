# 필요한 라이브러리들을 불러와요! 🤖
import RPi.GPIO as GPIO
import time

# 핀 번호를 정해줄게요. 실제 연결된 핀 번호로 수정해도 돼요!
PIR_PIN = 24  # PIR 센서의 OUT 핀과 연결된 GPIO 번호
LED_PIN = 23  # LED의 (+)극과 연결된 GPIO 번호

# GPIO 설정을 할 시간이에요! 🛠️
GPIO.setwarnings(False)     # 불필요한 경고 메시지는 꺼둘게요!
GPIO.setmode(GPIO.BCM)      # GPIO 번호 기준으로 핀을 쓸 거예요.
GPIO.setup(PIR_PIN, GPIO.IN) # PIR_PIN은 센서 값을 읽어야 하니 '입력(IN)'으로!
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW) # LED_PIN은 불을 켜야 하니 '출력(OUT)'으로! 시작은 꺼진 상태로!

print("✨ PIR 인체 감지 알림등 작동 시작! ✨")
print("👀 움직임이 감지되면 알려드릴게요. (Ctrl+C를 누르면 종료돼요)")

try:
    # 이제부터 무한 반복하면서 계속 감시할 거예요! 👀
    while True:
        # PIR 센서가 움직임을 감지하면(값이 1이 되면)
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            print("🚶‍♂️ 움직임 감지! 불을 켤게요! 💡")
            GPIO.output(LED_PIN, GPIO.HIGH) # LED를 뿅! 켠다.
            time.sleep(5) # 5초 동안 불을 켜둘게요. 이 시간은 마음대로 조절 가능!
            print("😴 5초가 지났어요. 다시 움직임을 기다릴게요.")
            GPIO.output(LED_PIN, GPIO.LOW) # LED를 스르륵 끈다.
            time.sleep(1) # 다시 감지하기 전에 잠깐만 쉴게요.
        
        # 움직임이 없으면(값이 0이면) 그냥 조용히 있어요.
        else:
            time.sleep(0.1) # 0.1초마다 계속 확인할게요.

except KeyboardInterrupt:
    # Ctrl+C를 누르면 여기가 실행돼요.
    print("\n안녕! 다음에 또 만나요! 👋")

finally:
    # 프로그램이 어떻게 끝나든 항상 GPIO를 깔끔하게 정리해줘요!
    GPIO.cleanup