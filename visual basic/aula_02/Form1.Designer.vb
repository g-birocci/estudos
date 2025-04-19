<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
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
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Me.btnTeste = New System.Windows.Forms.Button()
        Me.btcGo = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'btnTeste
        '
        Me.btnTeste.Location = New System.Drawing.Point(309, 141)
        Me.btnTeste.Name = "btnTeste"
        Me.btnTeste.Size = New System.Drawing.Size(93, 45)
        Me.btnTeste.TabIndex = 0
        Me.btnTeste.Text = "Teste"
        Me.btnTeste.UseVisualStyleBackColor = True
        '
        'btcGo
        '
        Me.btcGo.Location = New System.Drawing.Point(454, 141)
        Me.btcGo.Name = "btcGo"
        Me.btcGo.Size = New System.Drawing.Size(93, 45)
        Me.btcGo.TabIndex = 1
        Me.btcGo.Text = "Go"
        Me.btcGo.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(8.0!, 16.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(800, 450)
        Me.Controls.Add(Me.btcGo)
        Me.Controls.Add(Me.btnTeste)
        Me.Name = "Form1"
        Me.Text = "Form1"
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents btnTeste As Button
    Friend WithEvents btcGo As Button
End Class
