<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class VideoBoxForm
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
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(VideoBoxForm))
        Me.StreamBox = New AxAXVLC.AxVLCPlugin()
        Me.btn_load = New System.Windows.Forms.Button()
        Me.txt_streambox = New System.Windows.Forms.TextBox()
        Me.btn_clear = New System.Windows.Forms.Button()
        CType(Me.StreamBox, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'StreamBox
        '
        Me.StreamBox.Enabled = True
        Me.StreamBox.Location = New System.Drawing.Point(12, 12)
        Me.StreamBox.Name = "StreamBox"
        Me.StreamBox.OcxState = CType(resources.GetObject("StreamBox.OcxState"), System.Windows.Forms.AxHost.State)
        Me.StreamBox.Size = New System.Drawing.Size(640, 480)
        Me.StreamBox.TabIndex = 61
        '
        'btn_load
        '
        Me.btn_load.Location = New System.Drawing.Point(48, 500)
        Me.btn_load.Name = "btn_load"
        Me.btn_load.Size = New System.Drawing.Size(79, 31)
        Me.btn_load.TabIndex = 59
        Me.btn_load.Text = "Load"
        Me.btn_load.UseVisualStyleBackColor = True
        '
        'txt_streambox
        '
        Me.txt_streambox.Location = New System.Drawing.Point(153, 506)
        Me.txt_streambox.Name = "txt_streambox"
        Me.txt_streambox.Size = New System.Drawing.Size(336, 20)
        Me.txt_streambox.TabIndex = 58
        '
        'btn_clear
        '
        Me.btn_clear.Location = New System.Drawing.Point(529, 500)
        Me.btn_clear.Name = "btn_clear"
        Me.btn_clear.Size = New System.Drawing.Size(95, 31)
        Me.btn_clear.TabIndex = 60
        Me.btn_clear.Text = "Clear All"
        Me.btn_clear.UseVisualStyleBackColor = True
        '
        'VideoBoxForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(663, 538)
        Me.Controls.Add(Me.StreamBox)
        Me.Controls.Add(Me.btn_load)
        Me.Controls.Add(Me.txt_streambox)
        Me.Controls.Add(Me.btn_clear)
        Me.Name = "VideoBoxForm"
        Me.Text = "Robot Video Stream"
        CType(Me.StreamBox, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents StreamBox As AxAXVLC.AxVLCPlugin
    Friend WithEvents btn_load As System.Windows.Forms.Button
    Friend WithEvents txt_streambox As System.Windows.Forms.TextBox
    Friend WithEvents btn_clear As System.Windows.Forms.Button
End Class
