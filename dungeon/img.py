import common.common as cmn
import common.debug.debug as dbg
import common.pyd.createPass as cPass
import common.pyd.calc as calc
import dungeon.pyd.index as INDEX
import dungeon.pyd.mask as mask
import dungeon.data.map.map as map
import dungeon.debug as dunDbg
import pygame
import pygame.locals

# size
conner_size = (200, 150)
side_size = (200, 300)
wide_size = (400, 150)
center_size = (400, 300)
view_size = cmn.WINDOW_SIZE
map_size = (20, 20)
map_board_size = (200, 200)
board_m_size = (800, 200)
text3_size = (50, 20)
text5_size = (80, 20)
text6_size = (80, 20)
button_size = (150, 60)
compass_size = (100, 100)
item_size = (50, 50)
box_size = (60, 60)
box_tag_size = (60, 20)


class Download:
    def dungeonImag(case='test'):
        # return
        imgList = []
        # init list load
        R_load = []
        C_load = []
        L_load = []
        RU_load = []
        RC_load = []
        RD_load = []
        CU_load = []
        CC_load = []
        CD_load = []
        LU_load = []
        LC_load = []
        LD_load = []
        FlAME_load = []
        WALL_load = []
        PLAYER_load = []
        PATH_load = []
        BOARD_S_load = []
        TEXT3_load = []
        TEXT5_load = []
        TEXT6_load = []
        BOARD_M_load = []
        BUTTON_load = []
        ACTION_load = []
        ITEM_load = []
        BOX_load = []
        COMPASS_load = []
        BOX_TAG_load = []
        # download
        for file_name in range(0, 2, 1):
            RU_load.insert(int(file_name), Download.__loadImg(case, 'RU', file_name))
        for file_name in range(0, 2, 1):
            RC_load.insert(int(file_name), Download.__loadImg(case, 'RC', file_name))
        for file_name in range(0, 2, 1):
            RD_load.insert(int(file_name), Download.__loadImg(case, 'RD', file_name))
        for file_name in range(0, 1, 1):
            CU_load.insert(int(file_name), Download.__loadImg(case, 'CU', file_name))
        for file_name in range(0, 31, 1):
            CC_load.insert(int(file_name), Download.__loadImg(case, 'CC', file_name))
        for file_name in range(0, 1, 1):
            CD_load.insert(int(file_name), Download.__loadImg(case, 'CD', file_name))
        for file_name in range(0, 2, 1):
            LU_load.insert(int(file_name), Download.__loadImg(case, 'LU', file_name))
        for file_name in range(0, 2, 1):
            LC_load.insert(int(file_name), Download.__loadImg(case, 'LC', file_name))
        for file_name in range(0, 2, 1):
            LD_load.insert(int(file_name), Download.__loadImg(case, 'LD', file_name))
        for file_name in range(0, 2, 1):
            FlAME_load.insert(int(file_name), Download.__loadImg(case, 'FLAME', file_name))
        for file_name in range(0, 1, 1):
            WALL_load.insert(int(file_name), Download.__loadImg(case, 'WALL', file_name))
        for file_name in range(0, 3, 1):
            PLAYER_load.insert(int(file_name), Download.__loadImg(case, 'PLAYER', file_name))
        for file_name in range(0, 2, 1):
            PATH_load.insert(int(file_name), Download.__loadImg(case, 'PATH', file_name))
        for file_name in range(0, 2, 1):
            BOARD_S_load.insert(int(file_name), Download.__loadImg(case, 'BOARD_S', file_name))
        for file_name in range(0, 3, 1):
            TEXT3_load.insert(int(file_name), Download.__loadImg(case, 'TEXT3', file_name))
        for file_name in range(0, 9, 1):
            TEXT5_load.insert(int(file_name), Download.__loadImg(case, 'TEXT5', file_name))
        for file_name in range(0, 6, 1):
            TEXT6_load.insert(int(file_name), Download.__loadImg(case, 'TEXT6', file_name))
        for file_name in range(0, 1, 1):
            BOARD_M_load.insert(int(file_name), Download.__loadImg(case, 'BOARD_M', file_name))
        for file_name in range(0, 14, 1):
            BUTTON_load.insert(int(file_name), pygame.image.load(cmn.resource_path(cPass.getImgPass("common", 'BUTTON', file_name))))
        for file_name in range(0, 4, 1):
            ACTION_load.insert(int(file_name), Download.__loadImg(case, 'ACTION', file_name))
        for file_name in range(0, 2, 1):
            ITEM_load.insert(int(file_name), Download.__loadImg(case, 'ITEM', file_name))
        for file_name in range(0, 2, 1):
            BOX_load.insert(int(file_name), Download.__loadImg(case, 'BOX', file_name))
        for file_name in range(0, 1, 1):
            COMPASS_load.insert(int(file_name), Download.__loadImg(case, 'COMPASS', file_name))
        for file_name in range(0, 1, 1):
            BOX_TAG_load.insert(int(file_name), Download.__loadImg(case, 'BOX_TAG', file_name))
        R_load.insert(INDEX.UP_POS(), RU_load)
        R_load.insert(INDEX.CENTER_POS(), RC_load)
        R_load.insert(INDEX.DOWN_POS(), RD_load)
        C_load.insert(INDEX.UP_POS(), CU_load)
        C_load.insert(INDEX.CENTER_POS(), CC_load)
        C_load.insert(INDEX.DOWN_POS(), CD_load)
        L_load.insert(INDEX.UP_POS(), LU_load)
        L_load.insert(INDEX.CENTER_POS(), LC_load)
        L_load.insert(INDEX.DOWN_POS(), LD_load)
        # init list img
        R_img = []
        C_img = []
        L_img = []
        RU_img = []
        RC_img = []
        RD_img = []
        CU_img = []
        CC_img = []
        CD_img = []
        LU_img = []
        LC_img = []
        LD_img = []
        FLAME_img = []
        WALL_img = []
        PLAYER_img = []
        PATH_img = []
        BOARD_S_img = []
        TEXT3_img = []
        TEXT5_img = []
        TEXT6_img = []
        BOARD_M_img = []
        BUTTON_img = []
        ACTION_img = []
        ITEM_img = []
        BOX_img = []
        COMPASS_img = []
        BOX_TAG_img = []
        # img set
        for i in range(0, len(R_load[INDEX.UP_POS()]), 1):
            RU_img.insert(i, pygame.transform.scale(R_load[INDEX.UP_POS()][i], conner_size))
        for i in range(0, len(R_load[INDEX.CENTER_POS()]), 1):
            RC_img.insert(i, pygame.transform.scale(R_load[INDEX.CENTER_POS()][i], side_size))
        for i in range(0, len(R_load[INDEX.DOWN_POS()]), 1):
            RD_img.insert(i, pygame.transform.scale(R_load[INDEX.DOWN_POS()][i], conner_size))
        for i in range(0, len(C_load[INDEX.UP_POS()]), 1):
            CU_img.insert(i, pygame.transform.scale(C_load[INDEX.UP_POS()][i], wide_size))
        for i in range(0, len(C_load[INDEX.CENTER_POS()]), 1):
            CC_img.insert(i, pygame.transform.scale(C_load[INDEX.CENTER_POS()][i], center_size))
        for i in range(0, len(C_load[INDEX.DOWN_POS()]), 1):
            CD_img.insert(i, pygame.transform.scale(C_load[INDEX.DOWN_POS()][i], wide_size))
        for i in range(0, len(L_load[INDEX.UP_POS()]), 1):
            LU_img.insert(i, pygame.transform.scale(L_load[INDEX.UP_POS()][i], conner_size))
        for i in range(0, len(L_load[INDEX.CENTER_POS()]), 1):
            LC_img.insert(i, pygame.transform.scale(L_load[INDEX.CENTER_POS()][i], side_size))
        for i in range(0, len(L_load[INDEX.DOWN_POS()]), 1):
            LD_img.insert(i, pygame.transform.scale(L_load[INDEX.DOWN_POS()][i], conner_size))
        for i in range(0, len(FlAME_load), 1):
            FLAME_img.insert(i, pygame.transform.scale(FlAME_load[i], view_size))
        for i in range(0, len(WALL_load), 1):
            WALL_img.insert(i, pygame.transform.scale(WALL_load[i], map_size))
        for i in range(0, len(PLAYER_load), 1):
            PLAYER_img.insert(i, pygame.transform.scale(PLAYER_load[i], map_size))
        for i in range(0, len(PATH_load), 1):
            PATH_img.insert(i, pygame.transform.scale(PATH_load[i], map_size))
        for i in range(0, len(BOARD_S_load), 1):
            BOARD_S_img.insert(i, pygame.transform.scale(BOARD_S_load[i], map_board_size))
        for i in range(0, len(TEXT3_load), 1):
            TEXT3_img.insert(i, pygame.transform.scale(TEXT3_load[i], text3_size))
        for i in range(0, len(TEXT5_load), 1):
            TEXT5_img.insert(i, pygame.transform.scale(TEXT5_load[i], text5_size))
        for i in range(0, len(TEXT6_load), 1):
            TEXT6_img.insert(i, pygame.transform.scale(TEXT6_load[i], text6_size))
        for i in range(0, len(BOARD_M_load), 1):
            BOARD_M_img.insert(i, pygame.transform.scale(BOARD_M_load[i], board_m_size))
        for i in range(0, len(BUTTON_load), 1):
            BUTTON_img.insert(i, pygame.transform.scale(BUTTON_load[i], button_size))
        for i in range(0, len(ACTION_load), 1):
            ACTION_img.insert(i, pygame.transform.scale(ACTION_load[i], button_size))
        for i in range(0, len(ITEM_load), 1):
            ITEM_img.insert(i, pygame.transform.scale(ITEM_load[i], item_size))
        for i in range(0, len(BOX_load), 1):
            BOX_img.insert(i, pygame.transform.scale(BOX_load[i], box_size))
        for i in range(0, len(COMPASS_load), 1):
            COMPASS_img.insert(i, pygame.transform.scale(COMPASS_load[i], compass_size))
        for i in range(0, len(BOX_TAG_load), 1):
            BOX_TAG_img.insert(i, pygame.transform.scale(BOX_TAG_load[i], box_tag_size))
        R_img.insert(INDEX.UP_POS(), RU_img)
        R_img.insert(INDEX.CENTER_POS(), RC_img)
        R_img.insert(INDEX.DOWN_POS(), RD_img)
        C_img.insert(INDEX.UP_POS(), CU_img)
        C_img.insert(INDEX.CENTER_POS(), CC_img)
        C_img.insert(INDEX.DOWN_POS(), CD_img)
        L_img.insert(INDEX.UP_POS(), LU_img)
        L_img.insert(INDEX.CENTER_POS(), LC_img)
        L_img.insert(INDEX.DOWN_POS(), LD_img)
        imgList.insert(INDEX.RIGHT(), R_img)
        imgList.insert(INDEX.CENTER(), C_img)
        imgList.insert(INDEX.LEFT(), L_img)
        imgList.insert(INDEX.FLAME(), FLAME_img)
        imgList.insert(INDEX.WALL(), WALL_img)
        imgList.insert(INDEX.PLAYER(), PLAYER_img)
        imgList.insert(INDEX.PATH(), PATH_img)
        imgList.insert(INDEX.BOARD_S(), BOARD_S_img)
        imgList.insert(INDEX.TEXT3(), TEXT3_img)
        imgList.insert(INDEX.BOARD_M(), BOARD_M_img)
        imgList.insert(INDEX.TEXT5(), TEXT5_img)
        imgList.insert(INDEX.BUTTON(), BUTTON_img)
        imgList.insert(INDEX.TEXT6(), TEXT6_img)
        imgList.insert(INDEX.ACTION(), ACTION_img)
        imgList.insert(INDEX.ITEM(), ITEM_img)
        imgList.insert(INDEX.BOX(), BOX_img)
        imgList.insert(INDEX.COMPASS(), COMPASS_img)
        imgList.insert(INDEX.BOX_TAG(), BOX_TAG_img)
        return imgList

    def __loadImg(case, name, number):
        return pygame.image.load(cmn.resource_path(cPass.getImgPass(case, name, number)))


class Select:
    def RU(now_status):
        return calc.maskAndRight(now_status, mask.RU(), 0)

    def RC(now_status):
        return calc.maskAndRight(now_status, mask.RC(), 1)

    def RD(now_status):
        return calc.maskAndRight(now_status, mask.RD(), 0)

    def CU(now_status):
        return 0

    def CC(now_status):
        return calc.maskAndRight(now_status, mask.C(), 4)

    def CD(now_status):
        return 0

    def LU(now_status):
        return calc.maskAndRight(now_status, mask.LU(), 12)

    def LC(now_status):
        return calc.maskAndRight(now_status, mask.LC(), 13)

    def LD(now_status):
        return calc.maskAndRight(now_status, mask.LD(), 12)

    def FLAME(now_status):
        return 0

    def PLAYER(flash=1):
        return flash

    def WALL_OR_PATH(situation):
        if map.Judge.isNotWall(situation):
            return INDEX.PATH()
        else:
            return INDEX.WALL()

    def TEXT_FLASH(flash=0):
        return flash % 3


class pos:
    def L(situation, status):
        if map.Judge.isWall(situation[0][0]):
            # 左が壁
            status = calc.bitmask(status, 0 << 12)  # 0
        else:
            if map.Judge.isNotWall(situation[1][0]):
                status = calc.bitmask(status, 3 << 12)  # 3
            else:
                status = calc.bitmask(status, 1 << 12)  # 1
        return status

    def R(situation, status):
        if map.Judge.isWall(situation[4][0]):
            # 右が壁
            status = calc.bitmask(status, 0)  # 0
        else:
            if map.Judge.isNotWall(situation[3][0]):
                status = calc.bitmask(status, 3)  # 3
            else:
                status = calc.bitmask(status, 1)  # 1
        return status

    def C(situation, status):
        if map.Judge.isWall(situation[2][0]):
            status = status | (0 << 4)  # 0
        elif map.Judge.isWall(situation[1][0]) and map.Judge.isNotWall(situation[2][0]) and map.Judge.isWall(situation[3][0]):
            # ???
            # ???
            # ■□■
            # ?○?
            if map.Judge.isNotWall(situation[5][0]):
                if map.Judge.isWall(situation[6][0]) and map.Judge.isNotWall(situation[7][0]):
                    if map.Judge.isWall(situation[8][0]):
                        if map.Judge.isWall(situation[10][0]):
                            # ?■■
                            # ■□□
                            # ■□■
                            # ?○?
                            status = calc.bitmask(status, 9 << 4)  # 9
                        else:
                            # ?■□
                            # ■□□
                            # ■□■
                            # ?○?
                            status = calc.bitmask(status, 29 << 4)  # 29
                    else:
                        dbg.ERROR_LOG("画像なし")
                        dunDbg.Debug.showSituation(situation, True)
                        # ?□?
                        # ■□□
                        # ■□■
                        # ?○?
                        status = calc.bitmask(status, 27 << 4)  # 27
                elif map.Judge.isNotWall(situation[6][0]) and map.Judge.isWall(situation[7][0]):
                    if map.Judge.isWall(situation[8][0]):
                        if map.Judge.isWall(situation[9][0]):
                            # ■■?
                            # □□■
                            # ■□■
                            # ?○?
                            status = calc.bitmask(status, 10 << 4)  # 10
                        else:
                            # □■?
                            # □□■
                            # ■□■
                            # ?○?
                            status = calc.bitmask(status, 24 << 4)  # 24
                    else:
                        if map.Judge.isWall(situation[9][0]):
                            dbg.ERROR_LOG("画像なし")
                            dunDbg.Debug.showSituation(situation, True)
                            # ■□?
                            # □□■
                            # ■□■
                            # ?○?
                            status = calc.bitmask(status, 14 << 4)  # 14
                        else:
                            dbg.ERROR_LOG("画像なし")
                            dunDbg.Debug.showSituation(situation, True)
                            # □□?
                            # □□■
                            # ■□■
                            # ?○?
                            status = calc.bitmask(status, 14 << 4)  # 14
                elif map.Judge.isNotWall(situation[6][0]) and map.Judge.isNotWall(situation[7][0]):
                    if map.Judge.isNotWall(situation[8][0]):
                        dbg.ERROR_LOG("画像なし")
                        dunDbg.Debug.showSituation(situation, True)
                        # ?□?
                        # □□□
                        # ■□■
                        # ?○?
                        status = calc.bitmask(status, 13 << 4)  # 13
                    else:
                        if map.Judge.isNotWall(situation[9][0]) and map.Judge.isNotWall(situation[10][0]):
                            # □■□
                            # □□□
                            # ■□■
                            # ?○?
                            status = calc.bitmask(status, 16 << 4)  # 16
                        elif map.Judge.isNotWall(situation[9][0]) and map.Judge.isWall(situation[10][0]):
                            # □■■
                            # □□□
                            # ■□■
                            # ?○?
                            status = calc.bitmask(status, 18 << 4)  # 18
                        elif map.Judge.isWall(situation[9][0]) and map.Judge.isNotWall(situation[10][0]):
                            # ■■□
                            # □□□
                            # ■□■
                            # ?○?
                            status = calc.bitmask(status, 17 << 4)  # 17
                        else:
                            # ■■■
                            # □□□
                            # ■□■
                            # ?○?
                            status = calc.bitmask(status, 13 << 4)  # 13
                else:
                    if map.Judge.isWall(situation[8][0]):
                        # ?■?
                        # ■□■
                        # ■□■
                        # ?○?
                        status = calc.bitmask(status, 15 << 4)  # 15
                    else:
                        # ?□?
                        # ■□■
                        # ■□■
                        # ?○?
                        status = calc.bitmask(status, 4 << 4)  # 4
            else:
                # ■■■
                # ■□■
                # ?○?
                status = calc.bitmask(status, 11 << 4)  # 11
        elif map.Judge.isNotWall(situation[1][0]) and map.Judge.isNotWall(situation[2][0]) and map.Judge.isNotWall(situation[3][0]):
            # ???
            # ???
            # □□□
            # ?○?
            if map.Judge.isNotWall(situation[5][0]):
                if map.Judge.isWall(situation[6][0]) and map.Judge.isNotWall(situation[7][0]):
                    dbg.ERROR_LOG("画像なし")
                    dunDbg.Debug.showSituation(situation, True)
                    # ■□□
                    # □□□
                    # ?○?
                    status = calc.bitmask(status, 4 << 4)  # 4
                elif map.Judge.isNotWall(situation[6][0]) and map.Judge.isWall(situation[7][0]):
                    dbg.ERROR_LOG("画像なし")
                    dunDbg.Debug.showSituation(situation, True)
                    # □□■
                    # □□□
                    # ?○?
                    status = calc.bitmask(status, 4 << 4)  # 4
                else:
                    dbg.ERROR_LOG("画像なし")
                    dunDbg.Debug.showSituation(situation, True)
                    # □□□
                    # □□□
                    # ?○?
                    status = calc.bitmask(status, 4 << 4)  # 4
            else:
                if map.Judge.isWall(situation[6][0]) and map.Judge.isNotWall(situation[7][0]):
                    # ■■□
                    # □□□
                    # ?○?
                    status = calc.bitmask(status, 21 << 4)  # 21
                elif map.Judge.isNotWall(situation[6][0]) and map.Judge.isWall(situation[7][0]):
                    # □■■
                    # □□□
                    # ?○?
                    status = calc.bitmask(status, 20 << 4)  # 20
                elif map.Judge.isWall(situation[6][0]) and map.Judge.isWall(situation[7][0]):
                    # ■■■
                    # □□□
                    # ?○?
                    status = calc.bitmask(status, 5 << 4)  # 5
                else:
                    # □■□
                    # □□□
                    # ?○?
                    status = calc.bitmask(status, 19 << 4)  # 19
        elif map.Judge.isNotWall(situation[1][0]) and map.Judge.isNotWall(situation[2][0]) and map.Judge.isWall(situation[3][0]):
            # ???
            # ???
            # □□■
            # ?○?
            if map.Judge.isNotWall(situation[5][0]):
                # ?□?
                # □□■
                # ?○?
                if map.Judge.isWall(situation[6][0]) and map.Judge.isNotWall(situation[7][0]):
                    if map.Judge.isNotWall(situation[8][0]):
                        # ?□?
                        # ■□□
                        # □□■
                        # ?○?
                        status = calc.bitmask(status, 8 << 4)  # 8
                    else:
                        # ?■?
                        # ■□□
                        # □□■
                        # ?○?
                        status = calc.bitmask(status, 22 << 4)  # 22
                elif map.Judge.isNotWall(situation[6][0]) and map.Judge.isWall(situation[7][0]):
                    dbg.ERROR_LOG("画像なし")
                    dunDbg.Debug.showSituation(situation, True)
                    # □□■
                    # □□■
                    # ?○?
                    status = calc.bitmask(status, 4 << 4)  # 4
                elif map.Judge.isWall(situation[6][0]) and map.Judge.isWall(situation[7][0]):
                    if map.Judge.isWall(situation[8][0]):
                        # ?■?
                        # ■□■
                        # □□■
                        # ?○?
                        status = calc.bitmask(status, 25 << 4)  # 25
                    else:
                        # ?□?
                        # ■□■
                        # □□■
                        # ?○?
                        status = calc.bitmask(status, 26 << 4)  # 26
                else:
                    dbg.ERROR_LOG("画像なし")
                    dunDbg.Debug.showSituation(situation, True)
                    # □□□
                    # □□■
                    # ?○?
                    status = calc.bitmask(status, 4 << 4)  # 4
            elif map.Judge.isNotWall(situation[6][0]):
                # □■?
                # □□■
                # ?○?
                status = calc.bitmask(status, 28 << 4)  # 28
            else:
                # ■■?
                # □□■
                # ?○?
                status = calc.bitmask(status, 2 << 4)  # 1
        elif map.Judge.isWall(situation[1][0]) and map.Judge.isNotWall(situation[2][0]) and map.Judge.isNotWall(situation[3][0]):
            # ???
            # ???
            # ■□□
            # ?○?
            if map.Judge.isNotWall(situation[5][0]):
                if map.Judge.isWall(situation[6][0]) and map.Judge.isNotWall(situation[7][0]):
                    dbg.ERROR_LOG("画像なし")
                    dunDbg.Debug.showSituation(situation, True)
                    # ■□□
                    # ■□□
                    # ?○?
                    status = calc.bitmask(status, 4 << 4)  # 4
                elif map.Judge.isNotWall(situation[6][0]) and map.Judge.isWall(situation[7][0]):
                    if map.Judge.isNotWall(situation[8][0]):
                        # ?□?
                        # □□■
                        # ■□□
                        # ?○?
                        status = calc.bitmask(status, 23 << 4)  # 23
                    else:
                        if map.Judge.isNotWall(situation[9][0]):
                            dbg.ERROR_LOG("画像なし")
                            dunDbg.Debug.showSituation(situation, True)
                            # □■?
                            # □□■
                            # ■□□
                            # ?○?
                            status = calc.bitmask(status, 12 << 4)  # 12
                        else:
                            # ■■?
                            # □□■
                            # ■□□
                            # ?○?
                            status = calc.bitmask(status, 12 << 4)  # 12
                else:  # 4
                    dbg.ERROR_LOG("画像なし")
                    dunDbg.Debug.showSituation(situation, True)
                    # □□□
                    # ■□□
                    # ?○?
                    status = calc.bitmask(status, 6 << 4)  # 6
            else:
                if map.Judge.isNotWall(situation[7][0]):
                    # ?■□
                    # ■□□
                    # ?○?
                    status = calc.bitmask(status, 30 << 4)  # 30
                else:
                    # ?■■
                    # ■□□
                    # ?○?
                    status = calc.bitmask(status, 1 << 4)  # 1
        return status
