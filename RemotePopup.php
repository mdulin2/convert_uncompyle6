<?php
$fp = fopen('Remote.txt', 'w');
fwrite($fp, 'Cats hate mice');
fclose($fp);
?>
