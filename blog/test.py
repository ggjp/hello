Sub SplitAndReposition()
    Dim rng As Range
    Dim cell As Range
    Dim splitValues As Variant
    Dim i As Integer
    
    ' 変換したいセルを指定
    Set rng = Range("A1")
    
    ' 改行でテキストを分割
    splitValues = Split(rng.Value, vbLf)
    
    ' 分割したテキストを列に展開
    For i = LBound(splitValues) To UBound(splitValues)
        rng.Offset(0, i).Value = splitValues(i)
    Next i
End Sub
