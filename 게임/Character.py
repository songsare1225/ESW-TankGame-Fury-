import numpy as np
import time

class Character:
    def __init__(self, width, height):
        self.turret_angle = 0  # 포신 각도 추가
        self.appearance = 'circle'
        self.state = None
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        # 총알 발사를 위한 캐릭터 중앙 점 추가
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#FFFFFF"

        # 장전 관련 변수 추가
        self.last_shot_time = 0  # 마지막 총알 발사 시간
        self.reload_time = 2  # 장전 시간 (초)
        self.can_shoot = True  # 장전 완료 여부 (True: 발사 가능, False: 장전 중)

        # 초록색 불빛 상태
        self.green_light_on = False

    def move(self, command=None):
        pass

    def update_turret_angle(self, angle_command):
        self.turret_angle += angle_command * 5  # 각도 조절 속도 설정
        self.turret_angle = max(-10, min(40, self.turret_angle))  # 각도 제한 (-10도에서 40도)

    def move(self, command=None):
        if command['move'] == False:
            self.state = None
            self.outline = "#FFFFFF"  # 기본 색상
        else:
            self.state = 'move'
            self.outline = "#FF0000"  # 빨강색

            if command['up_pressed']:
                self.position[1] -= 5
                self.position[3] -= 5

            if command['down_pressed']:
                self.position[1] += 5
                self.position[3] += 5

            if command['left_pressed']:
                self.position[0] -= 5
                self.position[2] -= 5

            if command['right_pressed']:
                self.position[0] += 5
                self.position[2] += 5

        # 중앙 좌표 업데이트
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])

    def check_reload(self):
        """
        장전 시간이 완료되었는지 확인하는 함수
        장전 시간이 완료되면 `can_shoot`을 True로 설정하고 초록색 불빛을 켬
        """
        current_time = time.time()
        if not self.can_shoot and current_time - self.last_shot_time >= self.reload_time:
            self.can_shoot = True
            self.green_light_on = True  # 장전 완료되면 초록불 켬
        elif self.can_shoot:
            self.green_light_on = False  # 발사 가능 상태에서는 초록불 끄기
