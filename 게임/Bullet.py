import numpy as np
from PIL import Image


class Bullet:
    def __init__(self, position, command, turret_angle, bullet_image_path, explosion_image_paths):
        self.speed = 300
        self.gravity = 150
        self.damage = 10
        self.angle = turret_angle
        self.state = 'active'  # 'active', 'hit', 'exploding', 'finished'
        self.time = 0

        # 초기 위치 (발사 위치)
        self.initial_position = np.array([position[0], position[1]])
        self.position = np.array([position[0] - 1, position[1] - 1, position[0] + 1, position[1] + 1])

        # 충돌한 위치 (중심 좌표)
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

        # 초기 속도 구성 (발사 각도를 기반으로 속도 계산)
        self.velocity_x = self.speed * np.cos(np.radians(self.angle))
        self.velocity_y = -self.speed * np.sin(np.radians(self.angle))

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

    def collision_check(self, targets, ignore_targets=None):
        """
        충돌 검사를 수행합니다.
        :param targets: 충돌 가능한 대상 리스트
        :param ignore_targets: 충돌을 무시할 대상 리스트 (기본값: None)
        """
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

    def animate_explosion(self):
        """
        폭발 애니메이션 진행
        """
        if self.state == 'exploding':
            if self.current_frame < len(self.explosion_frames):
                self.current_frame += 1
            else:
                self.state = 'finished'  # 애니메이션 종료 상태로 변경

    def get_center(self):
        """
        현재 위치의 중심 좌표 반환
        """
        return [
            (self.position[0] + self.position[2]) / 2,  # x 중심
            (self.position[1] + self.position[3]) / 2   # y 중심
        ]

    @staticmethod
    def overlap(ego_position, other_position):
        return not (ego_position[2] < other_position[0] or
                    ego_position[0] > other_position[2] or
                    ego_position[3] < other_position[1] or
                    ego_position[1] > other_position[3])

