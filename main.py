def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 5 5 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        100,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite2, otherSprite2):
    info.change_life_by(-1)
    otherSprite2.destroy(effects.fire, 500)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.fire, 500)
    info.change_score_by(10)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

Enemy2: Sprite = None
EnemyShip: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . 1 4 4 . . . 
            . . . . . . . . . 1 1 1 . . . . 
            . . . . . . . 1 1 1 1 . . . . . 
            . . . . . 2 1 1 1 1 1 . . . . . 
            . . . . 2 1 1 1 2 2 1 1 . . . . 
            . . 2 2 1 1 1 1 1 2 2 1 1 2 . . 
            . . 2 2 1 1 1 1 1 2 2 1 1 2 . . 
            . . . . 2 1 1 1 2 2 1 1 . . . . 
            . . . . . 2 1 1 1 1 1 . . . . . 
            . . . . . . . 1 1 1 1 . . . . . 
            . . . . . . . . . 1 1 1 . . . . 
            . . . . . . . . . . 1 4 4 . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
info.set_life(3)

def on_update_interval():
    global EnemyShip
    EnemyShip = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . 4 6 . . . 
                    . . . . . . . . . 6 4 6 . . . . 
                    . . . . . . . 6 6 6 . . . . . . 
                    . . . . . 6 6 6 6 6 . . . . . . 
                    . . . 5 5 5 5 6 6 6 4 4 4 . . . 
                    . . . 5 5 6 6 6 6 6 . . . . . . 
                    . . . 5 5 6 6 6 6 6 . . . . . . 
                    . . . 5 5 5 5 6 6 6 4 4 4 . . . 
                    . . . . . 6 6 6 6 6 . . . . . . 
                    . . . . . . . 6 6 6 . . . . . . 
                    . . . . . . . . . 6 4 6 . . . . 
                    . . . . . . . . . . . 4 6 . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    EnemyShip.x = scene.screen_width()
    EnemyShip.vx = -20
    EnemyShip.y = randint(10, scene.screen_height() - 10)
game.on_update_interval(2000, on_update_interval)

def on_update_interval2():
    global Enemy2
    Enemy2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 8 8 . . . 8 8 8 8 . . . 
                    . . . . . . 8 . 8 8 8 8 8 . . . 
                    . . . . . 5 2 . 8 8 . . . . . . 
                    . . . . . 2 2 5 5 2 5 2 . . . . 
                    . . . . 5 5 5 5 5 2 5 2 2 . . . 
                    . . . . . 2 2 5 5 2 5 2 . . . . 
                    . . . . . 5 2 . 8 8 . . . . . . 
                    . . . . . . 8 . 8 8 8 8 8 . . . 
                    . . . . 8 8 . . . 8 8 8 8 . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    Enemy2.x = scene.screen_width()
    Enemy2.vx = -20
    Enemy2.y = randint(10, scene.screen_height() - 10)
game.on_update_interval(2000, on_update_interval2)
