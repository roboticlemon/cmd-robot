Imports System.Net
Imports System.Net.Sockets

Public Class StartForm
    Dim CMDrobot As String = ""
    Dim IPaddr As String = ""
    Dim Port As String = ""
    Dim DebugEn As String = ""
    Dim JoystickEn As String = ""
    Dim TCPEn As String = ""

    Private Sub btn_start_Click(sender As Object, e As EventArgs) Handles btn_start.Click
        IPaddr = txtbox_IPaddr.Text
        Port = txtbox_Port.Text
        CMDrobot = CMDrobot
        If CheckBox_JoystickEn.Checked = True Then
            JoystickEn = "y"
        Else
            JoystickEn = "n"
        End If
        If CheckBox_DebugmodeEn.Checked = True Then
            DebugEn = "y"
        Else
            DebugEn = "n"
        End If
        If CheckBox_TCPclientEn.Checked = True Then
            TCPEn = "y"
        Else
            TCPEn = "n"
        End If
        JoyTCP.Show()
    End Sub

    Private Sub btn_close_Click(sender As Object, e As EventArgs) Handles btn_close.Click
        Me.Close()
    End Sub

    Private Sub CheckBox_DevEn_CheckedChanged(sender As Object, e As EventArgs) Handles CheckBox_DevEn.CheckedChanged
        If CheckBox_DevEn.Checked = True Then
            btn_testmode.Enabled = True
        Else
            btn_testmode.Enabled = False
        End If
    End Sub

    Private Sub btn_testmode_Click(sender As Object, e As EventArgs) Handles btn_testmode.Click
        MessageBox.Show("Welcome to the Dev console, in future this will launch the Black Frost Console!", "Dev Console Alert")
        'Joystick_TCP.Show()
    End Sub

    Private Sub rabtn_CMDoverwatch_CheckedChanged(sender As Object, e As EventArgs) Handles rabtn_CMDoverwatch.CheckedChanged
        CMDrobot = "CMDoverwatch"
        txtbox_IPaddr.Text = "10.0.0.1"
        txtbox_Port.Text = "8999"
    End Sub

    Private Sub rabtn_CMDrecon_CheckedChanged(sender As Object, e As EventArgs) Handles rabtn_CMDrecon.CheckedChanged
        CMDrobot = "CMDrecon"
        txtbox_IPaddr.Text = "10.0.0.10"
        txtbox_Port.Text = "9999"
    End Sub

    Private Sub CheckBox_JoystickEn_CheckedChanged(sender As Object, e As EventArgs) Handles CheckBox_JoystickEn.CheckedChanged
        If CheckBox_JoystickEn.Checked = True Then
            CheckBox_DebugmodeEn.Checked = False
        End If
    End Sub

    Private Sub CheckBox_DebugmodeEn_CheckedChanged(sender As Object, e As EventArgs) Handles CheckBox_DebugmodeEn.CheckedChanged
        If CheckBox_DebugmodeEn.Checked = True Then
            CheckBox_JoystickEn.Checked = False
        End If
    End Sub


    Private Sub StartForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub RadioButton1_CheckedChanged(sender As Object, e As EventArgs) Handles RadioButton1.CheckedChanged
        txtbox_IPaddr.Text = "localhost"
        txtbox_Port.Text = "9999"
        CMDrobot = "CMDdebug"
    End Sub

End Class
