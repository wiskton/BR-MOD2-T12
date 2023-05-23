import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE,SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE:DUCKING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE:JUMPING_SHIELD}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD}
Y_POS_DUCK = 340

class Dinosaur:

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.dino_run = True
        self.dino_jump = False
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.has_power_up = False

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index//5]
        self.dino_rect.y = Y_POS
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.image = JUMP_IMG[self.type]

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL

    def update(self, user_input):
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_run = True

        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

