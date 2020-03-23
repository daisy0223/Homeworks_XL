Attribute VB_Name = "Module1"
Sub stock()
'Define varialbes
Dim Ticker As String
Dim Yearly_change As Double
Dim Percentage_char As Double
Dim Total_stock_volume As Double
Dim Open_value As Double
Dim Close_value As Double

'Set the initial values
Total_stock_volume = 0
Close_value = 0
Yearly_change = 0
Percentage_char = 0

'Give the headers for the summary table
Cells(1, 9).Value = "Ticker"
Cells(1, 10).Value = "Yearly_change"
Cells(1, 11).Value = "Percentage_char"
Cells(1, 12).Value = "Total_stock_volume"
Cells(1, 13).Value = "Open_value"
Cells(1, 14).Value = "End_value"

'keep track of the location for ticker
Dim Summary_table_row As Integer
Summary_table_row = 2

'Initial the Open_value
Cells(2, 13).Value = Cells(2, 3).Value

'loop through worksheet A
For i = 2 To 70926
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            Ticker = Cells(i, 1).Value
            Open_value = Cells(i + 1, 3).Value
            Close_value = Cells(i, 6).Value
            Total_stock_volume = Total_stock_volume + Cells(i, 7).Value
            Yearly_change = Close_value - Open_value
            'Percentage_char = (Close_value - Open_value) / Open_value
            
            'Display values
            Range("I" & Summary_table_row).Value = Ticker
            Range("J" & Summary_table_row).Value = Yearly_change
            Range("K" & Summary_table_row).Value = Percentage_char
            Range("L" & Summary_table_row).Value = Total_stock_volume
            Range("M" & Summary_table_row).Value = Open_value
            Range("N" & Summary_table_row).Value = Close_volume
            Summary_table_row = Summary_table_row + 1
            
        Else
            Total_stock_volume = Total_stock_volume + Cells(i, 7).Value
        
        
        End If
        
        
    If Yearly_change < 0 Then
                    Range("J" & Summary_table_row).Interior.ColorIndex = 3
                ElseIf Yearly_change > 0 Then
                    Range("J" & Summary_table_row).Interior.ColorIndex = 4
                End If
    Next i
End Sub

