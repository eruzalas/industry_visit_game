import road
import collision_preset

# this holds information about each game map stage, allowing for easy addition of maps and smooth map changes
class Game_Map(object):
    def __init__(self, filename):
        # strip filename of newline
        self.filename = filename.rstrip()

        # assign local variables
        self.player_xpos = 0
        self.player_ypos = 0
        self.roads = []
        self.presets = []
        self.car_limit = 0
        self.left_traffic_spawns = []
        self.right_traffic_spawns = []
        self.text = []
        self.reading_text = False

        # request processing
        self.process_filename()

    # loads information into relevant variables based off file information
    def process_filename(self):
        # open and load file using concatenated filename with file path
        filename = "game_files/maps/" + self.filename
        f = open(filename, "r")
        lines = f.readlines()

        xpos = 0
        ypos = 0

        index = 0
        # loop each line
        for line in lines:
            if len(line) == 0 or line[0] == "#":
                continue

            # if first line in file then load into car_limit or into reading_text based off line content
            if index == 0:
                if line.rstrip() != "FIN":
                    self.car_limit = int(line.rstrip())
                    index += 1
                    continue

                else:
                    self.reading_text = True
                    index += 1
                    continue

            # if not reading_text (reading_text signifies if a file contains the "congrats" information or not)
            if not self.reading_text:
                # split line and assign to certain locations
                line = line.split(',')
                entity = line[0]

                if len(line) == 2:
                    # load car spawns
                    if entity == "+":
                        self.left_traffic_spawns.append(int(line[1]))
                        
                    else:
                        self.right_traffic_spawns.append(int(line[1]))

                    continue

                else:
                    # set positions
                    xpos = int(line[1])
                    ypos = int(line[2])

                # set player
                if entity == "player":
                    self.player_xpos = xpos
                    self.player_ypos = ypos
                    continue

                # generate roads
                elif "road" in entity:
                    genroad = road.Road(xpos, ypos, entity)
                    self.roads.append(genroad)
                    continue

                else:
                    # generate collision objects
                    shape = collision_preset.Collision_Preset(xpos, ypos, entity)
                    self.presets.append(shape)

            else:
                self.text.append(line.rstrip())

        f.close()

