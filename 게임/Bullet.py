import numpy as np
from PIL import Image


class Bullet:
    def __init__(self, position, command, turret_angle, bullet_image_path, explosion_image_paths):
        self.speed = 300
        self.gravity = 150
        self.damage = 10
        self.angle = turret_angle
        self.state = 'active'  
        self.time = 0

        # 위에서부터 차례대로, 총알의 속도 중적용되는 중력값, 데미지, 총알의 발사각도(포신 부양각에 맞춰서 변합니다)
        # 총알의 상태와 총알이 발사된 뒤의 시간을 나타냅니다.

        # 총알이 처음에 발사된 위치
        self.initial_position = np.array([position[0], position[1]])
        #position 은 총알의 현재 위치를 나타냄
        self.position = np.array([position[0] - 1, position[1] - 1, position[0] + 1, position[1] + 1])

        # 총알이 충돌한 위치 
        self.explosion_center = None

        # 총알 이미지
        self.image = Image.open(bullet_image_path).convert('RGBA')
        self.image_size = (10, 10)  # 총알 크기
        self.image = self.image.resize(self.image_size)

        # 폭발 애니메이션 프레임
        self.explosion_frames = []
        self.explosion_size = (self.image_size[0] * 5, self.image_size[1] * 5)  # 폭발 크기: 총알 크기의 5배
        for path in explosion_image_paths:
            frame = Image.open(path).convert('RGBA').resize(self.explosion_size)  # 크기 조정
            self.explosion_frames.append(frame)
        self.current_frame = 0

        # 발사각에따라 초기속도가 다르므로, 이를 계산했습니다.
        self.velocity_x = self.speed * np.cos(np.radians(self.angle))
        self.velocity_y = -self.speed * np.sin(np.radians(self.angle))

    # move는 총알이 이동할때의 매커니즘입니다.
    def move(self, time_step=0.02):
        if self.state == 'active':
            self.time += time_step

            # x, y 좌표 계산 (중심에서의 위치 변화)
            new_x = self.initial_position[0] + self.velocity_x * self.time
            new_y = self.initial_position[1] + self.velocity_y * self.time + 0.5 * self.gravity * (self.time ** 2)

            # 위치 업데이트 (총알 크기를 고려하여 중심 좌표 계산)
            self.position = np.array([
                new_x - self.image_size[0] // 2,
                new_y - self.image_size[1] // 2,
                new_x + self.image_size[0] // 2,
                new_y + self.image_size[1] // 2,
            ])

    # collision check 는 총알이 충돌했는지, 아닌지를 확인하는 매서드입니다.
    def collision_check(self, targets, ignore_targets=None):
       
        # :param targets: 충돌 가능한 대상 리스트
        # :param ignore_targets: 충돌을 무시할 대상 리스트 
    
        if ignore_targets is None:
            ignore_targets = []

        for target in targets:
            if target in ignore_targets:
                continue  # 무시 대상이면 넘어감

            if self.overlap(self.position, target.position) and target.state != 'die':
                self.state = 'exploding'
                self.explosion_center = self.get_center()
                target.state = 'die'  # 적 캐릭터가 맞으면 죽음 처리
                if isinstance(target, Character):  # 캐릭터와 충돌 시 체력 감소
                    target.take_damage(self.damage)
                return

    def terrain_collision_check(self, terrain_height, terrain_offset, screen_width, screen_height):
        if self.state != 'active':
            return

        # 총알 중심 x 좌표
        bullet_center_x = int((self.position[0] + self.position[2]) / 2)

        # 화면 상의 실제 x 좌표 (오프셋 적용)
        adjusted_x = (bullet_center_x - terrain_offset) % len(terrain_height)

        # 지형 y 좌표
        terrain_y = screen_height - terrain_height[adjusted_x]

        # 총알이 지형에 닿으면 상태를 'exploding'으로 변경
        if self.position[3] >= terrain_y:
            self.state = 'exploding'
            self.explosion_center = self.get_center()  # 충돌한 위치를 저장

    # 폭발 애니메이션 구현용
    def animate_explosion(self):
        if self.state == 'exploding':
            if self.current_frame < len(self.explosion_frames):
                self.current_frame += 1
            else:
                self.state = 'finished'  # 애니메이션 종료 상태로 변경

    # 총알 중심의 좌표값을 계산(10, 10 사이즈 기준)
    def get_center(self):
        return [
            (self.position[0] + self.position[2]) / 2,  # x 중심
            (self.position[1] + self.position[3]) / 2   # y 중심
        ]

    # 두 객체가 충돌하는지 확인하기위한 매서드, 충돌여부는 두 객체의 경계값이 겹치는지 확인하여 판단합니다.
    @staticmethod
    def overlap(ego_position, other_position):
        return not (ego_position[2] < other_position[0] or
                    ego_position[0] > other_position[2] or
                    ego_position[3] < other_position[1] or
                    ego_position[1] > other_position[3])

