import mcpi.minecraft as minecraft
import mcpi.block as block


mc = minecraft.Minecraft.create()



#Making the welecome mat




#Setting the welcome mat location

setPosition = mc.player.getTilePos()
x,y,z = setPosition.x+1,setPosition.y,setPosition.z

while True:
    
    currentPosition = mc.player.getTilePos()
    onWelcomeMat = False;
    
    if x == currentPosition.x and y== currentPosition.y and z== currentPosition.z :
        onWelcomeMat = True;
    else:
        onWelcomeMat = False;
    
    if onWelcomeMat == True:
        mc.postToChat("You are on the block.")
        mc.setBlocks(x+5,  y,  z,  x+15,  y+10  , z  ,block.GOLD_ORE.id )
        mc.setBlocks(x+5,  y, z+10,  15,  y+10  ,z+10  ,block.GOLD_ORE.id )
        mc.setBlocks(x+5,  y,  currentPosition.z,  currentPosition.x+5,  currentPosition.y+10  ,currentPosition.z+10  ,block.GOLD_ORE.id )
        mc.setBlocks(x+15,  currentPosition.y,  currentPosition.z,  currentPosition.x+15,  currentPosition.y+10  ,currentPosition.z+10  ,block.GOLD_ORE.id )
    else:
        mc.postToChat("You are on the block.")
        mc.setBlocks(currentPosition.x+5,  currentPosition.y,  currentPosition.z,  currentPosition.x+15,  currentPosition.y+10  ,currentPosition.z  ,block.AIR.id )
        mc.setBlocks(currentPosition.x+5,  currentPosition.y,  currentPosition.z+10,  currentPosition.x+15,  currentPosition.y+10  ,currentPosition.z+10  ,block.AIR.id )
        mc.setBlocks(currentPosition.x+5,  currentPosition.y,  currentPosition.z,  currentPosition.x+5,  currentPosition.y+10  ,currentPosition.z+10  ,block.AIR.id)
        mc.setBlocks(currentPosition.x+15,  currentPosition.y,  currentPosition.z,  currentPosition.x+15,  currentPosition.y+10  ,currentPosition.z+10  ,block.AIR.id )
    
