<?php
$fp = fopen('f.txt', 'w');
fwrite($fp, 'Cats hate mice');
fclose($fp);
?>
