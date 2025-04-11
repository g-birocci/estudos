Imports System
Imports System.Security.Cryptography.X509Certificates



Module Program

    Public Class Retangulo
        Private comprimento As Double
        Private largura As Double

        Public Sub Mostrar()
            comprimento = 4.5
            largura = 5
        End Sub

        Public Function Getarea() As Double
            Getarea = comprimento * largura
        End Function

        Public Sub Imprimir()
            Console.WriteLine("Comprimento: {0}", comprimento)
            Console.WriteLine("largula: {0}", largura)
            Console.WriteLine("Àrea: {0}", Getarea())

        End Sub
    End Class
    Sub Main(args As String())

            Dim rec1 As New Retangulo()
            rec1.Mostrar()
            rec1.Imprimir()
            Console.ReadLine()

            Console.ReadKey()

        End Sub

End Module
