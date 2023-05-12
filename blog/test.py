Sub GetTodaysAppointments()
    Dim olApp As Outlook.Application
    Dim olNS As Outlook.Namespace
    Dim olFolder As Outlook.MAPIFolder
    Dim olApt As Object
    Dim strList As String
    Dim RestrictItems As Outlook.Items
    Dim strRestrict As String
    Dim duration As String

    ' Outlook セッションを開始
    Set olApp = New Outlook.Application
    Set olNS = olApp.GetNamespace("MAPI")

    ' カレンダーフォルダーを設定
    Set olFolder = olNS.GetDefaultFolder(olFolderCalendar)

    ' 当日のアイテムをフィルタリング
    strRestrict = "[Start] >= '" & Format(Now, "mm/dd/yyyy") & "' AND [End] <= '" & Format(Now + 1, "mm/dd/yyyy") & "'"
    Set RestrictItems = olFolder.Items.Restrict(strRestrict)

    ' アイテムを開始時間でソート
    RestrictItems.Sort "[Start]"

    ' アポイントメントをリストに追加
    For Each olApt In RestrictItems
        duration = Format((olApt.End - olApt.Start) * 24 * 60, "0") & " minutes"  ' 所要時間を分単位で計算
        strList = strList & olApt.Subject & ": " & duration & vbCrLf
    Next olApt

    ' リストを表示
    MsgBox strList, vbInformation, "本日の予定："

    ' オブジェクトをクリア
    Set olApt = Nothing
    Set olFolder = Nothing
    Set olNS = Nothing
    Set olApp = Nothing
End Sub
