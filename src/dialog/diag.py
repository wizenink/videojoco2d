class Dialog:
    def _prepareDialog(self):
        newList = []
        for string in self.dialogList:
            if(len(string) >= self.maxChars):
                
    def  __init__(self,dialogName):
        self.dialogList = resourceManager.loadDialog(dialogName)
        self.maxChars = 20
