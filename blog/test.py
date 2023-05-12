Sub GetTodaysAppointments()
    Dim olApp As Outlook.Application
    Dim olNS As Outlook.Namespace
    Dim olFolder As Outlook.MAPIFolder
    Dim olApt As Object
    Dim strList As String
    Dim MyItems As Outlook.Items
    Dim RestrictItems As Outlook.Items
    Dim strRestrict As String

    ' Outlook セッションを開始
    Set olApp = New Outlook.Application
    Set olNS = olApp.GetNamespace("MAPI")

    ' カレンダーフォルダーを設定
    Set olFolder = olNS.GetDefaultFolder(olFolderCalendar)

    ' 当日のアイテムをフィルタリング
    strRestrict = "[Start] >= '" & Format(Now, "mm/dd/yyyy hh:mm AMPM") & "' AND [End] <= '" & Format(Now, "mm/dd/yyyy") & " 11:59 PM'"
    Set RestrictItems = olFolder.Items.Restrict(strRestrict)

    ' アイテムを開始時間でソート
    RestrictItems.Sort "[Start]"

    ' アポイントメントをリストに追加
    For Each olApt In RestrictItems
        strList = strList & olApt.Start & " -- " & olApt.Subject & vbCrLf
    Next olApt

    ' リストを表示
    MsgBox strList, vbInformation, "本日の予定："

    ' オブジェクトをクリア
    Set olApt = Nothing
    Set olFolder = Nothing
    Set olNS = Nothing
    Set olApp = Nothing
End Sub
