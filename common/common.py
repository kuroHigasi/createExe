import pyd.hitJudge as jdg
import common.debug.debug as dbg
import pyd.save as SAVE
import common.save.aes as AES_METHOD
import os
import sys
import re
import binascii
# LOG TEXT
NOT_FOLDER_LOG = "フォルダがないです"
SAVE_ERROR_LOG = "[SaveAction.__save]エラー発生"
LOAD_ERROR_LOG = "[SaveAction.__load]エラー発生"
DELETE_ERROR_LOG = "[SaveAction.__delete]エラー発生"
# debug flag
DEBUG_FLAG = True

# window_size
WINDOW_SIZE = (800, 600)
TEST_SIZE = (1000, 800)


def resource_path(relative):
    """

    :rtype: object
    """
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
    @staticmethod
    def click(pos_x, pos_y, width, height, x, y, click_x, click_y, click):
        # BUTTON設定有無判定
        if not (pos_x == -1 and pos_y == -1):
            # 左クリック判定
            if (not (click_x == -1 and click_y == -1) and
                    jdg.hitJudgeSquare(pos_x, pos_y, width, height, x, y) and
                    (click and
                     jdg.hitJudgeSquare(pos_x, pos_y, width, height, click_x, click_y))):
                return True
            return False
        # BUTTON設定なし
        else:
            return False


class SaveMethod(AES_METHOD.Aes):
    def save(self, data, head, tail):
        dbg.LOG("SAVE処理開始")
        SaveMethod.__folder_check()
        if not (os.path.exists(SAVE.FOLDER())):
            dbg.LOG(SAVE.FOLDER() + NOT_FOLDER_LOG)
            os.mkdir(SAVE.FOLDER())
            dbg.LOG(SAVE.FOLDER() + "フォルダを作成しました")
        if not (os.path.isfile(SAVE.PASS())):
            try:
                with open(SAVE.PASS(), mode='xb') as f:
                    f.write(super().encrypt(head + data + tail))
            except FileExistsError:
                dbg.ERROR_LOG(SAVE_ERROR_LOG)
        else:
            try:
                with open(SAVE.PASS(), mode='rb') as f:
                        text = self.__binaryLoad(f)
                        rj = head + "(.+)" + tail
                        r_text = re.sub(rj, "", text)
            except :
                r_text = ""
                dbg.ERROR_LOG(SAVE_ERROR_LOG)
            try:
                with open(SAVE.PASS(), mode='ab+') as f:
                    f.truncate(0)
                    text = r_text + head + data +tail
                    f.write(super().encrypt(text))
            except FileExistsError:
                dbg.ERROR_LOG(SAVE_ERROR_LOG)
                return False
        dbg.LOG("SAVE処理終了")
        return True

    def load(self, head, tail):
        dbg.LOG("LOAD処理開始")
        retData = ""
        SaveMethod.__folder_check()
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
                dbg.ERROR_LOG(LOAD_ERROR_LOG)
        dbg.LOG("LOAD処理終了")
        return retData

    def delete(self, head, tail):
        dbg.LOG("DELETE処理開始")
        SaveMethod.__folder_check()
        if not (os.path.isfile(SAVE.PASS())):
            try:
                with open(SAVE.PASS(), mode='xb') as f:
                    f.write(b"")
            except FileExistsError:
                dbg.ERROR_LOG(DELETE_ERROR_LOG)
        else:
            try:
                with open(SAVE.PASS(), mode='rb') as f:
                        text = self.__binaryLoad(f)
                        r_text = re.sub(head+"(.+)"+tail, "", text)
                try:
                    with open(SAVE.PASS(), mode='ab+') as f:
                        f.truncate(0)
                        f.write(super().encrypt(r_text))
                except FileExistsError:
                    dbg.ERROR_LOG(DELETE_ERROR_LOG)
            except FileExistsError:
                dbg.ERROR_LOG(DELETE_ERROR_LOG)
        dbg.LOG("DELETE処理終了")

    @staticmethod
    def __folder_check():
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
