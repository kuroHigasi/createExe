class Common:
    def isPosPath(map, judDepth, judWidth, maxWidth, maxDepth):
        if judWidth < maxWidth and judWidth >= 0 and judDepth < maxDepth and judDepth >= 0:
            return map[judDepth][judWidth]
        else:
            return 0
