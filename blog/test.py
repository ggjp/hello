Sub GetTodaysAppointments()
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

    ' 全てのアイテムを取得
    Set MyItems = olFolder.Items

    ' アイテムを開始時間でソート
    MyItems.Sort "[Start]"

    ' 当日の作業時間内のアイテムをフィルタリング
    strRestrict = "[Start] >= '" & Format(Now, "mm/dd/yyyy") & " 09:00 AM' AND [End] <= '" & Format(Now, "mm/dd/yyyy") & " 06:00 PM'"
    Set RestrictItems = MyItems.Restrict(strRestrict)

    ' アポイントメントをリストに追加
    For Each olApt In RestrictItems
        ' キャンセルされた会議を除外
        If olApt.BusyStatus <> olBusyStatusFree Then
            duration = Format((olApt.End - olApt.Start) * 24 * 60, "0") & " 分"  ' 所要時間を分単位で計算
            strList = strList & olApt.Subject & ": " & duration & vbCrLf
        End If
    Next olApt

    ' リストを表示
    MsgBox strList, vbInformation, "本日の予定："

    ' オブジェクトをクリア
    Set olApt = Nothing
    Set olFolder = Nothing
    Set olNS = Nothing
    Set olApp = Nothing
End Sub
