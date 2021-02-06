from settings import *
import pygame as pg


def listener(obj):
    try:
        if obj.can_move:
            player_movement(obj)
    except AttributeError:
        pass


def player_movement(obj):
    x_change = y_change = 0
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        x_change -= PLAYER_SPEED
    if keys[pg.K_d]:
        x_change += PLAYER_SPEED
    if keys[pg.K_w]:
        y_change -= PLAYER_SPEED
    if keys[pg.K_s]:
        y_change += PLAYER_SPEED

    if y_change != 0 or x_change != 0:
        obj.updatable = True
        for x in obj.game.loaded_map.tiles:
            if x.pos[0] + TILE_SIZE < obj.rect.x < x.pos[0] + TILE_SIZE:
                x.updatable = True
        if not collision_check(obj, obj.rect.x + x_change, obj.rect.y):
            obj.rect.x += x_change
        else:
            for i in range(TILE_SIZE):
                if x_change > 0:
                    if not collision_check(obj, obj.rect.x + 1, obj.rect.y):
                        obj.rect.x += 1
                    else:
                        break
                elif x_change < 0:
                    if not collision_check(obj, obj.rect.x - 1, obj.rect.y):
                        obj.rect.x -= 1
                    else:
                        break

        if not collision_check(obj, obj.rect.x, obj.rect.y + y_change):
            obj.rect.y += y_change
        else:
            for i in range(TILE_SIZE):
                if y_change > 0:
                    if not collision_check(obj, obj.rect.x, obj.rect.y + 1):
                        obj.rect.y += 1
                    else:
                        break
                elif y_change < 0:
                    if not collision_check(obj, obj.rect.x, obj.rect.y - 1):
                        obj.rect.y -= 1
                    else:
                        break
    obj.pos = (obj.rect.x, obj.rect.y)


def collision_check(obj, x, y):
    for instance in obj.game.objects:
        if instance != obj:
            if instance.solid:
                if instance.rect.colliderect(pg.Rect(x, y, obj.rect[2], obj.rect[3])):
                    return True
    return False


def collision_object(obj, x, y):
    for instance in obj.game.objects:
        if instance != obj:
            if instance.solid:
                if instance.rect.colliderect(pg.Rect(x, y, obj.rect[2], obj.rect[3])):
                    return instance
    return None
