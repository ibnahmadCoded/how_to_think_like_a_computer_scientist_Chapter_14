class QueenSprite:

    def __init__(self, img, target_posn):
        """ Create and initialize a queen for this
            target position on the board
        """
        self.image = img
        self.target_position = target_posn
        self.position = target_position

    def update(self):
        return              #Do nothing atm

    def draw(self, target_surface):
        target_surface.blit(self.image, self.position)

    
