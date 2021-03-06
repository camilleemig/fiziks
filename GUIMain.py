from Graphics import * 
from sympy import * 
import ForceOther
 
x, y, z = symbols('x y z') 
init_printing(use_unicode=True) 
firstHeight = 40

## New Velocity With Distance Travelled, Acceleration without distance, acceleration without final velocity do not work
## Variables in Velocity from Acceleration, Distance from Velocity, Max Range, Max Height, Change in Motion Y/X Vector, Work Power Equation, Keplers Constant, Center of Mass have variables that I didn't recognize
class EquationBaseMenu(object): 
    def __init__(self):          
        #Equation Base Menu Buttons 
        self.force = Button((firstHeight, 50), "Force") 
        self.motion = Button((firstHeight, 70), "Motion") 
        self.momentumButton = Button((firstHeight, 90), "Momentum") 
        self.energy = Button((firstHeight, 110), "Energy") 
        self.work = Button((firstHeight, 130), "Work") 
        self.planetaryForce = Button((firstHeight, 150), "Planetary Force") 
        self.centerOfMass = Button((firstHeight, 170), "Center Of Mass") 
        self.circularMotion = Button((firstHeight, 190), "Circular Motion") 
        
        self.equationBaseMenu = Window("Fiziks Mill", 200, 300)
        self.force.draw(self.equationBaseMenu) 
        self.motion.draw(self.equationBaseMenu) 
        self.momentumButton.draw(self.equationBaseMenu) 
        self.energy.draw(self.equationBaseMenu) 
        self.work.draw(self.equationBaseMenu) 
        self.planetaryForce.draw(self.equationBaseMenu) 
        self.centerOfMass.draw(self.equationBaseMenu) 
        self.circularMotion.draw(self.equationBaseMenu) 
         
        self.force.connect("click", self.showForceBaseMenu) 
        self.motion.connect("click", self.showMotionBaseMenu) 
        self.momentumButton.connect("click", self.showMomentumBaseMenu) 
        self.energy.connect("click", self.showEnergyBaseMenu) 
        self.work.connect("click", self.showWorkBaseMenu) 
        self.planetaryForce.connect("click", self.showPlanetaryForceBaseMenu) 
        self.centerOfMass.connect("click", self.showCenterOfMassBaseMenu) 
        self.circularMotion.connect("click", self.showCircularMotionBaseMenu) 
     
    def showForceBaseMenu(self, o, e): 
        forceBaseMenu = ShowForceBaseMenu() 
    def showMotionBaseMenu(self, o, e): 
        showMotionMenu = ShowMotionBaseMenu() 
    def showMomentumBaseMenu(self, o, e): 
        momentumBaseMenu = ShowMomentumBaseMenu() 
    def showEnergyBaseMenu(self, o, e): 
        showEnergyMenu = ShowEnergyBaseMenu() 
    def showWorkBaseMenu(self, o, e): 
        workBaseMenu = ShowWorkBaseMenu() 
    def showPlanetaryForceBaseMenu(self, o, e): 
        planetaryForceBaseMenu = ShowPlanetaryForceBaseMenu() 
    def showCenterOfMassBaseMenu(self, o, e): 
        showCenterOfMassMenu = ShowCenterOfMassBaseMenu() 
    def showCircularMotionBaseMenu(self, o, e): 
        forceCircularMotionMenu = ShowCircularMotionBaseMenu() 
      

class ShowForceBaseMenu(object): 
    def __init__(self):          
        self.forceNet = Button((firstHeight, 50), "Net Force") 
        self.forceNormal = Button((firstHeight, 70), "Normal Force") 
        self.forceApplied = Button((firstHeight, 90), "Applied Force") 
        self.forceFriction = Button((firstHeight, 110), "Force of Friction") 
        self.forcePlanetary = Button((firstHeight, 130), "Planetary Force") 
        self.forceAcceleration = Button((firstHeight,150), "Solve for Acceleration") 
        self.mu = Button((firstHeight,170), "Solve for mu") 
        self.mu2 = Button((firstHeight,190), "Solve for mu without normal force") 
 
         
        self.equationForceMenu = Window("Solve Force Equation", 400, 300) 
        self.forceNet.draw(self.equationForceMenu) 
        self.forceNormal.draw(self.equationForceMenu) 
        self.forceApplied.draw(self.equationForceMenu) 
        self.forceFriction.draw(self.equationForceMenu) 
        self.forcePlanetary.draw(self.equationForceMenu) 
        self.forceAcceleration.draw(self.equationForceMenu) 
        self.mu.draw(self.equationForceMenu) 
        self.mu2.draw(self.equationForceMenu) 
 
        self.forceNet.connect("click", self.showNetForceBaseMenu) 
        self.forceNormal.connect("click", self.showNormalForceBaseMenu) 
        self.forceApplied.connect("click", self.showAppliedForceBaseMenu) 
        self.forceFriction.connect("click", self.showFrictionForceBaseMenu) 
        self.forcePlanetary.connect("click", self.showPlanetaryForceBaseMenu) 
        self.forceAcceleration.connect("click", self.showAccelerationForceBaseMenu) 
        self.mu.connect("click", self.showmuBaseMenu) 
        self.mu2.connect("click", self.showmu2BaseMenu) 
         
    def showNetForceBaseMenu(self, o, e): 
        showNetForceBaseMenu = ShowNetForceBaseMenu() 
    def showNormalForceBaseMenu(self, o, e): 
        showNormalForceBaseMenu = ShowNormalForceMenu() 
    def showAppliedForceBaseMenu(self, o, e): 
        showAppliedForceBaseMenu = ShowAppliedForceBaseMenu() 
    def showFrictionForceBaseMenu(self, o, e): 
        showFrictionForceBaseMenu = ShowFrictionForceMenu() 
    def showPlanetaryForceBaseMenu(self, o, e): 
        showPlanetaryForceBaseMenu = ShowPlanetaryForceBaseMenu()  
    def showAccelerationForceBaseMenu(self, o , e): 
        showAccelerationForceBaseMenu = ShowAccelerationForceBaseMenu() 
    def showmuBaseMenu(self, o, e): 
        showmuBaseMenu = ShowmuBaseMenu() 
    def showmu2BaseMenu(self, o, e): 
        showmu2BaseMenu = Showmu2BaseMenu() 
class ShowMomentumBaseMenu(object): 
    def __init__(self):          
        #Momentum Menu Buttons 
        self.momentum = Button((firstHeight, 50), "Momentum") 
        self.impulseFirst = Button((firstHeight, 70), "Impulse with Change in Momentum") 
        self.impulseSecond = Button((firstHeight, 90), "Impulse with Force and Change in Time") 
        self.impulseThird = Button((firstHeight, 110), "Impulse with Mass and Change in Velocity") 
        self.hitAndSeperate = Button((firstHeight, 150), "Hit and Seperate") 
        self.hitAndStick = Button((firstHeight, 170), "Hit and Stick") 
 
        self.equationMomentumMenu = Window("Solve Momentum Equation", 400, 300) 
        self.momentum.draw(self.equationMomentumMenu) 
        self.impulseFirst.draw(self.equationMomentumMenu) 
        self.impulseSecond.draw(self.equationMomentumMenu) 
        self.impulseThird.draw(self.equationMomentumMenu) 
        self.hitAndSeperate.draw(self.equationMomentumMenu) 
        self.hitAndStick.draw(self.equationMomentumMenu) 
         
        self.momentum.connect("click", self.showMomentumMenu) 
        self.impulseFirst.connect("click", self.showImpulseFirstMenu) 
        self.impulseSecond.connect("click", self.showImpulseSecondBaseMenu) 
        self.impulseThird.connect("click", self.showImpulseThirdBaseMenu) 
        self.hitAndSeperate.connect("click", self.showHitAndSeperateMenu) 
        self.hitAndStick.connect("click", self.showHitAndStickBaseMenu) 
         
    def showMomentumMenu(self, o, e): 
        momentumMenu = ShowMomentumMenu() 
    def showImpulseFirstMenu(self, o, e): 
        showImpulseFirstMenu = ShowImpulseFirstMenu() 
    def showImpulseSecondBaseMenu(self, o, e): 
        showImpulseSecondMenu = ShowImpulseSecondMenu() 
    def showImpulseThirdBaseMenu(self, o, e): 
        showImpulseThirdMenu = ShowImpulseThirdMenu() 
    def showHitAndSeperateMenu(self, o, e): 
        showHitAndSeperateMenu = ShowHitAndSeperateMenu() 
    def showHitAndStickBaseMenu(self, o, e): 
        HitAndStickMenu = ShowHitAndStickBaseMenu() 
 
 
class ShowMotionBaseMenu(object): 
    def __init__(self):          
        #Motion Menu Buttons 
        self.distanceTravelled = Button((firstHeight, 50), "Distance Travelled") 
        self.distanceTravelledWithAcceleration = Button((firstHeight, 70), "Distance Travelled with Acceleration") 
        self.newVelocityWithTime = Button((firstHeight, 90), "New velocity with time") 
        self.newVelocityWithDistanceTravelled = Button((firstHeight, 110), "New Velocity with distance travelled") 
        self.velocityFromDistance = Button((firstHeight, 130), "Velcotiy from Distance") 
        self.accelerationFromVelocity = Button((firstHeight, 150), "Acceleration from Velocity") 
        self.velocityFromAcceleration = Button((firstHeight, 170), "Velocity from Acceleration") 
        self.distanceFromVelocity = Button((firstHeight, 190), "Distance from Velocity") 
        self.maxRange = Button((firstHeight, 210), "Max Range") 
        self.maxHeight = Button((firstHeight, 230), "Max Height") 
        self.motionYVectors = Button((firstHeight, 250), "Motion y vectors") 
        self.deltaMotionYVectors = Button((firstHeight, 270), "Change in Motion y vectors") 
        self.motionXVectors = Button((firstHeight, 290), "Motion x vectors") 
        self.deltaMotionXVectors = Button((firstHeight, 310), "Change in Motion x vectors") 
        self.accelerationNoX = Button((firstHeight,330), "Acceleration without distance") 
        self.accelerationNoV2 = Button((firstHeight,350), "Accelerattion with out final velocity") 
 
        self.equationMotionMenu = Window("Solve Motion Equation", 400, 400) 
        self.distanceTravelled.draw(self.equationMotionMenu) 
        self.distanceTravelledWithAcceleration.draw(self.equationMotionMenu) 
        self.newVelocityWithTime.draw(self.equationMotionMenu) 
        self.newVelocityWithDistanceTravelled.draw(self.equationMotionMenu) 
        self.velocityFromDistance.draw(self.equationMotionMenu) 
        self.accelerationFromVelocity.draw(self.equationMotionMenu) 
        self.velocityFromAcceleration.draw(self.equationMotionMenu) 
        self.distanceFromVelocity.draw(self.equationMotionMenu) 
        self.maxRange.draw(self.equationMotionMenu) 
        self.maxHeight.draw(self.equationMotionMenu) 
        self.motionYVectors.draw(self.equationMotionMenu) 
        self.deltaMotionYVectors.draw(self.equationMotionMenu) 
        self.motionXVectors.draw(self.equationMotionMenu) 
        self.deltaMotionXVectors.draw(self.equationMotionMenu) 
        self.accelerationNoX.draw(self.equationMotionMenu) 
        self.accelerationNoV2.draw(self.equationMotionMenu) 
 
        self.distanceTravelled.connect("click", self.showDistanceTravelledBaseMenu) 
        self.distanceTravelledWithAcceleration.connect("click", self.showDistanceTravelledWithAccelerationMenu) 
        self.newVelocityWithTime.connect("click", self.showNewVelocityWithTimeBaseMenu) 
        self.newVelocityWithDistanceTravelled.connect("click", self.showNewVelocityWithDistanceTravelledMenu) 
        self.velocityFromDistance.connect("click", self.showVelocityFromDistanceBaseMenu) 
        self.accelerationFromVelocity.connect("click", self.showAccelerationFromVelocityMenu) 
        self.velocityFromAcceleration.connect("click", self.showVelocityFromAccelerationBaseMenu)  
        self.distanceFromVelocity.connect("click", self.showDistanceFromVelocityBaseMenu) 
        self.maxRange.connect("click", self.showMaxRangeBaseMenu) 
        self.maxHeight.connect("click", self.showMaxHeightBaseMenu) 
        self.motionYVectors.connect("click", self.showMotionYVectorsBaseMenu) 
        self.deltaMotionYVectors.connect("click", self.showDeltaMotionYVectorsBaseMenu) 
        self.motionXVectors.connect("click", self.showMotionXVectorsBaseMenu) 
        self.deltaMotionXVectors.connect("click", self.showDeltaMotionXVectorsBaseMenu) 
        self.accelerationNoX.connect("click", self.showAccelerationNoXBaseMenu) 
        self.accelerationNoV2.connect("click", self.showAccelerationNoV2BaseMenu) 
             
    def showDistanceTravelledBaseMenu(self, o, e): 
        distanceTravelledBaseMenu = ShowDistanceTravelledBaseMenu() 
    def showDistanceTravelledWithAccelerationMenu(self, o, e): 
        distanceTravelledWithAccelerationMenu = ShowDistanceTravelledWithAccelerationMenu() 
    def showNewVelocityWithTimeBaseMenu(self, o, e): 
        newVelocityWithTimeBaseMenu = ShowNewVelocityWithTimeBaseMenu() 
    def showNewVelocityWithDistanceTravelledMenu(self, o, e): 
        newVelocityWithDistanceTravelledEnergyMenu = ShowNewVelocityWithDistanceTravelledMenu() 
    def showVelocityFromDistanceBaseMenu(self, o, e): 
        velocityFromDistanceBaseMenu = ShowVelocityFromDistanceBaseMenu() 
    def showAccelerationFromVelocityMenu(self, o, e): 
        accelerationFromVelocityMenu = ShowAccelerationFromVelocityMenu() 
    def showVelocityFromAccelerationBaseMenu(self, o, e): 
        velocityFromAccelerationMenu = ShowVelocityFromAccelerationBaseMenu() 
    def showDistanceFromVelocityBaseMenu(self, o, e): 
        distanceFromVelocityBaseMenu = ShowDistanceFromVelocityBaseMenu() 
    def showMaxRangeBaseMenu(self, o, e): 
        maxRangeBaseMenu = ShowMaxRangeBaseMenu() 
    def showMaxHeightBaseMenu(self, o, e): 
        maxHeightBaseMenu = ShowMaxHeightBaseMenu() 
    def showMotionYVectorsBaseMenu(self, o, e): 
        motionYVectorsBaseMenu = ShowMotionYVectorsBaseMenu() 
    def showDeltaMotionYVectorsBaseMenu(self, o, e): 
        deltaMotionYVectorsBaseMenu = ShowDeltaMotionYVectorsBaseMenu() 
    def showMotionXVectorsBaseMenu(self, o, e): 
        motionXVectorsBaseMenu = ShowMotionXVectorsBaseMenu() 
    def showDeltaMotionXVectorsBaseMenu(self, o, e): 
        deltaMotionXVectorsBaseMenu = ShowDeltaMotionXVectorsBaseMenu() 
    def showAccelerationNoXBaseMenu(self, o, e): 
        accelertaionNoXBaseMenu = ShowAccelerationNoXBaseMenu() 
    def showAccelerationNoV2BaseMenu(self, o, e): 
        accelerationNoV2BaseMenu = ShowAccelerationNoV2BaseMenu() 
 
class ShowEnergyBaseMenu(object): 
    def __init__(self):          
        #Momentum Menu Buttons 
        self.kineticEnergy = Button((firstHeight, 50), "Kinetic Energy") 
        self.gravitationalPotentialEnergy = Button((firstHeight, 70), "Gravitational Potential Energy") 
        self.springPotentialEnergy = Button((firstHeight, 90), "Spring Potential Energy") 
         
        self.equationEnergyMenu = Window("Solve Energy Equation", 400, 300) 
         
        self.kineticEnergy.draw(self.equationEnergyMenu) 
        self.gravitationalPotentialEnergy.draw(self.equationEnergyMenu) 
        self.springPotentialEnergy.draw(self.equationEnergyMenu) 
         
        self.kineticEnergy.connect("click", self.showKineticEnergyBaseMenu) 
        self.gravitationalPotentialEnergy.connect("click", self.showGravitationalPotentialEnergyMenu) 
        self.springPotentialEnergy.connect("click", self.showSpringPotentialEnergyBaseMenu) 
         
        ##To be added after each of the next screens are made 
    def showKineticEnergyBaseMenu(self, o, e): 
        kineticEnergyBaseMenu = ShowKineticEnergyBaseMenu() 
    def showGravitationalPotentialEnergyMenu(self, o, e): 
        gravitationalPotentialEnergyMenu = ShowGravitationalPotentialEnergyMenu() 
    def showSpringPotentialEnergyBaseMenu(self, o, e): 
        springPotentialEnergyBaseMenu = ShowSpringPotentialEnergyBaseMenu() 
 
class ShowWorkBaseMenu(object): 
    def __init__(self):          
        #Momentum Menu Buttons 
        self.CalcWork = Button((firstHeight,70), "Calculus Work") 
        self.power = Button((firstHeight,90), "Power") 
 
        self.equationWorkMenu = Window("Solve Work Equation", 400, 300) 
        self.CalcWork.draw(self.equationWorkMenu) 
        self.power.draw(self.equationWorkMenu) 
 
        self.CalcWork.connect("click", self.showCalcWorkBaseMenu) 
        self.power.connect("click", self.showPowerBaseMenu) 
        
    def showCalcWorkBaseMenu(self, o, e): 
        CalcWorkBaseMenu = showCalcWorkBaseMenu() 
    def showPowerBaseMenu(self,o,e): 
        PowerBaseMenu = showPowerBaseMenu() 
class ShowPlanetaryForceBaseMenu(object): 
    def __init__(self):          
        #Momentum Menu Buttons 
        self.force = Button((firstHeight, 50), "Force") 
        self.gravity = Button((firstHeight, 70), "Gravity") 
        self.keplersConstant = Button((firstHeight, 90), "Keplers Constant") 
 
        self.equationPlanetaryForceMenu = Window("Solve Planetary Force Equation", 400, 300) 
        self.force.draw(self.equationPlanetaryForceMenu) 
        self.gravity.draw(self.equationPlanetaryForceMenu) 
        self.keplersConstant.draw(self.equationPlanetaryForceMenu) 
        self.force.connect("click", self.showPlanetaryForce) 
        self.gravity.connect("click", self.showPlanetaryGravity) 
        self.keplersConstant.connect("click", self.showKeplersConstant) 
 
    def showPlanetaryForce(self, o, e): 
        planetaryForceMenu = ShowPlanetaryForceMenu() 
    def showPlanetaryGravity(self, o, e): 
        planetaryGravityMenu = ShowPlanetaryGravityMenu() 
    def showKeplersConstant(self, o, e): 
        keplersConstant = ShowKeplersConstantMenu() 
class ShowCenterOfMassBaseMenu(object): 
    def __init__(self):          
        #Momentum Menu Buttons 
        self.centerOfMass = Button((firstHeight, 50), "Center Of Mass") 
 
        self.equationMomentumMenu = Window("Solve Center Of Mass Equation", 400, 300) 
        self.centerOfMass.draw(self.equationMomentumMenu) 
    
        self.centerOfMass.connect("click", self.showCenterOfMass) 
        
    def showCenterOfMass(self, o, e):
        centerOfMass = ShowCenterOfMass()

class ShowCircularMotionBaseMenu(object):
    def __init__(self):
        #Momentum Menu Buttons
        self.acceleration = Button((firstHeight, 50), "Acceleration")
        self.verticalCircleVelocity = Button((firstHeight, 70), "Vertical Circle Velocity")
        self.horizontalCircleVelocity = Button((firstHeight, 90), "Horizontal Circle Velocity")
        self.force = Button((firstHeight, 110), "Force")
        
        self.equationCircularMotionMenu = Window("Solve CircularMotion Equation", 400, 300)
        
        self.acceleration.draw(self.equationCircularMotionMenu)
        self.verticalCircleVelocity.draw(self.equationCircularMotionMenu)
        self.horizontalCircleVelocity.draw(self.equationCircularMotionMenu)
        self.force.draw(self.equationCircularMotionMenu)

        self.acceleration.connect("click", self.showAccelerationBaseMenu)
        self.verticalCircleVelocity.connect("click", self.showVerticalCircleVelocityMenu)
        self.horizontalCircleVelocity.connect("click", self.showHorizontalCircleVelocityBaseMenu)
        self.force.connect("click", self.showForceMenu)

    def showAccelerationBaseMenu(self, o, e):
        showAccelerationBaseMenu = ShowAccelerationBaseMenu()
    def showVerticalCircleVelocityMenu(self, o, e):
        verticalCircleVelocityBaseMenu = ShowVerticalCircleVelocityMenu()
    def showHorizontalCircleVelocityBaseMenu(self, o, e):
        horizontalCircleVelocityBaseMenu = ShowHorizontalCircleVelocityBaseMenu()
    def showForceMenu(self, o, e):
        forceMenu = ShowForceMenu()
class ShowNewVelocityWithDistanceTravelledMenu(object):
    def __init__(self):         
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        Text((15, 60),'F:').draw(self.window)
        self.entry0.Text = 'Force'
        Text((15, 90),'M:').draw(self.window)
        #**********************Start Here************************
        #The text should be whatever the fuck you want it to be
        #Please note that the formatting might look werid when you run it if the line is to long
        #I will fix that later.
        #Note, there are a shit ton of these.
        # <3 Sam Rory Cluff is fantastic for doing this for me!
        self.instructions = Text((300, 55),'Input your equation with "F" blergh blergh testing testing testing')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.wrap = 'true'
        self.instructions.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        #**********************************************************
        self.entry1.Text =  'Mass'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
    def callMathFunction(self, o, e):
        f = float(self.entry0.Text)
        m = float(self.entry1.Text)
        a = f/m
        self.result.Text = str(a)
class ShowAccelerationNoXBaseMenu(object):
    def __init__(self):         
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        Text((15, 60),'F:').draw(self.window)
        self.entry0.Text = 'Force'
        Text((15, 90),'M:').draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.entry1.Text =  'Mass'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
    def callMathFunction(self, o, e):
        f = float(self.entry0.Text)
        m = float(self.entry1.Text)
        a = f/m
        self.result.Text = str(a)
class ShowAccelerationNoV2BaseMenu(object):
    def __init__(self):         
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        Text((15, 60),'F:').draw(self.window)
        self.entry0.Text = 'Force'
        Text((15, 90),'M:').draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.entry1.Text =  'Mass'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
    def callMathFunction(self, o, e):
        f = float(self.entry0.Text)
        m = float(self.entry1.Text)
        a = f/m
        self.result.Text = str(a)
class ShowAccelerationForceBaseMenu(object):
    def __init__(self):         
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        Text((15, 60),'F:').draw(self.window)
        self.entry0.Text = 'Force'
        Text((15, 90),'M:').draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.entry1.Text =  'Mass'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
    def callMathFunction(self, o, e):
        f = float(self.entry0.Text)
        m = float(self.entry1.Text)
        a = f/m
        self.result.Text = str(a)
class ShowmuBaseMenu(object):
    def __init__(self):         
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        Text((15, 60),'Ff:').draw(self.window)
        self.entry0.Text = 'Force of Friction'
        Text((15, 90),'Fn:').draw(self.window)
        self.entry1.Text = 'Normal Force'
        self.instructions = Text((300, 55),'Input your equation with "Ff"')
        self.instructionsln2 = Text((300, 75),'for force of friction and "Fn" for normal force')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
    def callMathFunction(self, o, e):
        Ff = float(self.entry0.Text)
        Fn = float(self.entry1.Text)
        mu = Ff/Fn
        self.result.Text = str(mu)
class Showmu2BaseMenu(object):
   def __init__(self):         
        self.window = Window("Solve Equation", 400, 250)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.entry2 = Entry((firstHeight,110), 20)
        self.entry2.draw(self.window)
        self.entry3 = Entry((firstHeight,140), 20)
        self.entry3.draw(self.window)
        self.result = Entry((firstHeight,210), 20)
        self.result.draw(self.window)        
        Text((15, 60),'Ff:').draw(self.window)
        self.entry0.Text = 'Force of Friction'
        Text((15, 90),'M:').draw(self.window)
        self.entry1.Text = 'Mass'
        Text((15, 120),'G:').draw(self.window)
        self.entry2.Text = '9.81'
        Text((15, 150),'Theta:').draw(self.window)
        self.entry3.Text = 'Theta'
        self.instructions = Text((300, 55),'Input your equation with "Ff"')
        self.instructionsln2 = Text((300, 75),'for force of friction, M for mass, and "Theta" for the angle')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,170), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        Ff = float(self.entry0.Text)
        m = float(self.entry1.Text)
        g = float(self.entry2.Text)
        theta = float(self.entry3.Text)
        mu = Ff/m/g/sin(theta)
        self.result.Text = str(mu)
class showPowerBaseMenu(object):
    def __init__(self):
        self.window = Window("Solve Equation", 400, 160)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.result = Entry((firstHeight,120), 20)
        self.result.draw(self.window)        
        Text((15, 60),'w:').draw(self.window)
        self.entry0.Text = 'work'
        self.instructions = Text((300, 55),'Input your equation with "w"')
        self.instructionsln2 = Text((300, 75),'for work')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,80), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
    def callMathFunction(self, o, e):
        w = str(self.entry0.Text)
        t = x
        p = diff(w, t)
        self.result.Text = str(p)
class showCalcWorkBaseMenu(object):
   def __init__(self):         
        self.window = Window("Solve Equation", 400, 250)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.entry2 = Entry((firstHeight,110), 20)
        self.entry2.draw(self.window)
        self.entry3 = Entry((firstHeight,140), 20)
        self.entry3.draw(self.window)
        self.result = Entry((firstHeight,210), 20)
        self.result.draw(self.window)        
        Text((15, 60),'f:').draw(self.window)
        Text((15, 90),'x:').draw(self.window)
        self.entry0.Text = 'Function'
        self.entry1.Text = 'x'
        self.entry2.Text = 'A'
        self.entry3.Text = 'B'
        self.instructions = Text((300, 55),'Input your equation with "f"')
        self.instructionsln2 = Text((300, 75),'for the function evaluating from "a" to "b"')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,170), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        Fn = str(self.entry0.Text)
        x = str(self.entry1.Text)
        a = str(self.entry2.Text)
        b = str(self.entry3.Text)
        t = x
        w = integrate(Fn, (x, a, b))
        self.result.Text = str(w)
class ShowPlanetaryForceMenu(object):
   def __init__(self):         
        self.window = Window("Solve Equation", 400, 220)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.entry2 = Entry((firstHeight,110),20)
        self.entry2.draw(self.window)
        self.result = Entry((firstHeight,180), 20)
        self.result.draw(self.window)        
        Text((15, 60),'m1:').draw(self.window)
        Text((15, 90),'m2:').draw(self.window)
        Text((15,120),'r:').draw(self.window)
        self.entry0.Text = 'Mass One'
        self.entry1.Text = 'Mass Two'
        self.entry2.Text = 'Radius'
        self.instructions = Text((300, 55),'Input your equation with "M1"')
        self.instructionsln2 = Text((300, 75),'for the first mass and "M2" for the second mass and "r" for the radius')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,140), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        G = 6.67 * 10** -11
        M = float(self.entry0.Text)
        m = float(self.entry1.Text)
        r = float(self.entry2.Text)
        f = (G * M * m) / (r**2)
        self.result.Text = str(f)
class ShowPlanetaryGravityMenu(object):
   def __init__(self):         
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        Text((15, 60),'m:').draw(self.window)
        Text((15, 90),'r:').draw(self.window)
        self.entry0.Text = 'Mass'
        self.entry1.Text = 'Radius'
        self.instructions = Text((300, 55),'Input your equation with "m"')
        self.instructionsln2 = Text((300, 75),'for mass and "r" for radius')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        G = 6.67 * 10** -11
        m = float(self.entry0.Text)
        r = float(self.entry1.Text)
        g = (G * m) /(r**2)
        self.result.Text = str(g)
class ShowKeplersConstantMenu(object):
   def __init__(self):         
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        Text((15, 60),'k:').draw(self.window)
        Text((15, 90),'T:').draw(self.window)
        self.entry0.Text = 'K'
        self.entry1.Text = 'T'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        k = float(self.entry0.Text)
        t = float(self.entry1.Text)
        kc = (K**3)/(T**2)
        self.result.Text = str(kc)
class ShowNetForceBaseMenu(object):
   def __init__(self):         
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        Text((15, 60),'m:').draw(self.window)
        Text((15, 90),'a:').draw(self.window)
        self.entry0.Text = 'Mass'
        self.entry1.Text = 'Acceleration'
        self.instructions = Text((300, 55),'Input your equation with "m"')
        self.instructionsln2 = Text((300, 75),'for mass and "a" for acceleration')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        m = float(self.entry0.Text)
        a = float(self.entry1.Text)
        fnet = m * a
        self.result.Text = str(fnet)
class ShowNormalForceMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 220)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.entry2 = Entry((firstHeight,110), 20)
        self.entry2.draw(self.window)
        self.result = Entry((firstHeight,180), 20)
        self.result.draw(self.window)        
        Text((15, 60),'m:').draw(self.window)
        Text((15, 90),'a:').draw(self.window)
        Text((15,120),'theta').draw(self.window)
        self.entry0.Text = 'Mass'
        self.entry1.Text = 'Acceleration'
        self.entry2.Text = 'Theta'
        self.instructions = Text((300, 55),'Input your equation with "m"')
        self.instructionsln2 = Text((300, 75),'for mass, "a" for acceleration and "theta" for the angle')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,140), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        m = float(self.entry0.Text)
        g = float(self.entry1.Text)
        theta = float(self.entry2.Text)
        forceNormal = m * g * sin(theta)
        self.result.Text = str(forceNormal)
class ShowAppliedForceBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        Text((15, 60),'m:').draw(self.window)
        Text((15, 90),'a:').draw(self.window)
        self.entry0.Text = 'Mass'
        self.entry1.Text = 'Acceleration'
        self.instructions = Text((300, 55),'Input your equation with "m"')
        self.instructionsln2 = Text((300, 75),'for mass and "a" for acceleration')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        m = float(self.entry0.Text)
        a = float(self.entry1.Text)
        forceApplied = m * a
        self.result.Text = str(forceApplied)
class ShowFrictionForceMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        Text((15, 60),'mu:').draw(self.window)
        Text((15, 90),'FN:').draw(self.window)
        self.entry0.Text = 'Mu'
        self.entry1.Text = 'Normal Force'
        self.instructions = Text((300, 55),'Input your equation with "Mu"')
        self.instructionsln2 = Text((300, 75),'for coefficient of friction and "FN" for normal force')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        mu = float(self.entry0.Text)
        forceNormal = float(self.entry1.Text)
        forceFriction = mu * forceNormal
        self.result.Text = str(forceFriction)

class ShowMomentumMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)
        Text((15, 60),'m:').draw(self.window)
        Text((15, 90),'v:').draw(self.window)
        self.entry0.Text = 'Mass'
        self.entry1.Text = 'Velocity'
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        m = float(self.entry0.Text)
        v = float(self.entry1.Text)
        p = m * v
        self.result.Text = str(p)
class ShowImpulseFirstMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)
        Text((15, 60),'p1:').draw(self.window)
        Text((15, 90),'p2:').draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        self.entry0.Text = 'Momentum One'
        self.entry1.Text = 'Momentum Two'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        p1 = float(self.entry0.Text)
        p2 = float(self.entry1.Text)
        I = p2-p1
        self.result.Text = str(I)
class ShowImpulseSecondMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'f:').draw(self.window)
        Text((15, 90),'delta(t):').draw(self.window)
        self.entry0.Text = 'Force'
        self.entry1.Text = 'Change in Time'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        f = float(self.entry0.Text)
        t = float(self.entry1.Text)
        I = f * (t)
        self.result.Text = str(I)
class ShowImpulseThirdMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'f:').draw(self.window)
        Text((15, 90),'delta(v):').draw(self.window)
        self.entry0.Text = 'Force'
        self.entry1.Text = 'Change in Velocity'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        m = float(self.entry0.Text)
        v = float(self.entry1.Text)
        I = m * (v)
        self.result.Text = str(I)
class ShowHitAndSeperateMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 250)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.entry2 = Entry((firstHeight,110), 20)
        self.entry2.draw(self.window)
        self.entry3 = Entry((firstHeight,140), 20)
        self.entry3.draw(self.window)
        self.result = Entry((firstHeight,210), 20)
        self.result.draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'m1:').draw(self.window)
        Text((15, 90),'m2):').draw(self.window)
        Text((15, 110),'v3:').draw(self.window)
        Text((15, 140),'v4:').draw(self.window)
        self.entry0.Text = 'Mass One'
        self.entry1.Text = 'Mass Two'
        self.entry2.Text = 'Velocity One'
        self.entry3.Text = 'Velocity Two'
        self.submit = Button((firstHeight,170), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        m1 = float(self.entry0.Text)
        m2 = float(self.entry1.Text)
        v3 = float(self.entry2.Text)
        v4 = float(self.entry3.Text)
        p = m1* v3 + m2 * v4
        self.result.Text = str(p)
class ShowHitAndStickBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 220)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.entry2 = Entry((firstHeight,110), 20)
        self.entry2.draw(self.window)
        self.result = Entry((firstHeight,180), 20)
        self.result.draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'m1:').draw(self.window)
        Text((15, 90),'m2):').draw(self.window)
        Text((15, 110),'v1:').draw(self.window)
        self.entry0.Text = 'Mass One'
        self.entry1.Text = 'Mass Two'
        self.entry2.Text = 'Velocity'
        self.submit = Button((firstHeight,140), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        m1 = float(self.entry0.Text)
        m2 = float(self.entry1.Text)
        v3 = float(self.entry2.Text)
        p = (m1 + m2) * v3
        self.result.Text = str(p)
class ShowDistanceTravelledBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v:').draw(self.window)
        Text((15, 90),'t:').draw(self.window)
        self.entry0.Text = 'Velocity'
        self.entry1.Text = 'Time'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        v = float(self.entry0.Text)
        t = float(self.entry1.Text)
        x = v * t
        self.result.Text = str(x)
class ShowDistanceTravelledWithAccelerationMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 220)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.entry2 = Entry((firstHeight,110), 20)
        self.entry2.draw(self.window)
        self.result = Entry((firstHeight,180), 20)
        self.result.draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v1:').draw(self.window)
        Text((15, 90),'t:').draw(self.window)
        Text((15, 110),'a:').draw(self.window)
        self.entry0.Text = 'Velocity'
        self.entry1.Text = 'Time'
        self.entry2.Text = 'Acceleration'
        self.submit = Button((firstHeight,140), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        v1 = float(self.entry0.Text)
        t = float(self.entry1.Text)
        a = float(self.entry2.Text)
        x = v1 * t + .5 * a * (t**2)
        self.result.Text = str(x)
class ShowNewVelocityWithTimeBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 220)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.entry2 = Entry((firstHeight,110), 20)
        self.entry2.draw(self.window)
        self.result = Entry((firstHeight,180), 20)
        self.result.draw(self.window)
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v1:').draw(self.window)
        Text((15, 90),'t:').draw(self.window)
        Text((15, 110),'a:').draw(self.window)
        self.entry0.Text = 'Velocity'
        self.entry1.Text = 'Time'
        self.entry2.Text = 'Acceleration'
        self.submit = Button((firstHeight,140), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        v1 = float(self.entry0.Text)
        t = float(self.entry1.Text)
        a = float(self.entry2.Text)
        v2 = v1 + a * t
        self.result.Text = str(v2)

class ShowVelocityFromDistanceBaseMenu(object):
   def __init__(self):         
        self.window = Window("Solve Equation", 400, 160)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.result = Entry((firstHeight,120), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'x:').draw(self.window)
        self.entry0.Text = 'Fuction Of X'
        self.submit = Button((firstHeight,80), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        X = str(self.entry0.Text)
        v = diff(X,x)
        self.result.Text = str(v)

class ShowAccelerationFromVelocityMenu(object):
   def __init__(self):         
        self.window = Window("Solve Equation", 400, 160)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.result = Entry((firstHeight,120), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v:').draw(self.window)
        self.entry0.Text = 'Function of v'
        self.submit = Button((firstHeight,80), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        V = str(self.entry0.Text)
        v = Symbol('v')
        a = diff(V,v)
        self.result.Text = str(a)
        
class ShowVelocityFromAccelerationBaseMenu(object):
   def __init__(self):         
        self.window = Window("Solve Equation", 400, 220)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry2 = Entry((firstHeight,80), 20)
        self.entry2.draw(self.window)
        self.entry3 = Entry((firstHeight,110), 20)
        self.entry3.draw(self.window)
        self.result = Entry((firstHeight,180), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'A:').draw(self.window)
        Text((15, 90),'a:').draw(self.window)
        Text((15, 120),'b:').draw(self.window)
        self.entry0.Text = 'A'
        self.entry2.Text = 'a'
        self.entry3.Text = 'b'
        self.submit = Button((firstHeight,140), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        A = str(self.entry0.Text)
        a = str(self.entry2.Text)
        b = str(self.entry3.Text)
        v = integrate(A, (x, a, b))
        self.result.Text = str(v)
class ShowDistanceFromVelocityBaseMenu(object):
   def __init__(self):         
        self.window = Window("Solve Equation", 400, 220)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry2 = Entry((firstHeight,80), 20)
        self.entry2.draw(self.window)
        self.entry3 = Entry((firstHeight,110), 20)
        self.entry3.draw(self.window)
        self.result = Entry((firstHeight,180), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'V:').draw(self.window)
        Text((15, 90),'a:').draw(self.window)
        Text((15, 120),'b:').draw(self.window)
        self.entry0.Text = 'V'
        self.entry2.Text = 'a'
        self.entry3.Text = 'b'
        self.submit = Button((firstHeight,140), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        V = str(self.entry0.Text)
        a = str(self.entry2.Text)
        b = str(self.entry3.Text)
        d = integrate(V, (x, a, b))
        self.result.Text = str(d)   
class ShowMaxRangeBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry2 = Entry((firstHeight,80), 20)
        self.entry2.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v:').draw(self.window)
        Text((15, 90),'theta:').draw(self.window)
        self.entry0.Text = 'v'
        self.entry2.Text = 'theta'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        v = float(self.entry0.Text)
        theta = float(self.entry2.Text)
        g = 9.81
        r = ((v**2) * sin(2*theta))/(2*g)
        self.result.Text = str(r)  
class ShowMaxHeightBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry2 = Entry((50,80), 20)
        self.entry2.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v:').draw(self.window)
        Text((15, 90),'theta:').draw(self.window)
        self.entry0.Text = 'v'
        self.entry2.Text = 'theta'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        v = float(self.entry0.Text)
        theta = float(self.entry2.Text)
        g = 9.81
        h = ((v**2) * sin(2*theta))/(2*g)
        self.result.Text = str(h)
class ShowMotionYVectorsBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 220)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry2 = Entry((firstHeight,80), 20)
        self.entry2.draw(self.window)
        self.entry3 = Entry((firstHeight,110), 20)
        self.entry3.draw(self.window)
        self.result = Entry((firstHeight,180), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v1y:').draw(self.window)
        Text((15, 90),'a:').draw(self.window)
        Text((15, 120),'t:').draw(self.window)
        self.entry0.Text = 'Y Vector'
        self.entry2.Text = 'Acceleration'
        self.entry3.Text = 'Time'
        self.submit = Button((firstHeight,140), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        v1y = float(self.entry0.Text)
        a = float(self.entry2.Text)
        t = float(self.entry3.Text)
        v2y = v1y + a * t
        self.result.Text = str(v2y)
class ShowDeltaMotionYVectorsBaseMenu(object):  
   def __init__(self):
        self.window = Window("Solve Equation", 400, 300)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry2 = Entry((firstHeight,80), 20)
        self.entry2.draw(self.window)
        self.entry3 = Entry((firstHeight,110), 20)
        self.entry3.draw(self.window)
        self.result = Entry((firstHeight,180), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v1:').draw(self.window)
        Text((15, 90),'a:').draw(self.window)
        Text((15, 120),'t:').draw(self.window)
        self.entry0.Text = 'V'
        self.entry2.Text = 'Acceleration'
        self.entry3.Text = 'Time'
        self.submit = Button((firstHeight,140), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        v1 = float(self.entry0.Text)
        a = float(self.entry2.Text)
        t = float(self.entry3.Text)
        deltay = v1 * t + .5 * a * (t**2)
        self.result.Text = str(deltay)
class ShowMotionXVectorsBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 220)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry2 = Entry((firstHeight,80), 20)
        self.entry2.draw(self.window)
        self.entry3 = Entry((firstHeight,110), 20)
        self.entry3.draw(self.window)
        self.result = Entry((firstHeight,180), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v1x:').draw(self.window)
        Text((15, 90),'a:').draw(self.window)
        Text((15, 120),'t:').draw(self.window)
        self.entry0.Text = 'X Vector'
        self.entry2.Text = 'Acceleration'
        self.entry3.Text = 'Time'
        self.submit = Button((firstHeight,140), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        v1x = float(self.entry0.Text)
        a = float(self.entry2.Text)
        t = float(self.entry3.Text)
        v2x = v1x + a * t
        self.result.Text = str(v2y)
class ShowDeltaMotionXVectorsBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry2 = Entry((firstHeight,80), 20)
        self.entry2.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v1:').draw(self.window)
        Text((15, 90),'t:').draw(self.window)
        self.entry0.Text = 'v'
        self.entry2.Text = 'Time'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        v1 = float(self.entry0.Text)
        t = float(self.entry2.Text)
        deltax = v1 * t
        self.result.Text = str(deltax)
class ShowKineticEnergyBaseMenu(object):
    def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'v:').draw(self.window)
        Text((15, 90),'m:').draw(self.window)
        self.entry0.Text = 'Velocity'
        self.entry1.Text = 'Mass'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
    def callMathFunction(self, o, e):
        v = float(self.entry0.Text)
        m = float(self.entry1.Text)
        ke = .5 * m * v**2
        self.result.Text = str(ke)
class ShowGravitationalPotentialEnergyMenu(object):
    def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)        
        Text((15, 60),'m:').draw(self.window)
        Text((15, 90),'h:').draw(self.window)
        self.entry0.Text = 'Mass'
        self.entry1.Text = 'Height'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
    def callMathFunction(self, o, e):
        m = float(self.entry0.Text)
        h = float(self.entry1.Text)
        g = 9.81
        gpe = m * g * h
        self.result.Text = str(gpe)
class ShowSpringPotentialEnergyBaseMenu(object):
    def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry2 = Entry((firstHeight,80), 20)
        self.entry2.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)   
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)     
        Text((15, 60),'k:').draw(self.window)
        Text((15, 90),'x:').draw(self.window)
        self.entry0.Text = 'Spring Constant'
        self.entry2.Text = 'Distance Stretched'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
    def callMathFunction(self, o, e):
        k = float(self.entry0.Text)
        x = float(self.entry2.Text)
        spe = (0.5) * k * x**2
        self.result.Text = str(spe)
class ShowCenterOfMass(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)        
        Text((15, 60),'r:').draw(self.window)
        Text((15, 90),'v:').draw(self.window)
        self.entry0.Text = 'Radius'
        self.entry1.Text = 'v'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        r = float(self.entry0.Text)
        v = float(self.entry1.Text)
        cm = sigma((m*x)/x)
        self.result.Text = str(cm)
class ShowAccelerationBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)        
        Text((15, 60),'r:').draw(self.window)
        Text((15, 90),'v:').draw(self.window)
        self.entry0.Text = 'Radius'
        self.entry1.Text = 'Velocity'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        r = float(self.entry0.Text)
        v = float(self.entry1.Text)
        a = (v**2)/r 
        self.result.Text = str(a)
class ShowVerticalCircleVelocityMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 160)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.result = Entry((firstHeight,120), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)        
        Text((15, 60),'r:').draw(self.window)
        self.entry0.Text = 'Radius'
        self.submit = Button((firstHeight,80), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        r = float(self.entry0.Text)
        g = 9.81
        vv = (g * r)**.5
        self.result.Text = str(vv)
class ShowHorizontalCircleVelocityBaseMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'mu:').draw(self.window)
        Text((15, 90),'r:').draw(self.window)
        self.entry0.Text = 'Mu'
        self.entry1.Text = 'Radius'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        mu = float(self.entry0.Text)
        r = float(self.entry1.Text)
        g = 9.81
        vh = (r * mu * g)**.5
        self.result.Text = str(vh)
        
class ShowForceMenu(object):
   def __init__(self):
        self.window = Window("Solve Equation", 400, 190)
        self.entry0 = Entry((firstHeight,50), 20)
        self.entry0.draw(self.window)
        self.entry1 = Entry((firstHeight,80), 20)
        self.entry1.draw(self.window)
        self.entry2 = Entry((firstHeight,80), 20)
        self.entry2.draw(self.window)
        self.result = Entry((firstHeight,150), 20)
        self.result.draw(self.window)        
        self.instructions = Text((300, 55),'Input your equation with "F"')
        self.instructionsln2 = Text((300, 75),'for force and M for mass')
        self.instructions.fontSize = 12
        self.instructionsln2.fontSize = 12
        self.instructions.setWidth(30)
        self.instructionsln2.setWidth(30)
        self.instructions.draw(self.window)
        self.instructionsln2.draw(self.window)
        Text((15, 60),'m:').draw(self.window)
        Text((15, 90),'v:').draw(self.window)
        Text((15, 90),'r:').draw(self.window)
        self.entry0.Text = 'Mass'
        self.entry1.Text = 'Velocity'
        self.entry2.Text = 'Radius'
        self.submit = Button((firstHeight,110), "Submit")
        self.submit.draw(self.window)
        self.submit.connect("Click", self.callMathFunction)
   def callMathFunction(self, o, e):
        m = float(self.entry0.Text)
        v = float(self.entry1.Text)
        r = float(self.entry2.Text)
        
        f = (m * (v**2))/r
        self.result.Text = str(f)
        
  
#Base Menu Buttons 
equationBaseMenu = EquationBaseMenu() 
