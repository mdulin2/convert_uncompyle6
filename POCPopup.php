<?php
$fp = fopen('POC.txt', 'w');
fwrite($fp, 'Cats hate mice');
fclose($fp);
?>
