import pyd.way as WAY
import pyd.typeEnemy as ENEMY_TYPE
import pyd.typeEvent as EVENT_TYPE
import pyd.typeItem as ITEM_TYPE
import dungeon.form.enemies.enemy.form as EnemyForm
import dungeon.form.events.event.form as EventForm
import dungeon.form.items.item.form as ItemForm
import dungeon.data.text.infoText as infoText
import dungeon.form.position.form as pos_form

W = 0
P = 1
S = 2


class Judge:
    @staticmethod
    def isWall(situation):
        if situation == W:
            return True
        return False

    @staticmethod
    def isNotWall(situation):
        if situation == W:
            return False
        return True

    @staticmethod
    def isStairs(situation):
        if situation == S:
            return True
        return False

    @staticmethod
    def isNotStairs(situation):
        if situation == S:
            return False
        return True


class FirstFloor:
    map = []
    map.insert(0, [S, P, P, P, P])
    map.insert(1, [W, P, W, W, P])
    map.insert(2, [P, P, P, P, P])
    map.insert(3, [P, W, P, W, W])
    map.insert(4, [P, W, P, P, P])

    maxWidth = 5
    maxDepth = 5
    start_pos = pos_form.Form(4, 4)
    goal_pos = pos_form.Form(0, 0)
    start_way = WAY.LEFT()
    # ENEMY LIST
    enemyList = \
        [EnemyForm.Form([pos_form.Form(2, 1), pos_form.Form(1, 1), pos_form.Form(0, 1)], ENEMY_TYPE.DANGER())]
    # EVENT LIST
    eventList = [EventForm.Form([4, 4], WAY.LEFT(), "冒険の始まりはいつだって静かだ", EVENT_TYPE.FLAVOR()),
                 EventForm.Form([4, 2], WAY.LEFT(), infoText.ITEM_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([2, 0], WAY.UP(), infoText.WALL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([4, 0], WAY.UP(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([4, 0], WAY.DOWN(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([4, 0], WAY.RIGHT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([4, 0], WAY.LEFT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([0, 0], WAY.LEFT(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([0, 0], WAY.RIGHT(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([0, 0], WAY.DOWN(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([0, 0], WAY.UP(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO())]
    # ITEM LIST
    itemList = [ItemForm.Form([4, 0], ITEM_TYPE.COMPASS())]


class SecondFloor:
    map = []
    map.insert(0, [P, P, P, P, P, P, P, P, P, P])
    map.insert(1, [W, P, W, W, P, W, W, P, W, P])
    map.insert(2, [P, P, P, P, P, P, P, P, W, P])
    map.insert(3, [P, W, P, W, W, W, P, W, W, P])
    map.insert(4, [P, W, P, P, P, P, W, P, P, P])
    map.insert(5, [P, W, P, W, W, W, P, P, W, W])
    map.insert(6, [P, W, P, P, P, P, P, W, S, P])
    map.insert(7, [P, W, P, W, P, W, P, W, W, P])
    map.insert(8, [P, W, P, P, W, W, P, W, P, P])
    map.insert(9, [P, W, W, W, P, P, P, P, P, W])
    maxWidth = 10
    maxDepth = 10
    start_pos = pos_form.Form(9, 0)
    goal_pos = pos_form.Form(6, 8)
    start_way = WAY.UP()
    # ENEMY LIST
    enemyList = [EnemyForm.Form([pos_form.Form(6, 4), pos_form.Form(7, 4)], ENEMY_TYPE.DANGER())]
    # EVENT LIST
    eventList = [EventForm.Form([2, 0], WAY.UP(), infoText.ITEM_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([6, 3], WAY.DOWN(), infoText.ITEM_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([4, 8], WAY.DOWN(), infoText.WALL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([6, 6], WAY.RIGHT(), infoText.WALL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([8, 8], WAY.UP(), infoText.WALL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([0, 0], WAY.UP(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([0, 0], WAY.DOWN(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([0, 0], WAY.RIGHT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([0, 0], WAY.LEFT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([8, 3], WAY.RIGHT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([8, 3], WAY.LEFT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([8, 3], WAY.UP(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([8, 3], WAY.DOWN(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([6, 8], WAY.LEFT(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([6, 8], WAY.RIGHT(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([6, 8], WAY.DOWN(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([6, 8], WAY.UP(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO())]
    # ITEM LIST
    itemList = [ItemForm.Form([0, 0], ITEM_TYPE.COMPASS()),
                ItemForm.Form([8, 3], ITEM_TYPE.COMPASS())]


class ThirdFloor:
    map = []
    map.insert(0, [P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P])
    map.insert(1, [W, P, W, W, P, W, W, P, W, P, W, W, W, W, W, W, W, W, W, P])
    map.insert(2, [P, P, P, P, P, P, P, P, W, P, P, P, P, P, P, P, P, P, P, P])
    map.insert(3, [P, W, P, W, W, W, P, W, W, P, W, W, W, W, W, W, W, W, W, W])
    map.insert(4, [P, W, P, P, P, P, W, P, P, P, P, P, W, W, P, P, P, W, P, S])
    map.insert(5, [P, W, P, W, W, W, P, P, W, W, W, P, P, P, P, W, P, W, P, W])
    map.insert(6, [P, W, P, P, P, P, P, W, P, P, W, P, W, P, W, W, P, P, P, W])
    map.insert(7, [P, W, P, W, P, W, P, W, W, P, P, P, P, P, P, W, P, W, P, P])
    map.insert(8, [P, W, P, P, W, W, P, W, P, P, W, P, W, W, P, P, P, P, W, P])
    map.insert(9, [P, W, W, W, P, P, P, P, P, W, W, P, P, P, W, P, W, P, P, P])
    maxWidth = 20
    maxDepth = 10
    start_pos = pos_form.Form(9, 0)
    goal_pos = pos_form.Form(4, 19)
    start_way = WAY.UP()
    # ENEMY LIST
    enemyList = [EnemyForm.Form([pos_form.Form(2, 1), pos_form.Form(1, 1), pos_form.Form(0, 1)], ENEMY_TYPE.DANGER()),
                 EnemyForm.Form([pos_form.Form(6, 4), pos_form.Form(7, 4)], ENEMY_TYPE.DANGER())]
    # EVENT LIST
    eventList = [EventForm.Form([2, 19], WAY.DOWN(), infoText.WALL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([2, 0], WAY.UP(), infoText.ITEM_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([0, 0], WAY.UP(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([0, 0], WAY.DOWN(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([0, 0], WAY.RIGHT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([0, 0], WAY.LEFT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([4, 19], WAY.RIGHT(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([4, 19], WAY.LEFT(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([4, 19], WAY.UP(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([4, 19], WAY.DOWN(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO())]
    # ITEM LIST
    itemList = [ItemForm.Form([0, 0], ITEM_TYPE.COMPASS())]


class ForthFloor:
    map = []
    map.insert(0, [P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P, P])
    map.insert(1, [W, P, W, W, P, W, W, P, W, P, W, W, W, W, W, W, W, W, W, P])
    map.insert(2, [P, P, P, P, P, P, P, P, W, P, P, P, P, P, P, P, P, P, P, P])
    map.insert(3, [P, W, P, W, W, W, P, W, W, P, W, W, W, W, W, W, W, W, W, P])
    map.insert(4, [P, W, P, P, P, P, W, P, P, W, S, P, W, W, P, P, P, W, P, P])
    map.insert(5, [P, W, P, W, W, W, P, P, W, W, W, P, P, P, P, W, P, W, P, W])
    map.insert(6, [P, W, P, P, P, P, P, W, P, P, W, P, W, P, W, W, P, P, P, W])
    map.insert(7, [P, W, P, W, P, W, P, W, W, P, P, P, P, P, P, W, P, W, P, P])
    map.insert(8, [P, W, P, P, W, W, P, W, P, P, W, P, W, W, P, P, P, P, W, P])
    map.insert(9, [P, W, W, W, P, P, P, P, P, W, W, P, P, P, W, P, W, P, P, P])
    maxWidth = 20
    maxDepth = 10
    start_pos = pos_form.Form(4, 19)
    goal_pos = pos_form.Form(4, 10)
    start_way = WAY.UP()
    # ENEMY LIST
    enemyList = [EnemyForm.Form([pos_form.Form(2, 1), pos_form.Form(1, 1), pos_form.Form(0, 1)], ENEMY_TYPE.DANGER()),
                 EnemyForm.Form([pos_form.Form(6, 4), pos_form.Form(7, 4)], ENEMY_TYPE.DANGER())]
    # EVENT LIST
    eventList = [EventForm.Form([2, 19], WAY.DOWN(), infoText.WALL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([2, 0], WAY.UP(), infoText.ITEM_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([0, 0], WAY.UP(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([0, 0], WAY.DOWN(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([0, 0], WAY.RIGHT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([0, 0], WAY.LEFT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([4, 8], WAY.UP(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([4, 8], WAY.DOWN(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([4, 8], WAY.RIGHT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([4, 8], WAY.LEFT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([6, 6], WAY.RIGHT(), infoText.ITEM_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([8, 8], WAY.UP(), infoText.ITEM_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([6, 8], WAY.UP(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([6, 8], WAY.DOWN(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([6, 8], WAY.RIGHT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([6, 8], WAY.LEFT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([9, 0], WAY.UP(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([9, 0], WAY.DOWN(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([9, 0], WAY.RIGHT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([9, 0], WAY.LEFT(), infoText.ITEM_TEXT1, EVENT_TYPE.ITEM()),
                 EventForm.Form([4, 10], WAY.RIGHT(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([4, 10], WAY.LEFT(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([4, 10], WAY.UP(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO()),
                 EventForm.Form([4, 10], WAY.DOWN(), infoText.GOAL_TEXT0, EVENT_TYPE.INFO())]
    # ITEM LIST
    itemList = [ItemForm.Form([0, 0], ITEM_TYPE.COMPASS()),
                ItemForm.Form([4, 8], ITEM_TYPE.COMPASS()),
                ItemForm.Form([6, 8], ITEM_TYPE.COMPASS()),
                ItemForm.Form([9, 0], ITEM_TYPE.COMPASS())]
