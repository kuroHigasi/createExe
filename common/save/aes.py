
from Crypto.Cipher import AES
import common.debug.debug as dbg


class Aes:
    def __init__(self):
        self.__key = b"\x14m\xee\xa3\xa0\x8d\x87\xb5:\xeb^ZGR\x86\x8c"

    def encrypt(self, text):
        try:
            cipher = AES.new(self.__key, AES.MODE_EAX)
            (cipherText, tag) = cipher.encrypt_and_digest(text.encode())
            dbg.LOG("[Aes.encrypt]暗号化処理 START")
            dbg.LOG("[Aes.encrypt]cipherText")
            dbg.LOG(str(cipherText))
            dbg.LOG("[Aes.encrypt]tag")
            dbg.LOG(str(tag))
            tagLen = bytes.fromhex(str(format(len(tag), '08')))
            nonce = cipher.nonce
            nonceLen = bytes.fromhex(str(format(len(nonce), '08')))
            dbg.LOG("[Aes.encrypt]nonce")
            dbg.LOG(str(nonce))
            dbg.LOG("[Aes.encrypt]暗号化処理 END")
            return tagLen + tag + nonceLen + nonce + cipherText
        except:
            dbg.ERROR_LOG("[Aes.encrypt]暗号化処理 失敗 END")
            return b""

    def decrypt(self, datalist):
        dec = AES.new(self.__key, AES.MODE_EAX, datalist[1])
        return dec.decrypt_and_verify(datalist[2], datalist[0]).decode()