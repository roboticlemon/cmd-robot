Imports Microsoft.DirectX
Imports Microsoft.DirectX.DirectInput
Imports System.Net
Imports System.Net.Sockets

Public Class JoyTCP
    Property DefaultCharIsUnsigned As Boolean
    Dim Joystick As Device
    Dim ValueToSend As String
    Dim Paused As Boolean
    Dim _HOST As String = ""
    Dim _PORT As String = ""
    Dim _JoystickEn As String = ""
    Dim _DebugEn As String = ""
    Dim _TCPEn As String = ""
    Dim _CMDrobot As String = ""
    Dim oldValueToSend As String = ""
    Dim x As Integer = 0
    Dim y As Integer = 0
    Dim a As Integer = 0
    Dim b As Integer = 0

    Public Sub JoyTCP_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        GetVariablesFromStartForm()

        If _JoystickEn = "y" Then
            InitializeJoystick()
        End If
        txtbox_robot.Text = _CMDrobot
        If _TCPEn = "y" Then
            _ServerAddress = Nothing
            Dim remoteHost As IPHostEntry = Dns.GetHostEntry(StartForm.txtbox_IPaddr.Text)
            If remoteHost IsNot Nothing AndAlso remoteHost.AddressList.Length > 0 Then
                For Each deltaAddress As IPAddress In remoteHost.AddressList
                    If deltaAddress.AddressFamily = AddressFamily.InterNetwork Then
                        _ServerAddress = deltaAddress
                        Exit For
                    End If
                Next
            End If

            If _ServerAddress Is Nothing Then
                MessageBox.Show("Cannot resolove server address.", "Invalid Server", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
                StartForm.txtbox_Port.SelectAll()
            End If
            Connect()
        End If
        If _TCPEn = "n" Then
            btn_connect.Enabled = False
            btn_pause.Enabled = False
            btn_disconnect.Enabled = False
        End If
    End Sub
    Private Sub JoyPoll()
        Try
            Joystick.Poll()
            Dim state As JoystickState = Joystick.CurrentJoystickState
            Dim x As Integer
            Dim y As Integer
            Dim a As Integer
            Dim b As Integer
            Dim Direction As Integer
            Dim Button0 As Integer
            Dim Button1 As Integer
            Dim Button2 As Integer
            Dim Button3 As Integer
            Dim motor_a As Integer
            Dim motor_b As Integer
            Dim dir As Integer

            txtbox_Xcord.Text = state.X
            txtbox_Ycord.Text = state.Y
            txtbox_Zcord.Text = state.Z
            txtbox_RZcord.Text = state.Rz
            Button0 = state.GetButtons(0)
            Button1 = state.GetButtons(1)
            Button2 = state.GetButtons(2)
            Button3 = state.GetButtons(3)
            txtbox_Button0.Text = Button0
            txtbox_Button1.Text = Button1
            txtbox_Button2.Text = Button2
            txtbox_Button3.Text = Button3
            x = state.X
            y = state.Y

            If y < 0 Then
                y = Math.Abs(y)
                Direction = 1
            ElseIf y > 0 Then
                y = y * -1
                Direction = 2
            End If

            If Button1 = 0 And Button2 = 0 Then
                If x = 0 Then
                    a = Math.Abs(y)
                    b = Math.Abs(y)
                ElseIf y > 0 Then
                    If x > 0 And y <= x Then
                        a = Math.Abs(x)
                        b = 0
                    ElseIf x > 0 And y > x Then
                        a = Math.Abs(y)
                        b = Math.Abs(y) - Math.Abs(x)
                    ElseIf x < 0 And y <= -x Then
                        b = Math.Abs(x)
                        a = 0
                    ElseIf x < 0 And y > -x Then
                        b = Math.Abs(y)
                        a = Math.Abs(y) - Math.Abs(x)
                    End If
                ElseIf y = 0 And x <> 0 Then
                    If x < 0 Then
                        a = 0
                        b = Math.Abs(x)
                    ElseIf x > 0 Then
                        a = Math.Abs(x)
                        b = 0
                    End If
                ElseIf y < 0 Then
                    If x > 0 And y >= -x Then
                        a = Math.Abs(x)
                        b = 0
                    ElseIf x > 0 And y < -x Then
                        a = Math.Abs(y)
                        b = Math.Abs(y) - Math.Abs(x)
                    ElseIf x < 0 And y >= x Then
                        a = 0
                        b = Math.Abs(x)
                    ElseIf x < 0 And y < x Then
                        a = Math.Abs(y) - Math.Abs(x)
                        b = Math.Abs(y)
                    Else
                        a = 0
                        b = 0
                    End If
                End If
            ElseIf Button1 = 128 Or Button2 = 128 Then
                If Button1 = 128 Then
                    a = Math.Abs(y)
                    b = Math.Abs(y)
                    Direction = 3
                ElseIf Button2 = 128 Then
                    a = Math.Abs(y)
                    b = Math.Abs(y)
                    Direction = 4
                End If
            End If

            lbl_value_a.Text = Math.Round((a / 255) * 100) 'CHANGED so that is displays a percentage, not sure if working :D
            lbl_value_b.Text = Math.Round((b / 255) * 100)
            a = Math.Round(a, 1)
            b = Math.Round(b, 1)
            motor_a = Int(a)
            motor_b = Int(b)
            dir = Int(Direction)
            ValueToSend = (Chr(motor_a) & Chr(motor_b) & Chr(dir))
            If ValueToSend <> oldValueToSend Then
                If Paused = False Then
                    SendData()
                    oldValueToSend = ValueToSend
                End If
            End If

            'If Paused = False Then
            '    SendData()
            'End If
        Catch ex As Exception
        End Try
    End Sub

    Private Sub InitializeJoystick()
        Dim oInst As DeviceInstance
        Dim oDOInst As DeviceObjectInstance

        For Each oInst In Manager.GetDevices(DeviceClass.GameControl, EnumDevicesFlags.AttachedOnly)
            Joystick = New DirectInput.Device(oInst.InstanceGuid)
            Exit For
        Next

        If Not (Joystick Is Nothing) Then
            Joystick.SetDataFormat(DeviceDataFormat.Joystick)
            Joystick.SetCooperativeLevel(Me, CooperativeLevelFlags.NonExclusive Or DirectInput.CooperativeLevelFlags.Background)
            For Each oDOInst In Joystick.Objects
                If 0 <> (oDOInst.ObjectId And CInt(DeviceObjectTypeFlags.Axis)) Then
                    Joystick.Properties.SetRange(ParameterHow.ById, oDOInst.ObjectId, New InputRange(-255, +255))
                End If
            Next
        End If

        Try
            Joystick.Acquire()
        Catch ex As Exception
            MessageBox.Show(ex.Message, "Couldn't detect joystick!", MessageBoxButtons.OK, MessageBoxIcon.Error)
        End Try

        Timer1.Start()
    End Sub

    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        If _JoystickEn = "y" Then
            JoyPoll()
        End If
    End Sub

    Private Sub GetVariablesFromStartForm()
        _HOST = StartForm.txtbox_IPaddr.Text
        _PORT = StartForm.txtbox_Port.Text
        If StartForm.rabtn_CMDoverwatch.Checked = True Then
            _CMDrobot = "CMDoverwatch"
        ElseIf StartForm.rabtn_CMDrecon.Checked = True Then
            _CMDrobot = "CMDrecon"
        ElseIf StartForm.RadioButton1.Checked = True Then
            _CMDrobot = "CMDdebug"
        End If
        If StartForm.CheckBox_JoystickEn.Checked = True Then
            _JoystickEn = "y"
        Else
            _JoystickEn = "n"
        End If
        If StartForm.CheckBox_DebugmodeEn.Checked = True Then
            _DebugEn = "y"
        Else
            _DebugEn = "n"
        End If
        If StartForm.CheckBox_TCPclientEn.Checked = True Then
            _TCPEn = "y"
        Else
            _TCPEn = "n"
        End If
    End Sub

    Private _Connection As ConnectionInfo
    Private _ServerAddress As IPAddress
    Public Sub Connect()
        If _ServerAddress IsNot Nothing Then
            Try
                '_Connection = New ConnectionInfo(_ServerAddress, CInt(txtbox_Port.Text), AddressOf InvokeAppendOutput)
                _Connection = New ConnectionInfo(_ServerAddress, CInt(StartForm.txtbox_Port.Text), AddressOf InvokeAppendOutput)
                '_Connection = New ConnectionInfo(_ServerAddress, CInt(StartForm.txtbox_Port.Text))
                _Connection.AwaitData()
            Catch ex As Exception
                MessageBox.Show(ex.Message, "Error Connecting to Server", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
            End Try
        Else
            MessageBox.Show("Invalid server name or address. Try inputting it again!", "Cannot Connect to Server", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
        End If
    End Sub

    'The InvokeAppendOutput method could easily be replaced with a lambda method passed
    'to the ConnectionInfo contstructor in the ConnectButton_CheckChanged event handler
    Private Sub InvokeAppendOutput(message As String)
        Dim doAppendOutput As New Action(Of String)(AddressOf AppendOutput)
        Me.Invoke(doAppendOutput, message)
    End Sub
    'Private Sub AppendOutput(message As String)
    '    If StartForm.RichTextBox1.TextLength > 0 Then
    '        StartForm.RichTextBox1.AppendText(ControlChars.NewLine)
    '    End If
    '    StartForm.RichTextBox1.AppendText(message)
    '    StartForm.RichTextBox1.ScrollToCaret()
    'End Sub
    Public Sub SendData()
        If _Connection IsNot Nothing AndAlso _Connection.Client.Connected AndAlso _Connection.Stream IsNot Nothing Then
            Dim buffer() As Byte = System.Text.Encoding.Default.GetBytes(ValueToSend)
            _Connection.Stream.Write(buffer, 0, buffer.Length)
        End If
    End Sub
    Private Sub btn_disconnect_Click(sender As Object, e As EventArgs)
        _Connection.Close()
    End Sub

    '   Private Sub btn_pause_Click(sender As Object, e As EventArgs)
    '    If btn_pause.Text = "Pause" Then
    '        Paused = True
    '        btn_pause.Text = "Play"
    '        MessageBox.Show("Box shown!!  Play button pressed")
    '    ElseIf btn_pause.Text = "Play" Then
    '        Paused = False
    '        btn_pause.Text = "Pause"
    '        MessageBox.Show("Box shown!!  Pause button pressed")
    '    End If
    'End Sub

    'Private Sub btn_Forcetest_Click(sender As Object, e As EventArgs)
    '    lbl_value_a.Text = "75"
    '    lbl_value_b.Text = "100"
    '    MessageBox.Show("btn_Forcetest_Clicked")
    'End Sub

    Private Sub btn_close_Click(sender As Object, e As EventArgs) Handles btn_close.Click
        StartForm.Close()
        Me.Close()
    End Sub

    

    Private Sub btn_Forcetest_Click_1(sender As Object, e As EventArgs) Handles btn_Forcetest.Click
        lbl_value_a.Text = "75"
        lbl_value_b.Text = "100"
    End Sub

    Private Sub btn_connect_Click_1(sender As Object, e As EventArgs) Handles btn_connect.Click
        Connect()
    End Sub

    Private Sub btn_pause_Click_1(sender As Object, e As EventArgs) Handles btn_pause.Click
        If btn_pause.Text = "Pause" Then
            Paused = True
            btn_pause.Text = "Play"
            'MessageBox.Show("Box shown!!  Play button pressed")
        ElseIf btn_pause.Text = "Play" Then
            Paused = False
            btn_pause.Text = "Pause"
            'MessageBox.Show("Box shown!!  Pause button pressed")
        End If
    End Sub

    Private Sub btn_disconnect_Click_1(sender As Object, e As EventArgs) Handles btn_disconnect.Click
        _Connection.Close()
    End Sub

    Private Sub AppendOutput()
        Throw New NotImplementedException
    End Sub


    Private Sub btn_VideoGo_Click(sender As Object, e As EventArgs) Handles btn_VideoGo.Click
        VideoBoxForm.Show()
    End Sub
End Class

'Encapuslates the client connection and provides a state object for async read operations
Public Class ConnectionInfo
    Private _AppendMethod As Action(Of String)
    Public ReadOnly Property AppendMethod As Action(Of String)
        Get
            Return _AppendMethod
        End Get
    End Property

    Private _Client As TcpClient
    Public ReadOnly Property Client As TcpClient
        Get
            Return _Client
        End Get
    End Property

    Private _Stream As NetworkStream
    Public ReadOnly Property Stream As NetworkStream
        Get
            Return _Stream
        End Get
    End Property

    Private _LastReadLength As Integer
    Public ReadOnly Property LastReadLength As Integer
        Get
            Return _LastReadLength
        End Get
    End Property

    Private _Buffer(63) As Byte

    Public Sub New(address As IPAddress, port As Integer, append As Action(Of String))
        _AppendMethod = append
        _Client = New TcpClient
        _Client.Connect(address, port)
        _Stream = _Client.GetStream
    End Sub

    Public Sub AwaitData()
        _Stream.BeginRead(_Buffer, 0, _Buffer.Length, AddressOf DoReadData, Me)
    End Sub

    Public Sub Close()
        If _Client IsNot Nothing Then _Client.Close()
        _Client = Nothing
        _Stream = Nothing
    End Sub

    Private Sub DoReadData(result As IAsyncResult)
        Dim info As ConnectionInfo = CType(result.AsyncState, ConnectionInfo)
        Try
            If info._Stream IsNot Nothing AndAlso info._Stream.CanRead Then
                info._LastReadLength = info._Stream.EndRead(result)
                If info._LastReadLength > 0 Then
                    Dim message As String = System.Text.Encoding.ASCII.GetString(info._Buffer)
                    info._AppendMethod(message)
                End If
                info.AwaitData()
            End If
        Catch ex As Exception
            info._LastReadLength = -1
            info._AppendMethod(ex.Message)
        End Try
    End Sub
End Class