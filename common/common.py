import common.pyd.hitJudge as jdg
import common.debug.debug as dbg
import common.pyd.save as SAVE
import common.save.aes as AES_METHDO
import os
import sys
import re
import binascii
# LOG TEXT
NOT_FOLDER_LOG = "フォルダがないです"
# debug flag
DEBUG_FLAG = True

# window_size
WINDOW_SIZE = (800, 600)
TEST_SIZE = (1000, 800)


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


class Colors:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)


class Flash:
    def __init__(self, division=10, index=2):
        self.count = 0
        self.patarn = 0
        self.division = division
        self.index = index

    def countup(self):
        self.count = self.count + 1
        if self.count == self.division:
            self.count = 0
            if self.patarn < self.index - 1:
                self.patarn = self.patarn + 1
            else:
                self.patarn = 0

    def flash(self):
        return self.patarn


class Judge:
    def click(posX, posY, sizeW, sizeH, x, y, clickX, clickY, click, funcName="test"):
        # BUTTON設定有無判定
        if (not (posX == -1 and posY == -1)):
            # 左クリック判定
            if (not (clickX == -1 and clickY == -1) and
                    jdg.hitJudgeSquare(posX, posY, sizeW, sizeH, x, y) and
                    (click and
                     jdg.hitJudgeSquare(posX, posY, sizeW, sizeH, clickX, clickY))):
                return True
        # BUTTON設定なし
        else:
            dbg.ERROR_LOG("[" + funcName + "]ボタン設定不備")
        return False


class cmnDisplay:
    def dispText(self, screen, font, text, x, y, color=Colors.white):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width() / 2, y))
        screen.blit(text_surface, text_rect)

    def dispNumber(self, screen, font, number, x, y, color=Colors.white):
        text_surface = font.render(str(number), True, color)
        numCount = len(str(number))
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width() / 2 - ((numCount - 1) * 6), y))
        screen.blit(text_surface, text_rect)


class SaveMethod(AES_METHDO.Aes):
    def save(self, data, head, tail):
        dbg.LOG("SAVE処理開始")
        SaveMethod.__folderCheck()
        if not (os.path.exists(SAVE.FOLDER())):
            dbg.LOG(SAVE.FOLDER() + NOT_FOLDER_LOG)
            os.mkdir(SAVE.FOLDER())
            dbg.LOG(SAVE.FOLDER() + "フォルダを作成しました")
        if not (os.path.isfile(SAVE.PASS())):
            try:
                with open(SAVE.PASS(), mode='xb') as f:
                    f.write(super().encrypt(head + data + tail))
            except FileExistsError:
                dbg.ERROR_LOG("[SaveAction.__save]エラー発生")
        else:
            try:
                with open(SAVE.PASS(), mode='rb') as f:
                        rText = ""
                        text = self.__binaryLoad(f)
                        rj = head + "(.+)" + tail
                        rText = re.sub(rj, "", text)
            except :
                rText = ""
                dbg.ERROR_LOG("[SaveAction.__save]エラー発生")
            try:
                with open(SAVE.PASS(), mode='ab+') as f:
                    f.truncate(0)
                    text = rText + head + data +tail
                    f.write(super().encrypt(text))
            except FileExistsError:
                dbg.ERROR_LOG("[SaveAction.__save]エラー発生")
        dbg.LOG("SAVE処理終了")

    def load(self, head, tail):
        dbg.LOG("LOAD処理開始")
        retData = ""
        SaveMethod.__folderCheck()
        if not (os.path.exists(SAVE.FOLDER())):
            dbg.LOG(SAVE.FOLDER() + NOT_FOLDER_LOG)
        elif not (os.path.isfile(SAVE.PASS())):
            dbg.LOG(SAVE.FOLDER() + NOT_FOLDER_LOG)
        else:
            try:
                with open(SAVE.PASS(), mode='rb') as f:
                        text = self.__binaryLoad(f)
                        try:
                            r = re.search(head+"(.+)"+tail, text)
                            retData = r.group(1)
                        except BaseException:
                            dbg.LOG("[SaveAction.__load]取得データなし")
            except FileExistsError:
                dbg.ERROR_LOG("[SaveAction.__load]エラー発生")
        dbg.LOG("LOAD処理終了")
        return retData

    def delete(self, head, tail):
        dbg.LOG("DELETE処理開始")
        SaveMethod.__folderCheck()
        if not (os.path.isfile(SAVE.PASS())):
            try:
                with open(SAVE.PASS(), mode='xb') as f:
                    f.write("")
            except FileExistsError:
                dbg.ERROR_LOG("[SaveAction.__save]エラー発生")
        else:
            try:
                with open(SAVE.PASS(), mode='rb') as f:
                        text = self.__binaryLoad(f)
                        rText = re.sub(head+"(.+)"+tail, "", text)
                try:
                    with open(SAVE.PASS(), mode='ab+') as f:
                        f.truncate(0)
                        f.write(super().encrypt(rText))
                except FileExistsError:
                    dbg.ERROR_LOG("[SaveAction.__save]エラー発生")
            except FileExistsError:
                dbg.ERROR_LOG("[SaveAction.__save]エラー発生")
        dbg.LOG("DELETE処理終了")

    def __folderCheck():
        if not (os.path.exists(SAVE.FOLDER())):
            dbg.LOG(SAVE.FOLDER() + NOT_FOLDER_LOG)
            os.mkdir(SAVE.FOLDER())
            dbg.LOG(SAVE.FOLDER() + "フォルダを作成しました")

    def __binaryLoad(self, f):
        text = ""
        tagLen = f.read(4)
        if tagLen != b"":
            dataList = []
            f.seek(4)
            seekCount1 = int(str(binascii.b2a_hex(tagLen), 'utf-8'))
            dataList.insert(0, f.read(seekCount1))
            f.seek(seekCount1 + 4)
            nonceLen = f.read(4)
            seekCount2 = int(str(binascii.b2a_hex(nonceLen), 'utf-8'))
            f.seek(seekCount1 + 8)
            dataList.insert(1, f.read(seekCount2))
            f.seek(seekCount1 + seekCount2 + 8)
            dataList.insert(2, f.read())
            text = super().decrypt(dataList)
        return text