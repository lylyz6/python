<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>QQ音乐歌曲URL提交</title>
</head>
<body>
    <h1>提交QQ音乐歌曲URL</h1>
    <form method="post" action="">
        <label for="qqurl">歌曲URL：</label>
        <input type="text" id="qqurl" name="qqurl" required>
        <br><br>
        <input type="submit" value="提交">
    </form>
    <?php
    if (isset($_POST['qqurl'])) {
        $qqurl = trim($_POST['qqurl']);
        // 简单判断 URL 是否包含 "qq.com"，可根据需要扩展验证
        if (strpos($qqurl, "qq.com") !== false) {
            $filename = "qqurl.txt";
            // 追加换行符
            $data = $qqurl . PHP_EOL;
            if (file_put_contents($filename, $data, FILE_APPEND | LOCK_EX) !== false) {
                echo "<p>提交成功！</p>";
            } else {
                echo "<p>写入文件失败，请检查文件权限！</p>";
            }
        } else {
            echo "<p>请输入有效的QQ音乐URL！</p>";
        }
    }
    ?>
</body>
</html>
