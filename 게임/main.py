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
    if pygame.joystick.get_count() > 0:
        usb_joystick = pygame.joystick.Joystick(0)
        usb_joystick.init()
    else:
        usb_joystick = None
    joystick = Joystick()

    global current_health, bullets, enemys_bullets, enemys_list, terrain_offset, game_over
    max_health = 100
    current_health = max_health
    bullets = []
    enemys_bullets = []
    terrain_offset = 0
    game_over = False

    my_image = Image.new("RGBA", (joystick.width, joystick.height), (0, 0, 0, 0))
    my_draw = ImageDraw.Draw(my_image)

    background_image = Image.open('/home/song/_SMB/background.png').convert('RGBA')
    background_image = background_image.resize((joystick.width, joystick.height))

    my_circle = Character(joystick.width - 150, joystick.height)
    character_fixed_x = joystick.width // 2

    character_frames = [
        Image.open('/home/song/_SMB/character_frame1.png').convert('RGBA'),
        Image.open('/home/song/_SMB/character_frame2.png').convert('RGBA')
    ]
    character_idle = Image.open('/home/song/_SMB/character_idle.png').convert('RGBA')
    current_frame = 0
    frame_timer = 0

    turret_length = 40
    turret_offset_x = 0
    turret_offset_y = 13

    terrain_image = Image.open('/home/song/_SMB/terrain.png').convert('RGBA')
    terrain_image = terrain_image.resize((500, 200))
    terrain_height = [30] * 2000
    terrain_image_width, terrain_image_height = terrain_image.size

    enemy_image = Image.open('/home/song/_SMB/Enemy.png').convert('RGBA')
    enemy_size = (60, 40)
    specific_positions = [300, 500, 550, 750]
    enemys_list = [Enemy((pos, joystick.height - terrain_height[pos] - 25), enemy_image, size=enemy_size) for pos in specific_positions]

    bullet_image_path = '/home/song/_SMB/bullet.png'
    explosion_image_paths = [
        '/home/song/_SMB/explosion_frame1.png',
        '/home/song/_SMB/explosion_frame2.png',
        '/home/song/_SMB/explosion_frame3.png',
        '/home/song/_SMB/explosion_frame4.png'
    ]

    gravity = 5
    enemy_bullet_timer = 0
    enemy_bullet_interval = 1

    while True:
        if game_over:
            # 배경 이미지를 새로 생성
            my_image = Image.new("RGBA", (joystick.width, joystick.height), (0, 0, 0, 255))
            my_draw = ImageDraw.Draw(my_image)

            # "GAME OVER" 텍스트를 대신할 이미지 파일을 로드
            game_over_image = Image.open('/home/song/_SMB/game_over_image.png').convert('RGBA')
            
            # 이미지 크기 조정 (옵션, 원하는 크기로 변경 가능)
            game_over_image = game_over_image.resize((200, 200))  # 예시 크기

            # 이미지를 화면 중앙에 배치
            image_x = (joystick.width - game_over_image.width) // 2
            image_y = (joystick.height - game_over_image.height) // 2
            my_image.alpha_composite(game_over_image, (image_x, image_y))

            # 이미지를 디스플레이
            joystick.disp.image(my_image)

            # D 버튼이 눌리면 게임 리셋
            if not joystick.button_D.value:
                reset_game(max_health)
                continue
            time.sleep(0.1)
            continue

        if all(enemy.state == 'die' for enemy in enemys_list):
            my_image = Image.new("RGBA", (joystick.width, joystick.height), (0, 0, 0, 255))
            my_draw = ImageDraw.Draw(my_image)

            # "GAME OVER" 텍스트를 대신할 이미지 파일을 로드
            win_image = Image.open('/home/song/_SMB/win_image.png').convert('RGBA')
            
            # 이미지 크기 조정 (옵션, 원하는 크기로 변경 가능)
            win_image = win_image.resize((200, 200))  # 예시 크기

            # 이미지를 화면 중앙에 배치
            image_x = (joystick.width - win_image.width) // 2
            image_y = (joystick.height - win_image.height) // 2
            my_image.alpha_composite(win_image, (image_x, image_y))

            # 이미지를 디스플레이
            joystick.disp.image(my_image)

            # D 버튼이 눌리면 게임 리셋
            if not joystick.button_D.value:
                reset_game(max_health)
                continue
            time.sleep(0.1)
            continue

        if current_health <= 0 or my_circle.position[1] > joystick.height:
            game_over = True
            continue

        if usb_joystick is not None:
            pygame.event.pump()
            angle_command = usb_joystick.get_axis(1)
            my_circle.update_turret_angle(angle_command)

        command = {'move': False, 'left_pressed': False, 'right_pressed': False}
        if not joystick.button_L.value:
            command['left_pressed'] = True
            command['move'] = True
        if not joystick.button_R.value:
            command['right_pressed'] = True
            command['move'] = True

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

        x_center = (my_circle.position[0] + my_circle.position[2]) // 2
        adjusted_x_center = int((x_center - terrain_offset) % len(terrain_height))
        if my_circle.position[3] < joystick.height - terrain_height[adjusted_x_center]:
            my_circle.position[1] += gravity
            my_circle.position[3] += gravity
        else:
            my_circle.position[3] = joystick.height - terrain_height[adjusted_x_center]
            my_circle.position[1] = my_circle.position[3] - 40

        if (not joystick.button_A.value) or (usb_joystick is not None and usb_joystick.get_button(0)):
            turret_base_x = x_center - turret_offset_x -10
            turret_base_y = my_circle.position[1] - turret_offset_y +8
            turret_x = turret_base_x + turret_length * np.cos(np.radians(my_circle.turret_angle))
            turret_y = turret_base_y - turret_length * np.sin(np.radians(my_circle.turret_angle))

            bullet = Bullet((turret_x, turret_y), {}, my_circle.turret_angle, bullet_image_path, explosion_image_paths)
            bullets.append(bullet)

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

        for bullet in bullets :
            if bullet.state == 'active':
                bullet.move(time_step=0.05)
                bullet.terrain_collision_check(terrain_height, terrain_offset, joystick.width, joystick.height)

                for enemy in enemys_list:
                    if bullet.overlap(bullet.position, enemy.position) and enemy.state != 'die':
                        bullet.state = 'exploding'
                        bullet.explosion_center = bullet.get_center()
                        enemy.state = 'die'

                if bullet.overlap(bullet.position, my_circle.position):
                    current_health -= 10
                    bullet.state = 'exploding'
                    bullet.explosion_center = bullet.get_center()

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

            elif bullet.state == 'exploding':
                bullet.animate_explosion()

        background_x = -terrain_offset % background_image.width
        my_image.paste(background_image, (background_x, 0))
        if background_x > 0:
            my_image.paste(background_image, (background_x - background_image.width, 0))

        for x in range(0, joystick.width, terrain_image_width):
            draw_x = (x - terrain_offset) % len(terrain_height)
            y = joystick.height - terrain_height[draw_x]
            my_image.alpha_composite(terrain_image, (x, y - terrain_image_height))

        for enemy in enemys_list:
            if enemy.state != 'die':
                enemy_position = (int(enemy.position[0]), int(enemy.position[1]))
                my_image.alpha_composite(enemy.image, enemy_position)

        turret_base_x = x_center + turret_offset_x
        turret_base_y = my_circle.position[1] + turret_offset_y
        turret_x = turret_base_x + turret_length * np.cos(np.radians(my_circle.turret_angle))
        turret_y = turret_base_y - turret_length * np.sin(np.radians(my_circle.turret_angle))
        my_draw.line(
            xy=[(turret_base_x, turret_base_y), (turret_x, turret_y)],
            fill="black",
            width=3
        )

        if command['move']:
            current_image = character_frames[current_frame]
            frame_timer += 1
            if frame_timer >= 5:
                current_frame = (current_frame + 1) % len(character_frames)
                frame_timer = 0
        else:
            current_image = character_idle

        character_image_resized = current_image.resize(
            (int(my_circle.position[2] - my_circle.position[0])+40, int(my_circle.position[3] - my_circle.position[1])+20)
        )
        character_position = (int(x_center - (character_image_resized.width // 2)), int(my_circle.position[1]))
        my_image.alpha_composite(character_image_resized, character_position)

        health_fill_width = int(200 * (current_health / max_health))
        health_fill_image = Image.new("RGBA", (health_fill_width, 20), (255, 0, 0, 255))
        health_bar_image = Image.new("RGBA", (200, 20), (128, 128, 128, 255))
        my_image.alpha_composite(health_bar_image, (10, 10))
        my_image.alpha_composite(health_fill_image, (10, 10))

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

        joystick.disp.image(my_image)
        time.sleep(0.05)


if __name__ == '__main__':
    main()
