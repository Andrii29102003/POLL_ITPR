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
            Результати
        </title>
    </head>

    <body>

        <?php echo "<h2 class='headtext'>РЕЗУЛЬТАТИ ОПИТУВАННЯ [$arr[0]]</h2>"?>
        <hr>
        <!-- Питання1 -->
        <img src = "img/img1.bmp">
        <?php echo "<snap style='font-size: $imgmarktextsize'>&nbsp;$arr[1]</snap>" ?>

        <hr>

        <!-- Питання2 -->
        <img src = "img/img2.bmp">
        <?php echo "<snap style='font-size: $imgmarktextsize'>&nbsp;$arr[2]</snap>" ?>

        <hr>

        <!-- Питання3 -->
        <img src = "img/img3.bmp">
        <?php echo "<snap style='font-size: $imgmarktextsize'>&nbsp;$arr[3]</snap>" ?>

        <hr>

        <!-- Питання4 -->
        <img src = "img/img4.bmp">
        <?php echo "<snap style='font-size: $imgmarktextsize'>&nbsp;$arr[4]</snap>" ?>

        <hr>

        <!-- Питання5 -->
        <img src = "img/img5.bmp">
        <?php echo "<snap style='font-size: $imgmarktextsize'>&nbsp;$arr[5]</snap>" ?>
        
        <hr>

</html>