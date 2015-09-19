<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class JoyTCP
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(JoyTCP))
        Me.btn_BFconsole = New System.Windows.Forms.Button()
        Me.btn_tab3c_disconnect = New System.Windows.Forms.Button()
        Me.btn_tab3c_connect = New System.Windows.Forms.Button()
        Me.Tab2 = New System.Windows.Forms.TabPage()
        Me.btn_VideoGo = New System.Windows.Forms.Button()
        Me.btn_tab3c_pause = New System.Windows.Forms.Button()
        Me.txtbox_robot = New System.Windows.Forms.TextBox()
        Me.Label9 = New System.Windows.Forms.Label()
        Me.btn_Forcetest = New System.Windows.Forms.Button()
        Me.btn_pause = New System.Windows.Forms.Button()
        Me.btn_disconnect = New System.Windows.Forms.Button()
        Me.btn_connect = New System.Windows.Forms.Button()
        Me.Label8 = New System.Windows.Forms.Label()
        Me.txtbox_Button3 = New System.Windows.Forms.TextBox()
        Me.Timer1 = New System.Windows.Forms.Timer(Me.components)
        Me.btn_close = New System.Windows.Forms.Button()
        Me.Tab1 = New System.Windows.Forms.TabPage()
        Me.Label7 = New System.Windows.Forms.Label()
        Me.txtbox_RZcord = New System.Windows.Forms.TextBox()
        Me.Label6 = New System.Windows.Forms.Label()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.PictureBox1 = New System.Windows.Forms.PictureBox()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.txtbox_Button2 = New System.Windows.Forms.TextBox()
        Me.txtbox_Button1 = New System.Windows.Forms.TextBox()
        Me.txtbox_Button0 = New System.Windows.Forms.TextBox()
        Me.txtbox_Zcord = New System.Windows.Forms.TextBox()
        Me.txtbox_Ycord = New System.Windows.Forms.TextBox()
        Me.txtbox_Xcord = New System.Windows.Forms.TextBox()
        Me.Label11 = New System.Windows.Forms.Label()
        Me.Label10 = New System.Windows.Forms.Label()
        Me.lbl_value_b = New System.Windows.Forms.Label()
        Me.lbl_value_a = New System.Windows.Forms.Label()
        Me.TabControl1 = New System.Windows.Forms.TabControl()
        Me.Tab2.SuspendLayout()
        Me.Tab1.SuspendLayout()
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.TabControl1.SuspendLayout()
        Me.SuspendLayout()
        '
        'btn_BFconsole
        '
        Me.btn_BFconsole.Location = New System.Drawing.Point(20, 198)
        Me.btn_BFconsole.Name = "btn_BFconsole"
        Me.btn_BFconsole.Size = New System.Drawing.Size(265, 33)
        Me.btn_BFconsole.TabIndex = 3
        Me.btn_BFconsole.Text = "BlackFrost Console"
        Me.btn_BFconsole.UseVisualStyleBackColor = True
        '
        'btn_tab3c_disconnect
        '
        Me.btn_tab3c_disconnect.Location = New System.Drawing.Point(20, 140)
        Me.btn_tab3c_disconnect.Name = "btn_tab3c_disconnect"
        Me.btn_tab3c_disconnect.Size = New System.Drawing.Size(266, 33)
        Me.btn_tab3c_disconnect.TabIndex = 2
        Me.btn_tab3c_disconnect.Text = "Disconnect"
        Me.btn_tab3c_disconnect.UseVisualStyleBackColor = True
        '
        'btn_tab3c_connect
        '
        Me.btn_tab3c_connect.Location = New System.Drawing.Point(20, 33)
        Me.btn_tab3c_connect.Name = "btn_tab3c_connect"
        Me.btn_tab3c_connect.Size = New System.Drawing.Size(266, 33)
        Me.btn_tab3c_connect.TabIndex = 0
        Me.btn_tab3c_connect.Text = "Connect"
        Me.btn_tab3c_connect.UseVisualStyleBackColor = True
        '
        'Tab2
        '
        Me.Tab2.Controls.Add(Me.btn_VideoGo)
        Me.Tab2.Controls.Add(Me.btn_BFconsole)
        Me.Tab2.Controls.Add(Me.btn_tab3c_disconnect)
        Me.Tab2.Controls.Add(Me.btn_tab3c_pause)
        Me.Tab2.Controls.Add(Me.btn_tab3c_connect)
        Me.Tab2.Location = New System.Drawing.Point(4, 22)
        Me.Tab2.Name = "Tab2"
        Me.Tab2.Padding = New System.Windows.Forms.Padding(3)
        Me.Tab2.Size = New System.Drawing.Size(307, 315)
        Me.Tab2.TabIndex = 1
        Me.Tab2.Text = "Command Control Center"
        Me.Tab2.UseVisualStyleBackColor = True
        '
        'btn_VideoGo
        '
        Me.btn_VideoGo.Location = New System.Drawing.Point(20, 256)
        Me.btn_VideoGo.Name = "btn_VideoGo"
        Me.btn_VideoGo.Size = New System.Drawing.Size(265, 33)
        Me.btn_VideoGo.TabIndex = 4
        Me.btn_VideoGo.Text = "Video Stream"
        Me.btn_VideoGo.UseVisualStyleBackColor = True
        '
        'btn_tab3c_pause
        '
        Me.btn_tab3c_pause.Location = New System.Drawing.Point(20, 86)
        Me.btn_tab3c_pause.Name = "btn_tab3c_pause"
        Me.btn_tab3c_pause.Size = New System.Drawing.Size(266, 33)
        Me.btn_tab3c_pause.TabIndex = 1
        Me.btn_tab3c_pause.Text = "Pause"
        Me.btn_tab3c_pause.UseVisualStyleBackColor = True
        '
        'txtbox_robot
        '
        Me.txtbox_robot.Location = New System.Drawing.Point(79, 7)
        Me.txtbox_robot.Name = "txtbox_robot"
        Me.txtbox_robot.Size = New System.Drawing.Size(148, 20)
        Me.txtbox_robot.TabIndex = 52
        '
        'Label9
        '
        Me.Label9.AutoSize = True
        Me.Label9.Location = New System.Drawing.Point(17, 10)
        Me.Label9.Name = "Label9"
        Me.Label9.Size = New System.Drawing.Size(59, 13)
        Me.Label9.TabIndex = 51
        Me.Label9.Text = "Controlling "
        '
        'btn_Forcetest
        '
        Me.btn_Forcetest.Location = New System.Drawing.Point(81, 277)
        Me.btn_Forcetest.Name = "btn_Forcetest"
        Me.btn_Forcetest.Size = New System.Drawing.Size(138, 31)
        Me.btn_Forcetest.TabIndex = 50
        Me.btn_Forcetest.Text = "Test"
        Me.btn_Forcetest.UseVisualStyleBackColor = True
        '
        'btn_pause
        '
        Me.btn_pause.Location = New System.Drawing.Point(113, 248)
        Me.btn_pause.Name = "btn_pause"
        Me.btn_pause.Size = New System.Drawing.Size(75, 23)
        Me.btn_pause.TabIndex = 49
        Me.btn_pause.Text = "Pause"
        Me.btn_pause.UseVisualStyleBackColor = True
        '
        'btn_disconnect
        '
        Me.btn_disconnect.Location = New System.Drawing.Point(211, 248)
        Me.btn_disconnect.Name = "btn_disconnect"
        Me.btn_disconnect.Size = New System.Drawing.Size(75, 23)
        Me.btn_disconnect.TabIndex = 48
        Me.btn_disconnect.Text = "Disconnect"
        Me.btn_disconnect.UseVisualStyleBackColor = True
        '
        'btn_connect
        '
        Me.btn_connect.Location = New System.Drawing.Point(14, 248)
        Me.btn_connect.Name = "btn_connect"
        Me.btn_connect.Size = New System.Drawing.Size(75, 23)
        Me.btn_connect.TabIndex = 47
        Me.btn_connect.Text = "Connect"
        Me.btn_connect.UseVisualStyleBackColor = True
        '
        'Label8
        '
        Me.Label8.AutoSize = True
        Me.Label8.Location = New System.Drawing.Point(175, 216)
        Me.Label8.Name = "Label8"
        Me.Label8.Size = New System.Drawing.Size(13, 13)
        Me.Label8.TabIndex = 46
        Me.Label8.Text = "4"
        '
        'txtbox_Button3
        '
        Me.txtbox_Button3.Location = New System.Drawing.Point(211, 213)
        Me.txtbox_Button3.Name = "txtbox_Button3"
        Me.txtbox_Button3.Size = New System.Drawing.Size(78, 20)
        Me.txtbox_Button3.TabIndex = 45
        '
        'Timer1
        '
        Me.Timer1.Interval = 10
        '
        'btn_close
        '
        Me.btn_close.Location = New System.Drawing.Point(23, 424)
        Me.btn_close.Name = "btn_close"
        Me.btn_close.Size = New System.Drawing.Size(271, 66)
        Me.btn_close.TabIndex = 48
        Me.btn_close.Text = "Close"
        Me.btn_close.UseVisualStyleBackColor = True
        '
        'Tab1
        '
        Me.Tab1.Controls.Add(Me.txtbox_robot)
        Me.Tab1.Controls.Add(Me.Label9)
        Me.Tab1.Controls.Add(Me.btn_Forcetest)
        Me.Tab1.Controls.Add(Me.btn_pause)
        Me.Tab1.Controls.Add(Me.btn_disconnect)
        Me.Tab1.Controls.Add(Me.btn_connect)
        Me.Tab1.Controls.Add(Me.Label8)
        Me.Tab1.Controls.Add(Me.txtbox_Button3)
        Me.Tab1.Controls.Add(Me.Label7)
        Me.Tab1.Controls.Add(Me.txtbox_RZcord)
        Me.Tab1.Controls.Add(Me.Label6)
        Me.Tab1.Controls.Add(Me.Label5)
        Me.Tab1.Controls.Add(Me.Label4)
        Me.Tab1.Controls.Add(Me.PictureBox1)
        Me.Tab1.Controls.Add(Me.Label3)
        Me.Tab1.Controls.Add(Me.Label2)
        Me.Tab1.Controls.Add(Me.Label1)
        Me.Tab1.Controls.Add(Me.txtbox_Button2)
        Me.Tab1.Controls.Add(Me.txtbox_Button1)
        Me.Tab1.Controls.Add(Me.txtbox_Button0)
        Me.Tab1.Controls.Add(Me.txtbox_Zcord)
        Me.Tab1.Controls.Add(Me.txtbox_Ycord)
        Me.Tab1.Controls.Add(Me.txtbox_Xcord)
        Me.Tab1.Location = New System.Drawing.Point(4, 22)
        Me.Tab1.Name = "Tab1"
        Me.Tab1.Padding = New System.Windows.Forms.Padding(3)
        Me.Tab1.Size = New System.Drawing.Size(307, 315)
        Me.Tab1.TabIndex = 0
        Me.Tab1.Text = "Joystick Debug"
        Me.Tab1.UseVisualStyleBackColor = True
        '
        'Label7
        '
        Me.Label7.AutoSize = True
        Me.Label7.Location = New System.Drawing.Point(18, 216)
        Me.Label7.Name = "Label7"
        Me.Label7.Size = New System.Drawing.Size(22, 13)
        Me.Label7.TabIndex = 44
        Me.Label7.Text = "RZ"
        '
        'txtbox_RZcord
        '
        Me.txtbox_RZcord.Location = New System.Drawing.Point(52, 213)
        Me.txtbox_RZcord.Name = "txtbox_RZcord"
        Me.txtbox_RZcord.Size = New System.Drawing.Size(83, 20)
        Me.txtbox_RZcord.TabIndex = 43
        '
        'Label6
        '
        Me.Label6.AutoSize = True
        Me.Label6.Location = New System.Drawing.Point(175, 181)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(13, 13)
        Me.Label6.TabIndex = 42
        Me.Label6.Text = "3"
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Location = New System.Drawing.Point(175, 145)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(13, 13)
        Me.Label5.TabIndex = 41
        Me.Label5.Text = "2"
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Location = New System.Drawing.Point(175, 110)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(13, 13)
        Me.Label4.TabIndex = 40
        Me.Label4.Text = "1"
        '
        'PictureBox1
        '
        Me.PictureBox1.Image = CType(resources.GetObject("PictureBox1.Image"), System.Drawing.Image)
        Me.PictureBox1.InitialImage = Nothing
        Me.PictureBox1.Location = New System.Drawing.Point(14, 33)
        Me.PictureBox1.Name = "PictureBox1"
        Me.PictureBox1.Size = New System.Drawing.Size(278, 67)
        Me.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        Me.PictureBox1.TabIndex = 39
        Me.PictureBox1.TabStop = False
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(18, 181)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(14, 13)
        Me.Label3.TabIndex = 38
        Me.Label3.Text = "Z"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(18, 145)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(14, 13)
        Me.Label2.TabIndex = 37
        Me.Label2.Text = "Y"
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(18, 109)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(14, 13)
        Me.Label1.TabIndex = 36
        Me.Label1.Text = "X"
        '
        'txtbox_Button2
        '
        Me.txtbox_Button2.Location = New System.Drawing.Point(211, 178)
        Me.txtbox_Button2.Name = "txtbox_Button2"
        Me.txtbox_Button2.Size = New System.Drawing.Size(78, 20)
        Me.txtbox_Button2.TabIndex = 35
        '
        'txtbox_Button1
        '
        Me.txtbox_Button1.Location = New System.Drawing.Point(211, 142)
        Me.txtbox_Button1.Name = "txtbox_Button1"
        Me.txtbox_Button1.Size = New System.Drawing.Size(78, 20)
        Me.txtbox_Button1.TabIndex = 34
        '
        'txtbox_Button0
        '
        Me.txtbox_Button0.Location = New System.Drawing.Point(211, 107)
        Me.txtbox_Button0.Name = "txtbox_Button0"
        Me.txtbox_Button0.Size = New System.Drawing.Size(78, 20)
        Me.txtbox_Button0.TabIndex = 33
        '
        'txtbox_Zcord
        '
        Me.txtbox_Zcord.Location = New System.Drawing.Point(52, 178)
        Me.txtbox_Zcord.Name = "txtbox_Zcord"
        Me.txtbox_Zcord.Size = New System.Drawing.Size(83, 20)
        Me.txtbox_Zcord.TabIndex = 32
        '
        'txtbox_Ycord
        '
        Me.txtbox_Ycord.Location = New System.Drawing.Point(52, 142)
        Me.txtbox_Ycord.Name = "txtbox_Ycord"
        Me.txtbox_Ycord.Size = New System.Drawing.Size(83, 20)
        Me.txtbox_Ycord.TabIndex = 31
        '
        'txtbox_Xcord
        '
        Me.txtbox_Xcord.Location = New System.Drawing.Point(52, 107)
        Me.txtbox_Xcord.Name = "txtbox_Xcord"
        Me.txtbox_Xcord.Size = New System.Drawing.Size(83, 20)
        Me.txtbox_Xcord.TabIndex = 30
        '
        'Label11
        '
        Me.Label11.AutoSize = True
        Me.Label11.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label11.Location = New System.Drawing.Point(190, 356)
        Me.Label11.Name = "Label11"
        Me.Label11.Size = New System.Drawing.Size(86, 17)
        Me.Label11.TabIndex = 53
        Me.Label11.Text = "Power B (%)"
        '
        'Label10
        '
        Me.Label10.AutoSize = True
        Me.Label10.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label10.Location = New System.Drawing.Point(46, 356)
        Me.Label10.Name = "Label10"
        Me.Label10.Size = New System.Drawing.Size(86, 17)
        Me.Label10.TabIndex = 52
        Me.Label10.Text = "Power A (%)"
        '
        'lbl_value_b
        '
        Me.lbl_value_b.AutoSize = True
        Me.lbl_value_b.Font = New System.Drawing.Font("Arial Black", 14.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_value_b.Location = New System.Drawing.Point(217, 386)
        Me.lbl_value_b.Name = "lbl_value_b"
        Me.lbl_value_b.Size = New System.Drawing.Size(25, 27)
        Me.lbl_value_b.TabIndex = 55
        Me.lbl_value_b.Text = "0"
        '
        'lbl_value_a
        '
        Me.lbl_value_a.AutoSize = True
        Me.lbl_value_a.Font = New System.Drawing.Font("Arial Black", 14.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_value_a.Location = New System.Drawing.Point(75, 386)
        Me.lbl_value_a.Name = "lbl_value_a"
        Me.lbl_value_a.Size = New System.Drawing.Size(25, 27)
        Me.lbl_value_a.TabIndex = 54
        Me.lbl_value_a.Text = "0"
        '
        'TabControl1
        '
        Me.TabControl1.Controls.Add(Me.Tab1)
        Me.TabControl1.Controls.Add(Me.Tab2)
        Me.TabControl1.Location = New System.Drawing.Point(11, 6)
        Me.TabControl1.Name = "TabControl1"
        Me.TabControl1.SelectedIndex = 0
        Me.TabControl1.Size = New System.Drawing.Size(315, 341)
        Me.TabControl1.TabIndex = 56
        '
        'JoyTCP
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(334, 501)
        Me.Controls.Add(Me.btn_close)
        Me.Controls.Add(Me.Label11)
        Me.Controls.Add(Me.Label10)
        Me.Controls.Add(Me.lbl_value_b)
        Me.Controls.Add(Me.lbl_value_a)
        Me.Controls.Add(Me.TabControl1)
        Me.Name = "JoyTCP"
        Me.Text = "CMD3C - Robot Control Centre"
        Me.Tab2.ResumeLayout(False)
        Me.Tab1.ResumeLayout(False)
        Me.Tab1.PerformLayout()
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).EndInit()
        Me.TabControl1.ResumeLayout(False)
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents btn_BFconsole As System.Windows.Forms.Button
    Friend WithEvents btn_tab3c_disconnect As System.Windows.Forms.Button
    Friend WithEvents btn_tab3c_connect As System.Windows.Forms.Button
    Friend WithEvents Tab2 As System.Windows.Forms.TabPage
    Friend WithEvents btn_tab3c_pause As System.Windows.Forms.Button
    Friend WithEvents txtbox_robot As System.Windows.Forms.TextBox
    Friend WithEvents Label9 As System.Windows.Forms.Label
    Friend WithEvents btn_Forcetest As System.Windows.Forms.Button
    Friend WithEvents btn_pause As System.Windows.Forms.Button
    Friend WithEvents btn_disconnect As System.Windows.Forms.Button
    Friend WithEvents btn_connect As System.Windows.Forms.Button
    Friend WithEvents Label8 As System.Windows.Forms.Label
    Friend WithEvents txtbox_Button3 As System.Windows.Forms.TextBox
    Friend WithEvents Timer1 As System.Windows.Forms.Timer
    Friend WithEvents btn_close As System.Windows.Forms.Button
    Friend WithEvents Tab1 As System.Windows.Forms.TabPage
    Friend WithEvents Label7 As System.Windows.Forms.Label
    Friend WithEvents txtbox_RZcord As System.Windows.Forms.TextBox
    Friend WithEvents Label6 As System.Windows.Forms.Label
    Friend WithEvents Label5 As System.Windows.Forms.Label
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents PictureBox1 As System.Windows.Forms.PictureBox
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents txtbox_Button2 As System.Windows.Forms.TextBox
    Friend WithEvents txtbox_Button1 As System.Windows.Forms.TextBox
    Friend WithEvents txtbox_Button0 As System.Windows.Forms.TextBox
    Friend WithEvents txtbox_Zcord As System.Windows.Forms.TextBox
    Friend WithEvents txtbox_Ycord As System.Windows.Forms.TextBox
    Friend WithEvents txtbox_Xcord As System.Windows.Forms.TextBox
    Friend WithEvents Label11 As System.Windows.Forms.Label
    Friend WithEvents Label10 As System.Windows.Forms.Label
    Friend WithEvents lbl_value_b As System.Windows.Forms.Label
    Friend WithEvents lbl_value_a As System.Windows.Forms.Label
    Friend WithEvents TabControl1 As System.Windows.Forms.TabControl
    Friend WithEvents btn_VideoGo As System.Windows.Forms.Button
End Class
