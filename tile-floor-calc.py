#Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

#set variables


#take in floor, tile & cost values from user input
print("What is the floor width in feet?")
floorW = input()
print("What is the floor length in feet?")
floorL = input()
print("What is the tile's width in inches?")
tileW_in = input()
print("What is the tile's length in inches?")
tileL_in = input()
print("What is the cost per tile?")
tileCost = input()

tileW_int = int(tileW_in)
tileL_int = int(tileL_in)
tileW = tileW_int/12.0
tileL = tileL_int/12.0
floor_width = int(floorW)
floor_length = int(floorL)
tile_cost = int(tileCost)

#calculate area of floor
floor_area = floor_width * floor_length

#calculate area of each tile
tile_area = tileW * tileL

#calculate number of required tiles
req_tile = floor_area/tile_area

#calculate total cost
tot_cost = req_tile * tile_cost
#verify results
print(floor_area)
print(tile_area)
print(req_tile)
print(tot_cost)
