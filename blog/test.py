Function GetAppointmentsByDate(inputDate As Date) As String
    Dim olApp As Outlook.Application
    Dim olNS As Outlook.Namespace
    Dim olFolder As Outlook.MAPIFolder
    Dim olApt As Object
    Dim strList As String
    Dim MyItems As Outlook.Items
    Dim RestrictItems As Outlook.Items
    Dim strRestrict As String
    Dim duration As String

    ' Outlook セッションを開始
    Set olApp = New Outlook.Application
    Set olNS = olApp.GetNamespace("MAPI")

    ' カレンダーフォルダーを設定
    Set olFolder = olNS.GetDefaultFolder(olFolderCalendar)

    ' 指定した日付のアイテムをフィルタリング
    strRestrict = "[Start] >= '" & Format(inputDate, "mm/dd/yyyy") & " 09:00 AM' AND [Start] < '" & Format(inputDate + 1, "mm/dd/yyyy") & " 06:00 PM'"
    Set RestrictItems = olFolder.Items.Restrict(strRestrict)

    ' 作業時間内のアポイントメントをリストに追加
    For Each olApt In RestrictItems
        ' キャンセルされた会議を除外
        If olApt.BusyStatus <> olBusyStatusFree Then
            duration = Format((olApt.End - olApt.Start) * 24 * 60, "0") & " 分"  ' 所要時間を分単位で計算
            strList = strList & olApt.Subject & ": " & duration & vbCrLf
        End If
    Next olApt

    ' 結果を戻す
    GetAppointmentsByDate = strList

    ' オブジェクトをクリア
    Set olApt = Nothing
    Set olFolder = Nothing
    Set olNS = Nothing
    Set olApp = Nothing
End Function
Sub Test()
    Dim result As String
    result = GetAppointmentsByDate(#5/12/2023#) ' 日付を渡します
    MsgBox result, vbInformation, "予定："
End Sub
