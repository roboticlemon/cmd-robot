<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class StartForm
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
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(StartForm))
        Me.RadioButton1 = New System.Windows.Forms.RadioButton()
        Me.PictureBox1 = New System.Windows.Forms.PictureBox()
        Me.btn_testmode = New System.Windows.Forms.Button()
        Me.CheckBox_DevEn = New System.Windows.Forms.CheckBox()
        Me.CheckBox_TCPclientEn = New System.Windows.Forms.CheckBox()
        Me.CheckBox_DebugmodeEn = New System.Windows.Forms.CheckBox()
        Me.CheckBox_JoystickEn = New System.Windows.Forms.CheckBox()
        Me.txtbox_Port = New System.Windows.Forms.TextBox()
        Me.txtbox_IPaddr = New System.Windows.Forms.TextBox()
        Me.txtblk_Port = New System.Windows.Forms.TextBox()
        Me.txtblk_IPaddr = New System.Windows.Forms.TextBox()
        Me.rabtn_CMDrecon = New System.Windows.Forms.RadioButton()
        Me.rabtn_CMDoverwatch = New System.Windows.Forms.RadioButton()
        Me.btn_close = New System.Windows.Forms.Button()
        Me.btn_start = New System.Windows.Forms.Button()
        Me.Timer1 = New System.Windows.Forms.Timer(Me.components)
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'RadioButton1
        '
        Me.RadioButton1.AutoSize = True
        Me.RadioButton1.Location = New System.Drawing.Point(215, 86)
        Me.RadioButton1.Name = "RadioButton1"
        Me.RadioButton1.Size = New System.Drawing.Size(79, 17)
        Me.RadioButton1.TabIndex = 41
        Me.RadioButton1.Text = "CMDdebug"
        Me.RadioButton1.UseVisualStyleBackColor = True
        '
        'PictureBox1
        '
        Me.PictureBox1.Image = CType(resources.GetObject("PictureBox1.Image"), System.Drawing.Image)
        Me.PictureBox1.InitialImage = Nothing
        Me.PictureBox1.Location = New System.Drawing.Point(12, 12)
        Me.PictureBox1.Name = "PictureBox1"
        Me.PictureBox1.Size = New System.Drawing.Size(278, 67)
        Me.PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        Me.PictureBox1.TabIndex = 37
        Me.PictureBox1.TabStop = False
        '
        'btn_testmode
        '
        Me.btn_testmode.Location = New System.Drawing.Point(244, 218)
        Me.btn_testmode.Name = "btn_testmode"
        Me.btn_testmode.Size = New System.Drawing.Size(53, 35)
        Me.btn_testmode.TabIndex = 36
        Me.btn_testmode.Text = "Joy"
        Me.btn_testmode.UseVisualStyleBackColor = True
        '
        'CheckBox_DevEn
        '
        Me.CheckBox_DevEn.AutoSize = True
        Me.CheckBox_DevEn.Checked = True
        Me.CheckBox_DevEn.CheckState = System.Windows.Forms.CheckState.Checked
        Me.CheckBox_DevEn.Location = New System.Drawing.Point(320, 173)
        Me.CheckBox_DevEn.Name = "CheckBox_DevEn"
        Me.CheckBox_DevEn.Size = New System.Drawing.Size(126, 17)
        Me.CheckBox_DevEn.TabIndex = 35
        Me.CheckBox_DevEn.Text = "DEVELOPER MODE"
        Me.CheckBox_DevEn.UseVisualStyleBackColor = True
        '
        'CheckBox_TCPclientEn
        '
        Me.CheckBox_TCPclientEn.AutoSize = True
        Me.CheckBox_TCPclientEn.Checked = True
        Me.CheckBox_TCPclientEn.CheckState = System.Windows.Forms.CheckState.Checked
        Me.CheckBox_TCPclientEn.Location = New System.Drawing.Point(320, 143)
        Me.CheckBox_TCPclientEn.Name = "CheckBox_TCPclientEn"
        Me.CheckBox_TCPclientEn.Size = New System.Drawing.Size(118, 17)
        Me.CheckBox_TCPclientEn.TabIndex = 34
        Me.CheckBox_TCPclientEn.Text = "TCP Client Enabled"
        Me.CheckBox_TCPclientEn.UseVisualStyleBackColor = True
        '
        'CheckBox_DebugmodeEn
        '
        Me.CheckBox_DebugmodeEn.AutoSize = True
        Me.CheckBox_DebugmodeEn.Location = New System.Drawing.Point(320, 113)
        Me.CheckBox_DebugmodeEn.Name = "CheckBox_DebugmodeEn"
        Me.CheckBox_DebugmodeEn.Size = New System.Drawing.Size(130, 17)
        Me.CheckBox_DebugmodeEn.TabIndex = 33
        Me.CheckBox_DebugmodeEn.Text = "Debug Mode Enabled"
        Me.CheckBox_DebugmodeEn.UseVisualStyleBackColor = True
        '
        'CheckBox_JoystickEn
        '
        Me.CheckBox_JoystickEn.AutoSize = True
        Me.CheckBox_JoystickEn.Checked = True
        Me.CheckBox_JoystickEn.CheckState = System.Windows.Forms.CheckState.Checked
        Me.CheckBox_JoystickEn.Location = New System.Drawing.Point(320, 86)
        Me.CheckBox_JoystickEn.Name = "CheckBox_JoystickEn"
        Me.CheckBox_JoystickEn.Size = New System.Drawing.Size(106, 17)
        Me.CheckBox_JoystickEn.TabIndex = 32
        Me.CheckBox_JoystickEn.Text = "Joystick Enabled"
        Me.CheckBox_JoystickEn.UseVisualStyleBackColor = True
        '
        'txtbox_Port
        '
        Me.txtbox_Port.Location = New System.Drawing.Point(79, 175)
        Me.txtbox_Port.Name = "txtbox_Port"
        Me.txtbox_Port.Size = New System.Drawing.Size(214, 20)
        Me.txtbox_Port.TabIndex = 31
        Me.txtbox_Port.Text = "9999"
        '
        'txtbox_IPaddr
        '
        Me.txtbox_IPaddr.Location = New System.Drawing.Point(79, 142)
        Me.txtbox_IPaddr.Name = "txtbox_IPaddr"
        Me.txtbox_IPaddr.Size = New System.Drawing.Size(215, 20)
        Me.txtbox_IPaddr.TabIndex = 30
        Me.txtbox_IPaddr.Text = "localhost"
        '
        'txtblk_Port
        '
        Me.txtblk_Port.BorderStyle = System.Windows.Forms.BorderStyle.None
        Me.txtblk_Port.Location = New System.Drawing.Point(12, 179)
        Me.txtblk_Port.Name = "txtblk_Port"
        Me.txtblk_Port.ReadOnly = True
        Me.txtblk_Port.Size = New System.Drawing.Size(160, 13)
        Me.txtblk_Port.TabIndex = 29
        Me.txtblk_Port.Text = "Port:"
        '
        'txtblk_IPaddr
        '
        Me.txtblk_IPaddr.BorderStyle = System.Windows.Forms.BorderStyle.None
        Me.txtblk_IPaddr.Location = New System.Drawing.Point(12, 147)
        Me.txtblk_IPaddr.Name = "txtblk_IPaddr"
        Me.txtblk_IPaddr.ReadOnly = True
        Me.txtblk_IPaddr.Size = New System.Drawing.Size(161, 13)
        Me.txtblk_IPaddr.TabIndex = 28
        Me.txtblk_IPaddr.Text = "IP Address:"
        '
        'rabtn_CMDrecon
        '
        Me.rabtn_CMDrecon.AutoSize = True
        Me.rabtn_CMDrecon.Location = New System.Drawing.Point(128, 86)
        Me.rabtn_CMDrecon.Name = "rabtn_CMDrecon"
        Me.rabtn_CMDrecon.Size = New System.Drawing.Size(76, 17)
        Me.rabtn_CMDrecon.TabIndex = 27
        Me.rabtn_CMDrecon.Text = "CMDrecon"
        Me.rabtn_CMDrecon.UseVisualStyleBackColor = True
        '
        'rabtn_CMDoverwatch
        '
        Me.rabtn_CMDoverwatch.AutoSize = True
        Me.rabtn_CMDoverwatch.Checked = True
        Me.rabtn_CMDoverwatch.Location = New System.Drawing.Point(14, 86)
        Me.rabtn_CMDoverwatch.Name = "rabtn_CMDoverwatch"
        Me.rabtn_CMDoverwatch.Size = New System.Drawing.Size(99, 17)
        Me.rabtn_CMDoverwatch.TabIndex = 26
        Me.rabtn_CMDoverwatch.TabStop = True
        Me.rabtn_CMDoverwatch.Text = "CMDoverwatch"
        Me.rabtn_CMDoverwatch.UseVisualStyleBackColor = True
        '
        'btn_close
        '
        Me.btn_close.Location = New System.Drawing.Point(320, 218)
        Me.btn_close.Name = "btn_close"
        Me.btn_close.Size = New System.Drawing.Size(118, 35)
        Me.btn_close.TabIndex = 25
        Me.btn_close.Text = "Close"
        Me.btn_close.UseVisualStyleBackColor = True
        '
        'btn_start
        '
        Me.btn_start.Location = New System.Drawing.Point(13, 218)
        Me.btn_start.Name = "btn_start"
        Me.btn_start.Size = New System.Drawing.Size(102, 35)
        Me.btn_start.TabIndex = 23
        Me.btn_start.Text = "Start"
        Me.btn_start.UseVisualStyleBackColor = True
        '
        'StartForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(459, 264)
        Me.Controls.Add(Me.RadioButton1)
        Me.Controls.Add(Me.PictureBox1)
        Me.Controls.Add(Me.btn_testmode)
        Me.Controls.Add(Me.CheckBox_DevEn)
        Me.Controls.Add(Me.CheckBox_TCPclientEn)
        Me.Controls.Add(Me.CheckBox_DebugmodeEn)
        Me.Controls.Add(Me.CheckBox_JoystickEn)
        Me.Controls.Add(Me.txtbox_Port)
        Me.Controls.Add(Me.txtbox_IPaddr)
        Me.Controls.Add(Me.txtblk_Port)
        Me.Controls.Add(Me.txtblk_IPaddr)
        Me.Controls.Add(Me.rabtn_CMDrecon)
        Me.Controls.Add(Me.rabtn_CMDoverwatch)
        Me.Controls.Add(Me.btn_close)
        Me.Controls.Add(Me.btn_start)
        Me.Name = "StartForm"
        Me.Text = "CMD3C: Robot Control Centre"
        CType(Me.PictureBox1, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents RadioButton1 As System.Windows.Forms.RadioButton
    Friend WithEvents PictureBox1 As System.Windows.Forms.PictureBox
    Friend WithEvents btn_testmode As System.Windows.Forms.Button
    Friend WithEvents CheckBox_DevEn As System.Windows.Forms.CheckBox
    Friend WithEvents CheckBox_TCPclientEn As System.Windows.Forms.CheckBox
    Friend WithEvents CheckBox_DebugmodeEn As System.Windows.Forms.CheckBox
    Friend WithEvents CheckBox_JoystickEn As System.Windows.Forms.CheckBox
    Friend WithEvents txtbox_Port As System.Windows.Forms.TextBox
    Friend WithEvents txtbox_IPaddr As System.Windows.Forms.TextBox
    Friend WithEvents txtblk_Port As System.Windows.Forms.TextBox
    Friend WithEvents txtblk_IPaddr As System.Windows.Forms.TextBox
    Friend WithEvents rabtn_CMDrecon As System.Windows.Forms.RadioButton
    Friend WithEvents rabtn_CMDoverwatch As System.Windows.Forms.RadioButton
    Friend WithEvents btn_close As System.Windows.Forms.Button
    Friend WithEvents btn_start As System.Windows.Forms.Button
    Friend WithEvents Timer1 As System.Windows.Forms.Timer

End Class
