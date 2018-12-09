from mcpi import block, minecraft


def main():
  mc = minecraft.Minecraft.create()
  pos = mc.player.getTilePos()
  mc.setBlocks(pos.x-100, pos.y, pos.z-100,
               pos.x+100, pos.y+100, pos.z+100, block.AIR.id)
  mc.setBlocks(pos.x-100, pos.y-1, pos.z-100,
               pos.x+100, pos.y-1, pos.z+100, block.GRASS.id)


if __name__ == '__main__':
    main()

