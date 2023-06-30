Sub SplitAndReposition()
    Dim ws As Worksheet
    Dim rng As Range
    Dim cell As Range
    Dim splitValues As Variant
    Dim i As Integer
    Dim lastRow As Long
    Dim output As String

    Set ws = ThisWorkbook.Sheets("Sheet1")  ' シート名を適切に変更してください
    lastRow = ws.Cells(ws.Rows.Count, "B").End(xlUp).Row  ' B列の最終行を取得

    Set rng = ws.Range("B1:B" & lastRow)  ' B列にデータが入力されているセルを対象にする

    ' 範囲内の各セルに対して処理
    For Each cell In rng
        If cell.Value <> "" Then  ' B列のセルにデータが入力されている場合だけ処理を行う
            splitValues = Split(cell.Value, vbLf)

            output = ""
            For i = LBound(splitValues) To UBound(splitValues)
                ' 改行で分割したテキストをカンマで結合
                output = output & splitValues(i) & ","
            Next i

            ' 末尾の余分なカンマを削除
            output = Left(output, Len(output) - 1)

            ' 結果をL列に出力
            ws.Cells(cell.Row, "L").Value = output
        End If
    Next cell
End Sub
