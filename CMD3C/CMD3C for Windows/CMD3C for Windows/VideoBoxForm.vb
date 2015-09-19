Public Class VideoBoxForm
    Dim VideoStream As String = ""
    Private Sub VideoBoxForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        ' txtbox_VideoServer.Text = "192.168.12.43"
        'VideoStream = txtbox_VideoServer.Text
        txt_streambox.Text = "http://cmdlab.zapto.org:81/videostream.cgi?&user=admin&pwd="
    End Sub

    Private Sub Button1_Click_1(sender As Object, e As EventArgs)
        'A nice test video for you www.youtube.com/watch?v=dd3j0Qpq0tI
        streambox.stop()
        streambox.playlistClear()
        Dim address As String
        address = txt_streambox.Text
        streambox.addTarget(address, Nothing, AXVLC.VLCPlaylistMode.VLCPlayListReplaceAndGo, 0)
        streambox.play()
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs)
        streambox.stop()
        streambox.playlistClear()
    End Sub

    Private Sub txt_streambox_DoubleClick(sender As Object, e As EventArgs)
        txt_streambox.SelectAll()
    End Sub

End Class