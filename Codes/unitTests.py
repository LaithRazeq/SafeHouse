import unittest
from Controller import*
from Buzzer import*
from Lock import*
from Motion import*
from Flame import*

class TestSafeHouse(unittest.TestCase):
    
    ##Testing Config System functions
    def testConfigBuzzer(self):
        self.assertEqual(configBuzzer(),1,'Ensure that configuring buzzer returns 1 when successful')
    def testConfigFlame(self):
        self.assertEqual(configFlame(),1,'Ensure that configuring flame sensor returns 1 when successful')
    def testConfigLock(self):
        self.assertEqual(configLock(),1,'Ensure that configuring lock returns 1 when successful')
    def testConfigMotion(self):
        self.assertEqual(configMotion(),1,'Ensure that configuring motion sensor returns 1 when successful')    
    
        
    ##Testing Hardware Functionality
    def testBuzz(self):
        configBuzzer()
        self.assertEqual(buzz(1),1,'Ensure the result is 1 when the client switches ON the buzzer')
        self.assertEqual(buzz(0),1,'Ensure the result is 1 when the client switches OFF the buzzer')
        self.assertEqual(buzz(12222),0,'Ensure the result is 0 when the the input is anything other than ON OR OFF')
    def testFlameDetect(self):
        configFlame()
        self.assertEqual(flameDetect(1),0,'Ensures the result is 0 as the Flame sensor detects flame')
        self.assertEqual(flameDetect(0),1,'Ensures the result is 1 as the Flame sensor detects no flame')
        self.assertEqual(flameDetect(989898),0,'Ensures the result is 0 as the input is anything other than 0 or 1 (ON/OFF)')
    def testLock(self):
        configLock()
        self.assertEqual(lock(1),1,'Ensure the result is 1 when the client switches ON the lock')
        self.assertEqual(lock(0),1,'Ensure the result is 1 when the client switches OFF the lock')
        self.assertEqual(lock('1'),0,'Ensure the result is 0 when the the input is anything other than ON OR OFF')
    def testMotionDetect(self):
        configMotion()
        self.assertEqual(motionDetect(1),0,'Ensures the result is 0 as the Motion sensor detects motion')
        self.assertEqual(motionDetect(0),1,'Ensures the result is 1 as the Motion sensor detects no motion')
        self.assertEqual(motionDetect('Hi'),0,'Ensures the result is 0 as the input is anything other than 0 or 1 (ON/OFF)')
    def testRecordVideo(self):
        self.assertEqual(recordVideo(1),1,'Ensure the result is 1 when the camera switches ON to record')
        self.assertEqual(recordVideo(0),1,'Ensure the result is 1 when the camera switches OFF to record')
        self.assertEqual(recordVideo('A'),0,'Ensure the result is 0 when the the input is anything other than ON OR OFF') 
        
    ##Testing Integration of Hardware
    def testConfigSystem(self):
        self.assertEqual(configSystem(),1,'Ensure that configuring System returns 1 when successful')
    def testUpdateStatus(self):
        self.assertEqual(updateStatus(),1,'Ensure that configuring Status returns 1 when successful')
    def testTakeAction(self):
        self.assertEqual(takeAction(0),1,'Ensure the result is 1 when the system takes no action to record')
        self.assertEqual(takeAction(1),1,'Ensure the result is 1 when the system takes action to record')
        self.assertEqual(takeAction('B'),0,'Ensure the result is 0 when the the input is anything other than ON OR OFF')
    def testUpdateHistory(self):
        self.assertEqual(updateHistory(0,0),1,'Ensure that the result is 1 when the camera is switched OFF and motion is detected')
        self.assertEqual(updateHistory(0,1),1,'Ensure that the result is 1 when the camera is switched ON and motion is detected')
        self.assertEqual(updateHistory(1,0),1,'Ensure that the result is 1 when the camera is switched OFF and flame is detected')
        self.assertEqual(updateHistory(1,1),1,'Ensure that the result is 1 when the camera is switched ON and flame is detected')
        self.assertEqual(updateHistory('E', 'D'),0,'Ensure the result is 0 when the the input is anything other than ON OR OFF')
                         
                
if __name__ == '__main__':
    unittest.main()