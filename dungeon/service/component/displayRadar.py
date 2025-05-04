import dungeon.img as img
import common.layer.response.response as response
import common.layer.code.code as code
import pyd.indexDungeon as INDEX


class DisplayRadar:
	def __init__(self, screen, img_list, situation, enemy_pos_list, flash):
		self._screen = screen
		self._img_list = img_list
		self._situation = situation
		self._enemy_pos_list = enemy_pos_list
		self._flash = flash

	def execute(self, pos_x, pos_y):
		# 中心
		self._screen.blit(self.__get_img(9), (pos_x, pos_y))
		self._screen.blit(self.__get_img(6), (pos_x, pos_y + 20))
		self._screen.blit(self.__get_img(1), (pos_x, pos_y + 40))
		self._screen.blit(self.__get_img(0), (pos_x, pos_y + 60))
		self._screen.blit(self.__get_img(12), (pos_x, pos_y + 80))
		self._screen.blit(self.__get_img(15), (pos_x, pos_y + 100))
		self._screen.blit(self.__get_img(18), (pos_x, pos_y + 120))
		self._screen.blit(self.__get_img(8), (pos_x + 20, pos_y))
		self._screen.blit(self.__get_img(5), (pos_x + 20, pos_y + 20))
		self._screen.blit(self.__get_img(2), (pos_x + 20, pos_y + 40))
		self._screen.blit(self._img_list[INDEX.PLAYER()][img.Select.PLAYER(self._flash)], (pos_x + 20, pos_y + 60))
		self._screen.blit(self.__get_img(11), (pos_x + 20, pos_y + 80))
		self._screen.blit(self.__get_img(14), (pos_x + 20, pos_y + 100))
		self._screen.blit(self.__get_img(17), (pos_x + 20, pos_y + 120))
		self._screen.blit(self.__get_img(10), (pos_x + 40, pos_y))
		self._screen.blit(self.__get_img(7), (pos_x + 40, pos_y + 20))
		self._screen.blit(self.__get_img(3), (pos_x + 40, pos_y + 40))
		self._screen.blit(self.__get_img(4), (pos_x + 40, pos_y + 60))
		self._screen.blit(self.__get_img(13), (pos_x + 40, pos_y + 80))
		self._screen.blit(self.__get_img(16), (pos_x + 40, pos_y + 100))
		self._screen.blit(self.__get_img(19), (pos_x + 40, pos_y + 120))
		self._screen.blit(self.__get_img(20), (pos_x - 20, pos_y))
		self._screen.blit(self.__get_img(21), (pos_x - 20, pos_y + 20))
		self._screen.blit(self.__get_img(22), (pos_x - 20, pos_y + 40))
		self._screen.blit(self.__get_img(23), (pos_x - 20, pos_y + 60))
		self._screen.blit(self.__get_img(24), (pos_x - 20, pos_y + 80))
		self._screen.blit(self.__get_img(25), (pos_x - 20, pos_y + 100))
		self._screen.blit(self.__get_img(26), (pos_x - 20, pos_y + 120))
		self._screen.blit(self.__get_img(27), (pos_x + 60, pos_y))
		self._screen.blit(self.__get_img(28), (pos_x + 60, pos_y + 20))
		self._screen.blit(self.__get_img(29), (pos_x + 60, pos_y + 40))
		self._screen.blit(self.__get_img(30), (pos_x + 60, pos_y + 60))
		self._screen.blit(self.__get_img(31), (pos_x + 60, pos_y + 80))
		self._screen.blit(self.__get_img(32), (pos_x + 60, pos_y + 100))
		self._screen.blit(self.__get_img(33), (pos_x + 60, pos_y + 120))
		self._screen.blit(self.__get_img(34), (pos_x - 40, pos_y))
		self._screen.blit(self.__get_img(35), (pos_x - 40, pos_y + 20))
		self._screen.blit(self.__get_img(36), (pos_x - 40, pos_y + 40))
		self._screen.blit(self.__get_img(37), (pos_x - 40, pos_y + 60))
		self._screen.blit(self.__get_img(38), (pos_x - 40, pos_y + 80))
		self._screen.blit(self.__get_img(39), (pos_x - 40, pos_y + 100))
		self._screen.blit(self.__get_img(40), (pos_x - 40, pos_y + 120))
		self._screen.blit(self.__get_img(41), (pos_x + 80, pos_y))
		self._screen.blit(self.__get_img(42), (pos_x + 80, pos_y + 20))
		self._screen.blit(self.__get_img(43), (pos_x + 80, pos_y + 40))
		self._screen.blit(self.__get_img(44), (pos_x + 80, pos_y + 60))
		self._screen.blit(self.__get_img(45), (pos_x + 80, pos_y + 80))
		self._screen.blit(self.__get_img(46), (pos_x + 80, pos_y + 100))
		self._screen.blit(self.__get_img(47), (pos_x + 80, pos_y + 120))
		return response.Response(data=True, result=code.Code.OK)

	def __get_img(self, number):
		is_enemy = 0
		wall_or_path = img.Select.WALL_OR_PATH(self._situation[number][0])
		for enemy_pos in self._enemy_pos_list:
			if enemy_pos.x == self._situation[number][1] and enemy_pos.y == self._situation[number][2]:
				is_enemy = 1
		return self._img_list[wall_or_path][is_enemy]