<?php

$file='arr.txt';
//ARR CREATE
//times, img1..img5
$arr=array(0,0,0,0,0,0);

//READ ARR FROM FILE
$arr = json_decode(file_get_contents($file), true);

//ARR UPDATA
$arr[0]+=1;

$arr[1]=round(($arr[1]+$_GET["volume1"])/$arr[0]);
$arr[2]=round(($arr[2]+$_GET["volume2"])/$arr[0]);
$arr[3]=round(($arr[3]+$_GET["volume3"])/$arr[0]);
$arr[4]=round(($arr[4]+$_GET["volume4"])/$arr[0]);
$arr[5]=round(($arr[5]+$_GET["volume5"])/$arr[0]);

//WRITE ARR TO FILE
file_put_contents($file,  json_encode($arr));



echo '����:' . htmlspecialchars($arr[0]) . '<br>';
echo '����������1:' . htmlspecialchars($arr[1]) . '<br>';
echo '����������2:' . htmlspecialchars($arr[2]) . '<br>';
echo '����������3:' . htmlspecialchars($arr[3]) . '<br>';
echo '����������4:' . htmlspecialchars($arr[4]) . '<br>';
echo '����������5:' . htmlspecialchars($arr[5]) . '<br>';

?>