controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 100, 0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    info.changeLifeBy(-1)
    otherSprite2.destroy(effects.fire, 500)
    scene.cameraShake(4, 500)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.destroy(effects.fire, 500)
    info.changeScoreBy(10)
})
let Enemy2: Sprite = null
let EnemyShip: Sprite = null
let projectile: Sprite = null
let mySprite: Sprite = null
effects.starField.startScreenEffect()
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.setStayInScreen(true)
info.setLife(3)
game.onUpdateInterval(2000, function () {
    EnemyShip = sprites.create(img`
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
        `, SpriteKind.Enemy)
    EnemyShip.x = scene.screenWidth()
    EnemyShip.vx = -20
    EnemyShip.y = randint(10, scene.screenHeight() - 10)
})
game.onUpdateInterval(2000, function () {
    Enemy2 = sprites.create(img`
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
        `, SpriteKind.Enemy)
    Enemy2.x = scene.screenWidth()
    Enemy2.vx = -20
    Enemy2.y = randint(10, scene.screenHeight() - 10)
})
