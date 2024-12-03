import numpy as np
from PIL import Image

class Enemy:
    def __init__(self, spawn_position, image, size=(30, 60)):
        """
        적군 생성자
        :param spawn_position: (x, y) 스폰 위치
        :param image: 적군 이미지
        :param size: 적군 크기, 기본값 (50, 50)
        """
        self.spawn_position = spawn_position
        self.size = size  # 크기 저장

        # 이미지 크기 조정
        self.image = image.resize(size)

        # 위치 계산
        self.position = np.array([
            spawn_position[0] - size[0] // 2,
            spawn_position[1] - size[1] // 2,
            spawn_position[0] + size[0] // 2,
            spawn_position[1] + size[1] // 2
        ])
        self.state = 'alive'  # 상태: alive, die

    def update_position(self, offset_x):
        """
        적군의 위치를 업데이트합니다.
        :param offset_x: x축으로 이동할 거리
        """
        self.position[0] += offset_x
        self.position[2] += offset_x
        self.spawn_position = (self.spawn_position[0] + offset_x, self.spawn_position[1])

    def get_center(self):
        """
        적군의 중심 좌표 반환
        :return: (x_center, y_center)
        """
        return (
            (self.position[0] + self.position[2]) // 2,
            (self.position[1] + self.position[3]) // 2
        )
