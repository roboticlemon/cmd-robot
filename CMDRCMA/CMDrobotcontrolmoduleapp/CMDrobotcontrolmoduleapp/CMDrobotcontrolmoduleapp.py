import wpf
import clr
import os
import sys
from System.Diagnostics import Process
from time import gmtime, strftime, sleep
from System.Windows.Controls import Image
from System.Environment import OSVersion

from System.Windows import Application, Window, MessageBox   # This Line works when un-commented

class StartWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'CMDrobotcontrolmoduleapp.xaml')
        self.IPaddress_TextBox.Text = 'Type IP address'
        self.Port_TextBox.Text = 'Type Port Number'
        self.JoystickEnable_CheckBox.IsChecked = True
        self.DebugEnabled_CheckBox.IsChecked = False
        self.TCPEnabled_CheckBox.IsChecked = True
        self.dev_CheckBox.IsChecked = True
        if os.path.exists("C:\Users\Tom"):
            self.user = "Commander Ingram"
            self.User_TextBox_New.Text = self.user
            self.CMDrecon_radiobutton.IsChecked = True
        elif os.path.exists("C:\Users\Cian"):
            self.user = "Commander Byrne"
            self.User_TextBox_New.Text = self.user
            self.CMDoverwatch_radiobutton.IsChecked = True
        else:
            self.User_TextBox_New.Text = "Unknown"

    def Start_Button_Click(self, sender, e):
        self.Port = self.Port_TextBox.Text
        self.IPaddress = self.IPaddress_TextBox.Text
        if self.JoystickEnable_CheckBox.IsEnabled == True:
            self.Joystick = 'y'
        if self.JoystickEnable_CheckBox.IsChecked == False:
            self.Joystick = 'n'
        if self.DebugEnabled_CheckBox.IsChecked == True:
            self.Debug = 'y'
        if self.DebugEnabled_CheckBox.IsChecked == False:
            self.Debug = 'n'
        if self.TCPEnabled_CheckBox.IsChecked == True:
            self.TCP = 'y'
        if self.TCPEnabled_CheckBox.IsChecked == False:
            self.TCP = 'n'
        self.file = open('details.txt', 'w')
        self.file.write(self.Port+'\n'+self.IPaddress+'\n'+self.CMDrobot+'\n'+self.TCP+'\n'+self.Joystick+'\n'+self.Debug+'\n')
        self.file.close()
        Process.Start('python.exe', 'ControlModuleBeta1.6.6.py')
     
    def Info_Button_Click(self, sender, e):
        time = strftime("%H:%M:%S")
        major = str(OSVersion.Version.Major)
        minor = str(OSVersion.Version.Minor)
        kernel = major + "." + minor
       # opsys = "Unknown"
        if kernel == "6.2":
            opsys = "Windows 8"
        elif kernel == "6.1":
            opsys = "Windows 7"
        elif kernel == "6.0":
            opsys = "Windows Vista"
        else:
            opsys = "Windows XP"
        MessageBox.Show("Information about your PC: \n \n" + "OS Version = " + opsys + "\nKernel Version = " + kernel, "PC Information")

    def Close_Button_Click(self, sender, e):
        Application.Current.Shutdown()
    
    def CMDrecon_radiobutton_Checked(self, sender, e):
        self.Port_TextBox.Text = "9999"
        self.IPaddress_TextBox.Text = "10.0.0.10"
        self.CMDrobot = 'CMDrecon'
    
    def CMDoverwatch_radiobutton_Checked(self, sender, e):
        self.Port_TextBox.Text = "8999"
        self.IPaddress_TextBox.Text = "10.0.0.1"
        self.CMDrobot = 'CMDoverwatch'

    def Port_TextBox_GotFocus(self, sender, e):
        self.Port_TextBox.Text = ''

    def IPaddress_TextBox_GotFocus(self, sender, e):
        self.IPaddress_TextBox.Text = ''

    def IPaddress_TextBox_TextChanged(self, sender, e):
        pass
    
    def Port_TextBox_TextChanged(self, sender, e):
        pass
   
    def User_TextBox_New_TextChanged(self, sender, e):
        pass
    
    def btn_test_Click(self, sender, e):
        MessageBox.Show("Welcome " + self.user + " to the Dev console, in future this will launch the Black Frost Console!", "Dev Console Alert" )
    
    def dev_CheckBox_Checked(self, sender, e):
        self.btn_test.IsEnabled = True

    def dev_CheckBox_UnChecked(self, sender, e):
        self.btn_test.IsEnabled = False
    
    def JoystickEnable_CheckBox_Checked(self, sender, e):
        self.DebugEnabled_CheckBox.IsChecked = False
            
    def DebugEnabled_CheckBox_Checked(self, sender, e):
        self.JoystickEnable_CheckBox.IsChecked = False
            
    def TCPEnabled_CheckBox_Checked(self, sender, e):
        pass

if __name__ == '__main__':
    Application().Run(StartWindow())
    

