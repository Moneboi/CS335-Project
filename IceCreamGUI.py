from IceCreamOrder import *
#from IceCreamTutorial import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import * 
import sys

# Subclass QMainWindow to customize your application's main window
class IceCreamGUI(QMainWindow):
#Method: Display the default UI
    def __init__(self):
        super(IceCreamGUI, self).__init__()
    #Set the window Title
        self.setWindowTitle("Ice Cream Parlor")
    #Set geometry of the window
        self.setFixedSize(1000,800)
    #Default ice cream order
        self.order = IceCreamOrder()
    #Start Menu widgets
        self.startMenu()
    #Buttons for game
        self.buttons()
        
#Method: Before the game starts UI
    def startMenu(self):
#Start menu
    #Play menu music
        self.order.playMusic('game2')
    #Main Game Background
        #Create label
        self.gameBackground = QLabel(self)
        self.gameBackgroundPixmap = QPixmap('Ice Cream Parlor Color.png')
        self.gameBackground.setPixmap(self.gameBackgroundPixmap)
        self.gameBackground.resize(self.gameBackgroundPixmap.width(), self.gameBackgroundPixmap.height())
    #Score Labels
        self.scoreName = QLabel("Score:",self)
        self.scoreName.setFont(QFont('Times', 20)) 
        self.scoreName.setGeometry(20, 20, 80, 35)
        self.scoreNum = QLabel("0",self)
        self.scoreNum.setFont(QFont('Times', 20)) 
        self.scoreNum.setGeometry(106, 20, 135, 35)
    #Timer Labels
        self.timerLabel = QLabel("Time:",self)
        self.timerLabel.setFont(QFont('Times', 20)) 
        self.timerLabel.setGeometry(23, 50, 77, 35)
        self.countdownLabel = QLabel("60", self)
        self.countdownLabel.setFont(QFont('Times', 20)) 
        self.countdownLabel.setGeometry(106, 52, 64, 35)
    #Order Labels
        self.orderLabel = QLabel("Order #",self)
        self.orderLabel.setFont(QFont('Times', 19)) 
        self.orderLabel.setGeometry(408, 29, 102, 35)
        self.orderNumLabel = QLabel(str(self.order.orderNum),self)
        self.orderNumLabel.setFont(QFont('Times', 19)) 
        self.orderNumLabel.setGeometry(510, 29, 57, 35)
    #Order Image Label    
        self.orderImageLabel = QLabel(self)
        self.orderImageLabel.setGeometry(402, 70, 196, 338)
        self.orderImageLabel.hide()
    #Instructions
        self.instructionsLabel = QLabel(self)
        self.instructionsLabel.setGeometry(20, 70, 960, 338)
        self.instructionsLabelPixmap = QPixmap('How to Play.png')
        self.instructionsLabel.setPixmap(self.instructionsLabelPixmap)
        self.instructionsLabel.resize(self.instructionsLabelPixmap.width(), self.instructionsLabelPixmap.height())
    #Points
        self.pointsLabel = QLabel(self)
        self.pointsLabel.setGeometry(530, 430, 450, 225)
        self.pointsLabelPixmap = QPixmap('Points Ice Cream.png')
        self.pointsLabel.setPixmap(self.pointsLabelPixmap)
        self.pointsLabel.resize(self.pointsLabelPixmap.width(), self.pointsLabelPixmap.height())
    #Start Button
        self.startButton = QPushButton("Click Here to Begin!", self)
        self.startButton.setGeometry(530,667,450,125)
        self.startButton.setFont(QFont('Times', 20))
        #Action for startButton      
        self.startButton.clicked.connect(self.startGame) 
    #Serve Button    
        self.serveButton = QPushButton("SERVE", self)
        self.serveButton.setGeometry(854,454,124,108)
        self.serveButton.setFont(QFont('Times', 20))
    #Action for Serve Button
        self.serveButton.clicked.connect(self.servedIceCream)
        #Disable and hide
        #self.serveButton.setEnabled(False)
        self.serveButton.hide()
    #Reset Button    
        self.resetButton = QPushButton("RESET", self)
        self.resetButton.setGeometry(854,660,124,108)
        self.resetButton.setFont(QFont('Times', 20))
    #Action for Reset Button
        self.resetButton.clicked.connect(self.resetIceCream)
        #Disable and hide
        #self.resetButton.setEnabled(False)
        self.resetButton.hide()
    #Label for scoops
        self.yourIceCreamLabel = QLabel("Your Ice Cream")
        self.yourIceCreamLabel.setGeometry(614, 430, 191, 35)
        self.yourIceCreamLabel.setFont(QFont('Times', 20))
    #Scoop Top Label
        self.scoopTop = QLabel(self)
        self.scoopTop.setGeometry(542, 468, 150, 100)
        self.scoopTop.hide()
    #Scoop Middle Label
        self.scoopMiddle = QLabel(self)
        self.scoopMiddle.setGeometry(542, 574, 150, 100)
        self.scoopMiddle.hide()
    #Scoop Bottom Label
        self.scoopBottom = QLabel(self)
        self.scoopBottom.setGeometry(542, 680, 150, 100)
        self.scoopBottom.hide()
    #Container Label
        self.containerLabel = QLabel(self)
        self.containerLabel.setGeometry(705, 549, 100, 150)
        self.containerLabel.hide()

#Method: UI for buttons (ice cream things)
    def buttons(self):
#Buttons for the ice cream CONTAINERS
    #Waffle Cone Button
        self.waffleConeButton = QPushButton("Waffle Cone", self)
        self.waffleConeButton.setGeometry(20, 430, 150, 100)
    #Setting image on button
        self.waffleConeButton.setIcon(QIcon(QPixmap('Waffle Cone.png')))
        self.waffleConeButton.setIconSize(QSize(150,100))
    #Waffle Cone Label
        self.waffleConeLabel = QLabel("Waffle Cone", self)
        self.waffleConeLabel.setGeometry(20, 490, 150, 50)
        self.waffleConeLabel.setFont(QFont('Times', 15))
        self.waffleConeLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #Action for waffle cone button
        self.waffleConeButton.clicked.connect(self.waffleConeClicked)    
    
    #Cake Cone Button
        self.cakeConeButton = QPushButton("Cake Cone", self)
        self.cakeConeButton.setGeometry(20, 555, 150, 100)
        #Setting image on button
        self.cakeConeButton.setIcon(QIcon(QPixmap('Cake Cone.png')))
        self.cakeConeButton.setIconSize(QSize(150,100))
    #Cake Cone Label
        #self.cakeConeLabel = QLabel("Cake Cone", self)
        #self.cakeConeLabel.setGeometry(20, 609, 150, 50)
        #self.cakeConeLabel.setFont(QFont('Times', 15))
        #self.cakeConeLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #Action for cake cone button
        self.cakeConeButton.clicked.connect(self.cakeConeClicked)
    #Cup Button
        self.cupButton = QPushButton(self)
        self.cupButton.setGeometry(20, 680, 150, 100)
        #Set image on button
        self.cupButton.setIcon(QIcon(QPixmap('Cup.png')))
        self.cupButton.setIconSize(QSize(150,100))
    #Cup Label
        self.cupLabel = QLabel("Cup", self)
        self.cupLabel.setGeometry(20, 734, 150, 50)
        self.cupLabel.setFont(QFont('Times', 15))
        self.cupLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #Action for cup button
        self.cupButton.clicked.connect(self.cupClicked)
        
#Buttons for the ice cream FLAVORS      
    #Vanilla Button
        self.vanillaButton = QPushButton(self)
        self.vanillaButton.setGeometry(190, 430, 150, 100)
        #Set image on button
        self.vanillaButton.setIcon(QIcon(QPixmap('Vanilla.png')))
        self.vanillaButton.setIconSize(QSize(150,100))
        #Vanilla Label
        self.vanillaLabel = QLabel("Vanilla", self)
        self.vanillaLabel.setGeometry(190, 484, 150, 50)
        self.vanillaLabel.setFont(QFont('Times', 15))
        self.vanillaLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #Action for vanilla button
        self.vanillaButton.clicked.connect(self.vanillaClicked)
        
    #Chocolate Button
        self.chocolateButton = QPushButton(self)
        self.chocolateButton.setGeometry(190, 555, 150, 100)
        #Set image on button
        self.chocolateButton.setIcon(QIcon(QPixmap('Chocolate.png')))
        self.chocolateButton.setIconSize(QSize(150,100))
    #Chocolate Label
        self.chocolateLabel = QLabel("Chocolate", self)
        self.chocolateLabel.setGeometry(190, 609, 150, 50)
        self.chocolateLabel.setFont(QFont('Times', 15))
        self.chocolateLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #Action for chocolate button
        self.chocolateButton.clicked.connect(self.chocolateClicked)
        
    #Strawberry Button
        self.strawberryButton = QPushButton(self)
        self.strawberryButton.setGeometry(190, 680, 150, 100)
        #Set image on button
        self.strawberryButton.setIcon(QIcon(QPixmap('Strawberry.png')))
        self.strawberryButton.setIconSize(QSize(150,100))
    #Strawberry Label
        self.strawberryLabel = QLabel("Strawberry", self)
        self.strawberryLabel.setGeometry(190, 734, 150, 50)
        self.strawberryLabel.setFont(QFont('Times', 15))
        self.strawberryLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #Action for strawberry button
        self.strawberryButton.clicked.connect(self.strawberryClicked)
        
#Buttons for the ice cream TOPPINGS        
    #Cherry Button
        self.cherryButton = QPushButton(self)
        self.cherryButton.setGeometry(360, 430, 150, 100)
        #Set image on button
        self.cherryButton.setIcon(QIcon(QPixmap('Cherry.png')))
        self.cherryButton.setIconSize(QSize(150,100))
    #Cherry Label
        self.cherryLabel = QLabel("Cherry", self)
        self.cherryLabel.setGeometry(360, 484, 150, 50)
        self.cherryLabel.setFont(QFont('Times', 15))
        self.cherryLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #Action for cherry button
        self.cherryButton.clicked.connect(self.cherryClicked)
            
    #Sprinkles Button
        self.sprinklesButton = QPushButton(self)
        self.sprinklesButton.setGeometry(360, 555, 150, 100)
        #Set image on button
        self.sprinklesButton.setIcon(QIcon(QPixmap('Sprinkles.png')))
        self.sprinklesButton.setIconSize(QSize(150,100))    
    #Sprinkles Label
        self.sprinklesLabel = QLabel("Sprinkles", self)
        self.sprinklesLabel.setGeometry(360, 609, 150, 50)
        self.sprinklesLabel.setFont(QFont('Times', 15))
        self.sprinklesLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #Action for sprinkles button
        self.sprinklesButton.clicked.connect(self.sprinklesClicked)
         
    #Chocolate Chips Button
        self.chocolateChipsButton = QPushButton(self)
        self.chocolateChipsButton.setGeometry(360, 680, 150, 100)
        #Set image on button
        self.chocolateChipsButton.setIcon(QIcon(QPixmap('Chocolate Chips.png')))
        self.chocolateChipsButton.setIconSize(QSize(150,100))
    #Chocolate Chips Label
        self.chocolateChipsLabel = QLabel("Chocolate Chips", self)
        self.chocolateChipsLabel.setGeometry(360, 734, 150, 50)
        self.chocolateChipsLabel.setFont(QFont('Times', 15))
        self.chocolateChipsLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #Action for chocolate chips button
        self.chocolateChipsButton.clicked.connect(self.chocolateChipsClicked)
    
    #No Toppings Button
        self.noToppingsButton = QPushButton("No Toppings", self)
        self.noToppingsButton.setGeometry(190, 305, 150, 100)
        self.noToppingsButton.setFont(QFont('Times', 20))
        self.noToppingsButton.hide()
    #Action for no toppings button
        self.noToppingsButton.clicked.connect(self.noToppingsClicked)
    
    
    #Disable them for now; will be enabled when start button is clicked
        self.waffleConeButton.setEnabled(False)
        self.cakeConeButton.setEnabled(False)
        self.cupButton.setEnabled(False)
        self.vanillaButton.setEnabled(False)
        self.chocolateButton.setEnabled(False)
        self.strawberryButton.setEnabled(False)
        self.cherryButton.setEnabled(False)
        self.sprinklesButton.setEnabled(False)
        self.chocolateChipsButton.setEnabled(False)
        self.noToppingsButton.setEnabled(False)
        
#Method: Action for startButton
    def startGame(self):
    #Hide and disable components of the start menu
        self.startButton.setEnabled(False)
        self.startButton.hide()
        self.instructionsLabel.hide()
        self.pointsLabel.hide()
    #Enable the buttons
        self.serveButton.setEnabled(True)
        self.resetButton.setEnabled(True)
        self.waffleConeButton.setEnabled(True)
        self.cakeConeButton.setEnabled(True)
        self.cupButton.setEnabled(True)
        self.vanillaButton.setEnabled(True)
        self.chocolateButton.setEnabled(True)
        self.strawberryButton.setEnabled(True)
        self.cherryButton.setEnabled(True)
        self.sprinklesButton.setEnabled(True)
        self.chocolateChipsButton.setEnabled(True)
        self.noToppingsButton.setEnabled(True)
        self.resetButton.setEnabled(True)
        self.serveButton.setEnabled(True)  
    #Get new ice cream order
        self.order.takeOrder()
        self.order.getFinalOrder()
    #Order Image Label    
        self.orderImageLabelPixmap = QPixmap('order.png')
        self.orderImageLabel.setPixmap(self.orderImageLabelPixmap.scaled(196, 338, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.orderImageLabel.setGeometry(402, 70, 196, 338)
        self.orderNumLabel.setText(str(self.order.orderNum))
    #Show widgets needed
        self.resetButton.show()
        self.serveButton.show()
        self.orderImageLabel.show()
        self.noToppingsButton.show()
    #Play game music
        self.order.playMusic('game1')

#Method: User clicked a container button
    def waffleConeClicked(self):
    #Set the container user picked
        self.order.userContainer = "Waffle Cone"
    #Set image for the container
        self.containerShow()
    #Disable those buttons for container
        self.waffleConeButton.setEnabled(False)
        self.cakeConeButton.setEnabled(False)
        self.cupButton.setEnabled(False)

#Method: User clicked a container button
    def cakeConeClicked(self):
    #Set the container user picked
        self.order.userContainer = "Cake Cone"
    #Set image for the container
        self.containerShow()
    #Disable those buttons for container
        self.waffleConeButton.setEnabled(False)
        self.cakeConeButton.setEnabled(False)
        self.cupButton.setEnabled(False)
        
#Method: User clicked a container button
    def cupClicked(self):
    #Set the container user picked
        self.order.userContainer = "Cup"
    #Set image for the container
        self.containerShow()
    #Disable those buttons for container
        self.waffleConeButton.setEnabled(False)
        self.cakeConeButton.setEnabled(False)
        self.cupButton.setEnabled(False)
        
#Method: User clicked a container button
    def containerShow(self):
        self.containerLabelPixmap = QPixmap(f'{self.order.userContainer}.png')
        self.containerLabel.setPixmap(self.containerLabelPixmap.scaled(100, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.containerLabel.setGeometry(705, 549, 100, 150)
        self.containerLabel.resize(100,150)
        self.containerLabel.show()
        
#Method: User clicked the vanilla button
    def vanillaClicked(self):
    #Set the flavor user picked
        self.order.userFlavors[self.order.userScoopMaking-1] = "Vanilla"
        self.updateScoops()
        
#Method: User clicked the chocolate button
    def chocolateClicked(self):
        #Set the container user picked
        self.order.userFlavors[self.order.userScoopMaking-1] = "Chocolate"
        self.updateScoops()
        
#Method: User clicked the strawberry button
    def strawberryClicked(self):
        #Set the container user picked
        self.order.userFlavors[self.order.userScoopMaking-1] = "Strawberry"
        self.updateScoops()
        
#Method: User clicked the cherry button
    def cherryClicked(self):
        #Set the topping user picked
        self.order.userToppings[self.order.userScoopMaking-1] = "Cherry"
        self.updateScoops()
        self.order.userScoopMaking -= 1
        
#Method: User clicked the sprinkles button
    def sprinklesClicked(self):
        #Set the topping user picked
        self.order.userToppings[self.order.userScoopMaking-1] = "Sprinkles"
        self.updateScoops()
        self.order.userScoopMaking -= 1
                
#Method: User clicked the chocolate chips button
    def chocolateChipsClicked(self):
        #Set the topping user picked
        self.order.userToppings[self.order.userScoopMaking-1] = "Chocolate Chips"
        self.updateScoops()
        self.order.userScoopMaking -= 1
                
#Method: User clicked the no toppings button
    def noToppingsClicked(self):
        self.order.userToppings[self.order.userScoopMaking-1] = "No Topping"        
        self.updateScoops()
        self.order.userScoopMaking -= 1
                
#Method: Action for resetButton
    def resetIceCream(self):
        #Reset user's selection
        self.order.resetUserIceCream()
        #Deduct points for using reset button
        self.order.score -= 25
        self.scoreNum.setText(str(self.order.score))
        self.waffleConeButton.setEnabled(True)
        self.cakeConeButton.setEnabled(True)
        self.cupButton.setEnabled(True)
        self.vanillaButton.setEnabled(True)
        self.chocolateButton.setEnabled(True)
        self.strawberryButton.setEnabled(True)
        self.cherryButton.setEnabled(True)
        self.sprinklesButton.setEnabled(True)
        self.chocolateChipsButton.setEnabled(True)
        self.scoopTop.hide()
        self.scoopMiddle.hide()
        self.scoopBottom.hide()
        self.containerLabel.hide()
        
#Method: Action for serveButton
    def servedIceCream(self):
        orderSuccess = self.order.compareIceCream()
        if orderSuccess == True:
            self.order.score += 100
        else:   #Incorrect order
            self.order.score -=50
    #Update Score
        self.scoreNum.setText(str(self.order.score))
    #Get new order
        self.order.takeOrder()
        self.orderTaken()

#Method: When a new order is made, the adjustments needed
    def orderTaken(self):
    #This gets the image for the order
        self.order.getFinalOrder()
    #Update order number
        self.orderNumLabel.setText(str(self.order.orderNum))
    #Update the order image
        self.orderImageLabelPixmap = QPixmap('order.png')
        self.orderImageLabel.setPixmap(self.orderImageLabelPixmap.scaled(196, 338, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.orderImageLabel.resize(196, 338)
        self.orderImageLabel.setGeometry(402, 70, 196, 338)
        self.orderImageLabel.show()
    #Reset user's selection
        self.order.resetUserIceCream()
    #Enable buttons
        self.waffleConeButton.setEnabled(True)
        self.cakeConeButton.setEnabled(True)
        self.cupButton.setEnabled(True)
        self.vanillaButton.setEnabled(True)
        self.chocolateButton.setEnabled(True)
        self.strawberryButton.setEnabled(True)
        self.cherryButton.setEnabled(True)
        self.sprinklesButton.setEnabled(True)
        self.chocolateChipsButton.setEnabled(True)
    #Hide Scoops and Container
        self.scoopTop.hide()
        self.scoopMiddle.hide()
        self.scoopBottom.hide()
        self.containerLabel.hide()

#Method: uploading images for the scoops
    def updateScoops(self):
        scoopMaking = self.order.userScoopMaking
        print(scoopMaking)
        #Makes the image for the scoop
        self.order.singleScoop()
        if scoopMaking == 1:
        #Update the order image
            self.scoopTopPixmap = QPixmap('userScoop.png')
            self.scoopTop.setPixmap(self.scoopTopPixmap.scaled(150, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            self.scoopTop.resize(150, 100)
            self.scoopTop.setGeometry(542, 468, 150, 100)
            self.scoopTop.show()
        elif scoopMaking == 2:
            self.scoopMiddlePixmap = QPixmap('userScoop.png')
            self.scoopMiddle.setPixmap(self.scoopMiddlePixmap.scaled(150, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            self.scoopMiddle.resize(150, 100)
            self.scoopMiddle.setGeometry(542, 574, 150, 100)
            self.scoopMiddle.show()
        else: #Bottom scoop
            self.scoopBottomPixmap = QPixmap('userScoop.png')
            self.scoopBottom.setPixmap(self.scoopBottomPixmap.scaled(150, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            self.scoopBottom.resize(150, 100)
            self.scoopBottom.setGeometry(542, 680, 150, 100)
            self.scoopBottom.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = IceCreamGUI()
    window.show()

    app.exec()
