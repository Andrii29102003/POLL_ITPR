<?php
$file='arr.txt';
$arr = json_decode(file_get_contents($file), true);
$imgmarktextsize='100px';
?>

<html lang="uk">
    <head>
        <link rel="stylesheet" href="styles.css">
        <meta charset="utf-16">
        <title>
            Результат
        </title>
    </head>

    <body>

        <?php echo "<h2 class='headtext'>Результати опитування [$arr[0]]</h2>"?>
        <hr>
        <!-- 1 -->
        <img src = "img/img1.bmp">
        <?php echo "<snap style='font-size: $imgmarktextsize'>&nbsp;". round($arr[1]/$arr[0]) ."</snap>" ?>

        <hr>

        <!-- 2 -->
        <img src = "img/img2.bmp">
        <?php echo "<snap style='font-size: $imgmarktextsize'>&nbsp;". round($arr[2]/$arr[0]) ."</snap>" ?>

        <hr>

        <!-- 3 -->
        <img src = "img/img3.bmp">
        <?php echo "<snap style='font-size: $imgmarktextsize'>&nbsp;". round($arr[3]/$arr[0]) ."</snap>" ?>

        <hr>

        <!-- 4 -->
        <img src = "img/img4.bmp">
        <?php echo "<snap style='font-size: $imgmarktextsize'>&nbsp;". round($arr[4]/$arr[0]) ."</snap>" ?>

        <hr>

        <!-- 5 -->
        <img src = "img/img5.bmp">
        <?php echo "<snap style='font-size: $imgmarktextsize'>&nbsp;". round($arr[5]/$arr[0]) ."</snap>" ?>
        
        <hr>

</html>