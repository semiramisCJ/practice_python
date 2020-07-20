class TrainComposition:
    
    def __init__(self):
        self.right = None
        self.left = None
        self.values = [None, None]
    
    def attach_wagon_from_left(self, wagonId):
        if(wagonId in self.values):
            print("No repeated values allowed")
            return
        self.values.insert(0, wagonId)
        if self.right == None:
            self.right = self.left
        self.left = wagonId
    
    def attach_wagon_from_right(self, wagonId):
        if(wagonId in self.values):
            print("No repeated values allowed")
            return
        self.values.append( wagonId )
        if self.left == None:
            self.left = self.right
        self.right = wagonId
    
    def detach_wagon_from_left(self):
        previous_idx = self.values.index( self.left )
        try:
            self.left = self.values[ previous_idx + 1 ]
        except:
            self.left = None
        return self.values.pop(previous_idx)
    
    def detach_wagon_from_right(self):
        previous_idx = self.values.index( self.right )
        try:
            self.right = self.values[ previous_idx - 1 ]
        except:
            self.right = None
        return self.values.pop(previous_idx)

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    train.attach_wagon_from_right(15)
    train.attach_wagon_from_right(25)
    train.attach_wagon_from_left(17)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13