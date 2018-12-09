from mcpi import minecraft


def main():
  mc = minecraft.Minecraft.create()
  pos = mc.player.getTilePos()

  while True:
      blockEvents = mc.events.pollBlockHits()
      for be in blockEvents:
          b = mc.getBlockWithData(be.pos.x, be.pos.y, be.pos.z)
          print(b)


if __name__ == '__main__':
    main()

