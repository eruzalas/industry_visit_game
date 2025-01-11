import pyglet

# this is the parent object for other code classes
class GameObject(object):
    # accept input of x, y and filename (for loading information)
    def __init__(self, x, y, filename):
        # set local variables
        self.xpos = x
        self.ypos = y
        self.width = 0
        self.length = 0
        self.display = []
        self.filename = filename

        # check object name
            # if object is of "COL" (collision object) type or "car" (car entity) type, then process information accordingly
            # file processing is not needed if object is not of these two types
        if "COL" and "car" not in self.filename:
            if "txt" in self.filename:
                # process text based
                self.process_textbased_preset()

            else:
                # process image
                self.process_image()

    # load image using pyglet
    def process_image(self):
        # concatenate filename with file path
        filename = "game_files/maps/presets/" + self.filename

        # open and load file
        f = open(filename, "rb")
        image = pyglet.image.load(self.filename, file=f)

        # set image as sprite to allow for batch rendering
        self.display.append(pyglet.sprite.Sprite(image, self.xpos, self.ypos))

    # load textbased info via pyglet
    def process_textbased_preset(self):
        # add file path to name
        filename = "game_files/maps/presets/" + self.filename

        # open and read
        f = open(filename, "r")
        lines = f.readlines()

        # initialise variables
        length = 0
        width = 0

        # read lines and set length and width
        for line in lines:
            if len(line) == 0 or line[0] == "#":
                continue
            
            split = line.split(',')
            
            if len(split) == 2:
                length = split[0]
                width = split[1]

        # close and set
        f.close()
        self.length = int(length)
        self.width = int(width)