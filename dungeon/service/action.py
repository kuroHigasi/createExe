import dungeon.layer.request.dungeonActionRequest as dungeonActionRequest


class Action:
	def __init__(self, request: dungeonActionRequest.DungeonStatusRequest):
		self._request = request
