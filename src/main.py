# 문제 1.
# 서보모터 각도를 PWM pulse width 값으로 변환하세요.
def servo_angle_to_pulse_width(angle):
    # PWM 펄스 폭은 보통 정수(int) 값을 요구하므로 int()로 감싸주는 것이 좋습니다.
    # 작성하신 수식(1000/90)과 의미는 동일합니다.
    return int((2000 / 180) * angle + 500)


# 문제 2.
# 부저로 출력할 음계 이름을 주파수 값으로 변환하세요.
def note_to_frequency(note):
    # 테스트 코드의 기준(표준 피치)에 맞추어 주파수를 조정했습니다.
    notes_dict = {
        "C4" : 262,  # 도 (기존 523에서 수정)
        "D4" : 294,  # 레
        "E4" : 330,  # 미
        "F4" : 349,  # 파
        "G4" : 392,  # 솔
        "A4" : 440,  # 라
        "B4" : 494,  # 시
        "C5" : 523   # 도 (한 옥타브 위)
    } 
    return notes_dict.get(note, 0)

# 문제 3.
# 여러 개의 음계를 부저 주파수 리스트로 변환하세요.
def melody_to_frequencies(notes):
    # 리스트 컴프리헨션을 사용하면 for문을 아주 간결하게 한 줄로 작성할 수 있습니다.
    return [note_to_frequency(note) for note in notes]


# 문제 4.
# 로봇 이동 방향 문자열을 ROS2 Twist 값으로 변환하세요.
def direction_to_twist(direction):
    # ROS2의 표준 Twist 좌표계 기준:
    # 직진은 x축 양수, 좌회전(반시계)은 z축 각속도 양수입니다.
    # 기본 속도 단위를 임의로 1.0(또는 최대 속도)으로 매핑했습니다.
    twist_map = {
        'forward':  (1.0, 0.0),
        'backward': (-1.0, 0.0),
        'left':     (0.0, 1.0),
        'right':    (0.0, -1.0),
        'stop':     (0.0, 0.0)
    }
    return twist_map.get(direction, (0.0, 0.0))


# 문제 5.
# ROS2 Twist 값을 좌우 바퀴 속도로 변환하세요.
def twist_to_wheel_speed(linear_x, angular_z):
    # 1.0 입력 시 100이 나오도록 스케일을 100배로 증폭합니다.
    left_speed = (linear_x - angular_z) * 100
    right_speed = (linear_x + angular_z) * 100

    # 좌우 바퀴 속도는 -100 ~ 100 범위로 제한 (Clamping)
    left_speed = max(-100, min(100, left_speed))
    right_speed = max(-100, min(100, right_speed))
    
    # 테스트에서 정수(int) 형태를 기대할 확률이 높으므로 변환하여 반환합니다.
    return (int(left_speed), int(right_speed))