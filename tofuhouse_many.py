from mcpi import block, minecraft

WHITE_CONCRETE = 251
SEA_LANTERN = 169
WHITE_CARPET = block.Block(171, 0)
BROWN_CARPET = block.Block(171, 12)


def house(mc, x, y, z, w, h, d):
  # walls
  #mc.setBlocks(x, y, z, x+w, y, z+d, WHITE_CONCRETE)
  mc.setBlocks(x+w, y, z, x+w, y+h, z+d, WHITE_CONCRETE)
  mc.setBlocks(x, y+h, z, x+w, y+h, z+d, WHITE_CONCRETE)
  mc.setBlocks(x, y, z+d, x+w, y+h, z+d, WHITE_CONCRETE)
  mc.setBlocks(x, y, z, x, y+h, z+d, WHITE_CONCRETE)
  mc.setBlocks(x, y, z, x+w, y+h, z, WHITE_CONCRETE)
  # door
  mc.setBlock(x+3, y, z, block.DOOR_IRON.id, 1)
  mc.setBlock(x+3, y+1, z, block.DOOR_IRON.id, 9)
  # windows
  mc.setBlock(x+1, y+1, z, block.GLASS_PANE.id)
   # lantern
  mc.setBlock(x+2, y+2, z+2, block.GLOWSTONE_BLOCK.id)
  # carpet
  mc.setBlocks(x+1, y, z+1, x+w-1, y, z+d-1, BROWN_CARPET)


def main():
  mc = minecraft.Minecraft.create()
  pos = mc.player.getTilePos()
  for i in range(10):
    for j in range(10):
      house(mc, pos.x-20 + i * 7, pos.y, pos.z+5 + j * 7, 4, 3, 4)


if __name__ == '__main__':
    main()

