from PIL import Image, ImageDraw, ImageFont
import time
import pygame
import numpy as np
from Enemy import Enemy
from Bullet import Bullet
from Character import Character
from Joystick import Joystick


def reset_game(max_health):
    global current_health, bullets, enemys_bullets, enemys_list, terrain_offset, game_over
    current_health = max_health
    bullets = []
    enemys_bullets = []
    terrain_offset = 0
    for enemy in enemys_list:
        enemy.state = 'alive'
    game_over = False


def main():
    pygame.init() 
    #USB 조이스틱 컨트롤만을 위한 파이게임 라이브러리 초기화 및 USB 조이스틱 연결확인
    if pygame.joystick.get_count() > 0:
        usb_joystick = pygame.joystick.Joystick(0)
        usb_joystick.init()
    else:
        usb_joystick = None
    joystick = Joystick()

    #코드에 사용하는 전역변수들과, 배열들
    global current_health, bullets, enemys_bullets, enemys_list, terrain_offset, game_over
    max_health = 100
    current_health = max_health
    bullets = []
    enemys_bullets = []
    terrain_offset = 0
    game_over = False

    # 아래의 import 되는 이미지들은 인게임에서 사용되는 캐릭터, 적군, 총알, 배경, 지형등에 사용되는 이미지들입니다.
    my_image = Image.new("RGBA", (joystick.width, joystick.height), (0, 0, 0, 0))
    my_draw = ImageDraw.Draw(my_image)

    background_image = Image.open('/home/song/_SMB/background.png').convert('RGBA')
    background_image = background_image.resize((joystick.width, joystick.height))

    # 캐릭터의 화면 고정점 설정
    my_circle = Character(joystick.width - 150, joystick.height)
    character_fixed_x = joystick.width // 2

    # 캐릭터의 경우 움직이는 event 가 발생했을때 2프레임으로 구성된 애니메이션이 있습니다.
    # 구현을 위해 2가지 img를 import 하였습니다. 캐릭터가 움직이지 않을때는 idle 이라는 상태의 이미지로
    # 유지됩니다.
    character_frames = [
        Image.open('/home/song/_SMB/character_frame1.png').convert('RGBA'),
        Image.open('/home/song/_SMB/character_frame2.png').convert('RGBA')
    ]
    character_idle = Image.open('/home/song/_SMB/character_idle.png').convert('RGBA')
    current_frame = 0
    frame_timer = 0

    # 이 게임의 또 다른 특이한점은, 일반적인 횡스크롤 발사체가있는 게임과 다르게, 포텐셔미터가 내장된
    # 조이스틱을 사용함으로써 포탄이 쏴지는 각도를 미세하게 조절할수있습니다. 그래서 탱크의 포신을
    # turrent 관련된 변수로 각도를 조절할수있습니다.
    turret_length = 40
    turret_offset_x = 0
    turret_offset_y = 13

    terrain_image = Image.open('/home/song/_SMB/terrain.png').convert('RGBA')
    terrain_image = terrain_image.resize((500, 200))
    terrain_height = [30] * 2000
    terrain_image_width, terrain_image_height = terrain_image.size

    # 적 전차를 표현하기 위해 img import 및 img 사이즈를 적절히 조절하기 위한 변수와, positions 를 통해
    # 적이 배치되는 x 좌표값을 지정할수있습니다. list를 통해 Enemy class 에 생성할 Enemy 에 대한 데이터를
    # 넘겨주었습니다.
    enemy_image = Image.open('/home/song/_SMB/Enemy.png').convert('RGBA')
    enemy_size = (60, 40)
    specific_positions = [300, 500, 550, 750]
    enemys_list = [Enemy((pos, joystick.height - terrain_height[pos] - 25), enemy_image, size=enemy_size) for pos in specific_positions]

    # 캐릭터와 마찬가지로 총알이 그냥 맞기만 하면 밋밋할것같아 애니메이션 프레임을 추가했습니다.
    bullet_image_path = '/home/song/_SMB/bullet.png'
    explosion_image_paths = [
        '/home/song/_SMB/explosion_frame1.png',
        '/home/song/_SMB/explosion_frame2.png',
        '/home/song/_SMB/explosion_frame3.png',
        '/home/song/_SMB/explosion_frame4.png'
    ]

    # gravity의 경우, 처음에는 지형을 단조로운 평지가 아닌, 곡선으로 된 지형을 구현하려고했으나. 기술적
    # 한계로 인해 그냥 평지로 지형을 구현했습니다. 코드를 개발하다보니 그냥 넣어두었습니다. enemey bullet timer,
    # interval 의 경우 적군이 총알을 발사하는 시간을 계산하는 용도입니다. timer 가 증가해서 interval 값에 도달하면
    # 적은 총알을 발사합니다.
    gravity = 5
    enemy_bullet_timer = 0
    enemy_bullet_interval = 1

    while True:
        if game_over:
            # 게임오버 이미지를 띄우기 위해 초기화
            my_image = Image.new("RGBA", (joystick.width, joystick.height), (0, 0, 0, 255))
            my_draw = ImageDraw.Draw(my_image)

            # 게임오버 이미지 import 및 resizing 하기
            game_over_image = Image.open('/home/song/_SMB/game_over_image.png').convert('RGBA')
            game_over_image = game_over_image.resize((200, 200))  # 예시 크기

            # 이미지를 화면 중앙에 배치
            image_x = (joystick.width - game_over_image.width) // 2
            image_y = (joystick.height - game_over_image.height) // 2
            my_image.alpha_composite(game_over_image, (image_x, image_y))
            joystick.disp.image(my_image)

            # Down 버튼이 눌리면 게임 리셋함수 실행
            if not joystick.button_D.value:
                reset_game(max_health)
                continue
            time.sleep(0.1)
            continue

            # 게임을 이겼을때의 Victory 화면 띄우는 매커니즘, 위의 게임오버 매커니즘과 동일하다.
        if all(enemy.state == 'die' for enemy in enemys_list): 
            my_image = Image.new("RGBA", (joystick.width, joystick.height), (0, 0, 0, 255))
            my_draw = ImageDraw.Draw(my_image)
            win_image = Image.open('/home/song/_SMB/win_image.png').convert('RGBA')
            win_image = win_image.resize((200, 200))  # 예시 크기

            image_x = (joystick.width - win_image.width) // 2
            image_y = (joystick.height - win_image.height) // 2
            my_image.alpha_composite(win_image, (image_x, image_y))
            joystick.disp.image(my_image)

            if not joystick.button_D.value:
                reset_game(max_health)
                continue
            time.sleep(0.1)
            continue
        
        # 체력이 0이 되는경우 게임오버가 되는 if 문입니다.
        if current_health <= 0:
            game_over = True
            continue

        # USB 조이스틱이 활성화 된경우, 조이스틱의 1번 축을 활용하여 turret 즉 포신의 각도를 조절할수있도록 했습니다.
        if usb_joystick is not None:
            pygame.event.pump()
            angle_command = usb_joystick.get_axis(1)
            my_circle.update_turret_angle(angle_command)

        # 불리언 자료형을 사용해서, 현재 입력된 커맨드가 참인지, 좌-우 키를 구분할수있도록 했습니다.
        command = {'move': False, 'left_pressed': False, 'right_pressed': False}
        if not joystick.button_L.value:
            command['left_pressed'] = True
            command['move'] = True
        if not joystick.button_R.value:
            command['right_pressed'] = True
            command['move'] = True

        # 입력된 커맨드를 바탕으로, move 가 true 이고, 좌-우 입력에 따라 지형과 적의 오프셋값이 옮겨질수있도록 설정했습니다.
        if command['move']:
            if command['left_pressed']:
                if terrain_offset > 0:
                    terrain_offset -= 10
                    for enemy in enemys_list:
                        enemy.update_position(5)
            if command['right_pressed']:
                if terrain_offset < 2000:
                    terrain_offset += 10
                    for enemy in enemys_list:
                        enemy.update_position(-5)

        # my_circle 의 경우 전차 캐릭터의 위치를 추산하는데 사용됩니다. [0] 의 경우 캐릭터의 왼쪽상단, [2]는 오른쪽 하단의
        # x 좌표값이며 이 두값을 더하고 2로 나누어 중앙 x 좌표값을 지정합니다. 
        x_center = (my_circle.position[0] + my_circle.position[2]) // 2
        adjusted_x_center = int((x_center - terrain_offset) % len(terrain_height))

        # 아래 if else 문의 경우 위에서 언급했듯이, 지형에 닿으면 더이상 아래로 내려가지 못하도록 하는 물리엔진 효과를 담당하고
        # 있습니다. 처음에 기획단계에서는 곡선지형을 생각했으나 기술적한계로 평지로 하다보니 남아있는 잔재라고 생각하시면 편할것
        # 같습니다.
        if my_circle.position[3] < joystick.height - terrain_height[adjusted_x_center]:
            my_circle.position[1] += gravity
            my_circle.position[3] += gravity
        else:
            my_circle.position[3] = joystick.height - terrain_height[adjusted_x_center]
            my_circle.position[1] = my_circle.position[3] - 40

        # 게임기의 A 버튼이나, USB 조이스틱에 내장된 버튼 0번이 눌렸을경우 포탄이 발사되도록 하는 로직입니다.
        # 또한 turret x, y 좌표값의경우 포신 끝단에서 포탄이 나가야 어색하지 않기때문에, 포신의 끝단 좌표값을
        # 계산하는 로직입니다.
        if (not joystick.button_A.value) or (usb_joystick is not None and usb_joystick.get_button(0)):
            turret_base_x = x_center - turret_offset_x -10
            turret_base_y = my_circle.position[1] - turret_offset_y +8
            turret_x = turret_base_x + turret_length * np.cos(np.radians(my_circle.turret_angle))
            turret_y = turret_base_y - turret_length * np.sin(np.radians(my_circle.turret_angle))

        # 위에서 계산한 좌표값으로 Bullet.py (class)에 전달해줄 데이터를 마련했습니다.
            bullet = Bullet((turret_x, turret_y), {}, my_circle.turret_angle, bullet_image_path, explosion_image_paths)
            bullets.append(bullet)

        # enemy bullet timer의 경우 현재 1초 마다 적이 끊어서 포탄을 발사하는데 그 시점을 계산하는 if 문입니다.
        # eenemy bullet의 경우 왼쪽으로 발사하도록 각도 설정이 되어있으며, 만약 총알이 생성되면 enemy bullets 리스트
        # 에 추가하도록 로직을 구성하였습니다.
        enemy_bullet_timer += 0.05
        if enemy_bullet_timer >= enemy_bullet_interval:
            for enemy in enemys_list:
                if enemy.state != 'die':
                    bullet = Bullet(
                        (enemy.position[0], enemy.position[1]),
                        {}, 180,
                        bullet_image_path, explosion_image_paths
                    )
                    enemys_bullets.append(bullet)
            enemy_bullet_timer = 0

        # 아래 2가지 for문은 캐릭터가 발사한 포탄과, 적군이 발사한 포탄이 지형이나, 적군, 캐릭터와 충돌하였을때
        # 어떤 로직이 작동할건지 설정하는 for문이다. 
        for bullet in bullets : # 플레이어의 총알처리
            if bullet.state == 'active':
                bullet.move(time_step=0.05)
                bullet.terrain_collision_check(terrain_height, terrain_offset, joystick.width, joystick.height)

                for enemy in enemys_list:
                    if bullet.overlap(bullet.position, enemy.position) and enemy.state != 'die':
                        bullet.state = 'exploding' 
                        bullet.explosion_center = bullet.get_center()
                        enemy.state = 'die'
                        # 적군이 맞았을경우 총알의 상태는 폭발, 적군의 상태는 죽는다.

            elif bullet.state == 'exploding':
                bullet.animate_explosion()

        for bullet in enemys_bullets:
            if bullet.state == 'active':
                bullet.move(time_step=0.05)
                bullet.terrain_collision_check(terrain_height, terrain_offset, joystick.width, joystick.height)

                if bullet.overlap(bullet.position, my_circle.position):
                    current_health -= 10
                    bullet.state = 'exploding'
                    bullet.explosion_center = bullet.get_center()
                    #적군이 쏜 총알에 대한 for 문이며 캐릭터가 맞으면 폭발함과 동시에 체력이 -10 된다.

            elif bullet.state == 'exploding':
                bullet.animate_explosion()

        # 아래서부터는 화면에 직접 랜더링하는 내용이다.
        # terrain_offset 값이 위의 좌-우 이동의 버튼값에 따라 변하면서 x 좌표값을 정한다.
        background_x = -terrain_offset % background_image.width
        my_image.paste(background_image, (background_x, 0))
        if background_x > 0:
            my_image.paste(background_image, (background_x - background_image.width, 0))

        # 아래 for문은 조이스틱 class 에서 정해진 범위 내에서만 지형을 스크롤 해준다.
        # 위의 코드는 배경을 움직였다면 아래는 지형을 움직이는 역할을 한다.
        for x in range(0, joystick.width, terrain_image_width):
            draw_x = (x - terrain_offset) % len(terrain_height)
            y = joystick.height - terrain_height[draw_x]
            my_image.alpha_composite(terrain_image, (x, y - terrain_image_height))

        # 적 이미지를 설정해준 위치에 맞게 랜더링 해준다.
        for enemy in enemys_list:
            if enemy.state != 'die':
                enemy_position = (int(enemy.position[0]), int(enemy.position[1]))
                my_image.alpha_composite(enemy.image, enemy_position)

        # 포신의 기준 좌표점을 계산한뒤, draw.line을 통해 포신을 그려준다.
        turret_base_x = x_center + turret_offset_x
        turret_base_y = my_circle.position[1] + turret_offset_y
        turret_x = turret_base_x + turret_length * np.cos(np.radians(my_circle.turret_angle))
        turret_y = turret_base_y - turret_length * np.sin(np.radians(my_circle.turret_angle))
        my_draw.line(
            xy=[(turret_base_x, turret_base_y), (turret_x, turret_y)],
            fill="black",
            width=3
        )

        # move 명령이 있을경우 캐릭터 애니메이션이 2프레임으로 변화하도록 설정하였다.
        # 만약 move 명령이 없을경우 idle 이미지로 처리된다.
        if command['move']:
            current_image = character_frames[current_frame]
            frame_timer += 1
            if frame_timer >= 5:
                current_frame = (current_frame + 1) % len(character_frames)
                frame_timer = 0
        else:
            current_image = character_idle

        # 캐릭터 사이즈, 위치를 정하기 위한 계산 및 랜더코드이다.
        character_image_resized = current_image.resize(
            (int(my_circle.position[2] - my_circle.position[0])+40, int(my_circle.position[3] - my_circle.position[1])+20)
        )
        character_position = (int(x_center - (character_image_resized.width // 2)), int(my_circle.position[1]))
        my_image.alpha_composite(character_image_resized, character_position)

        # 아래는 체력바를 표시하기 위한 코드이다. fill_image는 실제 체력의 비율, bar_imge는 체력 막대 회색 배경이다.
        health_fill_width = int(200 * (current_health / max_health))
        health_fill_image = Image.new("RGBA", (health_fill_width, 20), (255, 0, 0, 255))
        health_bar_image = Image.new("RGBA", (200, 20), (128, 128, 128, 255))
        my_image.alpha_composite(health_bar_image, (10, 10))
        my_image.alpha_composite(health_fill_image, (10, 10))

        # 총알을 랜더하기 위한 코드이다. active 상태일때는 총알 이미지만.
        # 폭발상태일때는 애니메이션을 출력한다.
        for bullet in bullets + enemys_bullets:
            if bullet.state == 'active':
                bullet_x = int(bullet.position[0])
                bullet_y = int(bullet.position[1])+20
                my_image.alpha_composite(bullet.image, (bullet_x, bullet_y))
            elif bullet.state == 'exploding' and bullet.explosion_center:
                explosion_x = int(bullet.explosion_center[0] - bullet.explosion_size[0] / 2)
                explosion_y = int(bullet.explosion_center[1] - bullet.explosion_size[1] / 2)
                frame = bullet.explosion_frames[bullet.current_frame - 1]
                my_image.alpha_composite(frame, (explosion_x, explosion_y))

        # 최종적으로 완성된 이미지를 출력하는 코드이다.
        joystick.disp.image(my_image)
        time.sleep(0.05)


if __name__ == '__main__':
    main()
