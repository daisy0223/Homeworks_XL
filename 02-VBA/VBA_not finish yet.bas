Attribute VB_Name = "Module1"
Sub stock()
'Define varialbes
Dim Ticker As String
Dim Yearly_change As Double
Dim Percentage_char As Double
Dim Total_stock_volume As Double
Dim Open_value As Double
Dim Close_value As Double
Dim i As Integer
'keep track of the location for ticker
Dim Summary_table_row As Integer


'Set the initial values
Total_stock_volume = 0
Close_value = 0
Yearly_change = 0
Percentage_char = 0
Summary_table_row = 2

'Give the headers for the summary table
Cells(1, 9).Value = "Ticker"
Cells(1, 10).Value = "Yearly_change"
Cells(1, 11).Value = "Percentage_char"
Cells(1, 12).Value = "Total_stock_volume"
Cells(1, 13).Value = "Open_value"
Cells(1, 14).Value = "End_value"

' Get the row number of the last row with data
Row_count = Cells(Rows.Count, "A").End(xlUp).Row

Cells(2, 3).Value = Cells(2, 13).Value
'loop through worksheet A
For i = 2 To Row_count
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            Ticker = Cells(i, 1).Value
            Total_stock_volume = Total_stock_volume + Cells(i, 7).Value
    End_value = Cells(i, 6).Value
            Yearly_change = Close_value - Open_value
            'Percentage_char = (Close_value - Open_value) / Open_value
            
            'Display values
            Range("I" & 2 + j).Value = Ticker
            Range("J" & 2 + j).Value = Yearly_change
            Range("K" & 2 + j).Value = Percentage_char
            Range("L" & 2 + j).Value = Total_stock_volume
            Range("M" & 2 + j).Value = Open_value
            Range("N" & 2 + j).Value = Close_volume
            
            'start from next ticker
            Summary_table_row = Summary_table_row + 1
            
        Else
            Total_stock_volume = Total_stock_volume + Cells(i, 7).Value
            Open_value = Cells(i, 3).Value
        End If

    If Yearly_change < 0 Then
                    Range("J" & Summary_table_row).Interior.ColorIndex = 3
                ElseIf Yearly_change > 0 Then
                    Range("J" & Summary_table_row).Interior.ColorIndex = 4
                End If
    Next i
End Sub

