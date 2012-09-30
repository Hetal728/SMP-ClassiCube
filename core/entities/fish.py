#    iCraft is Copyright 2010-2011 both
#
#    The Archives team:
#                   <Adam Guy> adam@adam-guy.com AKA "Adam01"
#                   <Andrew Godwin> andrew@aeracode.org AKA "Aera"
#                   <Dylan Lukes> lukes.dylan@gmail.com AKA "revenant"
#                   <Gareth Coles> colesgareth2@hotmail.com AKA "gdude2002"
#
#    And,
#
#    The iCraft team:
#                   <Andrew Caluzzi> tehcid@gmail.com AKA "tehcid"
#                   <Andrew Dolgov> fox@bah.org.ru AKA "gothfox"
#                   <Andrew Horn> Andrew@GJOCommunity.com AKA "AndrewPH"
#                   <Brad Reardon> brad@bradness.co.cc AKA "PixelEater"
#                   <Clay Sweetser> CDBKJmom@aol.com AKA "Varriount"
#                   <James Kirslis> james@helplarge.com AKA "iKJames"
#                   <Jason Sayre> admin@erronjason.com AKA "erronjason"
#                   <Jonathon Dunford> sk8rjwd@yahoo.com AKA "sk8rjwd"
#                   <Joseph Connor> destroyerx100@gmail.com AKA "destroyerx1"
#                   <Kamyla Silva> supdawgyo@hotmail.com AKA "NotMeh"
#                   <Kristjan Gunnarsson> kristjang@ffsn.is AKA "eugo"
#                   <Nathan Coulombe> NathanCoulombe@hotmail.com AKA "Saanix"
#                   <Nick Tolrud> ntolrud@yahoo.com AKA "ntfwc"
#                   <Noel Benzinger> ronnygmod@gmail.com AKA "Dwarfy"
#                   <Randy Lyne> qcksilverdragon@gmail.com AKA "goober"
#                   <Willem van der Ploeg> willempieeploeg@live.nl AKA "willempiee"
#
#    Disclaimer: Parts of this code may have been contributed by the end-users.
#
#    iCraft is licensed under the Creative Commons
#    Attribution-NonCommercial-ShareAlike 3.0 Unported License. 
#    To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
#    Or, send a letter to Creative Commons, 171 2nd Street,
#    Suite 300, San Francisco, California, 94105, USA.

var_cango = True
if entity[5] >= 3:
    i = randint(-1,1)
    k = randint(-1,1)
    j = randint(-1,1)
    entity[4] = (i,j,k)
    entity[5] = 0
entity[5] = randint(1,5)
l, m, n = entity[4]
try:
    blocktocheck = ord(world.blockstore.raw_blocks[world.blockstore.get_offset(x+l,y+m,z+n)])
    if blocktocheck != 8:
        var_cango = False
except:
    pass
if var_cango:
    block = 8
    self.client.queueTask(TASK_BLOCKSET, (x,y,z, block), world=world)
    self.client.sendBlock(x,y,z, block)
    if entity[6]:
        block = randint(22,36)
    else:
        block = 22
    self.client.queueTask(TASK_BLOCKSET, (x+l,y+m,z+n, block), world=world)
    self.client.sendBlock(x+l,y+m,z+n, block)
    var_position = (x+l,y+m,z+n)
    x,y,z = var_position
