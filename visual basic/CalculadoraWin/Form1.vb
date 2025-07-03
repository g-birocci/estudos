Public Class Form1
    Private primeiroNumero As Double = 0
    Private operacaoAtual As String = ""
    Private isNewOperation As Boolean = True

    Private Sub btnLimpar_Click(sender As Object, e As EventArgs) Handles btnLimpar.Click
        TextBox1.Clear()
    End Sub

    Private Sub Number_Click(sender As Object, e As EventArgs) Handles btnUm.Click, btnDois.Click, btnTres.Click, btn4.Click, btnCinco.Click, btnSeis.Click, btnSete.Click, btnOito.Click, btnNove.Click, btnZero.Click, btnVirgula.Click

        Dim btn As Button = CType(sender, Button)

        If TextBox1.Text = "0" Or isNewOperation Then
            TextBox1.Text = btn.Text
            isNewOperation = False
        Else
            TextBox1.Text += btn.Text
        End If
    End Sub

    Private Sub Operacao_Click(sender As Object, e As EventArgs) Handles btnSoma.Click, btnSubtracao.Click, btnMultiplicacao.Click, btnDivisao.Click
        Dim btn As Button = CType(sender, Button)

        If Not isNewOperation Then
            primeiroNumero = Double.Parse(TextBox1.Text)
        End If

        operacaoAtual = btn.Text
        isNewOperation = True
    End Sub

    Private Sub btnIgual_Click(sender As Object, e As EventArgs) Handles btnIgual.Click
        If operacaoAtual = "" Or isNewOperation Then
            Return
        End If

        Dim segundoNumero As Double = Double.Parse(TextBox1.Text)
        Dim resultado As Double = 0

        Select Case operacaoAtual
            Case "+"
                resultado = primeiroNumero + segundoNumero
            Case "-"
                resultado = primeiroNumero - segundoNumero
            Case "x"
                resultado = primeiroNumero * segundoNumero
            Case "/"
                If segundoNumero = 0 Then
                    MessageBox.Show("Não é possível dividir por zero!", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error)
                    Return
                End If
                resultado = primeiroNumero / segundoNumero
        End Select

        TextBox1.Text = resultado.ToString()
        operacaoAtual = ""
        isNewOperation = True
    End Sub


End Class
